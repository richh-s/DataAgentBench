code = """import json, string

# Load stored result files
with open(var_call_SdeIzpwHWXTGbiSgCGNZzY8M, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Combine all document texts into one lowercase string
combined_text = ' '.join(d.get('text','') for d in docs).lower()

# Normalization helper: remove punctuation and collapse spaces
trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

def normalize(s):
    if s is None:
        return ''
    return ' '.join(s.lower().translate(trans).split())

norm_combined = normalize(combined_text)

matched = []
for rec in funding:
    amt_raw = rec.get('Amount', 0)
    try:
        amt = int(str(amt_raw))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            amt = 0
    if amt <= 50000:
        continue
    pname = rec.get('Project_Name', '').strip()
    if not pname:
        continue
    base = pname.split('(')[0].strip()
    if normalize(pname) and normalize(pname) in norm_combined:
        matched.append(pname)
        continue
    if base and normalize(base) and normalize(base) in norm_combined:
        matched.append(pname)
        continue

# Unique by normalized base name
unique_norms = set()
for m in matched:
    base = m.split('(')[0].strip()
    unique_norms.add(normalize(base))

result_count = len(unique_norms)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json', 'var_call_IP5GqWbgBMXPgqtaW3fnctqw': {'fund_len': 276, 'docs_len': 5}}

exec(code, env_args)
