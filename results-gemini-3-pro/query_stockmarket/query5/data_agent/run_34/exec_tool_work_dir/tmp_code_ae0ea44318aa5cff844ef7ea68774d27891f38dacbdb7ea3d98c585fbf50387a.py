code = """import json

# Load symbols from step 1
with open(locals()['var_function-call-17161419678548834227'], 'r') as f:
    # The previous result was a JSON string printed to stdout, which is stored as a string in the variable?
    # No, execute_python stores the *printed* output if it's small, or a file path if large.
    # The previous output was small. So var_function-call-... contains the string.
    # Actually, if I look at the previous output, it was:
    # {"count": 86, "symbols": [...]}
    # It was not a file path.
    pass

# Wait, the previous output was not a file path, it was the JSON string itself.
# But I can't access it directly as a file.
# I need to access the result of the *previous* execute_python call.
# The system stores the result. If it's small, it's the string.
# But the instructions say: "Inside execute_python code you may read storage entries using the provided key names".
# If the previous result was printed, it is in `locals()['var_call_id']`.
# The previous result was `{"count": 86, "symbols": [...]}`.
# So I can just parse it.

# However, I also need the list of tables which is in a file (var_function-call-7632084380373401256).

result_prev = locals()['var_function-call-17161419678548834227'] 
# It's a string.
data = json.loads(result_prev)
target_symbols = set(data['symbols'])

# Load table list
with open(locals()['var_function-call-7632084380373401256'], 'r') as f:
    tables = json.load(f)

existing_tables = set(tables)

valid_symbols = [s for s in target_symbols if s in existing_tables]

# Construct query
queries = []
for sym in valid_symbols:
    # Double quote table names to handle special characters or case sensitivity if needed, though DuckDB is case insensitive usually.
    # Using "Symbol" is safer.
    q = f"""SELECT '{sym}' as Symbol, COUNT(*) as Days FROM "{sym}" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)"""
    queries.append(q)

final_query = " UNION ALL ".join(queries) + " ORDER BY Days DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-8819135185628577805': 'file_storage/function-call-8819135185628577805.json', 'var_function-call-17161419678548834227': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_function-call-7632084380373401256': 'file_storage/function-call-7632084380373401256.json'}

exec(code, env_args)
