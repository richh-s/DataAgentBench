code = """import json

# Load candidate list
with open(locals()['var_function-call-259568999239465198'], 'r') as f:
    candidates = json.load(f)

# Load table list
with open(locals()['var_function-call-13316569487754645486'], 'r') as f:
    tables = json.load(f)

# Filter
valid_candidates = [c for c in candidates if c['Symbol'] in tables]

print(f"Total candidates: {len(candidates)}")
print(f"Valid candidates (in trade db): {len(valid_candidates)}")
print("__RESULT__:")
print(json.dumps(valid_candidates))"""

env_args = {'var_function-call-5874251965808723808': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-259568999239465198': 'file_storage/function-call-259568999239465198.json', 'var_function-call-13316569487754645486': 'file_storage/function-call-13316569487754645486.json'}

exec(code, env_args)
