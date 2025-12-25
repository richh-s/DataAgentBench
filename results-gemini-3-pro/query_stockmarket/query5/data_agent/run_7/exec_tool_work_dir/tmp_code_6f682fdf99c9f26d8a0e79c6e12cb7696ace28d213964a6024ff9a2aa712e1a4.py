code = """import json
s_file = locals()['var_function-call-14110950640077025215']
t_file = locals()['var_function-call-13695686615057088532']
with open(s_file, 'r') as f: s_list = json.load(f)
with open(t_file, 'r') as f: t_list = json.load(f)
t_set = set(t_list)
v_syms = [e['Symbol'] for e in s_list if e['Symbol'] in t_set]
b1 = v_syms[:45]
qs = []
for s in b1:
    qs.append("SELECT '" + s + "' as Symbol, COUNT(*) as Count FROM \"" + s + "\" WHERE Date LIKE '2019-%' AND (High - Low) > (0.2 * Low)")
res = " UNION ALL ".join(qs)
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-14110950640077025215': 'file_storage/function-call-14110950640077025215.json', 'var_function-call-578737381209602845': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-13695686615057088532': 'file_storage/function-call-13695686615057088532.json', 'var_function-call-5413487961120179899': 'file_storage/function-call-5413487961120179899.json', 'var_function-call-9334055806354211481': 'file_storage/function-call-9334055806354211481.json'}

exec(code, env_args)
