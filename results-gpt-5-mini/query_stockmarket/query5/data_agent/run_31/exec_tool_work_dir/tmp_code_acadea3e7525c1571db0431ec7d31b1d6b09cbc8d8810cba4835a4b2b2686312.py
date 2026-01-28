code = """import json
p_stock = var_call_Ukj7TVJicBB40tkmvqenGyBx
p_trade = var_call_5ITtwdMNsU1VtppAgfjRubYb
with open(p_stock) as f:
    stock_s = json.load(f)
with open(p_trade) as f:
    trade_tables = json.load(f)
sym_to_comp = {rec['Symbol']: rec['Company Description'] for rec in stock_s}
symbols = [s for s in sym_to_comp.keys() if s in trade_tables]
out = {'symbols': symbols, 'mapping': sym_to_comp}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_5ITtwdMNsU1VtppAgfjRubYb': 'file_storage/call_5ITtwdMNsU1VtppAgfjRubYb.json', 'var_call_Ukj7TVJicBB40tkmvqenGyBx': 'file_storage/call_Ukj7TVJicBB40tkmvqenGyBx.json', 'var_call_JjKrgSqh4gfIUOF4WM1EfHvX': {'n_symbols': 86, 'symbols_head': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}}

exec(code, env_args)
