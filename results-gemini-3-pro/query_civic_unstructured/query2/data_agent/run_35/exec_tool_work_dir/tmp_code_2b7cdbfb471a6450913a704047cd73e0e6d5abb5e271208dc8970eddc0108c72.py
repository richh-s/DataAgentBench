code = """import json

with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    lines = doc['text'].splitlines()
    indices = []
    for i, line in enumerate(lines):
        if ("Updates" in line and ":" in line) or ("Project Description" in line and ":" in line):
             indices.append(i)
    
    for k, idx in enumerate(indices):
        t_idx = idx - 1
        while t_idx >= 0 and not lines[t_idx].strip():
            t_idx -= 1
        if t_idx < 0: continue
        title = lines[t_idx].strip()
        
        if k + 1 < len(indices):
            next_idx = indices[k+1]
            nt_idx = next_idx - 1
            while nt_idx > idx and not lines[nt_idx].strip():
                nt_idx -= 1
            end_idx = nt_idx
        else:
            end_idx = len(lines)
        
        chunk = " ".join(lines[idx:end_idx]).lower()
        projects.append({"name": title, "text": chunk})

park_projects = []
for p in projects:
    name = p["name"]
    text = p["text"]
    
    # Check if park related (in name or text)
    if "park" in name.lower() or "playground" in name.lower() or "park" in text:
        # Check completion
        is_completed = False
        if "construction was completed" in text and "2022" in text:
             idx = text.find("construction was completed")
             if "2022" in text[idx:idx+60]:
                 is_completed = True
        elif "construction completed" in text and "2022" in text:
             idx = text.find("construction completed")
             if "2022" in text[idx:idx+60]:
                 is_completed = True
        elif "project completed" in text and "2022" in text:
             idx = text.find("project completed")
             if "2022" in text[idx:idx+60]:
                 is_completed = True
                 
        if is_completed:
            park_projects.append(name)

# Dedupe
park_projects = list(set(park_projects))

# Funding
funding_map = {d["Project_Name"].strip().lower(): int(d["Amount"]) for d in funding_data}
total = 0
matched = []
unmatched = []

for name in park_projects:
    clean_name = name.strip()
    n_lower = clean_name.lower()
    
    found_amt = 0
    if n_lower in funding_map:
        found_amt = funding_map[n_lower]
    else:
        for k, v in funding_map.items():
            if n_lower in k or k in n_lower:
                if abs(len(k) - len(n_lower)) < 20:
                    found_amt = v
                    break
    
    if found_amt > 0:
        total += found_amt
        matched.append(name)
    else:
        unmatched.append(name)

print("__RESULT__:")
print(json.dumps({"total": total, "matched": matched, "unmatched": unmatched}))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json', 'var_function-call-17487850353349175697': {'total': 125000, 'matched': ['Bluffs Park Shade Structure', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Malibu Park Drainage Improvements', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}, 'var_function-call-4855220179000724509': {'total': 21000, 'matched': ['Bluffs Park Shade Structure'], 'unmatched': []}}

exec(code, env_args)
