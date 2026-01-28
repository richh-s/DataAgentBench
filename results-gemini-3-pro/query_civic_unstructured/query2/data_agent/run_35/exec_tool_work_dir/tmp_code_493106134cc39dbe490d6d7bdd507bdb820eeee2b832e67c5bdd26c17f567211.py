code = """import json
import re

# Load data
with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

# Extract projects
projects = []
for doc in civic_docs:
    text = doc['text']
    
    # Regex pattern: 
    # Finds a line with text, followed by a line starting with (cid:190) (or similar bullet) and keywords
    # We use \\n to match newlines safely.
    pattern_str = r'\n([A-Z0-9][^\n]+?)\s*\n\s*\(cid:190\)\s*(?:Updates|Project Description)'
    
    matches = list(re.finditer(pattern_str, text, re.MULTILINE))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        project_text = text[start_idx:end_idx]
        
        projects.append({
            'name': project_name,
            'text': project_text
        })

park_projects_2022 = []
for p in projects:
    name = p['name']
    p_text = p['text'].lower()
    
    # Filter for park
    if 'park' in name.lower() or 'playground' in name.lower():
        # Check completion in 2022
        # Look for "completed" and "2022"
        if 'completed' in p_text and '2022' in p_text:
            # Simple check first, maybe refine if false positives occur
            # Specifically check if "completed" and "2022" are close or in same line
            lines = p_text.split('\n')
            for line in lines:
                if 'completed' in line and '2022' in line:
                    park_projects_2022.append(name)
                    break

# Match with funding
funding_map = {item['Project_Name'].strip().lower(): int(item['Amount']) for item in funding_data}

total_funding = 0
matched = []
unmatched = []

for name in set(park_projects_2022):
    # Direct match
    if name.lower() in funding_map:
        amt = funding_map[name.lower()]
        total_funding += amt
        matched.append((name, amt))
    else:
        unmatched.append(name)

# If unmatched, try fuzzy or partial
# From preview: "Bluffs Park Shade Structure" matched perfectly.
# "Broad Beach Road Water Quality Repair" matched perfectly.

result = {
    "total_funding": total_funding,
    "matched": matched,
    "unmatched": unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json'}

exec(code, env_args)
