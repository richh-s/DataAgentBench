code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_8DQPbtO3dKYO6n32ZAdgBBVJ)
symbols = json.loads(symbols_path.read_text())
syms = [r['Symbol'] for r in symbols]

all_syms = syms

from pathlib import Path
trade_tables = json.loads(Path(var_call_VVzGVAQojORj5Kibor2gdtMq).read_text())
valid_syms = [s for s in all_syms if s in trade_tables]

batch_syms = valid_syms

code = json.dumps({'batch': batch_syms})
print('__RESULT__:')
print(code)"""

env_args = {'var_call_VVzGVAQojORj5Kibor2gdtMq': 'file_storage/call_VVzGVAQojORj5Kibor2gdtMq.json', 'var_call_8DQPbtO3dKYO6n32ZAdgBBVJ': 'file_storage/call_8DQPbtO3dKYO6n32ZAdgBBVJ.json', 'var_call_ZlC9TSlvUfmkMS88B3KIgmDY': {'symbols_subset': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'valid_in_trade_db': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_lbXuaNVRJvUb0wPdcCO7iAut': [{'cnt': '13'}], 'var_call_9OtbxWpi7uc0KO036vlhN2KB': [{'cnt': '0'}], 'var_call_mvZxIoImzYsMHD4r1GgrDSVV': [{'cnt': '0'}], 'var_call_fwX4HABsBR8QzhHfY9JCBhhQ': [{'cnt': '0'}], 'var_call_UNkh3cIBd5k4ASQDhnqTRGZ4': [{'cnt': '15'}], 'var_call_eKMYNmAVf9jBmUKi6HWkcGsv': [{'Symbol': 'APEX', 'cnt2019': 15}, {'Symbol': 'AGMH', 'cnt2019': 13}, {'Symbol': 'ALACU', 'cnt2019': 0}, {'Symbol': 'AMHC', 'cnt2019': 0}, {'Symbol': 'ANDA', 'cnt2019': 0}]}

exec(code, env_args)
