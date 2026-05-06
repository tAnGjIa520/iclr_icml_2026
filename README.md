# ICLR & ICML 2026 论文数据提取工具

本项目用于从 ICLR 2026 和 ICML 2026 会议获取论文数据，并将其转换为统一的标准化 CSV 格式，便于后续分析和研究。

## 📋 项目概述

- **数据来源**：
  - ICLR 2026: OpenReview API
  - ICML 2026: ICML 官方 JSON 数据源
- **数据规模**：
  - ICLR 2026: 数千篇论文
  - ICML 2026: 6567 篇论文
- **输出格式**：统一的 13 列标准化 CSV 格式

## 📁 文件说明

### 数据抓取脚本

| 文件 | 说明 |
|------|------|
| `ICLR2026_fetch.py` | 从 OpenReview API 获取 ICLR 2026 全量论文数据 |
| `ICML2026_fetch.py` | 从 ICML 官方 JSON 数据源获取 ICML 2026 论文数据 |
| `convert_icml_to_csv.py` | 将 ICML 原始格式转换为标准化 CSV 格式 |

### 数据文件

| 文件 | 大小 | 说明 |
|------|------|------|
| `ICLR_2026_All_Data_Extracted.csv` | ~10MB | ICLR 2026 标准化数据 |
| `ICML_2026_All_Data_Extracted.csv` | ~10MB | ICML 2026 标准化数据（6567 篇） |
| `ICML_2026_Official_Database.csv` | ~22MB | ICML 2026 原始 JSON 格式数据 |

## 🚀 快速开始

### 环境要求

```bash
Python 3.x
pip install requests pandas openreview-py
```

### 使用方法

#### 1. 获取 ICLR 2026 数据

```bash
python ICLR2026_fetch.py
```

该脚本会：
- 连接到 OpenReview API
- 获取所有 ICLR 2026 接收的论文
- 自动保存为 `ICLR_2026_All_Data_Extracted.csv`

#### 2. 获取 ICML 2026 数据

```bash
python ICML2026_fetch.py
```

该脚本会：
- 从 ICML 官方服务器获取 JSON 数据
- 自动保存为 `ICML_2026_Official_Database.csv`

#### 3. 转换 ICML 数据格式

```bash
python convert_icml_to_csv.py
```

该脚本会：
- 读取 `ICML_2026_Official_Database.csv`
- 转换为标准化格式
- 输出 `ICML_2026_All_Data_Extracted.csv`

## 📊 数据格式说明

标准化 CSV 文件包含以下 13 列：

| 列名 | 说明 |
|------|------|
| `Paper ID` | 论文唯一标识符 |
| `Title` | 论文标题 |
| `Authors` | 作者列表（逗号分隔） |
| `Author IDs` | 作者 ID 列表 |
| `Venue (Status)` | 会议和录用状态（如 "ICML 2026 Accept (regular)"） |
| `Primary Area` | 主要研究领域 |
| `TL;DR` | 一句话摘要 |
| `Keywords` | 关键词（逗号分隔） |
| `Abstract` | 完整摘要 |
| `Code URL` | 代码链接 |
| `PDF Link` | PDF 下载链接 |
| `Forum URL` | OpenReview 论坛链接 |
| `Submit Date` | 提交日期 |

## 💡 使用场景

- **学术研究**：分析顶会论文趋势和热点方向
- **文献综述**：快速检索和筛选相关论文
- **数据分析**：统计作者、机构、研究方向分布
- **知识图谱**：构建学术关系网络

## 📝 示例代码

### 读取和分析数据

```python
import pandas as pd

# 读取数据
df = pd.read_csv('ICML_2026_All_Data_Extracted.csv')

# 查看基本信息
print(f"论文总数: {len(df)}")
print(f"列名: {df.columns.tolist()}")

# 统计录用类型
print(df['Venue (Status)'].value_counts())

# 搜索特定关键词的论文
keyword = "reinforcement learning"
results = df[df['Keywords'].str.contains(keyword, case=False, na=False)]
print(f"包含 '{keyword}' 的论文数: {len(results)}")
```

### 导出特定领域论文

```python
# 筛选特定领域
area = "Computer Vision"
cv_papers = df[df['Primary Area'] == area]
cv_papers.to_csv(f'{area}_papers.csv', index=False)
```

## ⚠️ 注意事项

1. **网络要求**：
   - ICLR 脚本需要访问 OpenReview API
   - ICML 脚本需要访问 ICML 官方服务器
   - 某些网络环境可能需要配置代理

2. **API 限制**：
   - OpenReview API 可能有请求频率限制
   - 脚本中已添加适当的延迟处理

3. **数据更新**：
   - 会议数据可能会更新（如增加新论文、修改状态）
   - 建议定期重新运行脚本获取最新数据

4. **编码问题**：
   - 所有 CSV 文件使用 `utf-8-sig` 编码
   - 确保 Excel 等工具正确显示中文

## 🔧 故障排除

### 问题：无法连接到 OpenReview API

```bash
# 检查网络连接
ping api2.openreview.net

# 或使用代理
export HTTP_PROXY=http://your-proxy:port
export HTTPS_PROXY=http://your-proxy:port
```

### 问题：CSV 文件中文乱码

确保使用支持 UTF-8 的工具打开，或在 Excel 中：
1. 数据 → 从文本/CSV
2. 文件原始格式选择 "65001: Unicode (UTF-8)"

## 📄 许可证

本项目仅用于学术研究目的。数据来源于公开的学术会议网站，请遵守相关使用条款。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题或建议，请通过 GitHub Issues 联系。

---

**最后更新**: 2026-05-06
