code = """import json
import re

# Load Funding Data
with open('var_function-call-17829266993034408002.json', 'r') as f:
    funding_data = json.load(f)

# Load Civic Docs Data
with open('var_function-call-17376844456995138725.json', 'r') as f:
    civic_data = json.load(f)

# Combine text
full_text = ""
for doc in civic_data:
    full_text += doc['text'] + chr(10)

# Filter Park Projects from Funding Data
park_projects = {}
all_project_names = set()
for item in funding_data:
    p_name = item['Project_Name']
    all_project_names.add(p_name)
    if 'park' in p_name.lower():
        if p_name not in park_projects:
            park_projects[p_name] = 0
        park_projects[p_name] += item['Amount']

# Check completion
completed_projects_2022 = []

for p_name in park_projects:
    # Escape regex special chars in project name
    pattern = re.escape(p_name)
    matches = [m.start() for m in re.finditer(pattern, full_text, re.IGNORECASE)]
    
    is_completed_2022 = False
    for start_idx in matches:
        # Window of 1000 chars
        snippet = full_text[start_idx:start_idx+1000]
        snippet_lower = snippet.lower()
        
        # Check for completion in 2022
        phrase = "construction was completed"
        if phrase in snippet_lower:
            idx = snippet_lower.find(phrase)
            # Check the next 100 chars for "2022"
            date_snippet = snippet_lower[idx:idx+100]
            if "2022" in date_snippet:
                is_completed_2022 = True
                break
        
    if is_completed_2022:
        completed_projects_2022.append(p_name)

total_funding = 0
for p_name in completed_projects_2022:
    total_funding += park_projects[p_name]

print("__RESULT__:")
print(json.dumps({
    "completed_park_projects": completed_projects_2022,
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-17376844456995135534': ['Funding'], 'var_function-call-17376844456995138725': 'file_storage/function-call-17376844456995138725.json', 'var_function-call-17829266993034408002': 'file_storage/function-call-17829266993034408002.json'}

exec(code, env_args)
