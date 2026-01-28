code = """import json
arca_etfs = var_call_LB1ZbwPPcY0PzkOXrLj7u8zh
if isinstance(arca_etfs, str):
    with open(arca_etfs,'r') as f:
        arca_etfs = json.load(f)

trade_tables = var_call_v7Kx9fKHDfirqP6JfQmY5K9t
if isinstance(trade_tables, str):
    with open(trade_tables,'r') as f:
        trade_tables = json.load(f)

arca_syms = sorted({r['Symbol'] for r in arca_etfs})
trade_set = set(trade_tables)
syms = [s for s in arca_syms if s in trade_set]

print('__RESULT__:')
print(json.dumps({'n_arca_etfs': len(arca_syms), 'n_with_price_table': len(syms), 'first20': syms[:20]}))"""

env_args = {'var_call_LB1ZbwPPcY0PzkOXrLj7u8zh': 'file_storage/call_LB1ZbwPPcY0PzkOXrLj7u8zh.json', 'var_call_v7Kx9fKHDfirqP6JfQmY5K9t': 'file_storage/call_v7Kx9fKHDfirqP6JfQmY5K9t.json', 'var_call_GmDFpj0kL8WliRT32OVeO2wu': {'a': 1}, 'var_call_8JMIp9Lp8qA5sZAzTPdhANgR': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_EejCYRDb9ug5PC13IdvH5vx4': [{'1': '1'}], 'var_call_G1rrVl49XhiprdmCB4Cd35MD': [{'ok': '1'}]}

exec(code, env_args)
