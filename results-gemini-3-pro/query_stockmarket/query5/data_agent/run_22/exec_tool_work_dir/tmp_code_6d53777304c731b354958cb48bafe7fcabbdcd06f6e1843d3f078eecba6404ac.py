code = """import json

data = locals()['var_function-call-4357663933427417758']
# data is already a dict or list? The output was json string in print, but usually the storage has the object if it was returned by python tool?
# Wait, the previous tool was execute_python.
# The previous execute_python printed:
# print("__RESULT__:")
# print(json.dumps({"count": len(valid_symbols), "symbols": valid_symbols}))
# So the result stored is the parsed JSON object (dict).

symbols = data['symbols']
subqueries = []
for sym in symbols:
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Days FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    subqueries.append(q)

full_query = " UNION ALL ".join(subqueries)
final_query = "SELECT Symbol, Days FROM (" + full_query + ") ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-1929074110490398114': 'file_storage/function-call-1929074110490398114.json', 'var_function-call-1929074110490396355': 'file_storage/function-call-1929074110490396355.json', 'var_function-call-4357663933427417758': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_function-call-10403538245628085554': [{'Date': '2018-04-18'}]}

exec(code, env_args)
