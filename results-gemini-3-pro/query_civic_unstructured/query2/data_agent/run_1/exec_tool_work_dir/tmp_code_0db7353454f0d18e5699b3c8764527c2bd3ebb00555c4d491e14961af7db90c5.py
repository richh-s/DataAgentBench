code = """import json
import re

# Load data
with open(locals()['var_function-call-11007729145767623025'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2656858989978563996'], 'r') as f:
    civic_docs_data = json.load(f)

# 1. Process Funding
# Create a map of Project_Name -> Total Amount (sum duplicates if any)
project_funding = {}
for record in funding_data:
    p_name = record['Project_Name']
    amount = int(record['Amount'])
    if p_name in project_funding:
        project_funding[p_name] += amount
    else:
        project_funding[p_name] = amount

project_names = list(project_funding.keys())

# 2. Process Docs
# Combine all texts? Or process per doc.
# Since a project might be in multiple docs, if *any* doc confirms "completed in 2022", we count it.
# We need to extract the text segment for each project.
completed_2022_projects = set()

# Helper to find project segments
# We'll valid project names in text
def find_projects_in_text(text, p_names):
    # Find all occurrences
    occurrences = []
    for p_name in p_names:
        # Simple string search, assuming project names are distinctive enough
        # Using re.escape to handle parens etc.
        # We look for the project name as a header (maybe followed by newline or updates)
        # But simple find is easier.
        for match in re.finditer(re.escape(p_name), text):
            occurrences.append((match.start(), p_name))
    
    occurrences.sort()
    
    segments = []
    for i in range(len(occurrences)):
        start, name = occurrences[i]
        # End is the start of the next project or end of text
        end = occurrences[i+1][0] if i+1 < len(occurrences) else len(text)
        # Limit segment length to avoid huge blocks if sparse? 
        # But documents seem to be lists of projects. 
        # Let's take the whole chunk until next project.
        segment = text[start:end]
        segments.append((name, segment))
    return segments

total_text = "\n".join([doc['text'] for doc in civic_docs_data])

# Extract segments
segments = find_projects_in_text(total_text, project_names)

# Analyze segments
debug_matches = []
for p_name, segment in segments:
    # Check if park related
    # "Park" in name?
    is_park = "park" in p_name.lower()
    
    if is_park:
        # Check if completed in 2022
        # Pattern: completed ... 2022
        # Look for "completed" within reasonable distance to "2022"
        # and ensure "2022" is part of the completion date.
        # Regex: completed.{0,30}2022
        if re.search(r"completed.{0,40}2022", segment, re.IGNORECASE):
             completed_2022_projects.add(p_name)
             debug_matches.append((p_name, "MATCHED"))
        else:
             # Check for "Status: Completed" ... "End Date: ... 2022"?
             # Text format: (cid:190) Updates: Construction was completed November 2022
             pass

# Calculate Total
total_funding = 0
found_projects = []
for p in completed_2022_projects:
    total_funding += project_funding[p]
    found_projects.append({"name": p, "amount": project_funding[p]})

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": found_projects, "debug": debug_matches}))"""

env_args = {'var_function-call-4881455227376236038': ['civic_docs'], 'var_function-call-4881455227376238215': ['Funding'], 'var_function-call-11007729145767623596': 'file_storage/function-call-11007729145767623596.json', 'var_function-call-11007729145767623025': 'file_storage/function-call-11007729145767623025.json', 'var_function-call-12661878134790433858': 'file_storage/function-call-12661878134790433858.json', 'var_function-call-2656858989978563996': 'file_storage/function-call-2656858989978563996.json'}

exec(code, env_args)
