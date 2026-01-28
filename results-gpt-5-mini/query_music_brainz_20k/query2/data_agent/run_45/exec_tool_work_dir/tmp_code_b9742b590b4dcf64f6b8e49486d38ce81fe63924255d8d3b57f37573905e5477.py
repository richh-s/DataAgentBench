code = """import pandas as pd
import json

# Load sales data from previous query
sales = pd.DataFrame(var_call_MDAFfTRJqyWun2fJiNrPTmQH)
# Ensure numeric types
sales['revenue_usd'] = sales['revenue_usd'].astype(float)
# Aggregate revenue by store
group = sales.groupby('store', dropna=False)['revenue_usd'].sum().reset_index()
# Prepare breakdown dict with rounded values
breakdown = {row['store']: round(float(row['revenue_usd']), 2) for _, row in group.iterrows()}
# Identify top store
top_idx = group['revenue_usd'].idxmax()
top_row = group.loc[top_idx]
result = {
    'top_store': top_row['store'],
    'revenue_usd': round(float(top_row['revenue_usd']), 2),
    'currency': 'USD',
    'breakdown': breakdown
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_C6UTUqpHp5GqTbUCgYiDFv7R': ['tracks'], 'var_call_FeJdaGItxC3AebjaoDdUo3Jt': ['sales'], 'var_call_TzDQABqlmxITkX1bKTpzrMCc': [{'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005', 'source_id': '5', 'source_track_id': '10609996'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05", 'source_id': '3', 'source_track_id': '46130411MB-01'}, {'track_id': '14080', 'title': '011-Street Hype', 'artist': 'Bruce Maginnis', 'album': 'Groove City (2005)', 'year': 'None', 'source_id': '4', 'source_track_id': '149437-A02'}], 'var_call_MDAFfTRJqyWun2fJiNrPTmQH': [{'sale_id': '12386', 'track_id': '4122', 'country': 'Germany', 'store': 'Apple Music', 'units_sold': '47', 'revenue_usd': '47.52'}, {'sale_id': '12387', 'track_id': '4122', 'country': 'France', 'store': 'Amazon Music', 'units_sold': '262', 'revenue_usd': '304.13'}, {'sale_id': '13851', 'track_id': '4628', 'country': 'France', 'store': 'iTunes', 'units_sold': '469', 'revenue_usd': '505.61'}, {'sale_id': '42367', 'track_id': '14080', 'country': 'UK', 'store': 'Apple Music', 'units_sold': '59', 'revenue_usd': '68.68'}]}

exec(code, env_args)
