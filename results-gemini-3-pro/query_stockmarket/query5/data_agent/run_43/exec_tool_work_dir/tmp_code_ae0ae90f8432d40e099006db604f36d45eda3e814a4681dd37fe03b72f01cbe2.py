code = """import json
l = locals()['var_function-call-5187337493383761189']
parts = []
for s in l:
    parts.append("SELECT '{0}' as Symbol, COUNT(*) as Days FROM \"{0}\" WHERE \"Date\" BETWEEN '2019-01-01' AND '2019-12-31' AND (\"High\"-\"Low\") > 0.2*\"Low\"".format(s))
q = " UNION ALL ".join(parts) + " ORDER BY Days DESC LIMIT 5"
print('__RESULT__:')
print(json.dumps(q))"""

env_args = {'var_function-call-5873850458865278019': 'file_storage/function-call-5873850458865278019.json', 'var_function-call-10785221419564258441': 'file_storage/function-call-10785221419564258441.json', 'var_function-call-16716209027256917724': 'file_storage/function-call-16716209027256917724.json', 'var_function-call-139130541756909283': 86, 'var_function-call-5187337493383761189': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-10017644991049900250': 86, 'var_function-call-13463905367897438554': 'SELECT * FROM "AGMH"', 'var_function-call-10675562062684245473': 'SELECT count(*) FROM "AGMH" UNION SELECT count(*) FROM "ALACU" UNION SELECT count(*) FROM "AMHC" UNION SELECT count(*) FROM "ANDA" UNION SELECT count(*) FROM "APEX" UNION SELECT count(*) FROM "BCLI" UNION SELECT count(*) FROM "BHAT" UNION SELECT count(*) FROM "BIOC" UNION SELECT count(*) FROM "BKYI" UNION SELECT count(*) FROM "BLFS"'}

exec(code, env_args)
