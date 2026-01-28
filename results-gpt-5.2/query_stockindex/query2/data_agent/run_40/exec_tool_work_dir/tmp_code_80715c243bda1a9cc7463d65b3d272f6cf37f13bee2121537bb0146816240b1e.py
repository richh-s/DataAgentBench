code = """import json, pandas as pd

trade = pd.DataFrame(var_call_Kd8HjUNJ5rBZOTovFcDksH8F)
# coerce numeric
for c in ['n_days','up_days','down_days']:
    trade[c]=pd.to_numeric(trade[c])

# Map index symbol to exchange (from provided hint knowledge + index list)
index_to_exchange = {
    'NYA':'New York Stock Exchange',
    'IXIC':'NASDAQ',
    'GSPTSE':'Toronto Stock Exchange'
}

na = trade[trade['Index'].isin(index_to_exchange.keys())].copy()
na['Exchange']=na['Index'].map(index_to_exchange)
na['more_up_than_down']=na['up_days']>na['down_days']
res = na[na['more_up_than_down']][['Index','Exchange','up_days','down_days','n_days']].sort_values(['Exchange','Index']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_DJjYE8TCRaR7NjhBAHPFcLxH': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_9Mm03A9dLeuDWkSFEpccy6rm': [{'Index': '000001.SS', 'n_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': '399001.SZ', 'n_days': '76', 'up_days': '33.0', 'down_days': '43.0'}], 'var_call_O2dXiCMQNPTetxJ87WM2PDeA': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_Kd8HjUNJ5rBZOTovFcDksH8F': [{'Index': 'J203.JO', 'n_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'n_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'n_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'n_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'n_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'n_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'n_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'NYA', 'n_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'n_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'n_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'n_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'n_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'n_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
