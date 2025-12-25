code = """symbols = ["AGMH", "ALACU", "AMHC", "ANDA", "APEX", "BCLI", "BHAT", "BIOC", "BKYI", "BLFS", "BOSC", "BOTJ", "BWEN", "CBAT", "CCCL", "CDMOP", "CEMI", "CFBK", "CFFA", "CLRB"]
parts = []
for s in symbols:
    parts.append("SELECT '" + s + "' as Symbol, COUNT(*) as Days FROM \"" + s + "\" WHERE Date LIKE '2019%' AND (High - Low) > (0.2 * Low)")
query = " UNION ALL ".join(parts)
import json
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-9762896799442664376': 'file_storage/function-call-9762896799442664376.json', 'var_function-call-7368161656916448319': 86, 'var_function-call-15346480681916956948': 'file_storage/function-call-15346480681916956948.json', 'var_function-call-4914821713470736250': 'file_storage/function-call-4914821713470736250.json', 'var_function-call-11518376507447731934': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
