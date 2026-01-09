code = """import json
syms = var_call_3O4uOALfdTapInqurELW4jFf['usable_symbols']
parts = []
for s in syms:
    t = '"' + s.replace('"','""') + '"'
    parts.append("SELECT '{}' AS Symbol, COUNT(*) AS days_exceed FROM {} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2".format(s, t))
query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps({'query': query, 'n': len(syms)}))"""

env_args = {'var_call_qdLIKDynnEUet9nJTfF5AaTo': 'file_storage/call_qdLIKDynnEUet9nJTfF5AaTo.json', 'var_call_JTHspwQDIinhSAQ1zuyKmlbC': 'file_storage/call_JTHspwQDIinhSAQ1zuyKmlbC.json', 'var_call_2g7LJVqzIFBNA2vkawUDopgn': 'file_storage/call_2g7LJVqzIFBNA2vkawUDopgn.json', 'var_call_3O4uOALfdTapInqurELW4jFf': {'usable_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_usable': 86, 'n_missing': 0}}

exec(code, env_args)
