code = """import json
import re

# Load data
with open(locals()['var_function-call-13241760497320549299'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-8006204082577017619'], 'r') as f:
    funding = json.load(f)

projects_started_spring_2022 = []
total_funding = 0

# Define Spring 2022 patterns
# Spring = March, April, May
# Patterns: "Spring 2022", "March 2022", "April 2022", "May 2022", "Spring, 2022"
spring_patterns = [
    r"Spring,? 2022",
    r"March,? 2022",
    r"April,? 2022",
    r"May,? 2022"
]

# Helper to check date string
def is_spring_2022(text):
    for pat in spring_patterns:
        if re.search(pat, text, re.IGNORECASE):
            return True
    return False

# Build a dictionary of project info to avoid duplicates
# Key: Project Name, Value: Funding Amount
project_map = {p['Project_Name']: int(p['Amount']) for p in funding}
found_projects = set()

# Iterate through docs
for doc in civic_docs:
    text = doc['text']
    # Split text into lines to process
    # But finding the project block is better with finding the name index
    
    for proj_name in project_map.keys():
        if proj_name in found_projects:
            continue
            
        # Find project name in text
        # We need to be careful about substrings. Use explicit search.
        # But project names are long and specific.
        if proj_name in text:
            # Find the start index
            idx = text.find(proj_name)
            # Take a chunk of text after the name (e.g., 2000 chars)
            chunk = text[idx:idx+2000]
            
            # Look for "Begin Construction" or "Start"
            # Regex for "Begin Construction: <Date>"
            # The text has lines like "(cid:131) Begin Construction: Fall 2023"
            # We'll look for "Begin Construction[:\s]+(.*?)\n"
            
            # Note: the cid chars might be annoying. Just look for "Begin Construction"
            match = re.search(r"Begin Construction[:\s]+([^\n]+)", chunk, re.IGNORECASE)
            if match:
                date_str = match.group(1).strip()
                if is_spring_2022(date_str):
                    found_projects.add(proj_name)
                    continue # Next project

            # Also check "Start Date" just in case
            match_start = re.search(r"Start Date[:\s]+([^\n]+)", chunk, re.IGNORECASE)
            if match_start:
                date_str = match_start.group(1).strip()
                if is_spring_2022(date_str):
                    found_projects.add(proj_name)
                    continue

            # Also check "Advertise" if that is considered start? 
            # The prompt says "started". Usually construction.
            # Let's stick to Begin Construction first.

# Calculate total
count = len(found_projects)
total_funding = sum(project_map[p] for p in found_projects)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-14343582955729451491': 'file_storage/function-call-14343582955729451491.json', 'var_function-call-8006204082577017619': 'file_storage/function-call-8006204082577017619.json', 'var_function-call-13241760497320549299': 'file_storage/function-call-13241760497320549299.json', 'var_function-call-857092213890831436': 5}

exec(code, env_args)
