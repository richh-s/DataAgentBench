code = """import json

symbols = ["AGMH", "ALACU", "AMHC", "ANDA", "APEX", "BCLI", "BHAT", "BIOC", "BKYI", "BLFS", "BOSC", "BOTJ", "BWEN", "CBAT", "CCCL", "CDMOP", "CEMI", "CFBK", "CFFA", "CLRB", "CORV", "CPAAU", "CPAH", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "GLG", "GRNVU", "GTEC", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IGIC", "IOTS", "ISNS", "ITI", "LACQ", "MBCN", "MBNKP", "MCEP", "MLND", "MMAC", "MNCLU", "MNPR", "NVEE", "NXTD", "OPOF", "OPTT", "ORGO", "ORSNU", "OTEL", "PBFS", "PBTS", "PCSB", "PECK", "PEIX", "PFIE", "PLIN", "POPE", "QRHC", "SES", "SHSP", "SNSS", "SSNT", "STKS", "TGLS", "TMSR", "VERB", "VMD", "VRRM", "VTIQW", "VVPR", "WHLM", "WHLR", "XBIOW", "XPEL"]

parts = []
for sym in symbols:
    # Use double quotes for table identifiers to be safe
    part = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM \"{sym}\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.2 * Low"
    parts.append(part)

full_query = " UNION ALL ".join(parts)
full_query = f"SELECT Symbol, Days FROM ({full_query}) ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-7676302026983721262': 'file_storage/function-call-7676302026983721262.json', 'var_function-call-13686535493729829546': 'file_storage/function-call-13686535493729829546.json', 'var_function-call-7722253651347684026': 'file_storage/function-call-7722253651347684026.json', 'var_function-call-2907215605741522332': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
