import openreview
import pandas as pd
from datetime import datetime
import time

# 1. 连接到 OpenReview API2
client = openreview.api.OpenReviewClient(baseurl='https://api2.openreview.net')

print("🚀 正在连接 OpenReview 数据库，准备提取 ICLR 2026 全量数据...")

# 2. 获取 ICLR 2026 被接收的论文
# 注意：ICLR 2026 官方 API 会将接收的论文放在该 Venue ID 下
accepted_papers = client.get_all_notes(content={'venueid': 'ICLR.cc/2026/Conference'})

papers_data = []

print(f"✅ 成功找到 {len(accepted_papers)} 篇接收论文！开始全部提取详细信息...")

# 3. 循环提取每一篇论文的全部信息
for i, paper in enumerate(accepted_papers):
    c = paper.content
    
    # 辅助函数，防止空值报错
    def get_val(key, default=""):
        return c.get(key, {}).get('value', default)

    # 处理时间戳
    submit_time = datetime.fromtimestamp(paper.cdate / 1000).strftime('%Y-%m-%d') if paper.cdate else "Unknown"

    # 将提取到的所有字段装入字典
    papers_data.append({
        'Paper ID': paper.id,
        'Title': get_val('title'),
        'Authors': ", ".join(get_val('authors', [])),
        'Author IDs': ", ".join(get_val('authorids', [])),
        'Venue (Status)': get_val('venue', 'ICLR 2026 Accept'), # 接收状态 (Oral/Spotlight/Poster)
        'Primary Area': get_val('primary_area'),              # 主领域
        'TL;DR': get_val('TL;DR') or get_val('tldr'),         # 一句话总结
        'Keywords': ", ".join(get_val('keywords', [])),       # 关键词
        'Abstract': get_val('abstract'),                      # 完整摘要
        'Code URL': get_val('code', 'No Code Provided'),      # 代码链接
        'PDF Link': f"https://openreview.net/pdf?id={paper.forum}", # PDF 下载链接
        'Forum URL': f"https://openreview.net/forum?id={paper.forum}", # 网页链接
        'Submit Date': submit_time
    })
    
    # 打印进度条
    if (i + 1) % 500 == 0:
        print(f"⏳ 已提取 {i + 1} 篇...")
        time.sleep(1) # 稍微暂停，防止请求过快被限制

# 4. 导出为本地文件
df = pd.DataFrame(papers_data)
csv_filename = "ICLR_2026_All_Data_Extracted.csv"
df.to_csv(csv_filename, index=False, encoding='utf-8-sig') # 使用 utf-8-sig 防止 Excel 打开中文乱码

print(f"🎉 全部提取完成！共计 {len(df)} 篇论文。")
print(f"📁 文件已保存在当前目录下：{csv_filename}")