code = """import json
syms = var_call_WKUqe5xjHnHDliDrFbGOUV85['symbols_avail']
parts=[]
for s in syms:
    parts.append("SELECT '{sym}' AS Symbol, SUM(CASE WHEN Low>0 AND (High-Low)/Low > 0.2 THEN 1 ELSE 0 END) AS days_exceed_20pct FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31'".format(sym=s))
query = " UNION ALL ".join(parts)
print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_hSnm5hkMQxk7jSRLKxP3Bsak': 'file_storage/call_hSnm5hkMQxk7jSRLKxP3Bsak.json', 'var_call_vQCNJzyENM60Hw8gh67BUjca': 'file_storage/call_vQCNJzyENM60Hw8gh67BUjca.json', 'var_call_FalNVgCpdE2Qn9pqgDr3kxkE': 'file_storage/call_FalNVgCpdE2Qn9pqgDr3kxkE.json', 'var_call_WKUqe5xjHnHDliDrFbGOUV85': {'symbols_avail': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n_avail': 86, 'n_missing': 0}}

exec(code, env_args)
