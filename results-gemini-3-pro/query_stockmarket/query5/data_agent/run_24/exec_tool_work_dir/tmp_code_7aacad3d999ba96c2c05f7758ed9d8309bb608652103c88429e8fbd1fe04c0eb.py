code = """import json

symbols = ["POPE", "GRNVU", "CFFA", "ANDA", "ORGO", "ISNS", "MLND", "IGIC", "SHSP", "GTEC", "CUBA", "HQI", "SES", "XBIOW", "BIOC", "WHLM", "APEX", "CCCL", "OPTT", "ORSNU", "CPAH", "XPEL", "PECK", "NVEE", "VVPR", "CORV", "GLG", "BOTJ", "MMAC", "PEIX", "BOSC", "DZSI", "CVV", "TMSR", "PBTS", "BHAT", "PFIE", "NXTD", "CLRB", "STKS", "CBAT", "QRHC", "MCEP", "EYEG", "SSNT", "OPOF", "ELSE", "HRTX", "ALACU", "FNCB", "MNCLU", "IOTS", "VERB", "WHLR", "IDEX", "CDMOP", "SNSS", "AMHC", "BKYI", "VRRM", "CFBK", "FTFT", "GDYN", "EXPC", "CPAAU", "HNNA", "PLIN", "AGMH", "VMD", "TGLS", "BWEN", "ITI", "MBNKP", "OTEL", "PCSB", "BLFS", "FAMI", "BCLI", "MNPR", "VTIQW", "FSBW", "PBFS", "HCCOU", "MBCN", "LACQ", "CEMI"]

queries = []
for sym in symbols:
    q = f"SELECT '{sym}' AS Symbol, COUNT(*) AS Days FROM \"{sym}\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.20 * Low"
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-15485977422406242611': 'file_storage/function-call-15485977422406242611.json', 'var_function-call-15853782635533120481': 'file_storage/function-call-15853782635533120481.json', 'var_function-call-10246397170160031370': {'count': 86, 'symbols': ['POPE', 'GRNVU', 'CFFA', 'ANDA', 'ORGO', 'ISNS', 'MLND', 'IGIC', 'SHSP', 'GTEC', 'CUBA', 'HQI', 'SES', 'XBIOW', 'BIOC', 'WHLM', 'APEX', 'CCCL', 'OPTT', 'ORSNU', 'CPAH', 'XPEL', 'PECK', 'NVEE', 'VVPR', 'CORV', 'GLG', 'BOTJ', 'MMAC', 'PEIX', 'BOSC', 'DZSI', 'CVV', 'TMSR', 'PBTS', 'BHAT', 'PFIE', 'NXTD', 'CLRB', 'STKS', 'CBAT', 'QRHC', 'MCEP', 'EYEG', 'SSNT', 'OPOF', 'ELSE', 'HRTX', 'ALACU', 'FNCB', 'MNCLU', 'IOTS', 'VERB', 'WHLR', 'IDEX', 'CDMOP', 'SNSS', 'AMHC', 'BKYI', 'VRRM', 'CFBK', 'FTFT', 'GDYN', 'EXPC', 'CPAAU', 'HNNA', 'PLIN', 'AGMH', 'VMD', 'TGLS', 'BWEN', 'ITI', 'MBNKP', 'OTEL', 'PCSB', 'BLFS', 'FAMI', 'BCLI', 'MNPR', 'VTIQW', 'FSBW', 'PBFS', 'HCCOU', 'MBCN', 'LACQ', 'CEMI']}}

exec(code, env_args)
