code = """import json

# Load existing results
results = [
    {'symbol': 'AGMH', 'volatile_days': 13},
    {'symbol': 'ALACU', 'volatile_days': 0},
    {'symbol': 'BCLI', 'volatile_days': 0},
    {'symbol': 'BHAT', 'volatile_days': 10},
    {'symbol': 'BIOC', 'volatile_days': 21},
    {'symbol': 'BKYI', 'volatile_days': 16},
    {'symbol': 'BLFS', 'volatile_days': 0},
    {'symbol': 'BOTJ', 'volatile_days': 0},
    {'symbol': 'BOSC', 'volatile_days': 3},
    {'symbol': 'BWEN', 'volatile_days': 5},
    {'symbol': 'CBAT', 'volatile_days': 23},
    {'symbol': 'CCCL', 'volatile_days': 13},
    {'symbol': 'CDMOP', 'volatile_days': 0},
    {'symbol': 'CEMI', 'volatile_days': 3},
    {'symbol': 'CFBK', 'volatile_days': 0},
    {'symbol': 'CFFA', 'volatile_days': 0},
    {'symbol': 'CLRB', 'volatile_days': 14},
    {'symbol': 'CORV', 'volatile_days': 10}
]

# Add results from most recent queries
cbat_result = locals()['var_functions.query_db:70']
cccl_result = locals()['var_functions.query_db:72']
cdmop_result = locals()['var_functions.query_db:74']
cemi_result = locals()['var_functions.query_db:76']
cfbk_result = locals()['var_functions.query_db:78']
cffa_result = locals()['var_functions.query_db:80']
clrb_result = locals()['var_functions.query_db:82']
corv_result = locals()['var_functions.query_db:84']

# Already added above - just need to get top 5
top_5 = sorted(results, key=lambda x: x['volatile_days'], reverse=True)[:5]

print('Current complete results:', results)
print('Top 5 so far:', top_5)

print('__RESULT__:')
print(json.dumps({'top_5_current': top_5, 'total_processed': len(results)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:6': 'file_storage/functions.list_db:6.json', 'var_functions.execute_python:12': {'total_companies': 86, 'sample': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}]}, 'var_functions.execute_python:18': {'available_vars': ['var_functions.query_db:0', 'var_functions.list_db:6', 'var_functions.execute_python:12']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'Symbol': 'AGMH'}, {'Symbol': 'ALACU'}, {'Symbol': 'AMHC'}, {'Symbol': 'ANDA'}, {'Symbol': 'APEX'}, {'Symbol': 'BCLI'}, {'Symbol': 'BHAT'}, {'Symbol': 'BIOC'}, {'Symbol': 'BKYI'}, {'Symbol': 'BLFS'}, {'Symbol': 'BOSC'}, {'Symbol': 'BOTJ'}, {'Symbol': 'BWEN'}, {'Symbol': 'CBAT'}, {'Symbol': 'CCCL'}, {'Symbol': 'CDMOP'}, {'Symbol': 'CEMI'}, {'Symbol': 'CFBK'}, {'Symbol': 'CFFA'}, {'Symbol': 'CLRB'}, {'Symbol': 'CORV'}, {'Symbol': 'CPAAU'}, {'Symbol': 'CPAH'}, {'Symbol': 'CUBA'}, {'Symbol': 'CVV'}, {'Symbol': 'DZSI'}, {'Symbol': 'ELSE'}, {'Symbol': 'EXPC'}, {'Symbol': 'EYEG'}, {'Symbol': 'FAMI'}, {'Symbol': 'FNCB'}, {'Symbol': 'FSBW'}, {'Symbol': 'FTFT'}, {'Symbol': 'GDYN'}, {'Symbol': 'GLG'}, {'Symbol': 'GRNVU'}, {'Symbol': 'GTEC'}, {'Symbol': 'HCCOU'}, {'Symbol': 'HNNA'}, {'Symbol': 'HQI'}, {'Symbol': 'HRTX'}, {'Symbol': 'IDEX'}, {'Symbol': 'IGIC'}, {'Symbol': 'IOTS'}, {'Symbol': 'ISNS'}, {'Symbol': 'ITI'}, {'Symbol': 'LACQ'}, {'Symbol': 'MBCN'}, {'Symbol': 'MBNKP'}, {'Symbol': 'MCEP'}, {'Symbol': 'MLND'}, {'Symbol': 'MMAC'}, {'Symbol': 'MNCLU'}, {'Symbol': 'MNPR'}, {'Symbol': 'NVEE'}, {'Symbol': 'NXTD'}, {'Symbol': 'OPOF'}, {'Symbol': 'OPTT'}, {'Symbol': 'ORGO'}, {'Symbol': 'ORSNU'}, {'Symbol': 'OTEL'}, {'Symbol': 'PBFS'}, {'Symbol': 'PBTS'}, {'Symbol': 'PCSB'}, {'Symbol': 'PECK'}, {'Symbol': 'PEIX'}, {'Symbol': 'PFIE'}, {'Symbol': 'PLIN'}, {'Symbol': 'POPE'}, {'Symbol': 'QRHC'}, {'Symbol': 'SES'}, {'Symbol': 'SHSP'}, {'Symbol': 'SNSS'}, {'Symbol': 'SSNT'}, {'Symbol': 'STKS'}, {'Symbol': 'TGLS'}, {'Symbol': 'TMSR'}, {'Symbol': 'VERB'}, {'Symbol': 'VMD'}, {'Symbol': 'VRRM'}, {'Symbol': 'VTIQW'}, {'Symbol': 'VVPR'}, {'Symbol': 'WHLM'}, {'Symbol': 'WHLR'}, {'Symbol': 'XBIOW'}, {'Symbol': 'XPEL'}], 'var_functions.list_db:26': 'file_storage/functions.list_db:26.json', 'var_functions.execute_python:30': {'nasdaq_tickers_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'total': 86}, 'var_functions.query_db:32': [{'volatile_days': '13'}], 'var_functions.query_db:40': [{'volatile_days': '0'}], 'var_functions.query_db:42': [{'volatile_days': '0'}], 'var_functions.query_db:44': [{'volatile_days': '10'}], 'var_functions.execute_python:46': {'nasdaq_tickers_count': 86, 'available_tables_count': 2753, 'available_nasdaq_tickers': 86, 'sample_available': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_functions.query_db:48': [{'volatile_days': '21'}], 'var_functions.query_db:50': [{'volatile_days': '16'}], 'var_functions.execute_python:52': {'processed': 6, 'current_top': [{'symbol': 'BIOC', 'volatile_days': 21}, {'symbol': 'BKYI', 'volatile_days': 16}, {'symbol': 'AGMH', 'volatile_days': 13}]}, 'var_functions.query_db:54': [{'volatile_days': '0'}], 'var_functions.query_db:58': [{'volatile_days': '0'}], 'var_functions.query_db:62': [{'volatile_days': '3'}], 'var_functions.query_db:64': [{'volatile_days': '5'}], 'var_functions.query_db:70': [{'volatile_days': '23'}], 'var_functions.query_db:72': [{'volatile_days': '13'}], 'var_functions.query_db:74': [{'volatile_days': '0'}], 'var_functions.query_db:76': [{'volatile_days': '3'}], 'var_functions.query_db:78': [{'volatile_days': '0'}], 'var_functions.query_db:80': [{'volatile_days': '0'}], 'var_functions.query_db:82': [{'volatile_days': '14'}], 'var_functions.query_db:84': [{'volatile_days': '10'}]}

exec(code, env_args)
