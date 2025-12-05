code = """import json
info = var_call_AG5rK2AIv246FdZVnLhOFhbq
symbols_nyse = info['symbols_nyse']

parts = []
for sym in symbols_nyse:
    parts.append(f"SELECT '{sym}' AS Symbol, Date, Open, Close FROM '{sym}' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'")
union_query = " UNION ALL ".join(parts)

out = json.dumps({'query': union_query})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_3CyaGEN6NIN9CXuI9ion3FSl': 'file_storage/call_3CyaGEN6NIN9CXuI9ion3FSl.json', 'var_call_BQxqSkOTGPacwhwwWSXyVAD3': 'file_storage/call_BQxqSkOTGPacwhwwWSXyVAD3.json', 'var_call_AG5rK2AIv246FdZVnLhOFhbq': {'symbols_nyse': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT'], 'needs_query': True, 'query_prefix': "SELECT 'AEFC' AS Symbol, Date, Open, Close FROM 'AEFC' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIN' AS Symbol, Date, Open, Close FROM 'AIN' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIV' AS Symbol, Date, Open, Close FROM 'AIV' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AIZP' AS Symbol, Date, Open, Close FROM 'AIZP' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AJRD' AS Symbol, Date, Open, Close FROM 'AJRD' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AL' AS Symbol, Date, Open, Close FROM 'AL' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMN' AS Symbol, Date, Open, Close FROM 'AMN' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMP' AS Symbol, Date, Open, Close FROM 'AMP' WHERE Date >= '2017-01-01' AND Date <= '2017-12-31' UNION ALL SELECT 'AMT' AS Symbol, Date, Open, Close FROM 'AMT' WHERE Date >= '2017-01-"}}

exec(code, env_args)
