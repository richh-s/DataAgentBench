code = """import json, pandas as pd
syms = json.loads(var_call_JqlWvFMucw9HdDp6KJD465H4)
chunks = [syms[i:i+50] for i in range(0, len(syms), 50)]
queries = []
for ch in chunks:
    in_list = ",".join(["'"+s+"'" for s in ch])
    q = f"SELECT '{','.join(ch)}' as syms"
    queries.append(q)
res = json.dumps(queries)
print('__RESULT__:')
print(res)"""

env_args = {'var_call_Bt5C9E86FGZG8FNuMbI95msq': 'file_storage/call_Bt5C9E86FGZG8FNuMbI95msq.json', 'var_call_J9M6S4H9ZdfxJ325wKSV5g7r': 'file_storage/call_J9M6S4H9ZdfxJ325wKSV5g7r.json', 'var_call_JqlWvFMucw9HdDp6KJD465H4': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}

exec(code, env_args)
