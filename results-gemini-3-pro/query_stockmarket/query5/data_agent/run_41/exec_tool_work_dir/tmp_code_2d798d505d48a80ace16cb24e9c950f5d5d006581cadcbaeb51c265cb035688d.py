code = """import json

valid = locals()['var_function-call-3672180801322585218']

# Split into 2 batches
batch1 = valid[:45]
batch2 = valid[45:]

q_parts = []
sq = "'"
dq = '"'
s_date = "2019-01-01"
e_date = "2019-12-31"

for sym in batch1:
    select_part = "SELECT " + sq + sym + sq + " as Symbol, COUNT(*) as cnt"
    from_part = "FROM " + dq + sym + dq
    where_part = "WHERE Date >= " + sq + s_date + sq + " AND Date <= " + sq + e_date + sq
    cond_part = "AND (High - Low) > (0.2 * Low)"
    full_q = select_part + " " + from_part + " " + where_part + " " + cond_part
    q_parts.append(full_q)

query1 = " UNION ALL ".join(q_parts)

print("__RESULT__:")
print(json.dumps(query1))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json', 'var_function-call-12333077852201621686': 'test', 'var_function-call-14389750051839597419': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-3575213330611054096': 86, 'var_function-call-6544636298507103744': 2753, 'var_function-call-15124897491698336167': 'file_storage/function-call-15124897491698336167.json', 'var_function-call-7070954927805906890': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as cnt FROM  + s +  WHER", 'var_function-call-3672180801322585218': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-14995171893931030059': 'file_storage/function-call-14995171893931030059.json', 'var_function-call-4471842619043211610': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + sym +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s", 'var_function-call-5095734550893166807': 'FROM  + sym + ', 'var_function-call-6708770351312283984': 'FROM "TEST"', 'var_function-call-5310496593737384305': 'file_storage/function-call-5310496593737384305.json'}

exec(code, env_args)
