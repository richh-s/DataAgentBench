code = """import json
import re

# Load data
with open(locals()['var_function-call-16242218225032044271'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-16242218225032040752'], 'r') as f:
    civic_docs = json.load(f)

# Extract projects from text
projects = []
for doc in civic_docs:
    text = doc['text']
    # Normalize text slightly to handle bullet points if they are weird chars
    # The snippet showed (cid:190) and (cid:131)
    
    # Regex to find project starts. 
    # Look for a line that is followed by a line starting with (cid:190) or similar bullet and "Updates" or "Project Description"
    # We'll use a lookahead or just capture the pattern.
    
    # Pattern: 
    # Group 1: Project Name (a non-empty line)
    # Followed by optional newlines
    # Followed by (cid:190) (or similar) and (Updates|Project Description)
    
    # We iterate through matches to get chunks
    pattern = re.compile(r'\n([A-Z0-9][^\n]+?)\s*\n\s*(?:\(cid:190\)|¾|•)\s*(?:Updates|Project Description|Project Schedule)', re.MULTILINE)
    
    matches = list(pattern.finditer(text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_idx = match.end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        project_text = text[start_idx:end_idx]
        
        projects.append({
            'name': project_name,
            'text': project_text,
            'source': doc['filename']
        })

# Filter and process
park_projects_2022 = []

for p in projects:
    name = p['name']
    text = p['text'].lower()
    
    # Check if park related
    if 'park' not in name.lower() and 'playground' not in name.lower():
        continue
        
    # Check if completed in 2022
    # Phrases to look for: "completed November 2022", "completed: 2022", "complete construction: ... 2022"
    # But watch out for "Complete Construction: Summer 2023" (future)
    # or "Complete Design: 2022" (not project completion)
    
    # We strictly want project completion.
    # Logic: Look for "construction was completed" or "notice of completion" or "complete construction"
    # AND "2022" in the same sentence or line.
    
    is_completed_2022 = False
    
    # Split text into lines for easier analysis
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check for completion keywords
        if 'completed' in line or 'complete construction' in line or 'notice of completion' in line:
            # Check year
            if '2022' in line:
                # Check negative lookaheads?
                # E.g. "Complete Construction: Summer 2023" -> No
                # "Construction was completed November 2022" -> Yes
                # "Complete Design: Fall 2022" -> No (handled by keyword check)
                
                # Verify it's not "Complete Design"
                if 'design' in line and 'construction' not in line:
                    continue
                
                is_completed_2022 = True
                break
    
    if is_completed_2022:
        park_projects_2022.append(name)

# Now join with funding
total_funding = 0
matched_projects = []

# Normalize funding names
funding_map = {item['Project_Name'].strip().lower(): int(item['Amount']) for item in funding_data}

for proj_name in set(park_projects_2022):
    # Try exact match first
    val = funding_map.get(proj_name.lower())
    if val is not None:
        total_funding += val
        matched_projects.append({'name': proj_name, 'amount': val})
    else:
        # fuzzy match or substring? 
        # The database description says names match.
        # Let's try to match by checking if one is substring of another or very close.
        # But let's check exact first.
        # print("Unmatched:", proj_name)
        pass

result = {
    "total_funding": total_funding,
    "matched_projects": matched_projects,
    "extracted_park_projects": park_projects_2022
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16242218225032044271': 'file_storage/function-call-16242218225032044271.json', 'var_function-call-16242218225032040752': 'file_storage/function-call-16242218225032040752.json'}

exec(code, env_args)
