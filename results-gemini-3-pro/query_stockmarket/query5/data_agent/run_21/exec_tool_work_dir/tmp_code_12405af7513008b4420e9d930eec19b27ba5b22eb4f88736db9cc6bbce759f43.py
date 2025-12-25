code = """import json

key = locals()['var_function-call-9945285838579919155']
with open(key, 'r') as f:
    valid_symbols = json.load(f)

subqueries = []
for symbol in valid_symbols:
    # Use simple string concatenation to avoid f-string quote confusion if any
    query_part = "SELECT '" + symbol + "' as Symbol, COUNT(*) as cnt FROM \"" + symbol + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    subqueries.append(query_part)

final_query = " UNION ALL ".join(subqueries)
final_query += " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-2999058475558920348': 'file_storage/function-call-2999058475558920348.json', 'var_function-call-14692438593092107821': 'file_storage/function-call-14692438593092107821.json', 'var_function-call-9945285838579919155': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
