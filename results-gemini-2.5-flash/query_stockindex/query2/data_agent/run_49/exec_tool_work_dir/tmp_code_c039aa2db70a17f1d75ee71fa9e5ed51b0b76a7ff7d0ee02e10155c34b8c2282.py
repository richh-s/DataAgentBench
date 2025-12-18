code = """import pandas as pd
import json
data = pd.read_json(locals()['var_function-call-5387443059870327053'])
data['Open'] = pd.to_numeric(data['Open'])
data['Close'] = pd.to_numeric(data['Close'])

# Calculate up days and down days
data['UpDay'] = data['Close'] > data['Open']
data['DownDay'] = data['Close'] < data['Open']

up_down_counts = data.groupby('Index')[['UpDay', 'DownDay']].sum()
up_down_counts['MoreUpDays'] = up_down_counts['UpDay'] > up_down_counts['DownDay']

result = up_down_counts[up_down_counts['MoreUpDays']].index.tolist()
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-5124879492398262545': ['index_info'], 'var_function-call-8613833286282055731': ['index_trade'], 'var_function-call-13245814137437327966': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-5387443059870327053': 'file_storage/function-call-5387443059870327053.json'}

exec(code, env_args)
