code = """import json, re
path = var_call_VUXvOspLetLt5Con2KvfAtOt
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
results = []
for d in docs[:200]:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    has_2016 = bool(re.search(r"2016", text))
    # find contexts
    contexts = []
    for m in re.finditer(r"(.{0,40}2016.{0,40})", text):
        contexts.append(m.group(1))
    # find first year by regex full year
    year_match = re.search(r"\b(?:19|20)\d{2}\b", text)
    year = int(year_match.group(0)) if year_match else None
    results.append({"title":title, "has_2016": has_2016, "year_detected": year, "contexts_2016": contexts[:3]})

import json as _json
print("__RESULT__:")
print(_json.dumps(results))"""

env_args = {'var_call_IGldEbXgZoelD1zKxMwMtdEX': ['paper_docs'], 'var_call_XACNxD8OT8SN9vqerPeW7TT0': ['Citations', 'sqlite_sequence'], 'var_call_VUXvOspLetLt5Con2KvfAtOt': 'file_storage/call_VUXvOspLetLt5Con2KvfAtOt.json', 'var_call_fqeblluy4MCxoD3QTv0TmFbA': []}

exec(code, env_args)
