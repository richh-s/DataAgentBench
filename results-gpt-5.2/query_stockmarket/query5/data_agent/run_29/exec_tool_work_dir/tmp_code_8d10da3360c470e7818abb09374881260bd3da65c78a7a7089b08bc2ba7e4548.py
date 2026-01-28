code = """import json

# Prepare list of tickers from previous result
res = var_call_a5WosSoUjRCnC7i63SsY0FAa

tickers = res['tickers']

# build a UNION ALL query across tickers
parts = []
for sym in tickers:
    tbl = '"' + sym.replace('"','""') + '"'
    parts.append(
        f"SELECT '{sym}' AS Symbol, COUNT(*) AS days_over_20pct FROM {tbl} WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) > 0.2 * Low"
    )
query = "\nUNION ALL\n".join(parts) + "\nORDER BY days_over_20pct DESC, Symbol\nLIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': query}))"""

env_args = {'var_call_t6qYTgEhLW52YPNGHQeKk6oL': 'file_storage/call_t6qYTgEhLW52YPNGHQeKk6oL.json', 'var_call_1gtyyeTNjea4vCWTo20aow0w': 'file_storage/call_1gtyyeTNjea4vCWTo20aow0w.json', 'var_call_a5WosSoUjRCnC7i63SsY0FAa': {'n_tickers': 86, 'tickers': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}}

exec(code, env_args)
