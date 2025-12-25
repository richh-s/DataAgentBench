code = """import json

# Data from var_call_uh6DEPAq0HuUrYhUqbq24buT (exchanges) and var_call_76Bblfl81nm9IqfJ1zCmweAJ (index up/down)
exchanges = var_call_uh6DEPAq0HuUrYhUqbq24buT
index_counts = var_call_76Bblfl81nm9IqfJ1zCmweAJ

# Map indices to regions manually based on exchange names / known associations
# First map exchange -> region
exchange_region = {
    'New York Stock Exchange': 'North America',
    'NASDAQ': 'North America',
    'Toronto Stock Exchange': 'North America',
    'Hong Kong Stock Exchange': 'Asia',
    'Shanghai Stock Exchange': 'Asia',
    'Shenzhen Stock Exchange': 'Asia',
    'Tokyo Stock Exchange': 'Asia',
    'National Stock Exchange of India': 'Asia',
    'Frankfurt Stock Exchange': 'Europe',
    'Euronext': 'Europe',
    'SIX Swiss Exchange': 'Europe',
    'Taiwan Stock Exchange': 'Asia',
    'Johannesburg Stock Exchange': 'Africa',
}

# Manually map index symbol -> exchange based on typical major indices
index_exchange = {
    'NYA': 'New York Stock Exchange',   # NYSE Composite
    'IXIC': 'NASDAQ',                   # Nasdaq Composite
    'GSPTSE': 'Toronto Stock Exchange', # S&P/TSX Composite
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'NSEI': 'National Stock Exchange of India',
    'GDAXI': 'Frankfurt Stock Exchange',
    'N100': 'Euronext',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'J203.JO': 'Johannesburg Stock Exchange',
}

# Determine which indices are in North America
north_american_indices = []
for rec in index_counts:
    idx = rec['Index']
    exch = index_exchange.get(idx)
    region = exchange_region.get(exch) if exch else None
    if region == 'North America':
        # compare up vs down days (values are strings, convert to float or int)
        up = float(rec['up_days'])
        down = float(rec['down_days'])
        if up > down:
            north_american_indices.append(idx)

result = north_american_indices

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9aPtlZxaudegALtIx54Tgw2g': ['index_info'], 'var_call_5YZHrqxxZSMwtOfe5nTjCmZN': ['index_trade'], 'var_call_uh6DEPAq0HuUrYhUqbq24buT': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_Gxm2uordqAtTIQ7asqklxzQ0': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_qCSLlmWlMahlh4p6kfFC7I74': [{'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}], 'var_call_Ua3PHMHmPnl1DvFsl4cn6nqd': [{'Date': '01 Apr 1969, 00:00'}, {'Date': '01 Apr 1971, 00:00'}, {'Date': '01 Apr 1974, 00:00'}, {'Date': '01 Apr 1975, 00:00'}, {'Date': '01 Apr 1976, 00:00'}], 'var_call_2R1PMkIgrNi7ClbtzhDCmxSH': [{'Date': 'January 02, 1973 at 12:00 AM'}, {'Date': 'January 02, 1974 at 12:00 AM'}, {'Date': 'January 02, 1975 at 12:00 AM'}, {'Date': 'January 02, 1979 at 12:00 AM'}, {'Date': 'January 02, 1981 at 12:00 AM'}], 'var_call_76Bblfl81nm9IqfJ1zCmweAJ': [{'Index': 'N225', 'up_days': '86.0', 'down_days': '86.0'}, {'Index': 'GSPTSE', 'up_days': '71.0', 'down_days': '94.0'}, {'Index': 'NSEI', 'up_days': '75.0', 'down_days': '91.0'}, {'Index': 'GDAXI', 'up_days': '66.0', 'down_days': '87.0'}, {'Index': 'NYA', 'up_days': '88.0', 'down_days': '84.0'}, {'Index': 'N100', 'up_days': '95.0', 'down_days': '92.0'}, {'Index': '399001.SZ', 'up_days': '82.0', 'down_days': '85.0'}, {'Index': 'HSI', 'up_days': '76.0', 'down_days': '84.0'}, {'Index': 'J203.JO', 'up_days': '88.0', 'down_days': '80.0'}, {'Index': '000001.SS', 'up_days': '78.0', 'down_days': '81.0'}, {'Index': 'SSMI', 'up_days': '73.0', 'down_days': '83.0'}, {'Index': 'TWII', 'up_days': '90.0', 'down_days': '77.0'}, {'Index': 'IXIC', 'up_days': '87.0', 'down_days': '89.0'}]}

exec(code, env_args)
