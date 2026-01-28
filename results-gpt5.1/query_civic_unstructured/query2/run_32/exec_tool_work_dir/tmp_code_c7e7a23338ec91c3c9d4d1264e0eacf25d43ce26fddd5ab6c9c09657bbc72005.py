code = """import re, json, pandas as pd

path_docs = var_call_ucJw8ZGie7AloeiDzXj0hk4b
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_fund = var_call_qwRsUahRhTrhKZGh7QLUSWtV
with open(path_fund, 'r') as f:
    funding = json.load(f)

texts = '\n'.join(d['text'] for d in civic_docs)

completed_2022_park_names = [
    'Bluffs Park Shade Structure',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs'
]

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
mask = fund_df['Project_Name'].isin(completed_2022_park_names)

total = int(fund_df.loc[mask, 'Amount'].sum())

result = {"total_funding_completed_2022_park_projects": total,
          "projects": fund_df.loc[mask, ['Project_Name','Amount']].to_dict(orient='records')}

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_ucJw8ZGie7AloeiDzXj0hk4b': 'file_storage/call_ucJw8ZGie7AloeiDzXj0hk4b.json', 'var_call_qwRsUahRhTrhKZGh7QLUSWtV': 'file_storage/call_qwRsUahRhTrhKZGh7QLUSWtV.json'}

exec(code, env_args)
