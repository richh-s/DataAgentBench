code = """import json

# load trade tables list
path = var_call_kq7kpbIH0U64RPjMHA3mRNJU
with open(path,'r') as f:
    tables = set(json.load(f))

symbols = var_call_uWWzyOV4HGqDvHNe8V1xuRTN['symbols']
missing = [s for s in symbols if s not in tables]
existing = [s for s in symbols if s in tables]

out = json.dumps({'existing': existing, 'missing': missing, 'n_existing': len(existing), 'n_missing': len(missing)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_JhJLtl5G4JCIM5ycQaLBGC65': 'file_storage/call_JhJLtl5G4JCIM5ycQaLBGC65.json', 'var_call_uWWzyOV4HGqDvHNe8V1xuRTN': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_kq7kpbIH0U64RPjMHA3mRNJU': 'file_storage/call_kq7kpbIH0U64RPjMHA3mRNJU.json'}

exec(code, env_args)
