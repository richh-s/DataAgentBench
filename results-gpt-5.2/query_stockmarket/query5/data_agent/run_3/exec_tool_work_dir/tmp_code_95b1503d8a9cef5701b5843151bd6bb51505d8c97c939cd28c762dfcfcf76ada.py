code = """import json
import pandas as pd

# reload tickers list
recs = var_call_FDTiVhHjPWJOtuRiaNWYAxO3
keep = recs['tickers']
print('__RESULT__:')
print(json.dumps(keep))"""

env_args = {'var_call_1jRHFCBn80Hw8bnbXg2d1CCc': 'file_storage/call_1jRHFCBn80Hw8bnbXg2d1CCc.json', 'var_call_FDTiVhHjPWJOtuRiaNWYAxO3': {'n_tickers': 86, 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_Y8HiqZHE2vh4Lb58yzrw6R0a': 'file_storage/call_Y8HiqZHE2vh4Lb58yzrw6R0a.json', 'var_call_4Nar47QrwubGaZ8rZN8wUl25': {'keep_n': 50, 'missing_n': 0, 'missing': []}, 'var_call_duvySdEGloT9o03ChbmPD63u': {'note': 'keep not stored in previous result'}}

exec(code, env_args)
