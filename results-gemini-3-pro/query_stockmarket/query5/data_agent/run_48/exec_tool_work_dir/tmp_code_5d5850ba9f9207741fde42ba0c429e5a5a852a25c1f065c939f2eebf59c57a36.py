code = """import json
syms_key = 'var_function-call-6251951759364074927'
tables_key = 'var_function-call-5786491863926317828'
syms = locals()[syms_key]
path = locals()[tables_key]
f = open(path, 'r')
tables = json.load(f)
f.close()

valid = []
tset = set(tables)
for s in syms:
    if s in tset:
        valid.append(s)

sq = []
for s in valid:
    p1 = "SELECT '" + s + "' as Symbol, COUNT(*) as Count FROM \"" + s + "\" "
    p2 = "WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    sq.append(p1 + p2)

query = " UNION ALL ".join(sq)
final_q = "SELECT Symbol, Count FROM (" + query + ") ORDER BY Count DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-5977330354183330062': 'file_storage/function-call-5977330354183330062.json', 'var_function-call-6251951759364074927': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5786491863926317828': 'file_storage/function-call-5786491863926317828.json', 'var_function-call-10176458139307025028': 'file_storage/function-call-10176458139307025028.json'}

exec(code, env_args)
