code = """import json
from pathlib import Path

symbols_info = var_call_vwz02XEKrjiTYQvsat8711ec['symbols']
trade_tables = json.loads(Path(var_call_fALySoJdBdYyRwIEi7cmHBVS).read_text())
trade_set = set([r['symbol'] for r in trade_tables if 'symbol' in r])
intersect = [s for s in symbols_info if s in trade_set]
missing = [s for s in symbols_info if s not in trade_set]

print('__RESULT__:')
print(json.dumps({'n_info': len(symbols_info), 'n_trade_tables': len(trade_set), 'n_intersect': len(intersect), 'intersect': intersect, 'missing': missing}))"""

env_args = {'var_call_CHRWuAjtR2wI3dKiUO6rzrAE': 'file_storage/call_CHRWuAjtR2wI3dKiUO6rzrAE.json', 'var_call_vwz02XEKrjiTYQvsat8711ec': {'n_symbols': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_fALySoJdBdYyRwIEi7cmHBVS': 'file_storage/call_fALySoJdBdYyRwIEi7cmHBVS.json'}

exec(code, env_args)
