code = """import json
import os
import sys

# Load the list of NASDAQ Capital Market symbols from previous result
result_key = 'var_functions.execute_python:14'
symbols_data = locals()[result_key]

# Extract the full list
symbol_list = symbols_data['symbols']

print(f"Processing {len(symbol_list)} symbols...", file=sys.stderr)
print(f"First few symbols: {symbol_list[:5]}", file=sys.stderr)

# Create a summary with symbols to process
result = {
    'total_symbols': len(symbol_list),
    'symbols': symbol_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:2': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.list_db:5': 'file_storage/functions.list_db:5.json', 'var_functions.execute_python:6': {'total_nasdaq_capital_symbols': 86, 'available_in_trade_db': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:10': {'symbol': 'AGMH', 'total_days': 252, 'high_vol_days': 13}, 'var_functions.execute_python:12': {'total_symbols_to_process': 86, 'first_20_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_functions.execute_python:14': {'total_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
