code = """import json

# Get valid candidates from previous result
valid_candidates_info_path = locals()['var_function-call-5198433240157830008']
with open(valid_candidates_info_path, 'r') as f:
    info = json.load(f)

valid_candidates = info['candidates']

# Generate SQL query
queries = []
for c in valid_candidates:
    sym = c['Symbol']
    q = f"SELECT '{sym}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM \"{sym}\" WHERE Date LIKE '2017-%'"
    queries.append(q)

final_query = " UNION ALL ".join(queries)

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-8728481266960557902': [{'Symbol': 'AAAU', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AADR', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies.", 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AAME', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAWW', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAXJ', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.', 'ETF': 'Y', 'Listing Exchange': 'Q'}], 'var_function-call-18388173402760033623': 'file_storage/function-call-18388173402760033623.json', 'var_function-call-2737364635753825341': 'file_storage/function-call-2737364635753825341.json', 'var_function-call-5198433240157830008': 'file_storage/function-call-5198433240157830008.json', 'var_function-call-9271570585805899091': [{'Date': '1987-09-30'}]}

exec(code, env_args)
