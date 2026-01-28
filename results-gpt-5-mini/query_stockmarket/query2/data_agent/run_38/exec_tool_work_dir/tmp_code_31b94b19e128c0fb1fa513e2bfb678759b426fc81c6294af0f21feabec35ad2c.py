code = """import json
path = var_call_hcdmhx3EaaPgeEfZkCQd8WiW
with open(path, 'r') as f:
    symbols = json.load(f)
# filter just in case
symbols = [s for s in symbols if isinstance(s, str) and s]
batch_size = 150
batches = [symbols[i:i+batch_size] for i in range(0, len(symbols), batch_size)]
sqls = []
for batch in batches:
    parts = []
    for s in batch:
        # safe literals
        s_q = "'" + s.replace("'", "''") + "'"
        tbl = '"' + s.replace('"', '""') + '"'
        parts.append('SELECT ' + s_q + ' AS Symbol, MAX("Adj Close") AS max_adj FROM ' + tbl + " WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'")
    sql = 'SELECT Symbol, max_adj FROM (\n' + '\nUNION ALL\n'.join(parts) + '\n) t WHERE max_adj > 200 ORDER BY Symbol;'
    sqls.append(sql)
out = {'num_symbols': len(symbols), 'num_batches': len(sqls), 'sqls': sqls}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_iy1Wl4j8WobUxW4UkYuf7dP0': 'file_storage/call_iy1Wl4j8WobUxW4UkYuf7dP0.json', 'var_call_sq3YAjllLjEkNwyEI3gkbR7h': 'file_storage/call_sq3YAjllLjEkNwyEI3gkbR7h.json', 'var_call_Fa61uvgKutZy5CtB1zXcJTTG': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX', 'CLIX', 'CLTL', 'CMBS', 'CMDY', 'CMF', 'CN', 'CNBS', 'CNRG', 'CNXT', 'COM', 'COMB', 'COPX', 'CORN', 'CORP', 'CPER', 'CPI', 'CQQQ', 'CRAK', 'CRBN', 'CROP', 'CSD', 'CURE', 'CUT', 'CVY', 'CWB', 'CWEB', 'CWI', 'CWS', 'CYB', 'CZA', 'DBA', 'DBAW', 'DBB', 'DBC', 'DBE', 'DBEF', 'DBEH', 'DBEM', 'DBEU', 'DBEZ', 'DBGR', 'DBJP', 'DBLV', 'DBMF', 'DBO', 'DBP', 'DBS', 'DBV', 'DDG', 'DDM', 'DEEF', 'DEF', 'DEM', 'DES', 'DEUS', 'DEW', 'DFE', 'DFEN', 'DFJ', 'DGL', 'DGRO', 'DGS', 'DGT', 'DHS', 'DIA', 'DIAL', 'DIET', 'DIG', 'DIM', 'DIV', 'DIVA', 'DIVO', 'DIVY', 'DJCB', 'DJD', 'DLBR', 'DLN', 'DLS', 'DMDV', 'DMRE', 'DMRI', 'DMRL', 'DMRM', 'DMRS', 'DNL', 'DOG', 'DOGS', 'DOL', 'DON', 'DOO', 'DPST', 'DRIP', 'DRN', 'DRV', 'DRW', 'DSI', 'DSTL', 'DTD', 'DTH', 'DTN'], 'var_call_hcdmhx3EaaPgeEfZkCQd8WiW': 'file_storage/call_hcdmhx3EaaPgeEfZkCQd8WiW.json'}

exec(code, env_args)
