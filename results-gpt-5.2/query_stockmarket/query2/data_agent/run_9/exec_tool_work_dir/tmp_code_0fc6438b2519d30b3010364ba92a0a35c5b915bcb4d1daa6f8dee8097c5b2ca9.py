code = """import json

path = var_call_yGpAynzIoSqSe9wxFVL88TgL
with open(path, 'r') as f:
    etf_recs = json.load(f)
syms = sorted({r['Symbol'] for r in etf_recs if r.get('Symbol')})

# build first 300 values clause
n=300
vals = ",".join(["('{s}')".format(s=s) for s in syms[:n]])
q = "WITH etfs(symbol) AS (SELECT * FROM (VALUES {vals})) SELECT COUNT(*) AS c FROM etfs;".format(vals=vals)

print('__RESULT__:')
print(json.dumps({'query': q[:4000], 'len': len(q)}))"""

env_args = {'var_call_a4jDHUOrnVwDbmbC1dsIe3Wg': ['stockinfo'], 'var_call_yGpAynzIoSqSe9wxFVL88TgL': 'file_storage/call_yGpAynzIoSqSe9wxFVL88TgL.json', 'var_call_v5GUXnTyPU6cpGhiSLYg0wi4': 'file_storage/call_v5GUXnTyPU6cpGhiSLYg0wi4.json', 'var_call_2WOBBjCIAoxpXHwQY12bOF5g': {'a': 1, 'b': 2}, 'var_call_WupEgDn2oRvzp98W4KGYYUdy': [{'max_adj_close': '193.3121490478516'}], 'var_call_YzHq4OWO2XmoiWMK6BFwd0ke': {'etf_arca': 1435, 'with_price_table': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_HIAnihxrlnXQNtvAYLPdbds6': [{'symbol': 'AAAU'}, {'symbol': 'AADR'}, {'symbol': 'ABEQ'}, {'symbol': 'ACSG'}, {'symbol': 'ACWF'}]}

exec(code, env_args)
