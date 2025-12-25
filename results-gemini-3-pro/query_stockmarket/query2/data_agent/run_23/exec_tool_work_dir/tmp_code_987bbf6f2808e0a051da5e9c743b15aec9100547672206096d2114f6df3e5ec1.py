code = """import json

# Get file paths from variables
etf_file_path = locals()['var_function-call-2414525597051241979']
tables_file_path = locals()['var_function-call-18281756366382191037']

with open(etf_file_path, 'r') as f:
    etf_symbols = [item['Symbol'] for item in json.load(f)]

with open(tables_file_path, 'r') as f:
    db_tables = set(json.load(f))

valid_symbols = [s for s in etf_symbols if s in db_tables]

# Generate query parts
query_parts = []
for sym in valid_symbols:
    # Escape symbol for string literal (if needed, though tickers usually safe)
    # Quote table name
    # Using "Adj Close"
    part = f"""SELECT '{sym}' as Symbol FROM "{sym}" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' HAVING MAX("Adj Close") > 200"""
    query_parts.append(part)

full_query = " UNION ALL ".join(query_parts)

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-9862830328002497441': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2414525597051241979': 'file_storage/function-call-2414525597051241979.json', 'var_function-call-18281756366382191037': 'file_storage/function-call-18281756366382191037.json', 'var_function-call-13110007690754917420': {'count': 1435, 'first_100': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX']}}

exec(code, env_args)
