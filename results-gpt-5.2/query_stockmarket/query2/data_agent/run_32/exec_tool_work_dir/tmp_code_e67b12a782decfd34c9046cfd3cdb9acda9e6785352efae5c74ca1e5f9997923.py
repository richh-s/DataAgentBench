code = """import json

def load(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

syms = load(var_call_cxUz4FCtwLwK13kwgV4VSxlj)['symbols']
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
chunk0 = chunks[0]

q_parts=[]
for s in chunk0:
    s_safe = s.replace("'","''")
    q_parts.append("SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{t}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" < '2016-01-01'".format(s=s_safe, t=s))

# join using \n to avoid Python parsing issues
q = (' UNION ALL ' ).join(q_parts)

# write to file
path = '/tmp/chunk0_query.sql'
with open(path,'w') as f:
    f.write(q)

print('__RESULT__:')
print(json.dumps({'path': path, 'n': len(chunk0)}))"""

env_args = {'var_call_WUWNAstTHRWuxShkejbmmb3q': 'file_storage/call_WUWNAstTHRWuxShkejbmmb3q.json', 'var_call_wN5P7wyYzbAWkh7ELYtCJadn': 'file_storage/call_wN5P7wyYzbAWkh7ELYtCJadn.json', 'var_call_cxUz4FCtwLwK13kwgV4VSxlj': 'file_storage/call_cxUz4FCtwLwK13kwgV4VSxlj.json', 'var_call_bzIiHOXKAVaDurLZUe3EHHme': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_DGidQhEOR4s7IAaFoMGUI6sO': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}], 'var_call_MWglBBk8bzXx5ui4ILjZUsvp': {'q': "SELECT 'AAAU' AS symbol UNION ALL SELECT 'AADR' AS symbol UNION ALL SELECT 'ABEQ' AS symbol UNION ALL SELECT 'ACSG' AS symbol UNION ALL SELECT 'ACWF' AS symbol"}, 'var_call_fO0S1lmK401H5vNT4tc8NLzO': {'q': "SELECT 'AAAU' AS symbol, MAX(Adj Close) AS max_adj_close_2015 FROM AAAU WHERE Date >= '2015-01-01' AND Date < '2016-01-01'"}, 'var_call_tlFcFZGgAplyHtnhDg9nxiXE': [{'max_adj_close_2015': 'nan'}], 'var_call_SG24JPmFMVT5EJDgugRNakuR': {'n_symbols': 1435, 'n_chunks': 8, 'first_chunk': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY', 'BFOR', 'BIBL', 'BIL', 'BIV', 'BIZD', 'BKF', 'BKLN', 'BLES', 'BLHY', 'BLOK', 'BLV', 'BNDC', 'BNO', 'BOIL', 'BOND', 'BOUT', 'BRF', 'BRZU', 'BSV', 'BTAL', 'BUL', 'BUY', 'BUYN', 'BVAL', 'BWX', 'BWZ', 'BYLD', 'BZQ', 'CANE', 'CBON', 'CCOR', 'CEF', 'CEW', 'CGW', 'CHAD', 'CHAU', 'CHEP', 'CHGX', 'CHIC', 'CHIE', 'CHIH', 'CHII', 'CHIK', 'CHIL', 'CHIM', 'CHIQ', 'CHIR', 'CHIS', 'CHIU', 'CHIX', 'CLIX', 'CLTL', 'CMBS', 'CMDY', 'CMF', 'CN', 'CNBS', 'CNRG', 'CNXT', 'COM', 'COMB', 'COPX', 'CORN', 'CORP', 'CPER', 'CPI', 'CQQQ', 'CRAK', 'CRBN', 'CROP', 'CSD', 'CURE', 'CUT', 'CVY', 'CWB', 'CWEB', 'CWI', 'CWS', 'CYB', 'CZA', 'DBA', 'DBAW', 'DBB', 'DBC', 'DBE', 'DBEF', 'DBEH', 'DBEM', 'DBEU', 'DBEZ', 'DBGR', 'DBJP', 'DBLV', 'DBMF', 'DBO', 'DBP', 'DBS', 'DBV', 'DDG', 'DDM', 'DEEF', 'DEF', 'DEM', 'DES', 'DEUS', 'DEW', 'DFE', 'DFEN', 'DFJ', 'DGL', 'DGRO', 'DGS', 'DGT', 'DHS', 'DIA', 'DIAL', 'DIET', 'DIG', 'DIM', 'DIV', 'DIVA', 'DIVO', 'DIVY', 'DJCB', 'DJD', 'DLBR', 'DLN', 'DLS', 'DMDV', 'DMRE', 'DMRI', 'DMRL', 'DMRM', 'DMRS', 'DNL', 'DOG', 'DOGS', 'DOL', 'DON', 'DOO', 'DPST', 'DRIP', 'DRN', 'DRV', 'DRW', 'DSI', 'DSTL', 'DTD', 'DTH', 'DTN']}, 'var_call_zFErIPQbgKoUQZfSJ0bcTeCy': [{'symbol': 'AAAU', 'max_adj_close_2015': 'nan'}]}

exec(code, env_args)
