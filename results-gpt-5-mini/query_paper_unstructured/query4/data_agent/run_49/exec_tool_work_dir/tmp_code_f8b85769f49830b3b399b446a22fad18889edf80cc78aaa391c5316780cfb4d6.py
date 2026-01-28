code = """import json, re
# load both Mongo query results
data1 = None
data2 = None
try:
    if isinstance(var_call_1Bqplr3rh53ChNvtEOW1gjRS, str):
        with open(var_call_1Bqplr3rh53ChNvtEOW1gjRS, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
    else:
        data1 = var_call_1Bqplr3rh53ChNvtEOW1gjRS
except Exception as e:
    data1 = var_call_1Bqplr3rh53ChNvtEOW1gjRS

try:
    if isinstance(var_call_I9tf0clGC8oTadzuC6RDDAPU, str):
        with open(var_call_I9tf0clGC8oTadzuC6RDDAPU, 'r', encoding='utf-8') as f:
            data2 = json.load(f)
    else:
        data2 = var_call_I9tf0clGC8oTadzuC6RDDAPU
except Exception as e:
    data2 = var_call_I9tf0clGC8oTadzuC6RDDAPU

all_docs = []
if isinstance(data1, list):
    all_docs.extend(data1)
if isinstance(data2, list):
    all_docs.extend(data2)

results = []
for doc in all_docs:
    text = doc.get('text','')
    if not text:
        continue
    if re.search(r'physical activity', text, re.I):
        filename = doc.get('filename','')
        title = filename[:-4] if filename.endswith('.txt') else filename
        # attempt to extract year
        year = None
        # search for 4-digit year
        m = re.search(r"\b(19|20)\d{2}\b", text)
        if m:
            year = int(m.group(0))
        else:
            # search for patterns like '16 (with apostrophe)
            m2 = re.search(r"'(?P<yy>\d{2})", text)
            if m2:
                yy = int(m2.group('yy'))
                # assume 2000s
                year = 2000 + yy
        results.append({"title": title, "year": year})

# filter for year==2016
titles_2016 = [r['title'] for r in results if r.get('year')==2016]
# deduplicate
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': []}

exec(code, env_args)
