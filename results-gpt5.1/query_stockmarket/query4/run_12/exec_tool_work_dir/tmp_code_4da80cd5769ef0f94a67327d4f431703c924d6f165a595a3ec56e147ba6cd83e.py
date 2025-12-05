code = """import json, pandas as pd

symbols = pd.read_json(var_call_pp8fsjKMZOdzb8uwE25JATR2)
meta = pd.read_json(var_call_gkaBzvbF3Zk1Jd5VEtxxplnE)

nyse_non_etf = set(meta['Symbol'].unique())

stock_tables = [s for s in symbols if s in nyse_non_etf]

result = json.dumps(stock_tables)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_pp8fsjKMZOdzb8uwE25JATR2': 'file_storage/call_pp8fsjKMZOdzb8uwE25JATR2.json', 'var_call_gkaBzvbF3Zk1Jd5VEtxxplnE': 'file_storage/call_gkaBzvbF3Zk1Jd5VEtxxplnE.json'}

exec(code, env_args)
