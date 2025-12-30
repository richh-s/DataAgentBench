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

# Helper to normalize strings for comparison
def normalize(text):
    return text.strip().lower()

# Regex for Spring 2022
# Matches: Spring 2022, Spring, 2022, March 2022, April 2022, May 2022, 03/2022, etc.
date_pattern = re.compile(r'(Spring|March|April|May),?\s*2022', re.IGNORECASE)

started_projects = set()

# Iterate over docs
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if line is a project name
        # We check if the line *is* a project name, or contains it?
        # Based on preview, the project name is on its own line.
        # But OCR/Text extraction might be messy.
        # Let's check if the line exactly matches a known project name (case-insensitive)
        # or if a known project name is contained in the line (if the line is short).
        
        found_project = None
        for name in project_names:
            if normalize(line) == normalize(name):
                found_project = name
                break
            # Handle potential noise or minor diffs
            if len(line) < len(name) + 10 and normalize(name) in normalize(line):
                found_project = name
                break
        
        if found_project:
            current_project = found_project
            # Look ahead for start date in the next, say, 20 lines
            # Limit scope to until next project or end of section
            # But simpler to just look ahead a fixed amount or until next empty line sequence?
            # The structure has "Project Schedule:" section.
            continue
            
        if current_project:
            # Look for keywords indicating start
            # "Begin Construction", "Start", "Estimated Schedule", "Project Schedule"
            # And then values.
            
            # Check for patterns like "Begin Construction: Spring 2022"
            # or "Start Date: March 2022"
            
            # We look for the date pattern in the line
            match = date_pattern.search(line)
            if match:
                # Check if this line is about starting
                # Keywords: "Begin", "Start", "Construction", "Advertise"? 
                # "Advertise" usually is before construction. 
                # If "Begin Construction" is Spring 2022, then it started then.
                # If "Advertise" is Spring 2022, construction starts later.
                # The query asks "started", usually meaning the project execution starts.
                # Or just the project "Start".
                # Let's look at the context in the line.
                
                lower_line = line.lower()
                if 'begin construction' in lower_line or 'start' in lower_line or 'construction' in lower_line:
                     # Exclude "Complete Construction"
                    if 'complete' not in lower_line and 'completion' not in lower_line and 'finish' not in lower_line:
                        started_projects.add(current_project)
                    elif 'start' in lower_line: # If it says "Construction Start" or "Start"
                        started_projects.add(current_project)

# Calculate total funding
total_funding = 0
found_projects_list = []
for p in started_projects:
    amount = int(funding_projects[p]['Amount'])
    total_funding += amount
    found_projects_list.append({"Project": p, "Amount": amount})

print("__RESULT__:")
print(json.dumps({"count": len(started_projects), "total_funding": total_funding, "projects": found_projects_list}))"""

env_args = {'var_function-call-1003584179187242714': 'file_storage/function-call-1003584179187242714.json', 'var_function-call-1003584179187241629': 'file_storage/function-call-1003584179187241629.json'}

exec(code, env_args)
