code = """import json
import pandas as pd

with open(var_call_m68jbtLvI9WvM3SmwBlWUERr, 'r') as f:
    businesses = json.load(f)

df_b = pd.DataFrame(businesses)

# basic stats
total = len(df_b)
attributes_notnull = df_b['attributes'].notnull().sum()
# extract wifi_attr raw
wifi_attr = df_b['attributes'].apply(lambda a: a.get('WiFi') if isinstance(a, dict) else (a if isinstance(a, str) else None))
wifi_attr_notnull = wifi_attr.notnull().sum()

# unique wifi values and counts (top 20)
val_counts = wifi_attr.fillna('NULL').value_counts().head(20).to_dict()

# sample rows
sample = df_b.head(50)[['business_id','attributes','description']].to_dict(orient='records')

result = {
    'total_rows': total,
    'attributes_notnull': int(attributes_notnull),
    'wifi_attr_notnull': int(wifi_attr_notnull),
    'wifi_attr_top_counts': val_counts,
    'sample_first_50': sample
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_m68jbtLvI9WvM3SmwBlWUERr': 'file_storage/call_m68jbtLvI9WvM3SmwBlWUERr.json', 'var_call_fVDfhyKnkuzxg50suzqi10DB': 'file_storage/call_fVDfhyKnkuzxg50suzqi10DB.json', 'var_call_AWI9RmHFlqMTNIVAjP60tCps': {'state': None, 'wifi_business_count': 0, 'average_rating': None}, 'var_call_51hd07zFeCaSF0tNTAAqBGBW': {'state': None, 'wifi_business_count': 0, 'average_rating': None}}

exec(code, env_args)
