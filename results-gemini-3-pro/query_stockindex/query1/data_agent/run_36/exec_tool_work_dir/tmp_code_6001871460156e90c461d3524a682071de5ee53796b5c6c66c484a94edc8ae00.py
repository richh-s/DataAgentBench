code = """import json

vol_data = locals()['var_function-call-18137126831047147376']

# Mapping Index to Region manually based on standard tickers
# N225: Japan (Asia)
# HSI: Hong Kong (Asia)
# 000001.SS: Shanghai (Asia)
# 399001.SZ: Shenzhen (Asia)
# NSEI: India (Asia)
# TWII: Taiwan (Asia)
# GDAXI: Germany (Europe)
# SSMI: Switzerland (Europe)
# N100: Euronext (Europe)
# J203.JO: South Africa (Africa)
# IXIC: USA (North America)
# NYA: USA (North America)
# GSPTSE: Canada (North America)

asia_indices = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII']

asian_volatility = []
for entry in vol_data:
    if entry['Index'] in asia_indices:
        asian_volatility.append(entry)

# Sort by volatility desc
asian_volatility.sort(key=lambda x: x['avg_volatility'], reverse=True)

print("__RESULT__:")
print(json.dumps(asian_volatility))"""

env_args = {'var_function-call-11314950928384246812': ['index_info'], 'var_function-call-11314950928384248485': ['index_trade'], 'var_function-call-18137126831047147376': [{'Index': '399001.SZ', 'avg_volatility': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_volatility': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_volatility': '0.01585173971531033'}, {'Index': 'HSI', 'avg_volatility': '0.01382304680245353'}, {'Index': 'GDAXI', 'avg_volatility': '0.013633557197891789'}, {'Index': 'TWII', 'avg_volatility': '0.01348835226084207'}, {'Index': 'J203.JO', 'avg_volatility': '0.012946183900303701'}, {'Index': 'SSMI', 'avg_volatility': '0.012884854571066692'}, {'Index': 'N100', 'avg_volatility': '0.012567255105983891'}, {'Index': 'IXIC', 'avg_volatility': '0.009869805134210418'}, {'Index': 'GSPTSE', 'avg_volatility': '0.009024336652288918'}, {'Index': 'N225', 'avg_volatility': '0.008720764073041308'}, {'Index': 'NYA', 'avg_volatility': '0.004147514635438383'}], 'var_function-call-18137126831047145549': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
