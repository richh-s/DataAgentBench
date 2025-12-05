code = """import json, pandas as pd
from pathlib import Path

symbols_path = Path(var_call_fS4cJnma67IiD6y0yGrZrzbc)
symbols = json.loads(symbols_path.read_text())

symbol_list = [row['Symbol'] for row in symbols]

chunks = []
chunk_size = 200
for i in range(0, len(symbol_list), chunk_size):
    chunk = symbol_list[i:i+chunk_size]
    table_list = set(json.loads(Path(var_call_62066qnaxokJHUtjmxIcsnXH).read_text()))
    present = [s for s in chunk if s in table_list]
    if present:
        chunks.append(present)

present_symbols = [s for sub in chunks for s in sub]

result = json.dumps(present_symbols)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_62066qnaxokJHUtjmxIcsnXH': 'file_storage/call_62066qnaxokJHUtjmxIcsnXH.json', 'var_call_fS4cJnma67IiD6y0yGrZrzbc': 'file_storage/call_fS4cJnma67IiD6y0yGrZrzbc.json'}

exec(code, env_args)
