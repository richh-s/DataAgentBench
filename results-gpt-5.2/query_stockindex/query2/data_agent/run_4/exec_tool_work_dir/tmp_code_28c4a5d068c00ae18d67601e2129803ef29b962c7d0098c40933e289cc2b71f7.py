code = """import json
import pandas as pd

df = pd.DataFrame(var_call_IqZSQ4uAWzvvVPkEvbzQDoy9)
# convert to numeric
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices present: NYA (NYSE Composite, US), IXIC (NASDAQ Composite, US), GSPTSE (S&P/TSX Composite, Canada)
na = df[df['idx'].isin(['NYA','IXIC','GSPTSE'])].copy()
na['more_up_than_down'] = na['up_days'] > na['down_days']
res = na[na['more_up_than_down']].sort_values('idx')[['idx','up_days','down_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_LzfcDh0B2mblsXnLMioKz0u9': ['index_info'], 'var_call_UhFuQGX6j8uNF1g2aZiDU3n7': ['index_trade'], 'var_call_qFJ4zp9H7mmjBPewLVbLB1uh': [{'idx': 'J203.JO', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'N225', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'GSPTSE', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'NSEI', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'GDAXI', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'HSI', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'NYA', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': '000001.SS', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'SSMI', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'TWII', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'N100', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': '399001.SZ', 'up_days': '0.0', 'down_days': '0.0'}, {'idx': 'IXIC', 'up_days': '0.0', 'down_days': '0.0'}], 'var_call_RXN3dzBaAtzZ3Ts3QcE4VBpS': [{'Date': 'February 01, 1966 at 12:00 AM'}, {'Date': '07 Mar 1966, 00:00'}, {'Date': '1966-04-15 00:00:00'}, {'Date': '1966-06-27 00:00:00'}, {'Date': 'July 19, 1966 at 12:00 AM'}, {'Date': '21 Jul 1966, 00:00'}, {'Date': 'August 18, 1966 at 12:00 AM'}, {'Date': '28 Sep 1966, 00:00'}, {'Date': 'October 04, 1966 at 12:00 AM'}, {'Date': '1966-10-17 00:00:00'}, {'Date': 'December 06, 1966 at 12:00 AM'}, {'Date': '1966-12-21 00:00:00'}, {'Date': '1966-12-28 00:00:00'}, {'Date': '1967-02-13 00:00:00'}, {'Date': '29 Mar 1967, 00:00'}, {'Date': 'April 10, 1967 at 12:00 AM'}, {'Date': '11 Apr 1967, 00:00'}, {'Date': '1967-04-14 00:00:00'}, {'Date': '02 May 1967, 00:00'}, {'Date': '16 May 1967, 00:00'}], 'var_call_IqZSQ4uAWzvvVPkEvbzQDoy9': [{'idx': 'J203.JO', 'up_days': '125.0', 'down_days': '124.0'}, {'idx': 'N225', 'up_days': '118.0', 'down_days': '128.0'}, {'idx': 'GSPTSE', 'up_days': '115.0', 'down_days': '135.0'}, {'idx': 'NSEI', 'up_days': '115.0', 'down_days': '130.0'}, {'idx': 'GDAXI', 'up_days': '116.0', 'down_days': '135.0'}, {'idx': 'HSI', 'up_days': '120.0', 'down_days': '126.0'}, {'idx': 'NYA', 'up_days': '125.0', 'down_days': '126.0'}, {'idx': '000001.SS', 'up_days': '125.0', 'down_days': '118.0'}, {'idx': 'SSMI', 'up_days': '127.0', 'down_days': '122.0'}, {'idx': 'TWII', 'up_days': '129.0', 'down_days': '116.0'}, {'idx': 'N100', 'up_days': '127.0', 'down_days': '128.0'}, {'idx': '399001.SZ', 'up_days': '115.0', 'down_days': '128.0'}, {'idx': 'IXIC', 'up_days': '131.0', 'down_days': '120.0'}]}

exec(code, env_args)
