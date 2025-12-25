code = """import json
key = 'var_function-call-11588894222788545089'
path = locals()[key]
with open(path, 'r') as f:
    data = json.load(f)

s = data['valid_symbols'][0]
d1 = '2019-01-01'
d2 = '2019-12-31'
factor = 0.2
q = "SELECT '{0}' as Symbol, COUNT(*) as Days FROM \"{0}\" WHERE Date >= '{1}' AND Date <= '{2}' AND (High - Low) > ({3} * Low)".format(s, d1, d2, factor)
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_function-call-2176412617243161922': 'file_storage/function-call-2176412617243161922.json', 'var_function-call-11082574715617122511': 'file_storage/function-call-11082574715617122511.json', 'var_function-call-11588894222788545089': 'file_storage/function-call-11588894222788545089.json', 'var_function-call-17828885364460578773': 'Hello', 'var_function-call-2995907560252921252': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-17856956371297009416': 'file_storage/function-call-17856956371297009416.json', 'var_function-call-1811509703427698202': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-5871326958725150364': 'file_storage/function-call-5871326958725150364.json', 'var_function-call-12517383240852430649': "SELECT 'AGMH' as Symbol, COUNT(*) as Days FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as Days FROM  + s", 'var_function-call-2737326290852428542': 'file_storage/function-call-2737326290852428542.json', 'var_function-call-16377467578248944887': 'SELECT  + s +  as Symbol, COUNT(*) as Days FROM "AGMH" WHERE Date >=  + d1 +  AND Date <=  + d2 +  AND (High - Low) > (0.2 * Low)'}

exec(code, env_args)
