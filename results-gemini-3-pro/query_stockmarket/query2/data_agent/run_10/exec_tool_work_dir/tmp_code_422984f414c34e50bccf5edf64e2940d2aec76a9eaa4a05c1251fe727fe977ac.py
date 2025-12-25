code = """import json

# Load symbols from step 1
with open(locals()['var_function-call-11166014520478941420'], 'r') as f:
    target_symbols = json.load(f)

# Load tables from step 2
with open(locals()['var_function-call-1334096834738266665'], 'r') as f:
    all_tables = json.load(f)

# Intersect
# Note: target_symbols is a list of strings
# all_tables is a list of strings
target_set = set(target_symbols)
tables_set = set(all_tables)

valid_symbols = list(target_set.intersection(tables_set))
valid_symbols.sort()

print(f"Valid symbols count: {len(valid_symbols)}")
print(f"First 10 valid symbols: {valid_symbols[:10]}")

print("__RESULT__:")
print(json.dumps(valid_symbols))"""

env_args = {'var_function-call-16208289775098928678': [{'Nasdaq Traded': 'Y', 'Symbol': 'AAAU', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AADR', 'Listing Exchange': 'P', 'Market Category': 'Not applicable or not NASDAQ-listed', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'None', 'NextShares': 'N', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies."}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAME', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAWW', 'Listing Exchange': 'Q', 'Market Category': 'Q', 'ETF': 'N', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.'}, {'Nasdaq Traded': 'Y', 'Symbol': 'AAXJ', 'Listing Exchange': 'Q', 'Market Category': 'G', 'ETF': 'Y', 'Round Lot Size': '100.0', 'Test Issue': 'N', 'Financial Status': 'N', 'NextShares': 'N', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.'}], 'var_function-call-10050416379202504823': 'file_storage/function-call-10050416379202504823.json', 'var_function-call-11166014520478941420': 'file_storage/function-call-11166014520478941420.json', 'var_function-call-1334096834738266665': 'file_storage/function-call-1334096834738266665.json'}

exec(code, env_args)
