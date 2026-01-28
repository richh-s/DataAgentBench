code = """import json
from pathlib import Path

companies = json.loads(Path(var_call_JTHspwQDIinhSAQ1zuyKmlbC).read_text())['companies']
top = var_call_v65dd1unPKC7rAeAR1369MGr
names = [companies.get(r['Symbol'], r['Symbol']) for r in top]
print('__RESULT__:')
print(json.dumps(names))"""

env_args = {'var_call_qdLIKDynnEUet9nJTfF5AaTo': 'file_storage/call_qdLIKDynnEUet9nJTfF5AaTo.json', 'var_call_JTHspwQDIinhSAQ1zuyKmlbC': 'file_storage/call_JTHspwQDIinhSAQ1zuyKmlbC.json', 'var_call_2g7LJVqzIFBNA2vkawUDopgn': 'file_storage/call_2g7LJVqzIFBNA2vkawUDopgn.json', 'var_call_3O4uOALfdTapInqurELW4jFf': {'usable_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_usable': 86, 'n_missing': 0}, 'var_call_a14BGY5VbNsKqOOinRUTu9ts': 'file_storage/call_a14BGY5VbNsKqOOinRUTu9ts.json', 'var_call_YTGNDz7bF4W1aqzBWnozt2d3': 'file_storage/call_YTGNDz7bF4W1aqzBWnozt2d3.json', 'var_call_v65dd1unPKC7rAeAR1369MGr': [{'Symbol': 'SES', 'days_exceed': '51'}, {'Symbol': 'GLG', 'days_exceed': '42'}, {'Symbol': 'TMSR', 'days_exceed': '40'}, {'Symbol': 'VERB', 'days_exceed': '38'}, {'Symbol': 'SNSS', 'days_exceed': '32'}]}

exec(code, env_args)
