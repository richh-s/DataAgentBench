code = """import json, pandas as pd
symbols_info_path = var_call_XutlXI7WfJsJZQTGrY7FduU5
with open(symbols_info_path, 'r') as f:
    symbols_info = json.load(f)
syms = [row['Symbol'] for row in symbols_info]
chunks = [syms[i:i+200] for i in range(0, len(syms), 200)]
result = json.dumps(chunks)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_l2OZI76iNWq57oZUH6RuuG4P': 'file_storage/call_l2OZI76iNWq57oZUH6RuuG4P.json', 'var_call_XutlXI7WfJsJZQTGrY7FduU5': 'file_storage/call_XutlXI7WfJsJZQTGrY7FduU5.json'}

exec(code, env_args)
