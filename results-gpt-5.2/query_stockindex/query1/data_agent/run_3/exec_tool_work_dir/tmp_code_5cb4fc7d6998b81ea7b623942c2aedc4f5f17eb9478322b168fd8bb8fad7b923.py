code = """import json
# From metadata + common mappings per prompt hint
asia = {
  'HSI': 'Hang Seng Index (Hong Kong)',
  '000001.SS': 'SSE Composite (Shanghai)',
  '399001.SZ': 'Shenzhen Component (Shenzhen)',
  'N225': 'Nikkei 225 (Tokyo)',
  'NSEI': 'NIFTY 50 (India)',
  'TWII': 'TAIEX (Taiwan)'
}
rows = var_call_7kniOmCmHVtllHYE0z70vFxP
# ensure numeric
for r in rows:
    r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
# filter to asia
asia_rows = [r for r in rows if r['Index'] in asia]
# best
best = max(asia_rows, key=lambda r: r['avg_intraday_vol'])
result = {
  'index_symbol': best['Index'],
  'index_name': asia[best['Index']],
  'avg_intraday_volatility': best['avg_intraday_vol'],
  'avg_intraday_volatility_pct': best['avg_intraday_vol']*100
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3jOVSuUFynpTMiwiRA4Cm5V8': ['index_info'], 'var_call_5pblCiXo5mjbYVJotumE4MGS': ['index_trade'], 'var_call_RkEzPnrtO0msehRttrnvRCOK': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_dIRYn4acNN0onwiIKmz8fWCW': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_7kniOmCmHVtllHYE0z70vFxP': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'GDAXI', 'avg_intraday_vol': '0.013633557197891789'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'J203.JO', 'avg_intraday_vol': '0.012946183900303701'}, {'Index': 'SSMI', 'avg_intraday_vol': '0.012884854571066692'}, {'Index': 'N100', 'avg_intraday_vol': '0.012567255105983891'}, {'Index': 'IXIC', 'avg_intraday_vol': '0.009869805134210418'}, {'Index': 'GSPTSE', 'avg_intraday_vol': '0.009024336652288918'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}, {'Index': 'NYA', 'avg_intraday_vol': '0.004147514635438383'}]}

exec(code, env_args)
