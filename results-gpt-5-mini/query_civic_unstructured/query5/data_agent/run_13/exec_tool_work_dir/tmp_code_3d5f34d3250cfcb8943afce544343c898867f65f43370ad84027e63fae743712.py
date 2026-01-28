code = """import json, re

funding_path = var_call_5bTpei777tnyEwOoHrzoqjsN
civic_docs_path = var_call_v3QtXqLSAoVAAsdW3jdtOTEz

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Normalize amounts
for r in funding:
    val = r.get('TotalAmount', 0)
    try:
        r['TotalAmount'] = int(val)
    except:
        digits = re.sub(r"[^0-9]", "", str(val))
        r['TotalAmount'] = int(digits) if digits else 0

keywords = ['fema', 'caloes', 'caljpia', 'fema/']

civic_texts = [d.get('text','') for d in civic_docs]

matched = []
seen = set()

for rec in funding:
    name = rec.get('Project_Name','')
    name_l = name.lower()
    if any(k in name_l for k in keywords):
        base = re.sub(r"\s*\([^)]*\)", "", name).strip()
        base_l = base.lower()
        found_2022 = False
        for text in civic_texts:
            t_l = text.lower()
            for pattern in (name_l, base_l):
                if not pattern:
                    continue
                idx = t_l.find(pattern)
                if idx != -1:
                    start = max(0, idx-200)
                    end = min(len(t_l), idx+len(pattern)+200)
                    snippet = t_l[start:end]
                    if '2022' in snippet:
                        found_2022 = True
                        break
            if found_2022:
                break
        if found_2022:
            if name not in seen:
                matched.append({'Project_Name': name, 'Base_Name': base, 'Amount': rec['TotalAmount']})
                seen.add(name)

# Sum amounts
total = sum(m['Amount'] for m in matched)

result = {'total_disaster_funding_started_2022': total, 'matched_projects': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_HlLq4TH1LZBMTIGorZ4YldDZ': ['Funding'], 'var_call_rD258WLarCW4yILJiRDBIw8J': ['civic_docs'], 'var_call_v3QtXqLSAoVAAsdW3jdtOTEz': 'file_storage/call_v3QtXqLSAoVAAsdW3jdtOTEz.json', 'var_call_5bTpei777tnyEwOoHrzoqjsN': 'file_storage/call_5bTpei777tnyEwOoHrzoqjsN.json'}

exec(code, env_args)
