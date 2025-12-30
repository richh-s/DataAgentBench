code = """import json
import re

# Load funding results
with open(locals()['var_function-call-9124692178282648902'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    name = record['Project_Name'].strip().lower()
    high_funding_projects.add(name)

# Load civic docs
with open(locals()['var_function-call-10183875392572160973'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

# Regex to find the section
section_start_regex = r"Capital Improvement Projects\s*\(Design\)"
section_end_regex = r"(?:Capital Improvement Projects|Disaster Recovery Projects|Agenda Item)"

for doc in civic_docs:
    text = doc['text']
    
    # Split text by the start header
    parts = re.split(section_start_regex, text, flags=re.IGNORECASE)
    
    # The first part is before the first header, skip it.
    for part in parts[1:]:
        # Find the end of the section
        end_match = re.search(section_end_regex, part, flags=re.IGNORECASE)
        if end_match:
            section_content = part[:end_match.start()]
        else:
            section_content = part
        
        # Now extract project names
        # Look for lines followed by (cid:190)
        lines = section_content.split('\n')
        for i in range(len(lines) - 1):
            line = lines[i].strip()
            next_line = lines[i+1].strip()
            
            if not line:
                continue
            
            # Check for bullet in next line
            # The preview showed "(cid:190)"
            if "(cid:190)" in next_line:
                # The project name is the current line
                found_projects.add(line.lower())

# Match
count = 0
matched_names = []
for p in found_projects:
    if p in high_funding_projects:
        count += 1
        matched_names.append(p)
    else:
        # Check for slight variations?
        # Maybe the project name in funding has suffix
        # e.g. "Project X (FEMA)" vs "Project X"
        # The prompt says names match, but one hint says disaster names include suffixes.
        # But we are looking for Capital Design projects.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matched_names, "extracted_example": list(found_projects)[:5], "funding_sample": list(high_funding_projects)[:5]}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json'}

exec(code, env_args)
