import pandas as pd
import sqlite3

# 读取 JSON 文件
df = pd.read_json("../amazonreview_query/origin_dataset/review_query.json", lines=True)

# ✅ 强制将 review_time 转换为字符串（防止 SQLite 自动识别为时间戳）
if "review_time" in df.columns:
    df["review_time"] = df["review_time"].astype(str)

# 创建 SQLite 连接
conn = sqlite3.connect("../amazonreview_query/origin_dataset/review_query.db")

# 写入 SQLite，表名为 meta
df.to_sql("meta", conn, if_exists="replace", index=False)

# 关闭连接
conn.close()

print("✅ 已成功将 JSON 转换为 SQLite 数据库，并保留 review_time 为自然语言字符串")
