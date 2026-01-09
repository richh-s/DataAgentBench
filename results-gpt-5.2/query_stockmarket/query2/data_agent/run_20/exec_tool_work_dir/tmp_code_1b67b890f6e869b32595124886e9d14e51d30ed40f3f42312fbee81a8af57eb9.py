code = """import json
arca_etfs = var_call_LB1ZbwPPcY0PzkOXrLj7u8zh
if isinstance(arca_etfs, str):
    with open(arca_etfs,'r') as f:
        arca_etfs = json.load(f)
trade_tables = var_call_v7Kx9fKHDfirqP6JfQmY5K9t
if isinstance(trade_tables, str):
    with open(trade_tables,'r') as f:
        trade_tables = json.load(f)

syms = sorted(set([r['Symbol'] for r in arca_etfs]).intersection(set(trade_tables)))

# build one union-all query for max adj close in 2015 for each symbol
parts = []
for s in syms:
    parts.append("SELECT '"+s+"' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \""+s+"\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
q = "SELECT Symbol, max_adj_close_2015 FROM (" + " UNION ALL ".join(parts) + ") WHERE max_adj_close_2015 > 200 ORDER BY Symbol"

print('__RESULT__:')
print(json.dumps({'query': q, 'n_symbols': len(syms), 'query_len': len(q)}))"""

env_args = {'var_call_LB1ZbwPPcY0PzkOXrLj7u8zh': 'file_storage/call_LB1ZbwPPcY0PzkOXrLj7u8zh.json', 'var_call_v7Kx9fKHDfirqP6JfQmY5K9t': 'file_storage/call_v7Kx9fKHDfirqP6JfQmY5K9t.json', 'var_call_GmDFpj0kL8WliRT32OVeO2wu': {'a': 1}, 'var_call_8JMIp9Lp8qA5sZAzTPdhANgR': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}], 'var_call_EejCYRDb9ug5PC13IdvH5vx4': [{'1': '1'}], 'var_call_G1rrVl49XhiprdmCB4Cd35MD': [{'ok': '1'}], 'var_call_djKWjvKdGXQL8Ou1d9dQJkO8': {'n_arca_etfs': 1435, 'n_with_price_table': 1435, 'first20': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}}

exec(code, env_args)
