code = """import json
import pandas as pd

# Load the data from the file
with open(var_functions.query_db:5, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert Open and Close to numeric
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Add a column to identify up/down days
df['direction'] = df.apply(lambda row: 'up' if row['Close'] > row['Open'] else ('down' if row['Close'] < row['Open'] else 'flat'), axis=1)

# Group by index and count up/down days
results = []
for index_name in df['Index'].unique():
    index_data = df[df['Index'] == index_name]
    up_days = (index_data['direction'] == 'up').sum()
    down_days = (index_data['direction'] == 'down').sum()
    flat_days = (index_data['direction'] == 'flat').sum()
    
    results.append({
        'Index': index_name,
        'Up Days': int(up_days),
        'Down Days': int(down_days),
        'Flat Days': int(flat_days),
        'Total Days': int(up_days + down_days + flat_days),
        'Net Days': int(up_days - down_days)
    })

# Create results DataFrame
results_df = pd.DataFrame(results)

# Filter indices with more up days than down days
winners_df = results_df[results_df['Net Days'] > 0]

print('__RESULT__:')
print(results_df.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
