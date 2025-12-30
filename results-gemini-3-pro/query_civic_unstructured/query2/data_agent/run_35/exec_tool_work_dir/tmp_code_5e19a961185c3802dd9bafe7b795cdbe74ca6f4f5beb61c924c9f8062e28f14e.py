code = """import json

with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        # check markers
        if "Updates" in line and ":" in line:
            # check if previous line is title
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()
                if "Capital" in title or "Page" in title:
                    continue
                # chunk
                chunk = " ".join(lines[i:i+40]).lower()
                projects.append({"name": title, "text": chunk})

park_projects = []
for p in projects:
    name = p["name"]
    text = p["text"]
    if "park" in name.lower() or "playground" in name.lower():
        if "completed" in text and "2022" in text:
            park_projects.append(name)
        elif "completion" in text and "2022" in text:
            park_projects.append(name)

# Funding
funding_map = {d["Project_Name"].strip().lower(): int(d["Amount"]) for d in funding_data}
total = 0
matched = []
seen = set()

for name in park_projects:
    if name in seen: continue
    seen.add(name)
    
    n_lower = name.lower()
    found_amt = 0
    
    # Exact
    if n_lower in funding_map:
        found_amt = funding_map[n_lower]
    else:
        # fuzzy
        for k, v in funding_map.items():
            if n_lower in k or k in n_lower:
                 # Check length
                 if abs(len(k) - len(n_lower)) < 20:
                     found_amt = v
                     break
    
    if found_amt > 0:
        total += found_amt
        matched.append(name)

print("__RESULT__:")
print(json.dumps({"total": total, "matched": matched}))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json'}

exec(code, env_args)
