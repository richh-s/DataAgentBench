code = """import json
# Read the storage file that contains Market Category S symbols and company descriptions
with open(var_call_I0eYLDdGovELtoxJKKig6MRB, 'r') as f:
    records = json.load(f)
symbols = [r['Symbol'] for r in records]
parts = []
for s in symbols:
    part = "SELECT '{sym}' AS symbol, COUNT(*) AS cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (\"High\" - \"Low\") > 0.2 * \"Low\"".format(sym=s)
    parts.append(part)
union_sql = '\nUNION ALL\n'.join(parts)
final_sql = 'SELECT symbol, cnt FROM (\n{inner}\n) ORDER BY cnt DESC LIMIT 5;'.format(inner=union_sql)
print('__RESULT__:')
print(json.dumps(final_sql))"""

env_args = {'var_call_7VImgvlgFEaHlFsiKpCoAckB': 'file_storage/call_7VImgvlgFEaHlFsiKpCoAckB.json', 'var_call_lbLogyRQLAZG0TxA1yH5r3aq': 'file_storage/call_lbLogyRQLAZG0TxA1yH5r3aq.json', 'var_call_I0eYLDdGovELtoxJKKig6MRB': 'file_storage/call_I0eYLDdGovELtoxJKKig6MRB.json', 'var_call_elBfmAEkw9Rwad3H5cvMHPtR': {'count': 86, 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}}

exec(code, env_args)
