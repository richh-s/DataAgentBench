code = """import json

sym_data = var_call_mO6KgQoztucnkZrYAtJwnebP
if isinstance(sym_data, str):
    with open(sym_data, 'r') as f:
        sym_data = json.load(f)

trade_tables = var_call_pT5LP1Ih8zWQyd1KBdU8QMPx
if isinstance(trade_tables, str):
    with open(trade_tables, 'r') as f:
        trade_tables = json.load(f)

trade_set = set(trade_tables)

eligible = [r['Symbol'] for r in sym_data if r.get('Symbol') in trade_set]
missing = [r['Symbol'] for r in sym_data if r.get('Symbol') not in trade_set]

print('__RESULT__:')
print(json.dumps({'eligible': eligible, 'eligible_n': len(eligible), 'missing_n': len(missing), 'missing': missing[:50]}))"""

env_args = {'var_call_mO6KgQoztucnkZrYAtJwnebP': 'file_storage/call_mO6KgQoztucnkZrYAtJwnebP.json', 'var_call_WGeI64HmUooUEC6F9TmLIOLq': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_pT5LP1Ih8zWQyd1KBdU8QMPx': 'file_storage/call_pT5LP1Ih8zWQyd1KBdU8QMPx.json'}

exec(code, env_args)
