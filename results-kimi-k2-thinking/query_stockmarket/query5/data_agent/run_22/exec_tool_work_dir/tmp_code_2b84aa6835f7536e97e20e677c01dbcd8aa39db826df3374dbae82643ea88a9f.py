code = """import json

# Get the available tickers from the database listing
var_name = 'var_functions.list_db:6'
print(f'Variable name: {var_name}')

try:
    data = locals()['var_functions.list_db:6']
    print(f'Type of data: {type(data)}')
    
    if isinstance(data, str) and data.endswith('.json'):
        print('Data is a JSON file path')
        with open(data, 'r') as f:
            available_tickers = json.load(f)
    elif isinstance(data, list):
        print('Data is a list')
        available_tickers = data
    else:
        print(f'Unexpected data type: {data}')
        available_tickers = []
        
    print(f'Number of available tickers: {len(available_tickers)}')
    
except Exception as e:
    print(f'Error accessing data: {e}')
    available_tickers = []

# If we have available tickers, also get the capital market tickers
if available_tickers:
    # Load capital market companies from the previous query
    cap_market_file = 'var_functions.query_db:0'
    try:
        cap_data = locals()['var_functions.query_db:0']
        if isinstance(cap_data, str) and cap_data.endswith('.json'):
            with open(cap_data, 'r') as f:
                capital_market_companies = json.load(f)
        elif isinstance(cap_data, list):
            capital_market_companies = cap_data
        else:
            print(f'Unexpected cap market data type: {cap_data}')
            capital_market_companies = []
            
        # Extract tickers and find intersection
        capital_tickers = [c['Symbol'] for c in capital_market_companies]
        common_tickers = list(set(capital_tickers) & set(available_tickers))
        
        print(f'Number of capital market tickers found in trade database: {len(common_tickers)}')
        
        result = {
            'available_tickers_sample': available_tickers[:10],
            'available_tickers_count': len(available_tickers),
            'capital_tickers_sample': capital_tickers[:10],
            'common_tickers_sample': common_tickers[:20],
            'common_tickers_count': len(common_tickers)
        }
        
    except Exception as e:
        print(f'Error loading capital market data: {e}')
        result = {}
else:
    result = {}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'num_companies': 86, 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json'}

exec(code, env_args)
