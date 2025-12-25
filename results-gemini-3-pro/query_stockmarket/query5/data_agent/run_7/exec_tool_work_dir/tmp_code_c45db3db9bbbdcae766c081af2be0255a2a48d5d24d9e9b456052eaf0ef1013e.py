code = """import json

# Load symbols from previous step
symbols_data = locals()['var_function-call-14110950640077025215']
with open(symbols_data, 'r') as f:
    stock_info_list = json.load(f)

# Load table list from previous step
tables_file = locals()['var_function-call-13695686615057088532']
with open(tables_file, 'r') as f:
    tables_list = json.load(f)

tables_set = set(tables_list)

# Filter symbols that have a table
valid_entries = []
for entry in stock_info_list:
    sym = entry['Symbol']
    if sym in tables_set:
        valid_entries.append(entry)

print(f"Valid symbols with tables: {len(valid_entries)}")

# Construct the large UNION ALL query
# We need to escape single quotes in company description if any
queries = []
for entry in valid_entries:
    sym = entry['Symbol']
    desc = entry['Company Description'].replace("'", "''") # escape single quotes for SQL
    # Query: count days where (High - Low) > 0.2 * Low in 2019
    # Using Date LIKE '2019-%' assuming YYYY-MM-DD format
    q = f"""
    SELECT '{sym}' as Symbol, '{desc}' as Company_Name, COUNT(*) as DayCount
    FROM "{sym}"
    WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)
    """
    queries.append(q)

full_query = " UNION ALL ".join(queries) + " ORDER BY DayCount DESC LIMIT 5"

# Print the query to inspect (or just pass it to the next tool)
# I'll print the query string to a variable to be used in the next step, but here I must print JSON result.
# I will return the query string as the result of this python step so I can copy it to the next tool call.
# Actually I can't pass variables directly between steps except via the result storage.
# So I will print the query string as the "__RESULT__".

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-14110950640077025215': 'file_storage/function-call-14110950640077025215.json', 'var_function-call-578737381209602845': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-13695686615057088532': 'file_storage/function-call-13695686615057088532.json'}

exec(code, env_args)
