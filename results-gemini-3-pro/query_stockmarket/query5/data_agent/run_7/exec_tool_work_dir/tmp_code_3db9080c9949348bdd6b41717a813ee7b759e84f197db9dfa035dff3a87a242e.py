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

valid_entries = []
for entry in stock_info_list:
    if entry['Symbol'] in tables_set:
        valid_entries.append(entry)

queries = []
for entry in valid_entries:
    sym = entry['Symbol']
    desc = entry['Company Description'].replace("'", "''")
    # simplified query construction
    q = "SELECT '" + sym + "' as Symbol, '" + desc + "' as Company_Name, COUNT(*) as DayCount FROM \"" + sym + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"
    queries.append(q)

if len(queries) > 0:
    full_query = " UNION ALL ".join(queries) + " ORDER BY DayCount DESC LIMIT 5"
else:
    full_query = "SELECT 'No Result' as Symbol, 'None' as Company_Name, 0 as DayCount"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14110950640077025215': 'file_storage/function-call-14110950640077025215.json', 'var_function-call-578737381209602845': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-13695686615057088532': 'file_storage/function-call-13695686615057088532.json'}

exec(code, env_args)
