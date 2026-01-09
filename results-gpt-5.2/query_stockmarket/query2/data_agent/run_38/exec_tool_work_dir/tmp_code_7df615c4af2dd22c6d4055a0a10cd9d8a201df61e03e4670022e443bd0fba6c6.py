code = """import json, pandas as pd

def load(m):
    if isinstance(m, str):
        with open(m, 'r', encoding='utf-8') as f:
            return json.load(f)
    return m

etf_arca = pd.DataFrame(load(var_call_L3QZsJ0Ybio1cEP6tPEvl8TU))
trade_tables = pd.DataFrame(load(var_call_OBbaVlEbu9WD55J30hWNWiTc))

trade_set = set(trade_tables['table_name'].astype(str))
symbols = sorted(set(etf_arca['symbol'].astype(str)).intersection(trade_set))

# Filter to safe identifiers (avoid problematic like CARR#)
import re
safe_symbols = [s for s in symbols if re.fullmatch(r"[A-Za-z0-9_]+", s)]

out = json.dumps({"n_etf_arca": int(etf_arca.shape[0]), "n_with_tables": int(len(symbols)), "n_safe": int(len(safe_symbols)), "has_unsafe": int(len(symbols)-len(safe_symbols))})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_L3QZsJ0Ybio1cEP6tPEvl8TU': 'file_storage/call_L3QZsJ0Ybio1cEP6tPEvl8TU.json', 'var_call_ug2sGvB80yUuHL6Kd0a243vi': 'file_storage/call_ug2sGvB80yUuHL6Kd0a243vi.json', 'var_call_OlDdcoADPbmT2QrdOQ2eemsY': {'n_symbols': 1435, 'sample_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA']}, 'var_call_OBbaVlEbu9WD55J30hWNWiTc': 'file_storage/call_OBbaVlEbu9WD55J30hWNWiTc.json'}

exec(code, env_args)
