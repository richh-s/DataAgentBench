code = """import json
import difflib

# Load funding data
with open(locals()['var_function-call-14381109173196317470'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = {item['Project_Name'].strip() for item in funding_data}

# Load civic docs
with open(locals()['var_function-call-3599675758928509690'], 'r') as f:
    civic_docs = json.load(f)

matched_projects = set()
unmatched_candidates = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    in_design_section = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if "Capital Improvement Projects (Design)" in line:
            in_design_section = True
            continue
        elif "Capital Improvement Projects" in line and "(Design)" not in line:
            in_design_section = False
        elif "Disaster Recovery Projects" in line:
            in_design_section = False
            
        if in_design_section:
            # We assume project names are lines that don't start with bullets like (cid:190) or (cid:131)
            # The text snippet shows bullets are "(cid:190)" and "(cid:131)" which might look like garbage characters or specific unicode.
            # Let's check if the line starts with "(" or has "Updates:"
            if line.startswith("(") or "Updates:" in line or "Project Schedule:" in line or "Page " in line or "Agenda Item" in line:
                continue
            
            # Also exclude date lines like "Complete Design: ..."
            if "Complete Design:" in line or "Advertise:" in line or "Begin Construction:" in line:
                continue
                
            # Now we have a candidate line
            if line in high_funding_projects:
                matched_projects.add(line)
            else:
                unmatched_candidates.append(line)

# Let's try to fuzzy match unmatched candidates to funding projects
# This helps identifying if we missed any due to slight naming differences
possible_matches = {}
for cand in unmatched_candidates:
    # Find closest match in funding projects
    matches = difflib.get_close_matches(cand, high_funding_projects, n=1, cutoff=0.6)
    if matches:
        possible_matches[cand] = matches[0]

result = {
    "matched_count": len(matched_projects),
    "matched_list": list(matched_projects),
    "unmatched_candidates": unmatched_candidates,
    "fuzzy_matches": possible_matches
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14381109173196317470': 'file_storage/function-call-14381109173196317470.json', 'var_function-call-14381109173196319441': 'file_storage/function-call-14381109173196319441.json', 'var_function-call-3599675758928509690': 'file_storage/function-call-3599675758928509690.json', 'var_function-call-7727963684795353611': 10}

exec(code, env_args)
