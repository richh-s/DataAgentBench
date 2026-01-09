code = """import json, pandas as pd

# load company info
with open(var_call_lsWEadc109kwWv5jdXkUgWbB, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# load counts from both batches
counts1 = pd.DataFrame(var_call_se7wRvt0IxMH6ofL49wfG1Fd)
counts2 = pd.DataFrame(var_call_ff6YZFhvfR8XYj2f3poTxLBT)
counts = pd.concat([counts1, counts2], ignore_index=True)

# convert to numeric
for c in ['up_days','down_days']:
    counts[c] = pd.to_numeric(counts[c], errors='coerce')

# filter more up than down
counts = counts.dropna(subset=['up_days','down_days'])
counts = counts[counts['up_days'] > counts['down_days']].copy()

# rank by (up_days - down_days) desc, then up_days desc
counts['diff'] = counts['up_days'] - counts['down_days']
counts = counts.sort_values(['diff','up_days'], ascending=[False, False])

top5 = counts.head(5)

# join to company names
res = top5.merge(info_df, on='Symbol', how='left')
answer_list = res['company_name'].tolist()

print('__RESULT__:')
print(json.dumps({'top5': answer_list, 'details': res[['Symbol','company_name','up_days','down_days','diff']].to_dict(orient='records')}))"""

