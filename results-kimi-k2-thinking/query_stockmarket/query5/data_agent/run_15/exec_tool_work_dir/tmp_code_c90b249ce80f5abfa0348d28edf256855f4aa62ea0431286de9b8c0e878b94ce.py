code = """# Get all valid symbols and process them systematically
import json

# Read the valid symbols from file
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    all_symbols_data = json.load(f)

all_symbols = [item['Symbol'] for item in all_symbols_data]

# Known results from first 10 queries
known_results = {
    'AGMH': 13, 'ALACU': 0, 'AMHC': 0, 'ANDA': 0, 'APEX': 15,
    'BCLI': 0, 'BHAT': 10, 'BIOC': 21, 'BKYI': 16, 'BLFS': 0
}

# Remaining symbols to query
remaining_symbols = [s for s in all_symbols if s not in known_results]

print('Total Capital Market symbols:', len(all_symbols))
print('Already queried:', len(known_results))
print('Remaining to query:', len(remaining_symbols))
print('First 20 remaining:', remaining_symbols[:20])

print('__RESULT__:')
print(json.dumps({'remaining': remaining_symbols}))"""

env_args = {'var_functions.list_db:0': ['stockinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:14': {'status': 'checked'}, 'var_functions.execute_python:16': {'symbols_count': 86}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:26': {'status': 'checked'}, 'var_functions.query_db:28': [{'day_count': '13'}], 'var_functions.query_db:30': [{'day_count': '0'}], 'var_functions.execute_python:34': {'type': 'str'}, 'var_functions.execute_python:36': {'valid_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'count': 86}, 'var_functions.execute_python:38': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'var_functions.query_db:40': [{'day_count': '0'}], 'var_functions.query_db:42': [{'Symbol': 'ANDA', 'day_count': '0'}, {'Symbol': 'APEX', 'day_count': '15'}], 'var_functions.query_db:44': [{'Symbol': 'BCLI', 'day_count': '0'}, {'Symbol': 'BHAT', 'day_count': '10'}, {'Symbol': 'BIOC', 'day_count': '21'}, {'Symbol': 'BKYI', 'day_count': '16'}, {'Symbol': 'BLFS', 'day_count': '0'}], 'var_functions.execute_python:46': [{'Symbol': 'AGMH', 'day_count': 13}, {'Symbol': 'ALACU', 'day_count': 0}, {'Symbol': 'AMHC', 'day_count': 0}, {'Symbol': 'ANDA', 'day_count': 0}, {'Symbol': 'APEX', 'day_count': 15}, {'Symbol': 'BCLI', 'day_count': 0}, {'Symbol': 'BHAT', 'day_count': 10}, {'Symbol': 'BIOC', 'day_count': 21}, {'Symbol': 'BKYI', 'day_count': 16}, {'Symbol': 'BLFS', 'day_count': 0}]}

exec(code, env_args)
