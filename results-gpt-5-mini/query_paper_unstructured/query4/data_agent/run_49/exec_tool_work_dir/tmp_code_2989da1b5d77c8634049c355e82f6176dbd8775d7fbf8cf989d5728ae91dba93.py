code = """import json, re
# Load data from previous Mongo query result stored in var_call_I9tf0clGC8oTadzuC6RDDAPU
data = None
try:
    if isinstance(var_call_I9tf0clGC8oTadzuC6RDDAPU, str):
        with open(var_call_I9tf0clGC8oTadzuC6RDDAPU, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = var_call_I9tf0clGC8oTadzuC6RDDAPU
except Exception as e:
    data = var_call_I9tf0clGC8oTadzuC6RDDAPU

titles = []
for doc in data:
    text = doc.get('text','')
    if not text:
        continue
    if re.search(r'physical activity', text, re.I):
        if re.search(r'\b2016\b', text):
            filename = doc.get('filename','')
            if filename.endswith('.txt'):
                title = filename[:-4]
            else:
                title = filename
            titles.append(title)

# deduplicate
titles = sorted(list(dict.fromkeys(titles)))
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json'}

exec(code, env_args)
