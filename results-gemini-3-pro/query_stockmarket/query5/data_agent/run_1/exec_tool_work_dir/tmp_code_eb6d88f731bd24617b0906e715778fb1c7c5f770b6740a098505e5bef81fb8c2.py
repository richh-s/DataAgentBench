code = """import json

symbols = ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']

mid = len(symbols) // 2
chunk1 = symbols[:mid]
chunk2 = symbols[mid:]

sqls1 = []
for sym in chunk1:
    sqls1.append("SELECT '" + sym + "' AS Symbol, COUNT(*) AS Days FROM " + sym + " WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")
query1 = " UNION ALL ".join(sqls1)

sqls2 = []
for sym in chunk2:
    sqls2.append("SELECT '" + sym + "' AS Symbol, COUNT(*) AS Days FROM " + sym + " WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")
query2 = " UNION ALL ".join(sqls2)

print("__RESULT__:")
print(json.dumps([query1, query2]))"""

env_args = {'var_function-call-9978005257229487382': 'file_storage/function-call-9978005257229487382.json', 'var_function-call-9978005257229485951': 'file_storage/function-call-9978005257229485951.json', 'var_function-call-14222819161857472104': 'file_storage/function-call-14222819161857472104.json', 'var_function-call-12731217047101193825': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-17568947071419391306': 'file_storage/function-call-17568947071419391306.json', 'var_function-call-4069014104984135899': 'file_storage/function-call-4069014104984135899.json', 'var_function-call-17698936183324553226': "SELECT 'AGMH' AS Symbol, COUNT(*) AS Days FROM  + sym +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*) AS Days FROM  + sym +  WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)", 'var_function-call-16421932056848285693': "SELECT 'AGMH' AS Symbol, COUNT(*) AS Days FROM AGMH WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*) AS Days FROM ALACU WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)", 'var_function-call-13150256639563200458': 'file_storage/function-call-13150256639563200458.json'}

exec(code, env_args)
