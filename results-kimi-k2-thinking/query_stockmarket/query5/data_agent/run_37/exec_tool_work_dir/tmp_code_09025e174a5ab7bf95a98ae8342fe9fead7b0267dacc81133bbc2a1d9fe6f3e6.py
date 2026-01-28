code = """import json

# Get the NASDAQ Capital Market symbols from previous result
nasdaq_result_key = 'var_functions.query_db:0'
result_file = locals()[nasdaq_result_key]

with open(result_file, 'r') as f:
    nasdaq_capital_stocks = json.load(f)

nasdaq_symbols = set([stock['Symbol'] for stock in nasdaq_capital_stocks])
print('__RESULT__:')
print(json.dumps(list(nasdaq_symbols)[:20]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_symbols': 86, 'sample_symbols': [['AGMH', 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'], ['ALACU', 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'], ['AMHC', 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'], ['ANDA', 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'], ['APEX', 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.']]}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
