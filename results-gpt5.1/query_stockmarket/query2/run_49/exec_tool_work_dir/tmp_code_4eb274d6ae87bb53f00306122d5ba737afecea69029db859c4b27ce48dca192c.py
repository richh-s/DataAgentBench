code = """import json, pandas as pd

etf_symbols_df = pd.DataFrame(var_call_wqklihAasrBKRuoWyy8oUS7J)
syms = etf_symbols_df['Symbol'].tolist()
placeholders = ', '.join(["'" + s.replace("'", "''") + "'" for s in syms])
query = f"""SELECT table_name FROM information_schema.tables WHERE table_name IN ({placeholders});"""

result = {'query': query, 'symbols_count': len(syms)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wqklihAasrBKRuoWyy8oUS7J': 'file_storage/call_wqklihAasrBKRuoWyy8oUS7J.json', 'var_call_OsjvFxMov1crpVghIc8litG0': 'file_storage/call_OsjvFxMov1crpVghIc8litG0.json'}

exec(code, env_args)
