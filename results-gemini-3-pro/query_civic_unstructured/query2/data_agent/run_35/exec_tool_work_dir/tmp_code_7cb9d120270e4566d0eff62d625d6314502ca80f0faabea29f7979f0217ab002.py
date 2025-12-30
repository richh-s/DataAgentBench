code = """import json

with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    lines = doc['text'].splitlines()
    # Find all indices of lines containing "Updates:" or "Project Description:"
    # Also require them to have the bullet (length check or content check)
    indices = []
    for i, line in enumerate(lines):
        if ("Updates" in line and ":" in line) or ("Project Description" in line and ":" in line):
             indices.append(i)
    
    for k, idx in enumerate(indices):
        # Title is likely the line before, unless empty
        t_idx = idx - 1
        while t_idx >= 0 and not lines[t_idx].strip():
            t_idx -= 1
        
        if t_idx < 0: continue
        title = lines[t_idx].strip()
        
        # End index is the start of the next project's title (approx next index - 1)
        if k + 1 < len(indices):
            next_idx = indices[k+1]
            # backtrack from next_idx to find its title start
            nt_idx = next_idx - 1
            while nt_idx > idx and not lines[nt_idx].strip():
                nt_idx -= 1
            end_idx = nt_idx # Start of next title is nt_idx, so content ends before it
        else:
            end_idx = len(lines)
        
        chunk = " ".join(lines[idx:end_idx]).lower()
        projects.append({"name": title, "text": chunk})

park_projects = []
for p in projects:
    name = p["name"]
    text = p["text"]
    
    # Filter for park
    if "park" not in name.lower() and "playground" not in name.lower():
        continue
    
    # Stricter completion check
    is_completed = False
    
    # Check 1: "construction was completed" + 2022
    if "construction was completed" in text and "2022" in text:
        # Check if 2022 is near 'completed'
        # Split by sentences or simplistic distance check?
        # Snippet: "Construction was completed November 2022"
        # Just check if '2022' is in text. 
        # But watch out for "Construction was completed January 2023... (Project started 2022)"
        # Or "Construction was completed. 2022 Annual Report..."
        # Let's extract the date near "completed".
        
        # Find index of "construction was completed"
        # Look at the next 20 chars
        idx = text.find("construction was completed")
        context = text[idx:idx+50]
        if "2022" in context:
            is_completed = True
    
    # Check 2: "notice of completion" + 2022 (filed in 2022? or completed in 2022?)
    # Snippet: "Construction was completed November 2022. Notice of completion filed January 2023"
    # So Notice filed in 2023, but completed in 2022.
    # If "notice of completion" is 2022, it was likely completed in 2022 or late 2021.
    # But "Construction was completed" is the gold standard.
    
    # Check 3: "project completed" + 2022
    if not is_completed and "project completed" in text and "2022" in text:
         idx = text.find("project completed")
         context = text[idx:idx+50]
         if "2022" in context:
             is_completed = True

    # Check 4: "construction completed" + 2022
    if not is_completed and "construction completed" in text and "2022" in text:
         idx = text.find("construction completed")
         context = text[idx:idx+50]
         if "2022" in context:
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
        # Fuzzy
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

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json', 'var_function-call-17487850353349175697': {'total': 125000, 'matched': ['Bluffs Park Shade Structure', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Malibu Park Drainage Improvements', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}}

exec(code, env_args)
