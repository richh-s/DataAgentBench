code = """import json

# Load candidate symbols
with open('var_function-call-18388173402760033623', 'r') as f:
    candidates = json.load(f)

# Load table names
with open('var_function-call-2737364635753825341', 'r') as f:
    tables = json.load(f)

# Create a set of tables for fast lookup
table_set = set(tables)

# Filter candidates
valid_candidates = []
for c in candidates:
    sym = c['Symbol']
    if sym in table_set:
        valid_candidates.append(c)

print(f"Total candidates: {len(candidates)}")
print(f"Valid candidates (in stocktrade_database): {len(valid_candidates)}")

# If valid candidates are too many, we might need batching.
# Let's print the count and maybe the first few to verify.
print("__RESULT__:")
print(json.dumps(valid_candidates)) # printing all for now to see size"""

env_args = {'var_function-call-8728481266960557902': [{'Symbol': 'AAAU', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AADR', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies.", 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AAME', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAWW', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAXJ', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.', 'ETF': 'Y', 'Listing Exchange': 'Q'}], 'var_function-call-18388173402760033623': 'file_storage/function-call-18388173402760033623.json', 'var_function-call-2737364635753825341': 'file_storage/function-call-2737364635753825341.json'}

exec(code, env_args)
