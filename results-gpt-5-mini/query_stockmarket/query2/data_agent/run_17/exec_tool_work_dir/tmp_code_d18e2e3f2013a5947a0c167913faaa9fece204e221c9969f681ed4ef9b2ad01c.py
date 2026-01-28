code = """import json
with open(var_call_BIK0Hjv2gbPX1NvQAo3iAnOq, 'r') as f:
    etf_info = json.load(f)
with open(var_call_6TjhZcDUyViOycvQAH95Lzxc, 'r') as f:
    tables = json.load(f)
etf_symbols = [rec['Symbol'] for rec in etf_info]
symbols = [s for s in tables if s in set(etf_symbols)]
# Build union query: for each symbol, select symbol and max adj close in 2015, include only if max>200 via HAVING
parts = []
for s in symbols:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS MaxAdjClose FROM \"{s}\" WHERE \"Date\" BETWEEN '2015-01-01' AND '2015-12-31' HAVING MAX(\"Adj Close\") > 200"
    parts.append(part)
union_sql = " UNION ALL ".join(parts)
final_sql = union_sql + " ORDER BY Symbol;"
result = {'num_symbols': len(symbols), 'sql': final_sql}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BIK0Hjv2gbPX1NvQAo3iAnOq': 'file_storage/call_BIK0Hjv2gbPX1NvQAo3iAnOq.json', 'var_call_6TjhZcDUyViOycvQAH95Lzxc': 'file_storage/call_6TjhZcDUyViOycvQAH95Lzxc.json', 'var_call_QGUq0ZHfUZ0MAj7NSjeXXxTF': {'num_etf_listed_on_arca': 1435, 'num_etf_tables_available': 1435, 'symbols_to_check_count': 1435, 'symbols_to_check_sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX', 'CLIX', 'CLTL', 'CMBS', 'CMDY', 'CMF', 'CN', 'CNBS', 'CNRG', 'CNXT', 'COM', 'COMB', 'COPX', 'CORN', 'CORP', 'CPER', 'CPI', 'CQQQ', 'CRAK', 'CRBN', 'CROP', 'CSD', 'CURE', 'CUT', 'CVY', 'CWB', 'CWEB', 'CWI', 'CWS', 'CYB', 'CZA', 'DBA', 'DBAW', 'DBB', 'DBC', 'DBE', 'DBEF', 'DBEH', 'DBEM', 'DBEU', 'DBEZ', 'DBGR', 'DBJP', 'DBLV', 'DBMF', 'DBO', 'DBP', 'DBS', 'DBV', 'DDG', 'DDM', 'DEEF', 'DEF', 'DEM', 'DES', 'DEUS', 'DEW', 'DFE', 'DFEN', 'DFJ', 'DGL', 'DGRO', 'DGS', 'DGT', 'DHS', 'DIA', 'DIAL', 'DIET', 'DIG', 'DIM', 'DIV', 'DIVA', 'DIVO', 'DIVY', 'DJCB', 'DJD', 'DLBR', 'DLN', 'DLS', 'DMDV', 'DMRE', 'DMRI', 'DMRL', 'DMRM', 'DMRS', 'DNL', 'DOG', 'DOGS', 'DOL', 'DON', 'DOO', 'DPST', 'DRIP', 'DRN', 'DRV', 'DRW', 'DSI', 'DSTL', 'DTD', 'DTH', 'DTN']}}

exec(code, env_args)
