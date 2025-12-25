code = """import json

k1 = 'var_function-call-4138560473481984299'
k2 = 'var_function-call-1719822641682209723'

# Read files
p1 = locals()[k1]
p2 = locals()[k2]

with open(p1, 'r') as f:
    d1 = json.load(f)
with open(p2, 'r') as f:
    d2 = json.load(f)

# Logic
valid = []
tables = set(d2)
for item in d1:
    s = item['Symbol']
    if s in tables:
        valid.append(s)

# Build Query
parts = []
for s in valid:
    # avoiding f-string
    # Query: SELECT 'SYM' as Symbol, COUNT(*) as cnt FROM "SYM" WHERE ...
    part = "SELECT '{0}' as Symbol, COUNT(*) as cnt FROM \"{0}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > (0.2 * Low)".format(s)
    parts.append(part)

if not parts:
    q = "SELECT 'None', 0"
else:
    q = " UNION ALL ".join(parts)
    q = q + " ORDER BY cnt DESC LIMIT 5"

print("__RESULT__:")
print(json.dumps(q))"""

env_args = {'var_function-call-4138560473481984299': 'file_storage/function-call-4138560473481984299.json', 'var_function-call-14789780059638436224': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_function-call-1719822641682209723': 'file_storage/function-call-1719822641682209723.json'}

exec(code, env_args)
