code = """import json
import pandas as pd

# Load the larger dataset file
data_file = var_call_swl0GTtF6aN5DlhRDthREPOU
with open(data_file, 'r') as f:
    records = json.load(f)

df = pd.DataFrame(records)
# convert Open and Close to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# compute up/down/tie
df['up'] = (df['Close'] > df['Open']).astype(int)
df['down'] = (df['Close'] < df['Open']).astype(int)

# aggregate counts per Index
agg = df.groupby('Index').agg({'up':'sum','down':'sum'}).reset_index()

# Determine which indices are North American by mapping known indices to regions
# From earlier list of indices in DB, North American indices present include: GSPTSE (Canada), IXIC (NASDAQ, USA), NYA (NYSE, USA)
# There might be other North American indices not obvious; we'll select GSPTSE, IXIC, NYA as North America for this dataset.
na_indices = ['GSPTSE','IXIC','NYA']
agg_na = agg[agg['Index'].isin(na_indices)].copy()
agg_na['more_up_than_down'] = agg_na['up'] > agg_na['down']

result_list = []
for _, row in agg_na.iterrows():
    result_list.append({
        'Index': row['Index'],
        'up_days': int(row['up']),
        'down_days': int(row['down']),
        'more_up_than_down': bool(row['more_up_than_down'])
    })

indices_more_up = [r['Index'] for r in result_list if r['more_up_than_down']]

output = {'results_by_index': result_list, 'indices_with_more_up_days': indices_more_up}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ikOlomFrSPKCZ7qJ4Sap4DqH': ['index_trade'], 'var_call_kHXPsO0DMUWCO29PqaldjOXt': ['index_info'], 'var_call_zgfuSPz5JMNs7pSslLei8Yjt': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_LnzM4yjCRvVFShkQhShOCsHT': 'file_storage/call_LnzM4yjCRvVFShkQhShOCsHT.json', 'var_call_oxwBOHMutbxSBKLlr76upLUk': {'results_by_index': [{'Index': 'GSPTSE', 'up_days': 44, 'down_days': 41, 'more_up_than_down': True}, {'Index': 'IXIC', 'up_days': 44, 'down_days': 31, 'more_up_than_down': True}, {'Index': 'NYA', 'up_days': 36, 'down_days': 42, 'more_up_than_down': False}], 'indices_with_more_up_days': ['GSPTSE', 'IXIC']}, 'var_call_swl0GTtF6aN5DlhRDthREPOU': 'file_storage/call_swl0GTtF6aN5DlhRDthREPOU.json'}

exec(code, env_args)
