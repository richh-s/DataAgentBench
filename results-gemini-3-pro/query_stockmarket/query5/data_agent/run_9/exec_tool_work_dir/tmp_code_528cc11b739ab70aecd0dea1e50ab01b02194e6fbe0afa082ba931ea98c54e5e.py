code = """import json
symbols = ["AGMH", "ALACU", "AMHC", "ANDA", "APEX", "BCLI", "BHAT", "BIOC", "BKYI", "BLFS", "BOSC", "BOTJ", "BWEN", "CBAT", "CCCL", "CDMOP", "CEMI", "CFBK", "CFFA", "CLRB", "CORV", "CPAAU", "CPAH", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "GLG", "GRNVU", "GTEC", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IGIC", "IOTS", "ISNS", "ITI", "LACQ", "MBCN", "MBNKP", "MCEP", "MLND", "MMAC", "MNCLU", "MNPR", "NVEE", "NXTD", "OPOF", "OPTT", "ORGO", "ORSNU", "OTEL", "PBFS", "PBTS", "PCSB", "PECK", "PEIX", "PFIE", "PLIN", "POPE", "QRHC", "SES", "SHSP", "SNSS", "SSNT", "STKS", "TGLS", "TMSR", "VERB", "VMD", "VRRM", "VTIQW", "VVPR", "WHLM", "WHLR", "XBIOW", "XPEL"]
chunk = symbols[:30]
dq = chr(34)
sq = chr(39)
parts = []
for s in chunk:
    p = "SELECT " + sq + s + sq + " as Symbol, COUNT(*) as Days FROM " + dq + s + dq + " WHERE " + dq + "Date" + dq + " LIKE " + sq + "2019%" + sq + " AND (" + dq + "High" + dq + " - " + dq + "Low" + dq + ") > 0.2 * " + dq + "Low" + dq
    parts.append(p)
q = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_function-call-5715290877284323167': 'file_storage/function-call-5715290877284323167.json', 'var_function-call-18378532918632794193': 'file_storage/function-call-18378532918632794193.json', 'var_function-call-9687647277801400069': 'file_storage/function-call-9687647277801400069.json', 'var_function-call-7849848251971865444': 'test', 'var_function-call-15107257653857092335': "SELECT 'AGMH' as S, COUNT(*) FROM  + s +  UNION SELECT 'ALACU' as S, COUNT(*) FROM  + s + ", 'var_function-call-6208406267745621237': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-16531064181173122604': 'file_storage/function-call-16531064181173122604.json'}

exec(code, env_args)
