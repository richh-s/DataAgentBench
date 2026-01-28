code = """import json
from pathlib import Path
q = json.loads(Path(var_call_a14BGY5VbNsKqOOinRUTu9ts).read_text())['query']
wrapped = "SELECT Symbol, days_exceed FROM (" + q + ") t ORDER BY days_exceed DESC, Symbol ASC LIMIT 5"
print('__RESULT__:')
print(json.dumps({'query': wrapped}))"""

env_args = {'var_call_qdLIKDynnEUet9nJTfF5AaTo': 'file_storage/call_qdLIKDynnEUet9nJTfF5AaTo.json', 'var_call_JTHspwQDIinhSAQ1zuyKmlbC': 'file_storage/call_JTHspwQDIinhSAQ1zuyKmlbC.json', 'var_call_2g7LJVqzIFBNA2vkawUDopgn': 'file_storage/call_2g7LJVqzIFBNA2vkawUDopgn.json', 'var_call_3O4uOALfdTapInqurELW4jFf': {'usable_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_usable': 86, 'n_missing': 0}, 'var_call_a14BGY5VbNsKqOOinRUTu9ts': 'file_storage/call_a14BGY5VbNsKqOOinRUTu9ts.json'}

exec(code, env_args)
