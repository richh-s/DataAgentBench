import snowflake.connector
import pandas as pd

conn = snowflake.connector.connect(
    user='richardspider',
    password='UCBquery123456',
    account='RSRSBDK-YDB67606'
)

tables = [
"CPC_DEFINITION", "PUBLICATIONS"
]

for t in tables:
    df = pd.read_sql(f"SELECT * FROM PATENTS.PATENTS.{t}", conn)

    df.to_csv(f"{t}.csv", index=False)
    print(f"download {t}.csv")

conn.close()
