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
        if '(cid:190) Updates' in line or '(cid:190) Project Description' in line:
            # Find title
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                title = lines[j].strip()
                # Ignore "Capital Improvement Projects (Design)" type headers
                if "Capital Improvement Projects" in title or "Page" in title:
                    continue
                
                # Get text chunk (next 30 lines)
                chunk_lines = lines[i:i+30]
                chunk_text = " ".join(chunk_lines).lower()
                
                projects.append({'name': title, 'text': chunk_text})

park_projects_2022 = []
for p in projects:
    name = p['name']
    text = p['text']
    
    if 'park' in name.lower() or 'playground' in name.lower():
        # Check completion
        # Logic: "completed" and "2022"
        # We also need to avoid "complete design: ... 2022"
        # The text snippet had: "Construction was completed November 2022"
        # "Construction was completed, January 2023"
        # "Complete Construction: Summer 2023"
        
        # We want Completed in 2022.
        # Check for 'completed' (past tense) + '2022'
        # Or 'notice of completion' + '2022'
        # Or 'complete construction: ... 2022' is NOT valid if it's a schedule (future). 
        # But 'Complete Construction: November 2022' would be valid? 
        # Usually schedule says "Summer 2023". If it says a month/year in the past, it's done.
        
        # Let's strict match "completed" (past tense) or "notice of completion"
        # AND "2022"
        
        if 'completed' in text or 'notice of completion' in text:
            if '2022' in text:
                # Exclude if it only says "complete design"
                # But 'completed' covers 'complete design'? No, 'completed' is past of complete.
                # "Complete Design" -> "Complete" is adjective or verb.
                # "Construction was completed" -> "completed" is verb.
                
                # Check for "design" nearby?
                # If "design" appears in the same sentence as completed?
                # Text: "Complete Design: Summer 2023" -> 'complete' (not completed)
                # Text: "Construction was completed November 2022" -> 'completed'
                # So searching for "completed" (with d) is good.
                
                if 'completed' in text:
                    # Verify it refers to the project/construction, not design
                    # If the string is "completed design", we ignore?
                    # Snippet: "Construction was completed November 2022"
                    # Snippet: "Construction was completed, January 2023"
                    park_projects_2022.append(name)
                elif 'notice of completion' in text:
                    park_projects_2022.append(name)

# Funding Match
funding_map = {item['Project_Name'].strip().lower(): int(item['Amount']) for item in funding_data}

total_funding = 0
matched = []
unmatched = []

# Deduplicate names
unique_park_projects = list(set(park_projects_2022))

for name in unique_park_projects:
    found = False
    # Exact match
    if name.lower() in funding_map:
        amt = funding_map[name.lower()]
        total_funding += amt
        matched.append((name, amt))
        found = True
    else:
        # Check for name variations
        # e.g. "Bluffs Park Shade Structure" vs "Bluffs Park Shade Structure Project"
        # or "(CalOES Project)" suffix
        # Let's check if the name is a substring of a funding key or vice versa
        for fname, famt in funding_map.items():
            if name.lower() in fname or fname in name.lower():
                # Verify similarity to avoid bad matches (e.g. "Park" in "Park Road")
                # Length difference shouldn't be too big
                if abs(len(name) - len(fname)) < 15:
                    total_funding += famt
                    matched.append((name, famt))
                    found = True
                    break
        if not found:
            unmatched.append(name)

print("__RESULT__:")
print(json.dumps({"total": total_funding, "matched": matched, "unmatched": unmatched}))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json'}

exec(code, env_args)
