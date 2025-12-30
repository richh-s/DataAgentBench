code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-10835669272488718990'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10835669272488721645'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Extraction logic
projects = []

for doc in civic_docs:
    text = doc['text']
    # Normalize text to handle bullet points if they vary
    text = text.replace('(cid:190)', 'BULLET_SECTION').replace('(cid:131)', 'BULLET_ITEM')
    
    # Split text by "BULLET_SECTION Updates:" to find potential project starts
    # The project name should be in the lines preceding "BULLET_SECTION Updates:"
    
    parts = text.split('BULLET_SECTION Updates:')
    
    # The first part is header/intro, skip or check for the first project if it starts immediately?
    # Usually the first part ends with the first project's name.
    
    # Actually, the split removes the separator. 
    # part[0] ends with Project Name 1
    # part[1] starts with body of Project 1, then some text, then Project Name 2 (at the end)
    
    for i in range(1, len(parts)):
        # The project name is at the end of parts[i-1]
        preceding_text = parts[i-1].strip()
        lines = preceding_text.split('\n')
        # Filter out empty lines
        lines = [l.strip() for l in lines if l.strip()]
        
        if not lines:
            continue
            
        # Assume the project name is the last non-empty line (or last few lines if wrapped)
        # Looking at preview: "Westward Beach Road Repair Project\n\n(cid:190) Updates:"
        project_name = lines[-1]
        
        # Sometimes names are on multiple lines or there are headers like "Capital Improvement Projects (Design)"
        # If the line is a known header, go back one more line?
        known_headers = ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]
        if project_name in known_headers:
            if len(lines) > 1:
                project_name = lines[-2]
            else:
                project_name = "UNKNOWN"

        # The body of the project is in parts[i] (up to the next project name)
        # But parts[i] also contains the Name of the NEXT project at the end.
        # So the body is everything except the last few lines of parts[i].
        # However, for the last part, it's all body.
        
        # Wait, if I split by "BULLET_SECTION Updates:", the current part `parts[i]` STARTS with the updates for `project_name`.
        # It goes on until the next "BULLET_SECTION Updates:".
        # So the text for this project is `parts[i]`.
        # But `parts[i]` ends with the name of the next project.
        # I need to separate the current project's body from the next project's name.
        # The next project's name appears before the NEXT "BULLET_SECTION Updates:".
        # So I can process `parts[i]` to extract info, ignoring the trailing name.
        
        body = parts[i]
        
        # Extract Start Date
        # Look for "Begin Construction:" or "Start Date:"
        st = None
        st_match = re.search(r'Begin Construction:\s*(.*)', body, re.IGNORECASE)
        if st_match:
            st = st_match.group(1).strip()
        
        # Extract Topic keywords from body
        # Common topics: "park", "road", "FEMA", "fire", "emergency", "drainage", etc.
        # Also check for "Disaster" in project name or body to determine type
        is_disaster = False
        
        body_lower = body.lower()
        name_lower = project_name.lower()
        
        # Check type
        if "disaster" in name_lower or "fema" in name_lower or "caloes" in name_lower:
            is_disaster = True
        elif "disaster" in body_lower or "fema" in body_lower or "recovery" in body_lower or "woolsey" in body_lower:
            is_disaster = True
            
        # Extract Topic just in case
        # ...
        
        projects.append({
            "extracted_name": project_name,
            "st": st,
            "is_disaster": is_disaster,
            "full_text_segment": body[:200] # preview
        })

# Now filter and match with funding
# Normalize names for matching? The hint says "matches the project names".
# I'll try exact match first, then fuzzy or stripped.

results = []
for p in projects:
    if p['st'] and '2022' in p['st'] and p['is_disaster']:
        results.append(p)

# Print intermediate to check
print("__RESULT__:")
print(json.dumps(results, indent=2))
print("DEBUG_PROJECT_NAMES:", json.dumps([p['extracted_name'] for p in projects[:10]], indent=2))"""

env_args = {'var_function-call-10835669272488718990': 'file_storage/function-call-10835669272488718990.json', 'var_function-call-10835669272488721645': 'file_storage/function-call-10835669272488721645.json'}

exec(code, env_args)
