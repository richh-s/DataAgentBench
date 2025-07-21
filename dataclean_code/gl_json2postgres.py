import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import json

# 加载 .env
load_dotenv()

# 从 .env 读取配置
PG_USER = os.getenv("PG_USER")
PG_PASSWORD = os.getenv("PG_PASSWORD")
PG_HOST = os.getenv("PG_HOST", "localhost")
PG_PORT = os.getenv("PG_PORT", "5432")
DB_NAME_DEFAULT = os.getenv("PG_DB")

# ✅ 如果你想在代码里直接指定一个 db_name，请填在这里
DB_NAME = "ucb_db"  # 👈 这里改成你想用的数据库名

if not DB_NAME:  # 如果上面留空，就用 .env 里的
    DB_NAME = DB_NAME_DEFAULT

if not DB_NAME:
    raise ValueError("❌ 没有找到数据库名，请在代码里设置 DB_NAME 或 .env 中设置 DB_NAME！")
# 构造连接字符串
engine = create_engine(
    f"postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
)
# 读取 JSONL 文件
data = []
with open("../query_googlelocal/origi_dataset/light_meta_LLM_tt.json", "r", encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

def serialize_complex(value):
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value

for col in df.columns:
    df[col] = df[col].apply(serialize_complex)

# 写入 PostgreSQL
table_name = "business_description"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"✅ 已将数据导入到表 `{table_name}` 中！共导入 {len(df)} 条记录。")

df_pg = pd.read_sql_table(table_name, engine)

# 写入 SQLite
sqlite_path = "business_description.db"
sqlite_engine = create_engine(f"sqlite:///{sqlite_path}")
df_pg.to_sql(table_name, sqlite_engine, if_exists="replace", index=False)

print(f"🎉 已将数据从 PostgreSQL 导出到 SQLite 文件 `{sqlite_path}`")