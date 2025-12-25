code = """import json

index_map = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI',
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': None,  # no direct index symbol in trade data
    'Taiwan Stock Exchange': 'TWII',
    'Johannesburg Stock Exchange': 'J203.JO',
    'New York Stock Exchange': 'NYA',
    'NASDAQ': 'IXIC',
    'Euronext': 'N100',
    'Frankfurt Stock Exchange': 'GDAXI',
    'SIX Swiss Exchange': 'SSMI',
    'Toronto Stock Exchange': 'GSPTSE'
}

asia_exchanges = {
    'Tokyo Stock Exchange',
    'Hong Kong Stock Exchange',
    'Shanghai Stock Exchange',
    'Shenzhen Stock Exchange',
    'National Stock Exchange of India',
    'Korea Exchange',
    'Taiwan Stock Exchange'
}

asia_indices = [index for ex, index in index_map.items() if ex in asia_exchanges and index is not None]

result = json.dumps({'asia_indices': asia_indices})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_WfEs6juHOs41b9mxJDYqOr23': ['index_info'], 'var_call_n7QyTWxdQjWhLIrAZYBlnORG': ['index_trade'], 'var_call_2X1zTzJNQUSlzevAgH8AzzrI': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_haS1578moaPKB4MEhQLK4lOe': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'HSI'}]}

exec(code, env_args)
