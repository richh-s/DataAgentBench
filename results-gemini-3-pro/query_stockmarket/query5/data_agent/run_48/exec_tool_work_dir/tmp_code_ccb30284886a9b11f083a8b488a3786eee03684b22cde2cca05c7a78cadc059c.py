code = """import json

with open(locals()['var_function-call-6251951759364074927'], 'r') as f:
    candidate_symbols = json.load(f)

with open(locals()['var_function-call-5786491863926317828'], 'r') as f:
    table_names = json.load(f)

table_set = set(table_names)
valid_symbols = [s for s in candidate_symbols if s in table_set]

sub_queries = []
for sym in valid_symbols:
    # Use simple string formatting
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Count FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    sub_queries.append(q)

if not sub_queries:
    print("__RESULT__:")
    print(json.dumps("NO_SYMBOLS"))
else:
    full_query = "SELECT Symbol, Count FROM (" + " UNION ALL ".join(sub_queries) + ") ORDER BY Count DESC LIMIT 5"
    print("__RESULT__:")
    print(json.dumps(full_query))"""

env_args = {'var_function-call-5977330354183330062': 'file_storage/function-call-5977330354183330062.json', 'var_function-call-6251951759364074927': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5786491863926317828': 'file_storage/function-call-5786491863926317828.json'}

exec(code, env_args)
