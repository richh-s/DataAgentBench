code = """import json

symbols = ["AGMH", "ALACU", "AMHC", "ANDA", "APEX", "BCLI", "BHAT", "BIOC", "BKYI", "BLFS", "BOSC", "BOTJ", "BWEN", "CBAT", "CCCL", "CDMOP", "CEMI", "CFBK", "CFFA", "CLRB", "CORV", "CPAAU", "CPAH", "CUBA", "CVV", "DZSI", "ELSE", "EXPC", "EYEG", "FAMI", "FNCB", "FSBW", "FTFT", "GDYN", "GLG", "GRNVU", "GTEC", "HCCOU", "HNNA", "HQI", "HRTX", "IDEX", "IGIC", "IOTS", "ISNS", "ITI", "LACQ", "MBCN", "MBNKP", "MCEP", "MLND", "MMAC", "MNCLU", "MNPR", "NVEE", "NXTD", "OPOF", "OPTT", "ORGO", "ORSNU", "OTEL", "PBFS", "PBTS", "PCSB", "PECK", "PEIX", "PFIE", "PLIN", "POPE", "QRHC", "SES", "SHSP", "SNSS", "SSNT", "STKS", "TGLS", "TMSR", "VERB", "VMD", "VRRM", "VTIQW", "VVPR", "WHLM", "WHLR", "XBIOW", "XPEL"]

queries = []
for sym in symbols:
    q = f"SELECT '{sym}' as Symbol, COUNT(*) as Days FROM {sym} WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    queries.append(q)

full_query = " UNION ALL ".join(queries)
full_query += " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-11393603106395449050': 'file_storage/function-call-11393603106395449050.json', 'var_function-call-11393603106395449519': 'file_storage/function-call-11393603106395449519.json', 'var_function-call-17289981033040106678': [{'Date': '2018-04-18', 'Open': '5.75', 'High': '7.5', 'Low': '5.010000228881836', 'Close': '6.300000190734863', 'Adj Close': '6.300000190734863', 'Volume': '291800'}, {'Date': '2018-04-19', 'Open': '6.800000190734863', 'High': '8.859999656677246', 'Low': '6.684000015258789', 'Close': '8.479999542236328', 'Adj Close': '8.479999542236328', 'Volume': '299600'}, {'Date': '2018-04-20', 'Open': '13.260000228881836', 'High': '14.989999771118164', 'Low': '7.590000152587891', 'Close': '7.788000106811523', 'Adj Close': '7.788000106811523', 'Volume': '830400'}, {'Date': '2018-04-23', 'Open': '7.5', 'High': '8.579999923706055', 'Low': '7.010000228881836', 'Close': '8.399999618530273', 'Adj Close': '8.399999618530273', 'Volume': '102600'}, {'Date': '2018-04-24', 'Open': '8.119999885559082', 'High': '8.640000343322754', 'Low': '7.28000020980835', 'Close': '8.449999809265137', 'Adj Close': '8.449999809265137', 'Volume': '87600'}], 'var_function-call-320031414088392535': {'count': 86, 'sample_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS'], 'all_symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
