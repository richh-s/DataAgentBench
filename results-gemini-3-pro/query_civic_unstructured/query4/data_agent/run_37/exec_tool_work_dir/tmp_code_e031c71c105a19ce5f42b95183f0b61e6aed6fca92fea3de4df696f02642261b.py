code = """import json
import re

# Load data
with open(locals()['var_function-call-7227617260641500172'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-7188498576282706077'], 'r') as f:
    civic_docs = json.load(f)

# Get list of project names
project_names = [item['Project_Name'] for item in funding_data]
# Sort by length descending to match longer names first
project_names.sort(key=len, reverse=True)

# Helper to normalize text for searching
def normalize(text):
    return text.lower().strip()

target_dates = ["spring 2022", "2022-spring", "march 2022", "april 2022", "may 2022"]
target_months = ["2022-03", "2022-04", "2022-05"]

found_projects = {}

for doc in civic_docs:
    text = doc['text']
    # Split text into lines
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue
            
        # Check if line is a project name
        # We look for exact match or close match
        is_project = False
        for pname in project_names:
            if pname in line_stripped: 
                # Be careful, "Project A" is in "Project A Phase 2". 
                # But we sorted by length, so "Project A Phase 2" should match first.
                # Also check if the line is predominantly the project name
                if len(line_stripped) < len(pname) + 10: # Allow some noise like punctuation
                    current_project = pname
                    is_project = True
                    break
        
        if is_project:
            continue
            
        if current_project:
            # Look for start date info in lines following project name
            # Looking for "Begin Construction", "Start", "Schedule"
            # And the target date
            lower_line = line_stripped.lower()
            
            # Check if line contains start indicators
            if "begin construction" in lower_line or "start" in lower_line:
                # Check for target dates
                for date in target_dates:
                    if date in lower_line:
                        found_projects[current_project] = line_stripped
                for date in target_months:
                    if date in lower_line:
                        found_projects[current_project] = line_stripped
            
            # Also check if just the date is there and it's a start context? 
            # The example shows: "(cid:131) Begin Construction: Fall 2023"
            # So searching for "Begin Construction" and the date on the same line is safe.

# Calculate totals
matched_projects = []
total_funding = 0

for pname in found_projects:
    matched_projects.append(pname)
    # Find amount
    for record in funding_data:
        if record['Project_Name'] == pname:
            total_funding += int(record['Amount'])
            break

result = {
    "count": len(matched_projects),
    "total_funding": total_funding,
    "projects": matched_projects,
    "details": found_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17279470663678048780': 'file_storage/function-call-17279470663678048780.json', 'var_function-call-7227617260641500172': 'file_storage/function-call-7227617260641500172.json', 'var_function-call-7188498576282706077': 'file_storage/function-call-7188498576282706077.json'}

exec(code, env_args)