env_args = {'var_call_lsWEadc109kwWv5jdXkUgWbB': 'file_storage/call_lsWEadc109kwWv5jdXkUgWbB.json', 'var_call_VDn7pDm6A1YBRdsQaIjs0gEy': 'file_storage/call_VDn7pDm6A1YBRdsQaIjs0gEy.json', 'var_call_xSqbgAv8TtV5xeodQAmRI5Vl': {'n_symbols': 234, 'n_batches': 2}, 'var_call_se7wRvt0IxMH6ofL49wfG1Fd': [{'Symbol': 'AEFC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AIN', 'up_days': '143.0', 'down_days': '101.0'}, {'Symbol': 'AIV', 'up_days': '118.0', 'down_days': '128.0'}, {'Symbol': 'AIZP', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'AJRD', 'up_days': '123.0', 'down_days': '123.0'}, {'Symbol': 'AL', 'up_days': '131.0', 'down_days': '117.0'}, {'Symbol': 'AMN', 'up_days': '134.0', 'down_days': '111.0'}, {'Symbol': 'AMP', 'up_days': '141.0', 'down_days': '110.0'}, {'Symbol': 'AMT', 'up_days': '128.0', 'down_days': '123.0'}, {'Symbol': 'ARD', 'up_days': '80.0', 'down_days': '119.0'}, {'Symbol': 'ARGD', 'up_days': '133.0', 'down_days': '82.0'}, {'Symbol': 'ARLO', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'ASG', 'up_days': '110.0', 'down_days': '110.0'}, {'Symbol': 'AVA', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'BANC', 'up_days': '108.0', 'down_days': '119.0'}, {'Symbol': 'BBU', 'up_days': '129.0', 'down_days': '120.0'}, {'Symbol': 'BBVA', 'up_days': '126.0', 'down_days': '104.0'}, {'Symbol': 'BDXA', 'up_days': '83.0', 'down_days': '77.0'}, {'Symbol': 'BKH', 'up_days': '134.0', 'down_days': '115.0'}, {'Symbol': 'BKT', 'up_days': '105.0', 'down_days': '97.0'}, {'Symbol': 'BLD', 'up_days': '131.0', 'down_days': '120.0'}, {'Symbol': 'BNS', 'up_days': '132.0', 'down_days': '117.0'}, {'Symbol': 'BV', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'BZH', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CADE', 'up_days': '88.0', 'down_days': '83.0'}, {'Symbol': 'CAE', 'up_days': '122.0', 'down_days': '117.0'}, {'Symbol': 'CAF', 'up_days': '131.0', 'down_days': '113.0'}, {'Symbol': 'CBT', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'CCC', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CCZ', 'up_days': '17.0', 'down_days': '10.0'}, {'Symbol': 'CHAP', 'up_days': '34.0', 'down_days': '23.0'}, {'Symbol': 'CIA', 'up_days': '130.0', 'down_days': '112.0'}, {'Symbol': 'CMA', 'up_days': '124.0', 'down_days': '124.0'}, {'Symbol': 'CMI', 'up_days': '127.0', 'down_days': '123.0'}, {'Symbol': 'CMSA', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'CNK', 'up_days': '128.0', 'down_days': '122.0'}, {'Symbol': 'COTY', 'up_days': '124.0', 'down_days': '123.0'}, {'Symbol': 'CRC', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CRM', 'up_days': '137.0', 'down_days': '113.0'}, {'Symbol': 'CRS', 'up_days': '121.0', 'down_days': '128.0'}, {'Symbol': 'CSL', 'up_days': '131.0', 'down_days': '119.0'}, {'Symbol': 'CTS', 'up_days': '113.0', 'down_days': '122.0'}, {'Symbol': 'CUBE', 'up_days': '133.0', 'down_days': '113.0'}, {'Symbol': 'CURO', 'up_days': '9.0', 'down_days': '7.0'}, {'Symbol': 'CVIA', 'up_days': 'nan', 'down_days': 'nan'}], 'var_call_NlakGaS25EgBGQvvIq3gMOH4': {'batch1_first10': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD'], 'batch2_first10': ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS']}, 'var_call_2OMLC53Uqla7QvSw3nw7nRpo': {'batch2_first20': ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL'], 'batch2_len': 34}, 'var_call_JayJhm6Qid6bf5Bvn4aGLJCI': {'batch2': ['SSD', 'STG', 'STL', 'STON', 'SYX', 'TBB', 'TCP', 'TDJ', 'TGP', 'TLYS', 'TNC', 'TPH', 'TRV', 'TTI', 'TUFN', 'TWTR', 'UHT', 'UIS', 'USX', 'UTL', 'VET', 'VGR', 'VHI', 'VIV', 'VKQ', 'VRT', 'VVI', 'WOR', 'WPG', 'WSM', 'X', 'YEXT', 'ZNH', 'ZTR']}, 'var_call_ff6YZFhvfR8XYj2f3poTxLBT': [{'Symbol': 'SSD', 'up_days': '134.0', 'down_days': '112.0'}, {'Symbol': 'STG', 'up_days': '97.0', 'down_days': '112.0'}, {'Symbol': 'STL', 'up_days': '121.0', 'down_days': '111.0'}, {'Symbol': 'STON', 'up_days': '134.0', 'down_days': '108.0'}, {'Symbol': 'SYX', 'up_days': '122.0', 'down_days': '121.0'}, {'Symbol': 'TBB', 'up_days': '28.0', 'down_days': '27.0'}, {'Symbol': 'TCP', 'up_days': '110.0', 'down_days': '139.0'}, {'Symbol': 'TDJ', 'up_days': '121.0', 'down_days': '112.0'}, {'Symbol': 'TGP', 'up_days': '114.0', 'down_days': '121.0'}, {'Symbol': 'TLYS', 'up_days': '125.0', 'down_days': '119.0'}, {'Symbol': 'TNC', 'up_days': '118.0', 'down_days': '121.0'}, {'Symbol': 'TPH', 'up_days': '135.0', 'down_days': '109.0'}, {'Symbol': 'TRV', 'up_days': '119.0', 'down_days': '131.0'}, {'Symbol': 'TTI', 'up_days': '112.0', 'down_days': '130.0'}, {'Symbol': 'TUFN', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'TWTR', 'up_days': '123.0', 'down_days': '126.0'}, {'Symbol': 'UHT', 'up_days': '135.0', 'down_days': '115.0'}, {'Symbol': 'UIS', 'up_days': '110.0', 'down_days': '112.0'}, {'Symbol': 'USX', 'up_days': 'nan', 'down_days': 'nan'}, {'Symbol': 'UTL', 'up_days': '135.0', 'down_days': '112.0'}, {'Symbol': 'VET', 'up_days': '109.0', 'down_days': '138.0'}, {'Symbol': 'VGR', 'up_days': '125.0', 'down_days': '121.0'}, {'Symbol': 'VHI', 'up_days': '123.0', 'down_days': '116.0'}, {'Symbol': 'VIV', 'up_days': '113.0', 'down_days': '130.0'}, {'Symbol': 'VKQ', 'up_days': '116.0', 'down_days': '116.0'}, {'Symbol': 'VRT', 'up_days': '106.0', 'down_days': '94.0'}, {'Symbol': 'VVI', 'up_days': '119.0', 'down_days': '118.0'}, {'Symbol': 'WOR', 'up_days': '125.0', 'down_days': '124.0'}, {'Symbol': 'WPG', 'up_days': '102.0', 'down_days': '141.0'}, {'Symbol': 'WSM', 'up_days': '126.0', 'down_days': '123.0'}, {'Symbol': 'X', 'up_days': '119.0', 'down_days': '128.0'}, {'Symbol': 'YEXT', 'up_days': '91.0', 'down_days': '88.0'}, {'Symbol': 'ZNH', 'up_days': '116.0', 'down_days': '125.0'}, {'Symbol': 'ZTR', 'up_days': '115.0', 'down_days': '111.0'}]}

exec(code, env_args)
