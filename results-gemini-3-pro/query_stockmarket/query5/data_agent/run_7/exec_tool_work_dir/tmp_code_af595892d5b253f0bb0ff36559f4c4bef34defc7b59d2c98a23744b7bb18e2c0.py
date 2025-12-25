code = """import json

# Load symbols
symbols_file = locals()['var_function-call-14110950640077025215']
with open(symbols_file, 'r') as f:
    stock_info_list = json.load(f)

# Load tables
tables_file = locals()['var_function-call-13695686615057088532']
with open(tables_file, 'r') as f:
    tables_list = json.load(f)

tables_set = set(tables_list)

valid_symbols = []
for entry in stock_info_list:
    if entry['Symbol'] in tables_set:
        valid_symbols.append(entry['Symbol'])

queries = []
for sym in valid_symbols:
    # Double quotes for table name, single quotes for string literal
    q = "SELECT '" + sym + "' as Symbol, COUNT(*) as Count FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY Count DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14110950640077025215': 'file_storage/function-call-14110950640077025215.json', 'var_function-call-578737381209602845': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-13695686615057088532': 'file_storage/function-call-13695686615057088532.json', 'var_function-call-5413487961120179899': 'file_storage/function-call-5413487961120179899.json'}

exec(code, env_args)
