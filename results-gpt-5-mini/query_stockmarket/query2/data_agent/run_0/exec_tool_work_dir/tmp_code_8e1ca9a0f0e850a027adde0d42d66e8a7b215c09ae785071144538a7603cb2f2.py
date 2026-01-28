code = """import json
# var_call_pioxFm3HMNADNVHF9KBLRTjt and var_call_rL51DkgtzdOWrf1cILYO8Xv8 are provided in storage
data = []
try:
    data = __import__('json').load(open(var_call_pioxFm3HMNADNVHF9KBLRTjt))
except Exception:
    # If storage provides list directly
    data = var_call_pioxFm3HMNADNVHF9KBLRTjt

all_tables = []
try:
    all_tables = __import__('json').load(open(var_call_rL51DkgtzdOWrf1cILYO8Xv8))
except Exception:
    all_tables = var_call_rL51DkgtzdOWrf1cILYO8Xv8

# Extract symbols from stockinfo results
symbols = [row['Symbol'] for row in data]
# Intersect with tables present in stocktrade_database
symbols_to_check = sorted([s for s in symbols if s in all_tables])

result = json.dumps(symbols_to_check)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_pioxFm3HMNADNVHF9KBLRTjt': 'file_storage/call_pioxFm3HMNADNVHF9KBLRTjt.json', 'var_call_rL51DkgtzdOWrf1cILYO8Xv8': 'file_storage/call_rL51DkgtzdOWrf1cILYO8Xv8.json'}

exec(code, env_args)
