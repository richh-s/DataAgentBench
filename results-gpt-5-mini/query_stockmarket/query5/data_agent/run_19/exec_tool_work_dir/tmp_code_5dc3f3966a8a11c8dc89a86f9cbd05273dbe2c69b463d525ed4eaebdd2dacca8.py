code = """import json
with open(var_call_mCZX40n6pNV9BgHm9Uf5whVa, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_X1mq3L2N4XZjiqZMtAqHx3up, 'r') as f:
    tables = json.load(f)

symbols = [rec['Symbol'] for rec in stockinfo]
available = [s for s in symbols if s in tables]

tool_uses = []
for s in available:
    q = "SELECT '{sym}' AS Symbol, SUM(CASE WHEN (\"High\" - \"Low\") > 0.2 * \"Low\" THEN 1 ELSE 0 END) AS cnt FROM \"{tbl}\" WHERE \"Date\" >= '2019-01-01' AND \"Date\" <= '2019-12-31';".format(sym=s, tbl=s)
    tool_uses.append({
        'recipient_name': 'functions.query_db',
        'parameters': {
            'db_name': 'stocktrade_database',
            'query': q
        }
    })

print('__RESULT__:')
print(json.dumps({'tool_uses': tool_uses}))"""

env_args = {'var_call_mCZX40n6pNV9BgHm9Uf5whVa': 'file_storage/call_mCZX40n6pNV9BgHm9Uf5whVa.json', 'var_call_X1mq3L2N4XZjiqZMtAqHx3up': 'file_storage/call_X1mq3L2N4XZjiqZMtAqHx3up.json', 'var_call_JpOng1p5KmSl1g16P5P08ksp': {'num_market_S': 86, 'num_available_in_trade_db': 86, 'available_symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}}

exec(code, env_args)
