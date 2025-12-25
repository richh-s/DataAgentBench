code = """import json

# Load results
r1_key = locals()['var_function-call-2690621405011536015']
r2_key = locals()['var_function-call-6728343243332737228']

# If they are files, load them. If they are objects (dictionaries/lists), use them directly.
# The tool output says "The result is stored under key...". It is a list of records. 
# But usually large results are in files. Small results are in variable directly?
# Wait, the previous tool outputs were lists of dicts directly in the "results" field?
# No, "The result is stored under key".
# Let's assume they are file paths or lists. I will check type.

def load_data(key):
    # Depending on how the system passes the variable, it might be the data or a file path string.
    # The system prompt says: "Inside execute_python code you may read storage entries...".
    # "If a tool result is large, the next message will include a preview... and the storage entry will be the .json file path".
    # The results of query_db looked small enough (43 records). But let's check.
    val = key
    if isinstance(val, str) and val.endswith('.json'):
        # It's a file path? Or maybe the tool result IS the file path if it was large?
        # In the previous message: "The result is stored under key: var_function-call-..."
        # And the preview showed the content.
        # This implies the variable IS the file path if it was "too large".
        # But if it wasn't "too large", it is the data.
        # However, for query_db, it always returns a list of records.
        # Let's try to assume it's a list first. If it's a string, try to open it.
        try:
            with open(val, 'r') as f:
                return json.load(f)
        except:
            pass
    return val

# Actually, the user message says: "The result is stored under key: var_function-call-..."
# And it shows the JSON list.
# If the JSON list is shown in full, the variable likely holds the list.
# But I should be robust.

r1 = load_data(r1_key)
r2 = load_data(r2_key)

# stock_info is definitely a file path from the first step
with open(locals()['var_function-call-14483470659460654413'], 'r') as f:
    stock_info = json.load(f)

stock_map = {item['Symbol']: item['Company Description'] for item in stock_info}

combined = r1 + r2
# Convert Days to int
for item in combined:
    item['Days'] = int(item['Days'])

# Sort
combined.sort(key=lambda x: x['Days'], reverse=True)

# Top 5
top5 = combined[:5]

# Get Names
result = []
for item in top5:
    desc = stock_map.get(item['Symbol'], "Unknown")
    # Extract name? Usually description starts with Name.
    # Let's just return the full description or a part of it.
    # The user asked for company names.
    # I'll strip "Inc." etc if needed, but safer to return the full string from the description which seems to be "Name is a ..."
    # Looking at the preview: "AGM Group Holdings Inc. specializes..."
    # So I will just use the Description.
    result.append({"Symbol": item['Symbol'], "Days": item['Days'], "Company Name": desc})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14483470659460654413': 'file_storage/function-call-14483470659460654413.json', 'var_function-call-14483470659460654526': 'file_storage/function-call-14483470659460654526.json', 'var_function-call-17026473911973201946': {'count': 86, 'first_10': ['DZSI', 'PLIN', 'PEIX', 'CPAH', 'CBAT', 'EXPC', 'CUBA', 'BKYI', 'PBFS', 'SSNT']}, 'var_function-call-12112332931073037359': [{'Date': '2003-11-14', 'Open': '169.25', 'High': '172.5', 'Low': '166.25'}], 'var_function-call-9515048861433129617': 'file_storage/function-call-9515048861433129617.json', 'var_function-call-3190209440704312918': 'file_storage/function-call-3190209440704312918.json', 'var_function-call-1689569685408152486': 'file_storage/function-call-1689569685408152486.json', 'var_function-call-11827687858533035227': 'file_storage/function-call-11827687858533035227.json', 'var_function-call-2690621405011536015': [{'Symbol': 'AGMH', 'Days': '13'}, {'Symbol': 'ALACU', 'Days': '0'}, {'Symbol': 'AMHC', 'Days': '0'}, {'Symbol': 'ANDA', 'Days': '0'}, {'Symbol': 'APEX', 'Days': '15'}, {'Symbol': 'BCLI', 'Days': '0'}, {'Symbol': 'BHAT', 'Days': '10'}, {'Symbol': 'BIOC', 'Days': '21'}, {'Symbol': 'BKYI', 'Days': '16'}, {'Symbol': 'BLFS', 'Days': '0'}, {'Symbol': 'BOSC', 'Days': '3'}, {'Symbol': 'BOTJ', 'Days': '0'}, {'Symbol': 'BWEN', 'Days': '5'}, {'Symbol': 'CBAT', 'Days': '23'}, {'Symbol': 'CCCL', 'Days': '13'}, {'Symbol': 'CDMOP', 'Days': '0'}, {'Symbol': 'CEMI', 'Days': '3'}, {'Symbol': 'CFBK', 'Days': '0'}, {'Symbol': 'CFFA', 'Days': '0'}, {'Symbol': 'CLRB', 'Days': '14'}, {'Symbol': 'CORV', 'Days': '10'}, {'Symbol': 'CPAAU', 'Days': '0'}, {'Symbol': 'CPAH', 'Days': '16'}, {'Symbol': 'CUBA', 'Days': '0'}, {'Symbol': 'CVV', 'Days': '0'}, {'Symbol': 'DZSI', 'Days': '1'}, {'Symbol': 'ELSE', 'Days': '0'}, {'Symbol': 'EXPC', 'Days': '0'}, {'Symbol': 'EYEG', 'Days': '18'}, {'Symbol': 'FAMI', 'Days': '23'}, {'Symbol': 'FNCB', 'Days': '1'}, {'Symbol': 'FSBW', 'Days': '0'}, {'Symbol': 'FTFT', 'Days': '21'}, {'Symbol': 'GDYN', 'Days': '0'}, {'Symbol': 'GLG', 'Days': '42'}, {'Symbol': 'GRNVU', 'Days': '0'}, {'Symbol': 'GTEC', 'Days': '0'}, {'Symbol': 'HCCOU', 'Days': '0'}, {'Symbol': 'HNNA', 'Days': '0'}, {'Symbol': 'HQI', 'Days': '2'}, {'Symbol': 'HRTX', 'Days': '1'}, {'Symbol': 'IDEX', 'Days': '15'}, {'Symbol': 'IGIC', 'Days': '0'}], 'var_function-call-564294519597386293': 'SELECT \'IOTS\' as Symbol, COUNT(*) as Days FROM "IOTS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'ISNS\' as Symbol, COUNT(*) as Days FROM "ISNS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'ITI\' as Symbol, COUNT(*) as Days FROM "ITI" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'LACQ\' as Symbol, COUNT(*) as Days FROM "LACQ" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MBCN\' as Symbol, COUNT(*) as Days FROM "MBCN" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MBNKP\' as Symbol, COUNT(*) as Days FROM "MBNKP" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MCEP\' as Symbol, COUNT(*) as Days FROM "MCEP" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MLND\' as Symbol, COUNT(*) as Days FROM "MLND" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MMAC\' as Symbol, COUNT(*) as Days FROM "MMAC" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MNCLU\' as Symbol, COUNT(*) as Days FROM "MNCLU" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'MNPR\' as Symbol, COUNT(*) as Days FROM "MNPR" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'NVEE\' as Symbol, COUNT(*) as Days FROM "NVEE" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'NXTD\' as Symbol, COUNT(*) as Days FROM "NXTD" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'OPOF\' as Symbol, COUNT(*) as Days FROM "OPOF" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'OPTT\' as Symbol, COUNT(*) as Days FROM "OPTT" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'ORGO\' as Symbol, COUNT(*) as Days FROM "ORGO" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'ORSNU\' as Symbol, COUNT(*) as Days FROM "ORSNU" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'OTEL\' as Symbol, COUNT(*) as Days FROM "OTEL" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PBFS\' as Symbol, COUNT(*) as Days FROM "PBFS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PBTS\' as Symbol, COUNT(*) as Days FROM "PBTS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PCSB\' as Symbol, COUNT(*) as Days FROM "PCSB" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PECK\' as Symbol, COUNT(*) as Days FROM "PECK" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PEIX\' as Symbol, COUNT(*) as Days FROM "PEIX" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PFIE\' as Symbol, COUNT(*) as Days FROM "PFIE" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'PLIN\' as Symbol, COUNT(*) as Days FROM "PLIN" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'POPE\' as Symbol, COUNT(*) as Days FROM "POPE" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'QRHC\' as Symbol, COUNT(*) as Days FROM "QRHC" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'SES\' as Symbol, COUNT(*) as Days FROM "SES" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'SHSP\' as Symbol, COUNT(*) as Days FROM "SHSP" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'SNSS\' as Symbol, COUNT(*) as Days FROM "SNSS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'SSNT\' as Symbol, COUNT(*) as Days FROM "SSNT" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'STKS\' as Symbol, COUNT(*) as Days FROM "STKS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'TGLS\' as Symbol, COUNT(*) as Days FROM "TGLS" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'TMSR\' as Symbol, COUNT(*) as Days FROM "TMSR" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'VERB\' as Symbol, COUNT(*) as Days FROM "VERB" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'VMD\' as Symbol, COUNT(*) as Days FROM "VMD" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'VRRM\' as Symbol, COUNT(*) as Days FROM "VRRM" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'VTIQW\' as Symbol, COUNT(*) as Days FROM "VTIQW" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'VVPR\' as Symbol, COUNT(*) as Days FROM "VVPR" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'WHLM\' as Symbol, COUNT(*) as Days FROM "WHLM" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'WHLR\' as Symbol, COUNT(*) as Days FROM "WHLR" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'XBIOW\' as Symbol, COUNT(*) as Days FROM "XBIOW" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low UNION ALL SELECT \'XPEL\' as Symbol, COUNT(*) as Days FROM "XPEL" WHERE Date LIKE \'2019%\' AND (High - Low) > 0.2 * Low', 'var_function-call-6728343243332737228': [{'Symbol': 'IOTS', 'Days': '1'}, {'Symbol': 'ISNS', 'Days': '0'}, {'Symbol': 'ITI', 'Days': '0'}, {'Symbol': 'LACQ', 'Days': '0'}, {'Symbol': 'MBCN', 'Days': '0'}, {'Symbol': 'MBNKP', 'Days': '0'}, {'Symbol': 'MCEP', 'Days': '14'}, {'Symbol': 'MLND', 'Days': '3'}, {'Symbol': 'MMAC', 'Days': '1'}, {'Symbol': 'MNCLU', 'Days': '0'}, {'Symbol': 'MNPR', 'Days': '4'}, {'Symbol': 'NVEE', 'Days': '1'}, {'Symbol': 'NXTD', 'Days': '15'}, {'Symbol': 'OPOF', 'Days': '0'}, {'Symbol': 'OPTT', 'Days': '12'}, {'Symbol': 'ORGO', 'Days': '15'}, {'Symbol': 'ORSNU', 'Days': '0'}, {'Symbol': 'OTEL', 'Days': '1'}, {'Symbol': 'PBFS', 'Days': '0'}, {'Symbol': 'PBTS', 'Days': '8'}, {'Symbol': 'PCSB', 'Days': '0'}, {'Symbol': 'PECK', 'Days': '19'}, {'Symbol': 'PEIX', 'Days': '12'}, {'Symbol': 'PFIE', 'Days': '2'}, {'Symbol': 'PLIN', 'Days': '1'}, {'Symbol': 'POPE', 'Days': '0'}, {'Symbol': 'QRHC', 'Days': '3'}, {'Symbol': 'SES', 'Days': '51'}, {'Symbol': 'SHSP', 'Days': '1'}, {'Symbol': 'SNSS', 'Days': '32'}, {'Symbol': 'SSNT', 'Days': '11'}, {'Symbol': 'STKS', 'Days': '0'}, {'Symbol': 'TGLS', 'Days': '0'}, {'Symbol': 'TMSR', 'Days': '40'}, {'Symbol': 'VERB', 'Days': '38'}, {'Symbol': 'VMD', 'Days': '1'}, {'Symbol': 'VRRM', 'Days': '0'}, {'Symbol': 'VTIQW', 'Days': '6'}, {'Symbol': 'VVPR', 'Days': '14'}, {'Symbol': 'WHLM', 'Days': '0'}, {'Symbol': 'WHLR', 'Days': '15'}, {'Symbol': 'XBIOW', 'Days': '7'}, {'Symbol': 'XPEL', 'Days': '4'}]}

exec(code, env_args)
