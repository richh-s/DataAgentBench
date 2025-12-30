code = """import json

# Load data
with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    lines = doc['text'].split('\n')
    for i, line in enumerate(lines):
        # Loose matching for the section headers
        if 'Updates:' in line or 'Project Description:' in line:
            # Check if it has the bullet or just looks like a header
            # The preview showed "(cid:190) Updates:"
            if not ('Updates:' in line or 'Project Description:' in line):
                continue
                
            # Find title in previous lines
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            
            if j >= 0:
                title = lines[j].strip()
                # Ignore generic headers
                if "Capital Improvement Projects" in title or "Page" in title or "Agenda" in title:
                    continue
                
                # Get text chunk
                chunk_lines = lines[i:i+30]
                chunk_text = " ".join(chunk_lines).lower()
                
                projects.append({'name': title, 'text': chunk_text})

park_projects_2022 = []
for p in projects:
    name = p['name']
    text = p['text']
    
    if 'park' in name.lower() or 'playground' in name.lower():
        # Check completion
        if 'completed' in text and '2022' in text:
            # verify 'completed' is not 'completed design'
            # simple check: if 'construction was completed' or 'completed, november 2022' etc.
            park_projects_2022.append(name)
        elif 'notice of completion' in text and '2022' in text:
            park_projects_2022.append(name)

# Funding Match
funding_map = {item['Project_Name'].strip().lower(): int(item['Amount']) for item in funding_data}

total_funding = 0
matched = []
unmatched = []

unique_park_projects = list(set(park_projects_2022))

for name in unique_park_projects:
    found = False
    
    # Clean name (sometimes title has extra chars?)
    clean_name = name.strip()
    
    # Exact match
    if clean_name.lower() in funding_map:
        amt = funding_map[clean_name.lower()]
        total_funding += amt
        matched.append((clean_name, amt))
        found = True
    else:
        # Fuzzy
        for fname, famt in funding_map.items():
            if clean_name.lower() == fname: # covered by exact
                continue
            # substring match
            if clean_name.lower() in fname or fname in clean_name.lower():
                 # Avoid short matches
                 if len(fname) > 10:
                    # check for major overlap?
                    # "Bluffs Park Shade Structure" in "Bluffs Park Shade Structure"
                    total_funding += famt
                    matched.append((clean_name, famt))
                    found = True
                    break
        if not found:
            unmatched.append(clean_name)

print("__RESULT__:")
print(json.dumps({"total": total_funding, "matched": matched, "unmatched": unmatched}))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json'}

exec(code, env_args)
