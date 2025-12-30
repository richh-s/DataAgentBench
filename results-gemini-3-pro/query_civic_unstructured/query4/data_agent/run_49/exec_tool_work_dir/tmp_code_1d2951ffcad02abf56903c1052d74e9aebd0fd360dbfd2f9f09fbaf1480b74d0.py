code = """import json
import re

# Load Funding Data
with open(locals()['var_function-call-1003584179187242714'], 'r') as f:
    funding_data = json.load(f)

funding_projects = {item['Project_Name']: item for item in funding_data}
project_names = list(funding_projects.keys())

# Load Civic Docs
with open(locals()['var_function-call-1003584179187241629'], 'r') as f:
    civic_docs = json.load(f)

def normalize(text):
    return text.strip().lower()

# Regex for Spring 2022
# Using double backslashes for JSON compatibility if needed, though usually the tool handles it.
# Start Date Pattern: Spring 2022, March 2022, April 2022, May 2022
# Also 03/2022, 04/2022, 05/2022
month_year_regex = r"(spring|march|april|may),?\s*2022"

started_projects = set()
debug_matches = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Identify Project Name
        found = False
        # strict match preferred
        norm_line = normalize(line)
        for name in project_names:
            if norm_line == normalize(name):
                current_project = name
                found = True
                break
        
        if found:
            continue
        
        # If we are in a project block, look for start date
        if current_project:
            # Check for start indicators
            lower_line = line.lower()
            
            # Indicators: "begin construction", "start date", "construction start"
            # We want to avoid "design start" unless the user considers that "start".
            # Usually "projects started" implies construction or the main phase. 
            # Given the text "Capital Improvement Projects (Design)" vs "(Construction)",
            # "Started" might be ambiguous. 
            # However, usually "Spring 2022" appearing with "Begin Construction" is a strong signal.
            
            if "begin construction" in lower_line or "construction start" in lower_line:
                # Check for date
                if re.search(month_year_regex, lower_line, re.IGNORECASE):
                    started_projects.add(current_project)
                    debug_matches.append((current_project, line))
            
            # Reset current_project if we hit a new header or something?
            # The structure seems to be Project Name -> details -> Project Name -> details.
            # So `current_project` stays valid until a new project name is found (which is handled above).
            # But we should be careful about other headers.
            # "Capital Improvement Projects (...)" is a header.
            if "capital improvement projects" in lower_line:
                current_project = None

total_funding = 0
for p in started_projects:
    total_funding += int(funding_projects[p]['Amount'])

print("__RESULT__:")
print(json.dumps({
    "count": len(started_projects),
    "total_funding": total_funding,
    "projects": list(started_projects),
    "matches": debug_matches
}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)
