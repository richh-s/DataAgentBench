code = """import json

# symbols from earlier result
symbols = json.loads(var_call_ViohjA2g7kDqYXIDjjz3qdWZ)['symbols']

# tables in trade db
p = var_call_AREtt9xxwb8L8HlhehNmyqYW
with open(p,'r') as f:
    tables = set(json.load(f))

symbols_in_db = [s for s in symbols if s in tables]
missing = [s for s in symbols if s not in tables]

out = json.dumps({'n_symbols': len(symbols), 'n_in_trade_db': len(symbols_in_db), 'missing': missing})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_DqrJ20Dt6kRZ0Xf4cm1RtXQg': 'file_storage/call_DqrJ20Dt6kRZ0Xf4cm1RtXQg.json', 'var_call_ViohjA2g7kDqYXIDjjz3qdWZ': {'n_total': 86, 'n_common': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_AREtt9xxwb8L8HlhehNmyqYW': 'file_storage/call_AREtt9xxwb8L8HlhehNmyqYW.json'}

exec(code, env_args)
