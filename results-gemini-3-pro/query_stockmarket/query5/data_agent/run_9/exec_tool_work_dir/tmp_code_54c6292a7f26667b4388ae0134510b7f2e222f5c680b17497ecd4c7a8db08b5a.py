code = """import json

symbols = ["AGMH", "ALACU", "AMHC", "ANDA", "APEX", "BCLI", "BHAT", "BIOC", "BKYI", "BLFS", "BOSC", "BOTJ", "BWEN", "CBAT", "CCCL", "CDMOP", "CEMI", "CFBK", "CFFA", "CLRB", "CORV", "CPAAU", "CPAH", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "GLG", "GRNVU", "GTEC", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IGIC", "IOTS", "ISNS", "ITI", "LACQ", "MBCN", "MBNKP", "MCEP", "MLND", "MMAC", "MNCLU", "MNPR", "NVEE", "NXTD", "OPOF", "OPTT", "ORGO", "ORSNU", "OTEL", "PBFS", "PBTS", "PCSB", "PECK", "PEIX", "PFIE", "PLIN", "POPE", "QRHC", "SES", "SHSP", "SNSS", "SSNT", "STKS", "TGLS", "TMSR", "VERB", "VMD", "VRRM", "VTIQW", "VVPR", "WHLM", "WHLR", "XBIOW", "XPEL"]

parts = []
for sym in symbols:
    # Construct subquery
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE \"Date\" LIKE '2019%' AND (\"High\" - \"Low\") > 0.2 * \"Low\""
    parts.append(q)

full_query = " UNION ALL ".join(parts) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json'}

exec(code, env_args)
