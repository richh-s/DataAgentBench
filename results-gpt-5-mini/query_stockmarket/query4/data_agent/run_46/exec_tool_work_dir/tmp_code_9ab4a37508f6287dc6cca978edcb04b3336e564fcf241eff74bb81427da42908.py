code = """import json
with open(var_call_LRt0exprHfOJ1inMQRTPA5Sp, 'r') as f:
    stockinfo_records = json.load(f)
with open(var_call_CrVKZQBqTmnPuAKFQp6jscWu, 'r') as f:
    trade_tables = json.load(f)
symbols_stockinfo = [r['Symbol'] for r in stockinfo_records]
available_symbols = sorted([s for s in symbols_stockinfo if s in trade_tables])
print("__RESULT__:")
print(json.dumps(available_symbols))"""

env_args = {'var_call_hR1ujv8iGbULDzfr7OEeOW0w': 'file_storage/call_hR1ujv8iGbULDzfr7OEeOW0w.json', 'var_call_CrVKZQBqTmnPuAKFQp6jscWu': 'file_storage/call_CrVKZQBqTmnPuAKFQp6jscWu.json', 'var_call_LRt0exprHfOJ1inMQRTPA5Sp': 'file_storage/call_LRt0exprHfOJ1inMQRTPA5Sp.json', 'var_call_7TsFAyghQqeeBjvHt22egi1X': {'count': 234, 'sample_symbols': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT']}}

exec(code, env_args)
