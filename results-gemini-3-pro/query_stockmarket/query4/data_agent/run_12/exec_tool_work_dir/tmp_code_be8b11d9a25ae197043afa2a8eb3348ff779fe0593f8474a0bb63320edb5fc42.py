code = """import json

path = locals()['var_function-call-5198433240157830008']
with open(path, 'r') as f:
    data = json.load(f)

candidates = data['candidates']
sqls = []
quote = chr(34)
for item in candidates:
    sym = item['Symbol']
    # SELECT 'SYM' as Symbol, ... FROM "SYM" ...
    part = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM " + quote + sym + quote + " WHERE Date LIKE '2017-%'"
    sqls.append(part)

full_sql = " UNION ALL ".join(sqls)
print("__RESULT__:")
print(json.dumps(full_sql))"""

env_args = {'var_function-call-8728481266960557902': [{'Symbol': 'AAAU', 'Company Description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.', 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AADR', 'Company Description': "AdvisorShares Dorsey Wright ADR ETF offers investors a dynamic way to access international markets through a diverse portfolio of American Depositary Receipts, leveraging the expertise of Dorsey Wright's investment strategies.", 'ETF': 'Y', 'Listing Exchange': 'P'}, {'Symbol': 'AAME', 'Company Description': 'Atlantic American Corporation provides a range of insurance products, specializing in life, health, and property insurance to meet diverse customer needs.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAWW', 'Company Description': 'Atlas Air Worldwide Holdings specializes in providing air cargo and passenger charter services, playing a crucial role in global logistics and transportation.', 'ETF': 'N', 'Listing Exchange': 'Q'}, {'Symbol': 'AAXJ', 'Company Description': 'iShares MSCI All Country Asia ex Japan Index Fund offers investors a unique opportunity to gain exposure to a diverse portfolio of companies across Asia, excluding Japan, through a well-managed exchange-traded fund.', 'ETF': 'Y', 'Listing Exchange': 'Q'}], 'var_function-call-18388173402760033623': 'file_storage/function-call-18388173402760033623.json', 'var_function-call-2737364635753825341': 'file_storage/function-call-2737364635753825341.json', 'var_function-call-5198433240157830008': 'file_storage/function-call-5198433240157830008.json', 'var_function-call-9271570585805899091': [{'Date': '1987-09-30'}], 'var_function-call-11821513599403744793': 'file_storage/function-call-11821513599403744793.json', 'var_function-call-1024401583214348154': "SELECT 'AEFC' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM  + sym +  WHERE Date LIKE '2017-%'", 'var_function-call-3618745275513914005': 'FROM  + sym + ', 'var_function-call-16736886928575519394': 'FROM "TEST"'}

exec(code, env_args)
