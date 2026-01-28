code = """import json
with open(var_call_BIK0Hjv2gbPX1NvQAo3iAnOq, 'r') as f:
    etf_info = json.load(f)
with open(var_call_6TjhZcDUyViOycvQAH95Lzxc, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in etf_info if rec['Symbol'] in set(tables)]

dq = chr(34)
batch_size = 100
tool_uses = []
for i in range(0, len(symbols), batch_size):
    batch = symbols[i:i+batch_size]
    parts = []
    for s in batch:
        parts.append(f"SELECT '{s}' AS Symbol, MAX({dq}Adj Close{dq}) AS MaxAdjClose FROM {dq}{s}{dq} WHERE {dq}Date{dq} BETWEEN '2015-01-01' AND '2015-12-31'")
    sql = ' UNION ALL '.join(parts)
    tool_uses.append({'recipient_name': 'functions.query_db', 'parameters': {'db_name': 'stocktrade_database', 'query': sql}})

print('__RESULT__:')
print(json.dumps(tool_uses))"""

env_args = {'var_call_BIK0Hjv2gbPX1NvQAo3iAnOq': 'file_storage/call_BIK0Hjv2gbPX1NvQAo3iAnOq.json', 'var_call_6TjhZcDUyViOycvQAH95Lzxc': 'file_storage/call_6TjhZcDUyViOycvQAH95Lzxc.json', 'var_call_QGUq0ZHfUZ0MAj7NSjeXXxTF': {'num_etf_listed_on_arca': 1435, 'num_etf_tables_available': 1435, 'symbols_to_check_count': 1435, 'symbols_to_check_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX', 'CLIX', 'CLTL', 'CMBS', 'CMDY', 'CMF', 'CN', 'CNBS', 'CNRG', 'CNXT', 'COM', 'COMB', 'COPX', 'CORN', 'CORP', 'CPER', 'CPI', 'CQQQ', 'CRAK', 'CRBN', 'CROP', 'CSD', 'CURE', 'CUT', 'CVY', 'CWB', 'CWEB', 'CWI', 'CWS', 'CYB', 'CZA', 'DBA', 'DBAW', 'DBB', 'DBC', 'DBE', 'DBEF', 'DBEH', 'DBEM', 'DBEU', 'DBEZ', 'DBGR', 'DBJP', 'DBLV', 'DBMF', 'DBO', 'DBP', 'DBS', 'DBV', 'DDG', 'DDM', 'DEEF', 'DEF', 'DEM', 'DES', 'DEUS', 'DEW', 'DFE', 'DFEN', 'DFJ', 'DGL', 'DGRO', 'DGS', 'DGT', 'DHS', 'DIA', 'DIAL', 'DIET', 'DIG', 'DIM', 'DIV', 'DIVA', 'DIVO', 'DIVY', 'DJCB', 'DJD', 'DLBR', 'DLN', 'DLS', 'DMDV', 'DMRE', 'DMRI', 'DMRL', 'DMRM', 'DMRS', 'DNL', 'DOG', 'DOGS', 'DOL', 'DON', 'DOO', 'DPST', 'DRIP', 'DRN', 'DRV', 'DRW', 'DSI', 'DSTL', 'DTD', 'DTH', 'DTN']}, 'var_call_7g52h2Thj0sb3lyW9HbA3d1c': {'num_symbols': 1435, 'sql_length': 228489, 'sql_preview': 'SELECT \'AAAU\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "AAAU" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'AADR\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "AADR" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'ABEQ\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "ABEQ" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'ACSG\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "ACSG" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'ACWF\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "ACWF" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'AFK\' AS Symbol, MAX("Adj Close") AS MaxAdjClose FROM "AFK" WHERE "Date" BETWEEN \'2015-01-01\' AND \'2015-12-31\' HAVING MAX("Adj Close") > 200 UNION ALL SELECT \'AFLG\' AS Symbol, MAX("Adj Close") '}, 'var_call_IvxyOZ7usxX1oE0MH4FTEva4': [], 'var_call_A4ennZkRNhhcLDhv7pHouGJl': [{'Symbol': 'SPY', 'Listing Exchange': 'P', 'ETF': 'Y'}], 'var_call_j2zI97QeP35LpNcjSUBocHwL': 'file_storage/call_j2zI97QeP35LpNcjSUBocHwL.json', 'var_call_qZE0bbNoLGeLGvzgwJdaBW79': [], 'var_call_wAS6R4ZvGjohMspJT9HcSsjG': 'file_storage/call_wAS6R4ZvGjohMspJT9HcSsjG.json'}

exec(code, env_args)
