code = """import json, pandas as pd

# load capital tickers
obj = var_call_8z0hOoCRDAGDWUY6KxgLogHY
if isinstance(obj, str):
    with open(obj, 'r') as f:
        symbols = json.load(f)
else:
    symbols = obj
sym_df = pd.DataFrame(symbols)

# load trade tables
obj2 = var_call_sB1dlFjC01RJNrtqfKeMDI7e
if isinstance(obj2, str):
    with open(obj2, 'r') as f:
        tables = json.load(f)
else:
    tables = obj2
trade_tables = set(pd.DataFrame(tables)['table_name'].dropna().unique())

# find which capital tickers are not in trade
missing = sorted([t for t in sym_df['Symbol'].dropna().unique() if t not in trade_tables])

# also show any capital tickers containing non-alnum
nonalnum = sorted([t for t in sym_df['Symbol'].dropna().unique() if not t.isalnum()])

print('__RESULT__:')
print(json.dumps({'missing': missing, 'nonalnum': nonalnum}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json', 'var_call_sB1dlFjC01RJNrtqfKeMDI7e': 'file_storage/call_sB1dlFjC01RJNrtqfKeMDI7e.json', 'var_call_EwHLllYQrpKboI1PLYIB8yyd': [{'Symbol': 'AGMH', 'days_exceeded': '13'}], 'var_call_zFLlHJFPlho5PrG7ibBaCPJo': {'n': 86, 'first5': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}, 'var_call_d6bIfwrvNmxPBBmeTjq7Wz1A': {'query': "SELECT 'AGMH' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'AMHC' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ANDA' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'APEX' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM +t+ WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 ORDER BY days_exceeded DESC LIMIT 5;"}, 'var_call_4zh3XG9LDBFgPJjtJbCgkHsN': {'query': "SELECT 'AGMH' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ALACU' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'AMHC' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'ANDA' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT 'APEX' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM  + t +  WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2 ORDER BY days_exceeded DESC LIMIT 5;"}, 'var_call_puCySYteXM489YDQRq99GxQL': {'parts': ["SELECT 'AGMH' AS Symbol", "SELECT 'ALACU' AS Symbol", "SELECT 'AMHC' AS Symbol", "SELECT 'ANDA' AS Symbol", "SELECT 'APEX' AS Symbol"]}, 'var_call_QPYJtC38ndCrTQCBklwtTrfw': {'expr': 'FROM  + t + '}, 'var_call_UUAlVgZ4DZ5ZOPHgevzqu9OE': {'expr': 'FROM "AGMH"'}, 'var_call_u269QNSW1lYi1bqfMAIeVr0y': {'q': "SELECT 'AGMH' AS Symbol"}, 'var_call_yWRsJeMAdI9Wa4LJLuyfsX0H': {'q': 'SELECT "AGMH" as t'}, 'var_call_wr7vIkUBbgMlrXV3uzBqCwYA': {'q': 'SELECT "AGMH" as t FROM "AGMH"'}, 'var_call_XiBTD2DjXL9YzRoMFrBRV5Ih': {'n_tickers': 86, 'n_queries': 1, 'q0': 'SELECT \'AGMH\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ALACU\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'AMHC\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AMHC" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ANDA\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ANDA" WHERE'}, 'var_call_6DIhmZI1cr46b4ASDvGwdCgw': {'n_tickers': 86, 'query': 'SELECT Symbol, days_exceeded FROM (SELECT \'AGMH\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ALACU\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'AMHC\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AMHC" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'ANDA\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "ANDA" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) / Low > 0.2 UNION ALL SELECT \'APEX\' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM "AP'}, 'var_call_QDsI4hV4cCONPfh3JLGxgjKQ': {'n_capital_rows': 86, 'n_trade_tables': 2753, 'n_capital_with_trade': 86, 'missing_examples': []}, 'var_call_pV9BpMCvitNrRS8MjXm4kJbS': {'n_tickers': 86, 'not_in_trade': []}, 'var_call_136NdK78wVNMpYF6XCVbRYli': [], 'var_call_2hKrlMgOAEvkl3VG4pEFfURA': {'check': {'KBLM': False, 'KALA': False}, 'kb_prefix': ['KBA', 'KBE', 'KBWB', 'KBWD', 'KBWP', 'KBWR', 'KBWY']}}

exec(code, env_args)
