code = """import json
# load the Mongo query result
data = None
try:
    if isinstance(var_call_I9tf0clGC8oTadzuC6RDDAPU, str):
        with open(var_call_I9tf0clGC8oTadzuC6RDDAPU, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = var_call_I9tf0clGC8oTadzuC6RDDAPU
except Exception as e:
    data = var_call_I9tf0clGC8oTadzuC6RDDAPU

filenames = [doc.get('filename','') for doc in data]
filenames = sorted(list(dict.fromkeys(filenames)))
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': [], 'var_call_CR3mHeGx2Vc5CLD705Vvdb00': []}

exec(code, env_args)
