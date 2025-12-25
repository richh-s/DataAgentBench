code = """import json
path = locals()['var_function-call-8068012716588702622']
with open(path, 'r') as f:
    symbols = json.load(f)['symbols']

qs = []
for s in symbols:
    qs.append("SELECT '" + s + "' as Symbol, COUNT(*) as Days FROM \"" + s + "\" WHERE Date LIKE '2019-%' AND (High - Low) > 0.2 * Low")

final_q = " UNION ALL ".join(qs) + " ORDER BY Days DESC LIMIT 5"
print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-12883889055046152323': 'file_storage/function-call-12883889055046152323.json', 'var_function-call-4688559592186676218': 'file_storage/function-call-4688559592186676218.json', 'var_function-call-8068012716588702622': {'count': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
