code = """import json

obj = var_call_Nd7bM7x7ixnLz0bOPPJyWtm0
inter = obj['tickers_in_trade_db']
parts = [f"SELECT '{t}' AS Symbol, Date, High, Low FROM \"{t}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01'" for t in inter]
union_sql = " UNION ALL ".join(parts)
query = (
    "WITH all_data AS (" + union_sql + ") "
    + "SELECT Symbol, COUNT(*) AS days "
    + "FROM all_data "
    + "WHERE Low IS NOT NULL AND Low>0 AND High IS NOT NULL AND (High - Low) / Low > 0.2 "
    + "GROUP BY Symbol "
    + "ORDER BY days DESC "
    + "LIMIT 5;"
)
print('__RESULT__:')
print(json.dumps({'query': query, 'n_tickers': len(inter)}))"""

env_args = {'var_call_Wpf4IymfEgb0zEcD2bqrB3Mg': 'file_storage/call_Wpf4IymfEgb0zEcD2bqrB3Mg.json', 'var_call_swtzwSQ1S4sF4VjwNFnli5ws': 'file_storage/call_swtzwSQ1S4sF4VjwNFnli5ws.json', 'var_call_jsXvi8EahP2fQEcI3BU84UB5': 'file_storage/call_jsXvi8EahP2fQEcI3BU84UB5.json', 'var_call_Nd7bM7x7ixnLz0bOPPJyWtm0': {'tickers_in_trade_db': ['AGMH', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GTEC', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MCEP', 'MLND', 'MMAC', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VVPR', 'WHLM', 'WHLR', 'XPEL'], 'n': 76, 'missing': 0}}

exec(code, env_args)
