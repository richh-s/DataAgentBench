code = """import json

# Re-calculate batches with size 70
etf_file_path = locals()['var_function-call-2414525597051241979']
tables_file_path = locals()['var_function-call-18281756366382191037']

with open(etf_file_path, 'r') as f:
    etf_symbols = [item['Symbol'] for item in json.load(f)]

with open(tables_file_path, 'r') as f:
    db_tables = set(json.load(f))

valid_symbols = sorted([s for s in etf_symbols if s in db_tables])

batch_size = 70
batches = []
current_batch = []
q = chr(39)
qq = chr(34)

for sym in valid_symbols:
    # Minimal query: SELECT 'SYM' FROM "SYM" WHERE Date>='2015-01-01' AND Date<='2015-12-31' HAVING MAX("Adj Close")>200
    part = f"SELECT {q}{sym}{q} as Symbol FROM {qq}{sym}{qq} WHERE Date>={q}2015-01-01{q} AND Date<={q}2015-12-31{q} HAVING MAX({qq}Adj Close{qq})>200"
    current_batch.append(part)
    if len(current_batch) >= batch_size:
        batches.append(" UNION ALL ".join(current_batch))
        current_batch = []

if current_batch:
    batches.append(" UNION ALL ".join(current_batch))

# Save batches and index 0
with open('batches.json', 'w') as f:
    json.dump(batches, f)

with open('batch_index.json', 'w') as f:
    json.dump(0, f)

print("__RESULT__:")
print(json.dumps({"total_batches": len(batches)}))"""

env_args = {'var_function-call-9862830328002497441': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-2414525597051241979': 'file_storage/function-call-2414525597051241979.json', 'var_function-call-18281756366382191037': 'file_storage/function-call-18281756366382191037.json', 'var_function-call-13110007690754917420': {'count': 1435, 'first_100': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX']}, 'var_function-call-13982974205828624836': 'file_storage/function-call-13982974205828624836.json', 'var_function-call-7711694181051852980': 'file_storage/function-call-7711694181051852980.json', 'var_function-call-3761610589896855101': 'file_storage/function-call-3761610589896855101.json'}

exec(code, env_args)
