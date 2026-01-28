code = """import json
import pandas as pd
from datetime import datetime

# Load stored results (could be large files)
def load_var(v):
    if isinstance(v, str):
        # it's a file path
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

orders = load_var(var_call_lu5BsEnVvzmNGLWmGAO77Opx)
orderitems = load_var(var_call_gm3AD9dbCXBI2n2Y4qkcL5ZS)

# Create DataFrames
df_orders = pd.DataFrame(orders)
df_items = pd.DataFrame(orderitems)

# Helper clean function
def clean_str_col(s):
    if pd.isna(s):
        return s
    try:
        return str(s).strip().lstrip('#')
    except Exception:
        return s

# Clean Ids and OwnerId and OrderId
for col in ['Id','OwnerId','EffectiveDate']:
    if col in df_orders.columns:
        if col!='EffectiveDate':
            df_orders[col] = df_orders[col].apply(clean_str_col)
        else:
            df_orders[col] = df_orders[col].apply(lambda x: str(x).strip() if not pd.isna(x) else x)

for col in ['Id','OrderId','Quantity','UnitPrice']:
    if col in df_items.columns:
        if col in ['Id','OrderId']:
            df_items[col] = df_items[col].apply(clean_str_col)
        else:
            df_items[col] = df_items[col].apply(lambda x: x if x==x else None)

# Parse dates
# Today's date: 2022-11-25. Past five months -> from 2022-06-25 (inclusive) to 2022-11-25 (inclusive)
start = datetime(2022,6,25)
end = datetime(2022,11,25)

def parse_date(s):
    if pd.isna(s):
        return None
    s = str(s).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S.000%z", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except Exception:
            continue
    # try parsing first 10 chars
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d")
    except Exception:
        return None

df_orders['EffectiveDate_dt'] = df_orders['EffectiveDate'].apply(parse_date)

# Filter orders in window
df_orders_window = df_orders[(df_orders['EffectiveDate_dt'].notna()) & (df_orders['EffectiveDate_dt'] >= start) & (df_orders['EffectiveDate_dt'] <= end)].copy()

# Merge items with filtered orders
# Clean df_items Quantity and UnitPrice to numeric
df_items['Quantity_num'] = pd.to_numeric(df_items['Quantity'], errors='coerce')
df_items['UnitPrice_num'] = pd.to_numeric(df_items['UnitPrice'], errors='coerce')

# Merge on Id
merged = pd.merge(df_items, df_orders_window, left_on='OrderId', right_on='Id', how='inner', suffixes=('_item','_order'))

if merged.empty:
    top_agent = None
else:
    merged['SalesAmount'] = merged['Quantity_num'].fillna(0) * merged['UnitPrice_num'].fillna(0)
    # Clean OwnerId
    merged['OwnerId_clean'] = merged['OwnerId'].apply(clean_str_col)
    sales_by_agent = merged.groupby('OwnerId_clean', dropna=True)['SalesAmount'].sum()
    if sales_by_agent.empty:
        top_agent = None
    else:
        top_agent = sales_by_agent.idxmax()
        # Ensure string
        if pd.isna(top_agent):
            top_agent = None
        else:
            top_agent = str(top_agent)

# Prepare output JSON-serializable string
out = json.dumps(top_agent)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_lu5BsEnVvzmNGLWmGAO77Opx': 'file_storage/call_lu5BsEnVvzmNGLWmGAO77Opx.json', 'var_call_gm3AD9dbCXBI2n2Y4qkcL5ZS': 'file_storage/call_gm3AD9dbCXBI2n2Y4qkcL5ZS.json', 'var_call_hiQce4hJ5zYaUEr5tYR6Iv7l': 'file_storage/call_hiQce4hJ5zYaUEr5tYR6Iv7l.json', 'var_call_TSR6sZPUxDAJ2LQg3ZD18sxX': 'file_storage/call_TSR6sZPUxDAJ2LQg3ZD18sxX.json'}

exec(code, env_args)
