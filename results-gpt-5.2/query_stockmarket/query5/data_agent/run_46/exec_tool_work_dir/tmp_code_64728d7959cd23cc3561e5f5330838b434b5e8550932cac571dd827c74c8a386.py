code = """import json
import pandas as pd

trade_tables_path = var_call_KmtwSX4n5QJJJd1qjBEg1MJC
with open(trade_tables_path,'r') as f:
    trade_tables = set(json.load(f))

tickers = var_call_7c3vqwXm2AFxDsBzu1jrqhnH['tickers']
existing = [t for t in tickers if t in trade_tables]
missing = [t for t in tickers if t not in trade_tables]
print('__RESULT__:')
print(json.dumps({'existing': existing, 'missing': missing, 'n_existing': len(existing), 'n_missing': len(missing)}))"""

env_args = {'var_call_SvMPKSqnbhDIbNMtLSBDwbpr': 'file_storage/call_SvMPKSqnbhDIbNMtLSBDwbpr.json', 'var_call_7c3vqwXm2AFxDsBzu1jrqhnH': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_KmtwSX4n5QJJJd1qjBEg1MJC': 'file_storage/call_KmtwSX4n5QJJJd1qjBEg1MJC.json'}

exec(code, env_args)
