code = """import json
# Correct variable names from storage
with open(var_call_TPrlylFvNg0ArgMCp6iMvsZG, 'r') as f:
    stockinfo = json.load(f)
with open(var_call_ZRBtlxtgy59qSRwQ30i11mL9, 'r') as f:
    trade_tables = json.load(f)
# stockinfo is a list of dicts with keys Symbol and Company Description
symbols = []
mapping = {}
trade_set = set(trade_tables)
for rec in stockinfo:
    sym = rec.get('Symbol')
    if sym in trade_set:
        symbols.append(sym)
        mapping[sym] = rec.get('Company Description')
# sort symbols for consistency
symbols = sorted(symbols)
output = {'symbols': symbols, 'mapping_sample_count': len(mapping)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ZRBtlxtgy59qSRwQ30i11mL9': 'file_storage/call_ZRBtlxtgy59qSRwQ30i11mL9.json', 'var_call_TPrlylFvNg0ArgMCp6iMvsZG': 'file_storage/call_TPrlylFvNg0ArgMCp6iMvsZG.json'}

exec(code, env_args)
