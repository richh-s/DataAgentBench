code = """import json

# Access the list of symbols
symbols = locals().get('var_function-call-5644259161849807501')

if isinstance(symbols, str) and symbols.endswith('.json'):
    # It's a file path
    with open(symbols, 'r') as f:
        symbols = json.load(f)

# Construct query
parts = []
for s in symbols:
    # Query part for one symbol
    # Condition: Date starts with 2019, (High-Low) > 0.2*Low
    part = "SELECT '" + s + "' as Symbol, COUNT(*) as DayCount FROM \"" + s + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low"
    parts.append(part)

query = " UNION ALL ".join(parts)
query += " ORDER BY DayCount DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-752038609392442353': 'file_storage/function-call-752038609392442353.json', 'var_function-call-16254905597670293192': 'file_storage/function-call-16254905597670293192.json', 'var_function-call-5644259161849807501': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
