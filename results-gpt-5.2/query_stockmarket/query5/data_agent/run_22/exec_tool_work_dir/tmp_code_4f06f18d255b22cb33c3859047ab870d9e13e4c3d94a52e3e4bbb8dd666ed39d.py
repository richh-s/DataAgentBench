code = """import json

tickers = json.loads(var_call_8g0HIWs4ELdsHpjHWXpXeV74)['tickers']
# DuckDB table named ELSE conflicts with SQL keyword; quote it.
quoted = []
for t in tickers:
    if not t.isidentifier() or t.upper() in {'ELSE'}:
        quoted.append('"'+t+'"')
    else:
        quoted.append(t)

unions = []
for t, qt in zip(tickers, quoted):
    unions.append(f"SELECT '{t}' AS Symbol, COUNT(*) AS days_over_20pct_range FROM {qt} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2")

query = "SELECT Symbol, days_over_20pct_range FROM (\n" + "\nUNION ALL\n".join(unions) + "\n) ORDER BY days_over_20pct_range DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_5rlnM7Pvk7TR2Co1NWSE5ph4': 'file_storage/call_5rlnM7Pvk7TR2Co1NWSE5ph4.json', 'var_call_8g0HIWs4ELdsHpjHWXpXeV74': {'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}}

exec(code, env_args)
