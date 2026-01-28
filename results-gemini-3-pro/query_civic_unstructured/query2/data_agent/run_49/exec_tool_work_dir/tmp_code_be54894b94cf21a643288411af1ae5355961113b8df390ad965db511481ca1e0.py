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
    full_text += doc['text'] + "\n"

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
        
        # Check for completion in 2022
        # Use simple string checks to avoid regex escaping hell in JSON
        snippet_lower = snippet.lower()
        if "construction was completed" in snippet_lower:
            # Check for 2022 nearby
            # Find the index of "construction was completed"
            idx = snippet_lower.find("construction was completed")
            # Check the next 50 chars for "2022"
            date_snippet = snippet_lower[idx:idx+50]
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
    "total_funding": total_funding,
    "park_projects_found": list(park_projects.keys())
}))"""

env_args = {'var_function-call-17376844456995135534': ['Funding'], 'var_function-call-17376844456995138725': 'file_storage/function-call-17376844456995138725.json', 'var_function-call-17829266993034408002': 'file_storage/function-call-17829266993034408002.json'}

exec(code, env_args)
