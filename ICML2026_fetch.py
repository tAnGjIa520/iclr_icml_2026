import requests
import pandas as pd

# 1. 目标 JSON 数据源 URL
url = "https://icml.cc/static/virtual/data/icml-2026-orals-posters.json"

print(f"🚀 正在从 ICML 官方服务器直连拉取底层 JSON 数据...\nURL: {url}")

# 2. 发送请求获取数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ 成功截获官方 JSON 数据库！正在解析并转换为表格...")
    
    # 将 JSON 解析为 Python 字典/列表
    data = response.json()
    
    # 3. 转换为 Pandas 数据表
    # 通常这种 JSON 文件本身就是一个列表形式，可以直接转换为 DataFrame
    df = pd.DataFrame(data)
    
    # 优化表格显示：如果某些列（如作者列表、关键词）是 Python 的 list 结构，将其转换为逗号分隔的字符串
    for col in df.columns:
        if df[col].apply(type).eq(list).any():
            df[col] = df[col].apply(lambda x: ", ".join(map(str, x)) if isinstance(x, list) else x)
    
    # 4. 导出为本地文件
    csv_filename = "ICML_2026_Official_Database.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')
    
    print(f"🎉 提取彻底完成！共计 {len(df)} 篇论文。")
    print(f"📁 数据已完美保存在当前目录下：{csv_filename}")
    
else:
    print(f"❌ 获取失败，服务器返回状态码: {response.status_code}")
    print("请检查链接是否正确或当前网络是否能够正常访问该地址。")