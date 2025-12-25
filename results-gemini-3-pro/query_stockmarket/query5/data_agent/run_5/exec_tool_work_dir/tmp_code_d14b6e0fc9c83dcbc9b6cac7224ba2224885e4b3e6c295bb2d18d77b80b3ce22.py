code = """import json

data = locals()['var_function-call-1602718910402106253']
symbols = data

# Split symbols into two batches
batch1 = symbols[:44]

dq = chr(34)
sq = chr(39)

parts = []
for sym in batch1:
    q = "SELECT " + sq + sym + sq + " as Symbol, COUNT(*) as Count FROM " + dq + sym + dq + " WHERE Date LIKE " + sq + "2019%" + sq + " AND (High - Low) > (0.2 * Low)"
    parts.append(q)

full_query = " UNION ALL ".join(parts)
# We don't limit 5 here, we want all counts so we can merge later
final_query = "SELECT Symbol, Count FROM (" + full_query + ")"

print("__RESULT__:")
print(json.dumps(final_query))"""

env_args = {'var_function-call-16810362353464456006': 'file_storage/function-call-16810362353464456006.json', 'var_function-call-16803666523160065497': 'file_storage/function-call-16803666523160065497.json', 'var_function-call-1602718910402106253': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-2155876558491863382': 'file_storage/function-call-2155876558491863382.json', 'var_function-call-12316265843873107757': "SELECT 'AGMH' as Symbol, COUNT(*) as Count FROM  + sym +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)", 'var_function-call-17951650173914390156': 'file_storage/function-call-17951650173914390156.json'}

exec(code, env_args)
