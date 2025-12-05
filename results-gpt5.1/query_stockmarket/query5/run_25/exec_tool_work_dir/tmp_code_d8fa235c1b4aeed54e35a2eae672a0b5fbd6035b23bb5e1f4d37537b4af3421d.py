code = """import json
symbols = var_call_ot2zE2oBlhTyop2jFq786BfE
queries = {}
for s in symbols:
    queries[s] = f"SELECT Date, High, Low FROM {s} WHERE Date >= '2019-01-01' AND Date <= '2019-12-31';"

print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_w1vUtuST3MvJbDPMwk7Ucsdu': 'file_storage/call_w1vUtuST3MvJbDPMwk7Ucsdu.json', 'var_call_0X399AXUbK3Y4jtEddGSMQap': 'file_storage/call_0X399AXUbK3Y4jtEddGSMQap.json', 'var_call_apdfinIemV1wUe2xdV0NG5Jd': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_aXkGetIKxWpvAiwhZUF2oHlB': "SHOW TABLES WHERE name IN ('AGMH','ALACU','AMHC','ANDA','APEX','BCLI','BHAT','BIOC','BKYI','BLFS','BOSC','BOTJ','BWEN','CBAT','CCCL','CDMOP','CEMI','CFBK','CFFA','CLRB','CORV','CPAAU','CPAH','CUBA','CVV','DZSI','ELSE','EXPC','EYEG','FAMI','FNCB','FSBW','FTFT','GDYN','GLG','GRNVU','GTEC','HCCOU','HNNA','HQI','HRTX','IDEX','IGIC','IOTS','ISNS','ITI','LACQ','MBCN','MBNKP','MCEP','MLND','MMAC','MNCLU','MNPR','NVEE','NXTD','OPOF','OPTT','ORGO','ORSNU','OTEL','PBFS','PBTS','PCSB','PECK','PEIX','PFIE','PLIN','POPE','QRHC','SES','SHSP','SNSS','SSNT','STKS','TGLS','TMSR','VERB','VMD','VRRM','VTIQW','VVPR','WHLM','WHLR','XBIOW','XPEL');", 'var_call_ot2zE2oBlhTyop2jFq786BfE': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI']}

exec(code, env_args)
