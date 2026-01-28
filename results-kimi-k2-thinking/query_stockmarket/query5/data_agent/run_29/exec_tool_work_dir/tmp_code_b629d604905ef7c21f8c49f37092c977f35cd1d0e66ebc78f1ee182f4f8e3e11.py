code = """import json

# Load full results from previous steps
with open(locals()['var_functions.query_db:0'], 'r') as f:
    nasdaq_capital_stocks = json.load(f)

with open(locals()['var_functions.list_db:2'], 'r') as f:
    all_trade_tables = json.load(f)

# Get valid symbols
nasdaq_symbols = set(stock['Symbol'] for stock in nasdaq_capital_stocks)
trade_symbols = set(all_trade_tables)
valid_symbols = list(nasdaq_symbols.intersection(trade_symbols))

# Create company name mapping
def get_company_name(description):
    # Extract company name (text before first period)
    name = description.split('.')[0]
    # Remove trailing " Inc" or " Corp" etc if it's too long, but for now just return
    return name

company_map = {stock['Symbol']: get_company_name(stock['Company Description']) for stock in nasdaq_capital_stocks}

print('__RESULT__:')
print(json.dumps({
    'total_valid_symbols': len(valid_symbols),
    'symbols': valid_symbols,
    'company_map': company_map
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:6': {'nasdaq_capital_count': 86, 'trade_tables_count': 2753, 'valid_symbols_count': 86, 'sample_valid_symbols': ['CCCL', 'ELSE', 'BOTJ', 'CPAH', 'AMHC', 'MNPR', 'CPAAU', 'XBIOW', 'PECK', 'OTEL']}, 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': [{'Date': '2019-01-02', 'Open': '1.8200000524520876', 'High': '2.3499999046325684', 'Low': '1.7000000476837158', 'Close': '1.8899999856948853', 'Adj Close': '1.8899999856948853', 'Volume': '17102800'}, {'Date': '2019-01-03', 'Open': '1.7999999523162842', 'High': '1.8899999856948853', 'Low': '1.3799999952316284', 'Close': '1.3799999952316284', 'Adj Close': '1.3799999952316284', 'Volume': '2197600'}, {'Date': '2019-01-04', 'Open': '1.3600000143051147', 'High': '1.899999976158142', 'Low': '1.3600000143051147', 'Close': '1.6399999856948853', 'Adj Close': '1.6399999856948853', 'Volume': '7201200'}, {'Date': '2019-01-07', 'Open': '1.590000033378601', 'High': '1.6399999856948853', 'Low': '1.440000057220459', 'Close': '1.5800000429153442', 'Adj Close': '1.5800000429153442', 'Volume': '1078600'}, {'Date': '2019-01-08', 'Open': '1.559999942779541', 'High': '1.6100000143051147', 'Low': '1.440000057220459', 'Close': '1.5199999809265137', 'Adj Close': '1.5199999809265137', 'Volume': '574900'}], 'var_functions.execute_python:16': {'valid_symbols_count': 86, 'sample_symbols': ['CDMOP', 'BCLI', 'ITI', 'PCSB', 'CFFA', 'PBFS', 'PLIN', 'FTFT', 'FNCB', 'HCCOU'], 'company_map_sample': {'AGMH': 'AGM Group Holdings Inc', 'ALACU': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential', 'AMHC': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation', 'ANDA': 'Andina Acquisition Corp', 'APEX': 'Apex Global Brands Inc', 'BCLI': 'Brainstorm Cell Therapeutics Inc', 'BHAT': 'Blue Hat Interactive Entertainment Technology specializes in developing immersive gaming experiences and interactive entertainment solutions, captivating audiences worldwide with their innovative digital platforms', 'BIOC': 'Biocept, Inc', 'BKYI': 'BIO-key International, Inc', 'BLFS': 'BioLife Solutions, Inc'}}}

exec(code, env_args)
