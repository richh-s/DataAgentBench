code = """import json
syms = locals()['var_function-call-6251951759364074927']
tables = json.load(open(locals()['var_function-call-5786491863926317828']))
tset = set(tables)
valid = [s for s in syms if s in tset]
# First 30
chunk = valid[:30]

sq = []
dq = chr(34)
for s in chunk:
    p1 = "SELECT '" + s + "' as Symbol, COUNT(*) as Count FROM " + dq + s + dq + " "
    p2 = "WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    sq.append(p1 + p2)

query = " UNION ALL ".join(sq)
# No wrapping outer select needed for partial results, but good for structure.
final_q = "SELECT Symbol, Count FROM (" + query + ") ORDER BY Count DESC"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-5977330354183330062': 'file_storage/function-call-5977330354183330062.json', 'var_function-call-6251951759364074927': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5786491863926317828': 'file_storage/function-call-5786491863926317828.json', 'var_function-call-10176458139307025028': 'file_storage/function-call-10176458139307025028.json', 'var_function-call-15837535591424154889': 'file_storage/function-call-15837535591424154889.json', 'var_function-call-10643510482919177405': '"SELECT Symbol, Count FROM (SELECT \'AGMH\' as Symbol, COUNT(*) as Count FROM  + s +  WHERE Date LIKE \'2019-%\' AND (High - Low) > (0.2 * Low) UNION ALL SELECT \'ALACU\' as Symbol, COUNT(*) as Count FROM  + s +  WHERE Date LIKE \'2019-%\' AND (High - Low) > (0.2 * Low) UNION ALL SELECT \'AMHC\' as Symbol, COUNT(*) as Count FROM  + s +  WHERE Date LIKE \'2019-%\' AND (High - Low) > (0.2 * Low) UNION ALL SELECT \'ANDA\' as Symbol, COUNT(*) as Count FROM  + s +  WHERE Date LIKE \'2019-%\' AND (High - Low) > (0.2 ', 'var_function-call-14321875698678529277': 'file_storage/function-call-14321875698678529277.json'}

exec(code, env_args)
