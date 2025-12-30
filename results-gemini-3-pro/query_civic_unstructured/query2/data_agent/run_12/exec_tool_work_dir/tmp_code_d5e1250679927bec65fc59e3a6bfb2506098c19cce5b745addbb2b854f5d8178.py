code = """import json
import re

# Load civic docs
with open(locals()['var_function-call-12716671968640832607'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-12716671968640831510'], 'r') as f:
    funding_data = json.load(f)

# Create a dictionary for funding: Name -> Amount
funding_map = {item['Project_Name']: int(item['Amount']) for item in funding_data}

# Extract text
text = civic_docs[0]['text']

# Regex to find projects
# Pattern: Project Name (line) followed by (cid:190) (Updates|Project Description|Project Updates)
# We assume the project name is the non-empty line before the marker.
# We'll split the text by the marker logic to get chunks.

# Find all starts of projects
# (cid:190) is \u00be
marker_regex = re.compile(r'\n([^\n]+)\s*\n\s*(?:\(cid:190\)|\u00be)\s*(?:Updates|Project Description|Project Updates)', re.MULTILINE)

projects = []
matches = list(marker_regex.finditer(text))

for i, match in enumerate(matches):
    project_name = match.group(1).strip()
    start_idx = match.end()
    
    # End index is the start of the next project, or end of string
    if i + 1 < len(matches):
        # We need to find where the next project name starts. 
        # The next match start is the beginning of the name line.
        end_idx = matches[i+1].start()
    else:
        end_idx = len(text)
    
    project_text = text[start_idx:end_idx]
    
    projects.append({
        'name': project_name,
        'text': project_text
    })

# Filter for Park projects completed in 2022
target_projects = []
total_funding = 0

keywords = ['park', 'playground']

for p in projects:
    name = p['name']
    details = p['text']
    
    # Check Topic
    is_park = any(k in name.lower() for k in keywords)
    # Also check if description mentions park if name doesn't? 
    # Prompt says "topic field contains...". Since I don't have the field, I rely on name.
    # Let's inspect "Bluffs Park", "Trancas Canyon Park" -> they have "Park".
    # "Point Dume Walkway" -> Not explicit.
    # Let's check description for "park" if name doesn't have it?
    # "Bluffs Park Shade Structure" -> yes.
    # "Point Dume Walkway Repairs" -> description?
    # Let's stick to name keywords first.
    
    if not is_park:
        continue
        
    # Check Status and Date
    # Look for "completed" and "2022"
    # Regex for completion date
    # "Construction was completed November 2022"
    # "Construction was completed, November 2022"
    
    # Find "completed" followed by date
    # We want to ensure it refers to 2022.
    
    completed_match = re.search(r'completed.*?([A-Za-z]+)\s*(\d{4})', details, re.IGNORECASE)
    
    is_completed_2022 = False
    if completed_match:
        month = completed_match.group(1)
        year = completed_match.group(2)
        if year == '2022':
            is_completed_2022 = True
            
    if is_completed_2022:
        amount = funding_map.get(name, 0)
        target_projects.append({'name': name, 'amount': amount})
        total_funding += amount

print("__RESULT__:")
print(json.dumps({'target_projects': target_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-12716671968640832607': 'file_storage/function-call-12716671968640832607.json', 'var_function-call-12716671968640831510': 'file_storage/function-call-12716671968640831510.json'}

exec(code, env_args)
