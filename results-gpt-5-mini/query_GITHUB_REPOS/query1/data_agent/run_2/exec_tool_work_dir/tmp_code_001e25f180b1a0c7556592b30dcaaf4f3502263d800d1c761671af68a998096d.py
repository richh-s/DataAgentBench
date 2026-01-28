code = """import json

# Load languages data
if isinstance(var_call_OAcMzXQ4h0sAM0j6EdwHTCDR, str):
    with open(var_call_OAcMzXQ4h0sAM0j6EdwHTCDR, 'r', encoding='utf-8') as f:
        langs = json.load(f)
else:
    langs = var_call_OAcMzXQ4h0sAM0j6EdwHTCDR

# Load README contents data
if isinstance(var_call_cO61syuiV82JACtoHx9Avdix, str):
    with open(var_call_cO61syuiV82JACtoHx9Avdix, 'r', encoding='utf-8') as f:
        readmes = json.load(f)
else:
    readmes = var_call_cO61syuiV82JACtoHx9Avdix

print("__RESULT__:")
print(json.dumps({"langs_count": len(langs), "readmes_count": len(readmes)}))"""

env_args = {'var_call_OAcMzXQ4h0sAM0j6EdwHTCDR': 'file_storage/call_OAcMzXQ4h0sAM0j6EdwHTCDR.json', 'var_call_cO61syuiV82JACtoHx9Avdix': 'file_storage/call_cO61syuiV82JACtoHx9Avdix.json'}

exec(code, env_args)
