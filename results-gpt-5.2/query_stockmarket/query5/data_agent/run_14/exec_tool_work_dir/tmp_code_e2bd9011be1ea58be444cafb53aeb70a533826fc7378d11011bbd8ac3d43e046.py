code = """import json, pandas as pd
from pathlib import Path

prior = var_call_mA403jh9R1Bu4KDfW34Zcfk9  # already a dict
syms = prior['symbols_sample']
trade_tables = set(json.loads(Path(var_call_wiTjaVSyXiJ9Z5mRdl3fhPV8).read_text()))
syms_in_trade = [s for s in syms if s in trade_tables]

print('__RESULT__:')
print(json.dumps({'n_syms_considered': len(syms), 'n_in_trade_db': len(syms_in_trade), 'syms_in_trade': syms_in_trade}))"""

env_args = {'var_call_uLyJm1FW9XUZpkWFLLdTk1x8': 'file_storage/call_uLyJm1FW9XUZpkWFLLdTk1x8.json', 'var_call_mA403jh9R1Bu4KDfW34Zcfk9': {'n_total_symbols': 86, 'n_common_symbols': 76, 'symbols_sample': ['AGMH', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT']}, 'var_call_wiTjaVSyXiJ9Z5mRdl3fhPV8': 'file_storage/call_wiTjaVSyXiJ9Z5mRdl3fhPV8.json'}

exec(code, env_args)
