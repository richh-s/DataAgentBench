code = """import json
import re

# Load data
with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-9845122995383564769'], 'r') as f:
    funding_data = json.load(f)

# Normalize project names
def normalize(name):
    # Remove (FEMA...), (CalOES...), (CalJPIA...)
    # Remove leading/trailing spaces
    # Case insensitive for matching
    base = re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA).*?\)$', '', name, flags=re.IGNORECASE)
    return base.strip()

funding_base_names = set()
for row in funding_data:
    funding_base_names.add(normalize(row['Project_Name']))

project_data = {} # name -> {'disaster': False, 'started_2022': False}

# Iterate docs
for doc in civic_docs:
    text = doc['text']
    # Split by lines
    lines = text.split('\n')
    
    current_proj = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        # Check if this line is a project name
        # We check if it matches a funding base name
        # Heuristic: exact match or contained
        # The line in doc might be "2022 Morning View..."
        # Funding might be "Morning View..."
        # Or Funding might be "2022 Morning View..."
        
        found = None
        # Try direct match
        if line_clean in funding_base_names:
            found = line_clean
        else:
            # Check if line contains a base name
            for base in funding_base_names:
                if base in line_clean:
                    # Verify it's effectively the whole line or close to it
                    if len(line_clean) < len(base) + 10:
                        found = base
                        break
        
        if found:
            current_proj = found
            if current_proj not in project_data:
                project_data[current_proj] = {'disaster': False, 'started_2022': False, 'raw_text': []}
            continue
            
        if current_proj:
            project_data[current_proj]['raw_text'].append(line_clean)
            
            # Check for disaster keywords
            disaster_kw = ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster", "Emergency"]
            for kw in disaster_kw:
                if kw.lower() in line_clean.lower():
                    project_data[current_proj]['disaster'] = True
            
            # Check for start date 2022
            # "Begin Construction: ... 2022"
            if "Begin Construction" in line_clean or "Start Construction" in line_clean:
                if "2022" in line_clean:
                    project_data[current_proj]['started_2022'] = True
            
            # "Construction was completed ... 2022"
            if "Construction was completed" in line_clean and "2022" in line_clean:
                project_data[current_proj]['started_2022'] = True
            
            # "Awarded ... 2022"
            if "Awarded" in line_clean and "2022" in line_clean:
                project_data[current_proj]['started_2022'] = True

# Process funding data
total_funding = 0
matched_projects = []

for row in funding_data:
    raw_name = row['Project_Name']
    base = normalize(raw_name)
    amount = int(row['Amount'])
    
    # Is it disaster?
    # 1. Name has suffix
    is_disaster_name = False
    if re.search(r'\((?:FEMA|CalOES|CalJPIA).*?\)', raw_name, re.IGNORECASE):
        is_disaster_name = True
    
    # 2. Text context
    is_disaster_text = False
    started_2022 = False
    
    if base in project_data:
        if project_data[base]['disaster']:
            is_disaster_text = True
        if project_data[base]['started_2022']:
            started_2022 = True
    
    # Is it disaster related?
    is_disaster = is_disaster_name or is_disaster_text
    
    if is_disaster and started_2022:
        total_funding += amount
        matched_projects.append({'name': raw_name, 'amount': amount})

print("__RESULT__:")
print(json.dumps({'total_funding': total_funding, 'matched_projects': matched_projects}))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json'}

exec(code, env_args)
