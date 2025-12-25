code = """import json

k1 = 'var_function-call-4138560473481984299'
k2 = 'var_function-call-1719822641682209723'

try:
    with open(locals()[k1], 'r') as f:
        d1 = json.load(f)
    with open(locals()[k2], 'r') as f:
        d2 = json.load(f)
        
    s1 = set(x['Symbol'] for x in d1)
    s2 = set(d2)
    valid = list(s1.intersection(s2))
    
    # Generate query
    parts = []
    for s in valid:
        parts.append(f"SELECT '{s}' as Symbol, COUNT(*) as cnt FROM \"{s}\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > 0.2 * Low")
    
    full_q = " UNION ALL ".join(parts) + " ORDER BY cnt DESC LIMIT 5"
    
    print("__RESULT__:")
    print(json.dumps(full_q))
except Exception as e:
    print("__RESULT__:")
    print(json.dumps(str(e)))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json'}

exec(code, env_args)
