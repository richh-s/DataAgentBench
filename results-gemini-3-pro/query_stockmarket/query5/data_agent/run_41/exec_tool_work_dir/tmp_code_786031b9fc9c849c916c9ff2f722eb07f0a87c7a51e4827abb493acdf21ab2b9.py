code = """import json

p1 = locals()['var_function-call-4138560473481984299']
p2 = locals()['var_function-call-1719822641682209723']

with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

# Intersection
tables = set(d2)
valid = []
for x in d1:
    if x['Symbol'] in tables:
        valid.append(x['Symbol'])

# Build Query
parts = []
for s in valid:
    # Use .format to ensure substitution
    # We want: FROM "AGMH"
    part = "SELECT '{0}' as Symbol, COUNT(*) as cnt FROM \"{0}\" WHERE Date BETWEEN '2019-01-01' AND '2019-12-31' AND (High - Low) > (0.2 * Low)".format(s)
    parts.append(part)

final_q = " UNION ALL ".join(parts) + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(final_q))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json', 'var_function-call-12333077852201621686': 'test', 'var_function-call-14389750051839597419': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-3575213330611054096': 86, 'var_function-call-6544636298507103744': 2753, 'var_function-call-15124897491698336167': 'file_storage/function-call-15124897491698336167.json', 'var_function-call-7070954927805906890': "SELECT 'AGMH' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ALACU' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'AMHC' as Symbol, COUNT(*) as cnt FROM  + s +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low) UNION ALL SELECT 'ANDA' as Symbol, COUNT(*) as cnt FROM  + s +  WHER"}

exec(code, env_args)
