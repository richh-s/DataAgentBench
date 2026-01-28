code = """import json
import pandas as pd

# Load the query result stored in a file path variable provided by the previous query_db call
data_file = var_call_LnzM4yjCRvVFShkQhShOCsHT
with open(data_file, 'r') as f:
    records = json.load(f)

# Create DataFrame
df = pd.DataFrame(records)
# Convert numeric fields to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Determine up/down/tie
df['up'] = (df['Close'] > df['Open']).astype(int)
df['down'] = (df['Close'] < df['Open']).astype(int)

# Aggregate by Index
agg = df.groupby('Index').agg({'up':'sum','down':'sum'}).reset_index()

# Identify North American indices from the dataset we queried (these were the NA indices)
# The query included GSPTSE (Canada), IXIC (NASDAQ), NYA (NYSE)
na_indices = ['GSPTSE','IXIC','NYA']

# Filter agg for these indices
agg_na = agg[agg['Index'].isin(na_indices)].copy()

# Determine which had more up days than down days
agg_na['more_up_than_down'] = agg_na['up'] > agg_na['down']

# Build result
result_list = []
for _, row in agg_na.iterrows():
    result_list.append({
        'Index': row['Index'],
        'up_days': int(row['up']),
        'down_days': int(row['down']),
        'more_up_than_down': bool(row['more_up_than_down'])
    })

# Also produce a concise list of indices that had more up days
indices_more_up = [r['Index'] for r in result_list if r['more_up_than_down']]

output = {
    'results_by_index': result_list,
    'indices_with_more_up_days': indices_more_up
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ikOlomFrSPKCZ7qJ4Sap4DqH': ['index_trade'], 'var_call_kHXPsO0DMUWCO29PqaldjOXt': ['index_info'], 'var_call_zgfuSPz5JMNs7pSslLei8Yjt': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_LnzM4yjCRvVFShkQhShOCsHT': 'file_storage/call_LnzM4yjCRvVFShkQhShOCsHT.json'}

exec(code, env_args)
