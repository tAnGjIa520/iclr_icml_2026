<!-- Generated: 2026-05-06 | Updated: 2026-05-06 -->

# ICLR_ICML_2026

## Purpose
数据采集和处理项目，用于从 ICLR 2026 和 ICML 2026 会议获取论文数据，并将其转换为统一的 CSV 格式以便分析。该项目包含数据抓取脚本、格式转换工具和处理后的数据集。

## Key Files

| File | Description |
|------|-------------|
| `ICLR2026_fetch.py` | 从 OpenReview API 获取 ICLR 2026 全量论文数据 |
| `ICML2026_fetch.py` | 从 ICML 官方 JSON 数据源获取 ICML 2026 论文数据 |
| `convert_icml_to_csv.py` | 将 ICML 原始数据格式转换为与 ICLR 相同的标准化 CSV 格式 |
| `ICLR_2026_All_Data_Extracted.csv` | ICLR 2026 处理后的标准化数据（~10MB，包含论文元数据） |
| `ICML_2026_All_Data_Extracted.csv` | ICML 2026 处理后的标准化数据（~10MB，6567 篇论文） |
| `ICML_2026_Official_Database.csv` | ICML 2026 原始 JSON 格式数据（~22MB，未处理） |

## Subdirectories

| Directory | Purpose |
|-----------|---------|
| `.claude/` | Claude Code 配置文件（项目级设置） |
| `.omc/` | Oh-My-ClaudeCode 状态和会话数据 |

## For AI Agents

### Working In This Directory

**数据处理流程**：
1. **数据获取**：运行 `ICLR2026_fetch.py` 或 `ICML2026_fetch.py` 获取原始数据
2. **格式转换**：对于 ICML 数据，运行 `convert_icml_to_csv.py` 转换为标准格式
3. **数据分析**：使用 `*_All_Data_Extracted.csv` 文件进行后续分析

**标准化 CSV 格式**（13 列）：
- `Paper ID`: 论文唯一标识符
- `Title`: 论文标题
- `Authors`: 作者列表（逗号分隔）
- `Author IDs`: 作者 ID 列表
- `Venue (Status)`: 会议和录用状态（如 "ICML 2026 Accept (regular)"）
- `Primary Area`: 主要研究领域
- `TL;DR`: 一句话摘要
- `Keywords`: 关键词（逗号分隔）
- `Abstract`: 完整摘要
- `Code URL`: 代码链接
- `PDF Link`: PDF 下载链接
- `Forum URL`: OpenReview 论坛链接
- `Submit Date`: 提交日期

**环境要求**：
- Python 3.x
- 依赖包：`requests`, `pandas`, `openreview-py`
- 网络访问：ICLR 脚本需要访问 OpenReview API，ICML 脚本需要访问 ICML 官方服务器

**注意事项**：
- 当前运行环境为 CPU 节点，可以联网但无法访问 GitHub/Hugging Face
- 数据文件较大（CSV 文件 10-22MB），注意存储空间
- 使用 `utf-8-sig` 编码以确保中文兼容性

### Testing Requirements

**验证数据完整性**：
```bash
# 检查 CSV 行数
wc -l *.csv

# 查看前几行验证格式
head -n 3 ICML_2026_All_Data_Extracted.csv

# 验证转换脚本
python convert_icml_to_csv.py
```

**预期输出**：
- ICLR 数据：数千篇论文（具体数量取决于会议规模）
- ICML 数据：6567 篇论文（已验证）

### Common Patterns

**数据抓取模式**：
- 使用 `requests` 库获取 JSON 数据
- 使用 `pandas.DataFrame` 处理表格数据
- 使用 `openreview` 官方客户端访问 OpenReview API

**错误处理**：
- 网络请求包含 User-Agent 头避免被拒绝
- 使用 `try-except` 捕获解析错误
- 批量处理时显示进度（每 100 行）

**数据转换模式**：
- 使用 `eval()` 解析 Python 字典格式的 JSON 字符串
- 列表字段转换为逗号分隔字符串
- 缺失字段使用默认值（如 "No Code Provided"）

## Dependencies

### External
- `requests` - HTTP 请求库，用于获取 ICML 数据
- `pandas` - 数据处理和 CSV 操作
- `openreview-py` - OpenReview API 客户端，用于获取 ICLR 数据

### Data Sources
- **ICLR 2026**: OpenReview API (`https://api2.openreview.net`)
- **ICML 2026**: ICML 官方 JSON (`https://icml.cc/static/virtual/data/icml-2026-orals-posters.json`)

## Project Context

**用途场景**：
- 学术研究：分析顶会论文趋势
- 文献综述：快速检索相关论文
- 数据分析：统计作者、机构、研究方向分布

**数据规模**：
- ICLR 2026: 数千篇（待确认）
- ICML 2026: 6567 篇已确认

<!-- MANUAL: Any manually added notes below this line are preserved on regeneration -->
