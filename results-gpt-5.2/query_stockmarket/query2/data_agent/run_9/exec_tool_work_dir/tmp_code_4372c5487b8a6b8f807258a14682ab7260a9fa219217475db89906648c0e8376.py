code = """import json

path = var_call_yGpAynzIoSqSe9wxFVL88TgL
with open(path, 'r') as f:
    etf_recs = json.load(f)
etf_symbols = sorted({r['Symbol'] for r in etf_recs if r.get('Symbol')})

path2 = var_call_v5GUXnTyPU6cpGhiSLYg0wi4
with open(path2, 'r') as f:
    trade_tables = set(json.load(f))

symbols = [s for s in etf_symbols if s in trade_tables]

print('__RESULT__:')
print(json.dumps({'etf_arca': len(etf_symbols), 'with_price_table': len(symbols), 'sample': symbols[:20]}))"""

env_args = {'var_call_a4jDHUOrnVwDbmbC1dsIe3Wg': ['stockinfo'], 'var_call_yGpAynzIoSqSe9wxFVL88TgL': 'file_storage/call_yGpAynzIoSqSe9wxFVL88TgL.json', 'var_call_v5GUXnTyPU6cpGhiSLYg0wi4': 'file_storage/call_v5GUXnTyPU6cpGhiSLYg0wi4.json', 'var_call_2WOBBjCIAoxpXHwQY12bOF5g': {'a': 1, 'b': 2}, 'var_call_WupEgDn2oRvzp98W4KGYYUdy': [{'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
