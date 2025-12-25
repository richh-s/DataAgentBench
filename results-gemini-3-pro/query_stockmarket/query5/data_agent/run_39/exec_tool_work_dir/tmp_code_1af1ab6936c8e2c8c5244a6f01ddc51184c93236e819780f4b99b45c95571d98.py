code = """import json

# Retrieve the list of symbols
symbols = locals()['var_function-call-12421252814377455322']

queries = []
chunk_size = 20
# Manual chunking
for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i + chunk_size]
    subqueries = []
    for sym in chunk:
        # Construct the SQL part
        # SELECT 'SYM' as Symbol, COUNT(*) as cnt FROM "SYM" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low
        part = "SELECT '" + sym + "' as Symbol, COUNT(*) as cnt FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
        subqueries.append(part)
    
    # Combine subqueries
    full_q = " UNION ALL ".join(subqueries)
    full_q = full_q + " ORDER BY cnt DESC"
    queries.append(full_q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-4097608082559162712': 'file_storage/function-call-4097608082559162712.json', 'var_function-call-14328794898966256946': 'file_storage/function-call-14328794898966256946.json', 'var_function-call-12421252814377455322': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-4398600765810608563': 'file_storage/function-call-4398600765810608563.json', 'var_function-call-6956460276915258918': 'file_storage/function-call-6956460276915258918.json'}

exec(code, env_args)
