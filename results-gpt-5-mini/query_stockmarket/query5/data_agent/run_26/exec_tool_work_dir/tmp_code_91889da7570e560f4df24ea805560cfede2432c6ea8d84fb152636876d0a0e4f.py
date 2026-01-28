code = """import json
# Load symbol list from previous storage
symbols = var_call_72wbhJ4Q9Egjzl07hLEFc5Fw
# Build SQL
parts = []
for sym in symbols:
    part = ('SELECT "{sym}" AS symbol, SUM(CASE WHEN "Date" >= ''2019-01-01'' AND "Date" <= ''2019-12-31'' AND ("High" - "Low") > 0.2 * "Low" THEN 1 ELSE 0 END) AS cnt FROM "{sym}"').format(sym=sym)
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
final_sql = 'SELECT symbol, cnt FROM (\n' + union_sql + '\n) t ORDER BY cnt DESC LIMIT 5;'
# Output the SQL
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_zS6ooOlqOTROyoR6BVuOpZjd': 'file_storage/call_zS6ooOlqOTROyoR6BVuOpZjd.json', 'var_call_VE63NDAtYBpaiHZ8oLi7Rhez': 'file_storage/call_VE63NDAtYBpaiHZ8oLi7Rhez.json', 'var_call_72wbhJ4Q9Egjzl07hLEFc5Fw': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
