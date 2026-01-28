code = """import json, pandas as pd
from pathlib import Path

# load NYSE Arca ETFs
p = Path(var_call_4zvnEpy4TcgDPxNN3yfwUgQc)
with p.open() as f:
    arca_etfs = json.load(f)
arca_symbols = sorted({r['symbol'] for r in arca_etfs})

# load available price tables
p2 = Path(var_call_PK2VWvd4xur6MI6L2CYBTa7J)
with p2.open() as f:
    price_tables = set(json.load(f))

symbols = [s for s in arca_symbols if s in price_tables]

print('__RESULT__:')
print(json.dumps({'arca_etf_symbols': symbols, 'n_arca_etfs': len(arca_symbols), 'n_with_prices': len(symbols)}))"""

env_args = {'var_call_4zvnEpy4TcgDPxNN3yfwUgQc': 'file_storage/call_4zvnEpy4TcgDPxNN3yfwUgQc.json', 'var_call_PK2VWvd4xur6MI6L2CYBTa7J': 'file_storage/call_PK2VWvd4xur6MI6L2CYBTa7J.json'}

exec(code, env_args)
