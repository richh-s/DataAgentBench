code = """import json
from pathlib import Path
rows = json.loads(Path(var_call_lsVzhsWRcJPMqreLutxe9gCr).read_text())
etf_symbols = sorted({r['Symbol'] for r in rows})
price_tables = set(json.loads(Path(var_call_sOPO5ItDyEQ2ND9iPkJlrrQb).read_text()))
symbols = [s for s in etf_symbols if s in price_tables]
print('__RESULT__:')
print(json.dumps({'etf_symbols': len(etf_symbols), 'price_tables': len(price_tables), 'intersection': len(symbols), 'first10': symbols[:10]}))"""

env_args = {'var_call_lsVzhsWRcJPMqreLutxe9gCr': 'file_storage/call_lsVzhsWRcJPMqreLutxe9gCr.json', 'var_call_sOPO5ItDyEQ2ND9iPkJlrrQb': 'file_storage/call_sOPO5ItDyEQ2ND9iPkJlrrQb.json', 'var_call_i8orDA4VAqo1k3XXAVEWSomT': [{'Symbol': 'SPY'}], 'var_call_qTNhFNS5vyJ6kJJdRzHdTHVF': {'ok': True}, 'var_call_rSOlu28hVlop4YlMQy9rcjSw': {'n': 1435, 'first': {'Symbol': 'AAAU', 'company_description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}}}

exec(code, env_args)
