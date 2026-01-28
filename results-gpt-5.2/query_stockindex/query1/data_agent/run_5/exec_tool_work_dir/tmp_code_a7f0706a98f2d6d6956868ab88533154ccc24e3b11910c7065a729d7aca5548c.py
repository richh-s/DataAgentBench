code = """import json, pandas as pd

trade = pd.DataFrame(var_call_Z3bvjmTwtLAjmyFhPLPbJrjR)
# infer Asia indices present in dataset
asia_indices = {
    'N225': 'Japan (Tokyo Stock Exchange) - Nikkei 225',
    'HSI': 'Hong Kong (Hong Kong Stock Exchange) - Hang Seng Index',
    'TWII': 'Taiwan (Taiwan Stock Exchange) - TAIEX',
    '000001.SS': 'China (Shanghai Stock Exchange) - SSE Composite',
    '399001.SZ': 'China (Shenzhen Stock Exchange) - SZSE Component',
    'NSEI': 'India (NSE) - NIFTY 50'
}

# parse date cutoff to match data format: include any dates with year >= 2020
# We'll query DB directly for required indices from 2020 onward using string match on year.
print('__RESULT__:')
print(json.dumps({'asia_indices': list(asia_indices.keys())}))"""

env_args = {'var_call_TNZzkoDMs5rTuyjR5LIAzWOO': ['index_info'], 'var_call_R0rwZxNQSSesR015YCiLaPYb': ['index_trade'], 'var_call_Z3bvjmTwtLAjmyFhPLPbJrjR': [{'idx': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'idx': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'idx': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'idx': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'idx': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'idx': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}]}

exec(code, env_args)
