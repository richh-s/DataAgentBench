code = """import json
import os

# key for valid symbols
key_syms = 'var_function-call-12240742963505795241'
with open(locals()[key_syms], 'r') as f:
    valid_symbols = json.load(f)

state_file = 'state.json'
if not os.path.exists(state_file):
    state = {
        'valid_symbols': valid_symbols,
        'current_index': 0,
        'batch_size': 100,
        'found_symbols': []
    }
else:
    with open(state_file, 'r') as f:
        state = json.load(f)

# If we have a previous result to process, we would do it here, but this is step 1.
# We will handle result processing in the next python call.

idx = state['current_index']
batch_size = state['batch_size']
chunk = state['valid_symbols'][idx : idx + batch_size]

if not chunk:
    print('__RESULT__:')
    print(json.dumps({"action": "DONE", "found_symbols": state['found_symbols']}))
else:
    # Generate query
    sq = chr(39)
    dq = chr(34)
    sub_queries = []
    for sym in chunk:
        q = "SELECT " + sq + sym + sq + " as Symbol FROM " + dq + sym + dq + " WHERE " + dq + "Adj Close" + dq + " > 200 AND Date >= " + sq + "2015-01-01" + sq + " AND Date <= " + sq + "2015-12-31" + sq + " LIMIT 1"
        sub_queries.append(q)
    
    full_query = " UNION ALL ".join(sub_queries)
    
    # Update state (only index will be updated after processing, but here we just want to output query)
    # Actually, we should not update index yet. We wait until we process results.
    
    print('__RESULT__:')
    print(json.dumps({"action": "QUERY", "query": full_query}))"""

env_args = {'var_function-call-11304267723591981203': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-9114954391718964864': 'file_storage/function-call-9114954391718964864.json', 'var_function-call-10741500597713023606': 'file_storage/function-call-10741500597713023606.json', 'var_function-call-12240742963505795241': 'file_storage/function-call-12240742963505795241.json', 'var_function-call-10700936405339732652': 1435, 'var_function-call-8853969729957837933': 1435, 'var_function-call-7545740587256053064': 'file_storage/function-call-7545740587256053064.json'}

exec(code, env_args)
