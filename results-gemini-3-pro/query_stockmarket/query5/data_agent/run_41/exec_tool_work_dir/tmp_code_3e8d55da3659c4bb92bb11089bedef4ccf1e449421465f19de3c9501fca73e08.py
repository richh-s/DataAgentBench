code = """import json
p = locals()['var_function-call-3672180801322585218']
with open(p, 'r') as f:
    valid = json.load(f)

# Construct parts
q_parts = []
# Avoid complex string in one line
s_date = "2019-01-01"
e_date = "2019-12-31"

for sym in valid:
    # "SELECT 'SYM' as Symbol, COUNT(*) as cnt FROM \"SYM\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)"
    # We construct it via list to be clean
    
    # Select part
    select_clause = "SELECT '" + sym + "' as Symbol, COUNT(*) as cnt"
    from_clause = "FROM \"" + sym + "\""
    # Date clause
    where_clause = "WHERE Date >= '" + s_date + "' AND Date <= '" + e_date + "'"
    # Condition clause
    cond_clause = "AND (High - Low) > (0.2 * Low)"
    
    full_q = select_clause + " " + from_clause + " " + where_clause + " " + cond_clause
    q_parts.append(full_q)

final_query = " UNION ALL ".join(q_parts) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json', 'var_function-call-12333077852201621686': 'test', 'var_function-call-14389750051839597419': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-3575213330611054096': 86, 'var_function-call-6544636298507103744': 2753, 'var_function-call-15124897491698336167': 'file_storage/function-call-15124897491698336167.json', 'var_function-call-7070954927805906890': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as cnt FROM  + s +  WHER", 'var_function-call-3672180801322585218': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
