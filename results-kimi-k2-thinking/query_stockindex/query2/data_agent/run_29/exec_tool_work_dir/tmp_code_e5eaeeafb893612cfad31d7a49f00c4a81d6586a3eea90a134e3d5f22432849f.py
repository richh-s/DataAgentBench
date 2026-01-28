code = """import json
import pandas as pd

# Read the full result from the file
result_file = var_functions.query_db:10
with open(result_file, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Convert price columns to float
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)

# Determine up days (Close > Open) and down days (Close < Open)
# Exclude flat days (Close = Open)
df['Day_Type'] = df.apply(lambda row: 'Up' if row['Close'] > row['Open'] else ('Down' if row['Close'] < row['Open'] else 'Flat'), axis=1)

# Group by Index and count up/down days
summary = df.groupby(['Index', 'Day_Type']).size().unstack(fill_value=0)

# Calculate net days (Up - Down)
summary['Net_Days'] = summary.get('Up', 0) - summary.get('Down', 0)

# Identify indices with more up days than down days
indices_more_up = summary[summary['Net_Days'] > 0].index.tolist()

# Get detailed counts for all North American indices
result_details = []
for idx in ['IXIC', 'NYA', 'GSPTSE']:
    if idx in summary.index:
        up_days = summary.loc[idx].get('Up', 0)
        down_days = summary.loc[idx].get('Down', 0)
        flat_days = summary.loc[idx].get('Flat', 0)
        total_days = up_days + down_days + flat_days
        result_details.append({
            'Index': idx,
            'Up_Days': int(up_days),
            'Down_Days': int(down_days),
            'Flat_Days': int(flat_days),
            'Total_Days': int(total_days),
            'Net_Days': int(summary.loc[idx]['Net_Days'])
        })

# Format final answer
final_answer = []
for idx_info in result_details:
    if idx_info['Net_Days'] > 0:
        final_answer.append(f"{idx_info['Index']}: {idx_info['Up_Days']} up days vs {idx_info['Down_Days']} down days (Net: +{idx_info['Net_Days']})")
    else:
        final_answer.append(f"{idx_info['Index']}: {idx_info['Up_Days']} up days vs {idx_info['Down_Days']} down days (Net: {idx_info['Net_Days']})")

if not final_answer:
    answer_text = "No North American indices had more up days than down days in 2018."
else:
    answer_text = "\n".join(final_answer)

print('__RESULT__:')
print(answer_text)"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:1': ['index_trade'], 'var_functions.query_db:4': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:5': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
