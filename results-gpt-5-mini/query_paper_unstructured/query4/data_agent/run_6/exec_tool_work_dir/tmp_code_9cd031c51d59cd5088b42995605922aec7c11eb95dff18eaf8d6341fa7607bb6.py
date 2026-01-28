code = """import json, re
path = var_call_VUXvOspLetLt5Con2KvfAtOt
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

total = len(docs)
count_physical = 0
count_2016 = 0
count_both = 0
samples = []
for d in docs:
    text = d.get('text','') or ''
    has_phys = bool(re.search(r'physical activity', text, re.I))
    has_2016 = bool(re.search(r'\b2016\b', text))
    if has_phys:
        count_physical += 1
    if has_2016:
        count_2016 += 1
    if has_phys and has_2016:
        count_both += 1
        if len(samples) < 20:
            filename = d.get('filename','')
            title = filename[:-4] if filename.lower().endswith('.txt') else filename
            samples.append(title)

import json as _json
out = {"total_docs": total, "count_physical": count_physical, "count_2016": count_2016, "count_both": count_both, "samples": samples}
print("__RESULT__:")
print(_json.dumps(out))"""

env_args = {'var_call_IGldEbXgZoelD1zKxMwMtdEX': ['paper_docs'], 'var_call_XACNxD8OT8SN9vqerPeW7TT0': ['Citations', 'sqlite_sequence'], 'var_call_VUXvOspLetLt5Con2KvfAtOt': 'file_storage/call_VUXvOspLetLt5Con2KvfAtOt.json', 'var_call_fqeblluy4MCxoD3QTv0TmFbA': [], 'var_call_MNhg9l6BcC75PtwFc5e5j8E2': 'file_storage/call_MNhg9l6BcC75PtwFc5e5j8E2.json', 'var_call_d3174HDFIbtarpuuLwakJwIl': []}

exec(code, env_args)
