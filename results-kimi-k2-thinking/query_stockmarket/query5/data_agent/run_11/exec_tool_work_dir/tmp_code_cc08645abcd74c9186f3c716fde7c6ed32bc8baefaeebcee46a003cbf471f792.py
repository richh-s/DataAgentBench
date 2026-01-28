code = """import json
import pandas as pd

# Read company mapping
stockinfo_path = locals()['var_functions.query_db:0']
if isinstance(stockinfo_path, str):
    with open(stockinfo_path, 'r') as f:
        stockinfo_data = json.load(f)
else:
    stockinfo_data = locals()['var_functions.query_db:0']

company_map = {item['Symbol']: item['Company Description'] for item in stockinfo_data}

# List of symbols to process
symbols = ["SES", "POPE", "PCSB", "CEMI", "PBTS", "MCEP", "MNPR", "ANDA", "IGIC", "WHLR", "AEGN", "CPSR", "YTRA", "MCC", "RHE", "FSTR", "CPSH", "PRPO", "MCHX", "BLCM", "BCDA", "MBII", "GLG", "FCRE", "DWIN", "BKYI", "CFBK", "ALACU", "ATXI", "AMHC", "GRNVU", "BCLI", "AGMH", "CLRB", "CPAAU", "BOSC", "BVSN", "CHFS", "BVXV", "CANF", "CORV", "CSSE", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "HEPA", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IOTS", "JFK", "LJPC", "MTP", "NEPT", "NKTR", "NSYS", "NXTD", "ONCY", "OSS", "PBMD", "PFMT", "PLXP", "PSTV", "REED", "RLMD", "RMTI", "SHIP", "SNMP", "SPNV", "TANH", "TKAT", "TMDI", "TRIB", "TTOO", "VBIV", "VYGR", "WHLM", "YJ"]

# Stock trade data paths
stocktrade_paths = {
    "SES": locals()['var_functions.query_db:10'],
    "POPE": locals()['var_functions.query_db:16'],
    "PCSB": locals()['var_functions.query_db:18']
}

# Initialize results
results = []

# Process available data
for symbol in ["SES", "POPE", "PCSB"]:
    path = stocktrade_paths[symbol]
    if isinstance(path, str):
        with open(path, 'r') as f:
            data = json.load(f)
    else:
        data = path
    
    if data:
        df = pd.DataFrame(data)
        df['High'] = pd.to_numeric(df['High'])
        df['Low'] = pd.to_numeric(df['Low'])
        df['range'] = df['High'] - df['Low']
        df['threshold'] = df['Low'] * 0.20
        df['exceeds_20pct'] = df['range'] > df['threshold']
        
        count = df['exceeds_20pct'].sum()
        company_name = company_map.get(symbol, 'Unknown')
        
        results.append({
            'symbol': symbol,
            'company': company_name,
            'days_exceeding_20pct': int(count),
            'total_days': len(df)
        })

# Sort by days_exceeding_20pct descending
results_sorted = sorted(results, key=lambda x: x['days_exceeding_20pct'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': 'file_storage/functions.list_db:2.json', 'var_functions.execute_python:5': {'eligible_count': 86, 'sample_symbols': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR']}, 'var_functions.query_db:6': [{'Date': '2019-01-02', 'High': '7.28000020980835', 'Low': '5.840000152587891'}, {'Date': '2019-01-03', 'High': '7.28000020980835', 'Low': '6.400000095367432'}, {'Date': '2019-01-04', 'High': '8.319999694824219', 'Low': '6.480000019073486'}, {'Date': '2019-01-07', 'High': '7.039999961853027', 'Low': '6.960000038146973'}, {'Date': '2019-01-08', 'High': '7.039999961853027', 'Low': '6.400000095367432'}], 'var_functions.execute_python:8': {'symbols_to_process': 88, 'sample': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS']}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'symbol': 'SES', 'company': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.', 'days_2019': 252, 'days_exceeding_20pct': 51, 'calculation_logic_test': 'passed'}, 'var_functions.execute_python:14': {'status': 'starting_batch_process', 'total_symbols': 88, 'batch_size': 20, 'batches': 5, 'first_batch': ['SES', 'POPE', 'PCSB', 'CEMI', 'PBTS', 'MCEP', 'MNPR', 'ANDA', 'IGIC', 'WHLR', 'AEGN', 'CPSR', 'YTRA', 'MCC', 'RHE', 'FSTR', 'CPSH', 'PRPO', 'MCHX', 'BLCM']}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_symbols': 88, 'sample_queries': ['SELECT Date, High, Low FROM "SES" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'', 'SELECT Date, High, Low FROM "POPE" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\'', 'SELECT Date, High, Low FROM "PCSB" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\''], 'company_sample': {'SES': 'Synthesis Energy Systems, Inc. specializes in tran...', 'POPE': 'Pope Resources - Limited Partnership is dedicated ...', 'PCSB': 'PCSB Financial Corporation operates as a community...'}}}

exec(code, env_args)
