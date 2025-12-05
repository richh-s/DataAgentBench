code = """import json
symbols = var_call_8nWdiRYlGLf7n6yBdV2BQHfi
query = ' ; '.join([f'SELECT "Date", "High", "Low", "Close" FROM "{s}" WHERE "Date" LIKE "2019-%"' for s in symbols])

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_3KyktpZgnMcbPjsPWe4HOmrP': 'file_storage/call_3KyktpZgnMcbPjsPWe4HOmrP.json', 'var_call_PwQrdg3QQTTSgKtPFJW7Iqa0': 'file_storage/call_PwQrdg3QQTTSgKtPFJW7Iqa0.json', 'var_call_8nWdiRYlGLf7n6yBdV2BQHfi': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
