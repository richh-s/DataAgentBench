code = """import json
from pathlib import Path
etfs = json.loads(Path(var_call_lsVzhsWRcJPMqreLutxe9gCr).read_text())
syms = sorted({r['Symbol'] for r in etfs})

def qident(name: str) -> str:
    return '"' + name.replace('"','""') + '"'

s = syms[0]
sel = "SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {} WHERE \"Date\" >= DATE '2015-01-01' AND \"Date\" <= DATE '2015-12-31'".format(s, qident(s))
print('__RESULT__:')
print(json.dumps({'sel': sel}))"""

env_args = {'var_call_lsVzhsWRcJPMqreLutxe9gCr': 'file_storage/call_lsVzhsWRcJPMqreLutxe9gCr.json', 'var_call_sOPO5ItDyEQ2ND9iPkJlrrQb': 'file_storage/call_sOPO5ItDyEQ2ND9iPkJlrrQb.json', 'var_call_i8orDA4VAqo1k3XXAVEWSomT': [{'Symbol': 'SPY'}], 'var_call_qTNhFNS5vyJ6kJJdRzHdTHVF': {'ok': True}, 'var_call_rSOlu28hVlop4YlMQy9rcjSw': {'n': 1435, 'first': {'Symbol': 'AAAU', 'company_description': 'Perth Mint Physical Gold ETF offers investors an opportunity to buy shares backed by physical gold, providing a secure and tangible way to invest in precious metals.'}}, 'var_call_B7mg0RoP66h0yBFLUBFuhuDb': {'etf_symbols': 1435, 'price_tables': 2753, 'intersection': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_WsN6orjhZe9FJP90S8PQb7eR': {'s': 'AAAU'}, 'var_call_bJIMpQdNywKBe3FhLdI3N89l': [{'max_adj_close_2015': 'nan'}], 'var_call_c07qUQAOkGZTStG0soF5ef9i': [{'max_adj_close_2015': '193.3121490478516'}], 'var_call_4cdagsAU5F2IMnrYP0mUIbRS': [{'min_date': '2018-08-15', 'max_date': '2020-04-01', 'n': '410'}], 'var_call_NRwTbmbNlVIMw75K3AaqP836': {'n_symbols': 1435}, 'var_call_3WewzLoSWtah63zjRI6Qyhg5': [{'table_name': 'AAAU'}, {'table_name': 'AADR'}, {'table_name': 'AAME'}, {'table_name': 'AAWW'}, {'table_name': 'AAXJ'}]}

exec(code, env_args)
