code = """import json, pandas as pd

obj = var_call_6DIhmZI1cr46b4ASDvGwdCgw
# can't access full query because truncated; rebuild from symbols and trade tables directly without KBLM etc

# load symbols list
import json as js
objS = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(objS, str):
    with open(objS,'r') as f:
        symbols = js.load(f)
else:
    symbols = objS
sym_df = pd.DataFrame(symbols)

objT = var_call_sB1dlFjC01RJNrtqfKeMDI7e
if isinstance(objT, str):
    with open(objT,'r') as f:
        tables = js.load(f)
else:
    tables = objT
trade_tables = set(pd.DataFrame(tables)['table_name'].dropna().unique())

capital = sym_df[['Symbol','company_name']].dropna()
capital = capital[capital['Symbol'].isin(trade_tables)]

tickers = capital['Symbol'].tolist()

# ensure no spurious tickers
bad = [t for t in tickers if t not in trade_tables]

print('__RESULT__:')
print(js.dumps({'n': len(tickers), 'bad': bad}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json', 'var_call_sB1dlFjC01RJNrtqfKeMDI7e': 'file_storage/call_sB1dlFjC01RJNrtqfKeMDI7e.json', 'var_call_EwHLllYQrpKboI1PLYIB8yyd': [{'Symbol': 'AGMH', 'days_exceeded': '13'}], 'var_call_zFLlHJFPlho5PrG7ibBaCPJo': {'n': 86, 'first5': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_call_d6bIfwrvNmxPBBmeTjq7Wz1A': {'query': "SELECT 'AGMH' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'AMHC' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ANDA' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'APEX' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 ORDER BY days_exceeded DESC LIMIT 5;"}, 'var_call_4zh3XG9LDBFgPJjtJbCgkHsN': {'query': "SELECT 'AGMH' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'AMHC' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ANDA' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'APEX' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 ORDER BY days_exceeded DESC LIMIT 5;"}, 'var_call_puCySYteXM489YDQRq99GxQL': {'parts': ["SELECT 'AGMH' AS Symbol", "SELECT 'ALACU' AS Symbol", "SELECT 'AMHC' AS Symbol", "SELECT 'ANDA' AS Symbol", "SELECT 'APEX' AS Symbol"]}, 'var_call_QPYJtC38ndCrTQCBklwtTrfw': {'expr': 'FROM  + t + '}, 'var_call_UUAlVgZ4DZ5ZOPHgevzqu9OE': {'expr': 'FROM "AGMH"'}, 'var_call_u269QNSW1lYi1bqfMAIeVr0y': {'q': "SELECT 'AGMH' AS Symbol"}, 'var_call_yWRsJeMAdI9Wa4LJLuyfsX0H': {'q': 'SELECT "AGMH" as t'}, 'var_call_wr7vIkUBbgMlrXV3uzBqCwYA': {'q': 'SELECT "AGMH" as t FROM "AGMH"'}, 'var_call_XiBTD2DjXL9YzRoMFrBRV5Ih': {'n_tickers': 86, 'n_queries': 1, 'q0': 'SELECT \'AGMH\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ALACU\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'AMHC\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AMHC" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ANDA\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ANDA" WHERE'}, 'var_call_6DIhmZI1cr46b4ASDvGwdCgw': {'n_tickers': 86, 'query': 'SELECT Symbol, days_exceeded FROM (SELECT \'AGMH\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ALACU\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'AMHC\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AMHC" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ANDA\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ANDA" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'APEX\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AP'}, 'var_call_QDsI4hV4cCONPfh3JLGxgjKQ': {'n_capital_rows': 86, 'n_trade_tables': 2753, 'n_capital_with_trade': 86, 'missing_examples': []}, 'var_call_pV9BpMCvitNrRS8MjXm4kJbS': {'n_tickers': 86, 'not_in_trade': []}, 'var_call_136NdK78wVNMpYF6XCVbRYli': [], 'var_call_2hKrlMgOAEvkl3VG4pEFfURA': {'check': {'KBLM': False, 'KALA': False}, 'kb_prefix': ['KBA', 'KBE', 'KBWB', 'KBWD', 'KBWP', 'KBWR', 'KBWY']}, 'var_call_OQwbi6sG6cZOvHfD7q6LlsQZ': {'missing': [], 'nonalnum': []}, 'var_call_ldFiLgdLhiojuu70DlJ76eDt': {'contains_KBLM': False, 'contains_AGMH': True}, 'var_call_0CnfMOsAU0pULk41vxhvxGPD': [], 'var_call_bQEos0GWE0WFeUsmTOw3CIow': [], 'var_call_uVmYWxdzaoJPhlLfDkSqEAT3': {'n_syms_in_query': 5, 'n_unique': 5, 'extra': []}}

exec(code, env_args)
