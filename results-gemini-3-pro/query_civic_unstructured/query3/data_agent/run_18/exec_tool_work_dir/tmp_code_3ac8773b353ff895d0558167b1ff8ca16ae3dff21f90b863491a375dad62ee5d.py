code = """import json
import sqlite3
import pandas as pd
import re

# Load funding data
funding_path = locals()['var_function-call-400742028544773800']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

# Load civic docs
docs_path = locals()['var_function-call-400742028544771257']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Helper to normalize strings for matching
def normalize(s):
    return s.strip()

# Store extracted projects: {name: {status, text}}
extracted_projects = {}

# Parse documents
# Assuming structure based on preview:
# Sections start with "Capital Improvement Projects" or similar?
# Project names are lines followed by "(cid:190)" or bullets?

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_project = None
    project_buffer = []
    
    # Iterate lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check for section headers
        if "Capital Improvement Projects" in line or "Disaster Recovery Projects" in line:
            # Determine status from header
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction_section" # To be refined
            elif "(Not Started)" in line:
                current_status = "not started"
            else:
                # Fallback or maybe the status is on next line?
                pass
            i += 1
            continue
            
        # Check for potential project name
        # Heuristic: Non-empty, doesn't start with bullets, next non-empty line starts with (cid:190) or similar
        # Also ignore page numbers or known headers
        if line and current_status:
            # Look ahead for project start indicator
            is_project = False
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            if j < len(lines):
                next_line = lines[j].strip()
                # Check for bullet points often used in this text
                if next_line.startswith("(cid:190)") or next_line.startswith("Updates:"):
                    is_project = True
            
            # Additional check: Line shouldn't be a page number or header repetition
            if "Agenda Item" in line or "Page" in line and "of" in line:
                is_project = False
            
            if is_project:
                # Save previous project if exists
                if current_project:
                    extracted_projects[current_project['name']] = current_project
                
                # Start new project
                current_project = {
                    'name': line,
                    'status': current_status,
                    'text': ''
                }
                project_buffer = []
                i += 1
                continue

        # Accumulate text for current project
        if current_project:
            current_project['text'] += line + "\n"
        
        i += 1
    
    # Add last project
    if current_project:
        extracted_projects[current_project['name']] = current_project

# Refine statuses in "construction_section"
for name, data in extracted_projects.items():
    if data['status'] == 'construction_section':
        if "completed" in data['text'].lower() and "construction" in data['text'].lower():
             data['status'] = "completed"
        elif "notice of completion" in data['text'].lower():
             data['status'] = "completed"
        else:
             # Assume under construction if not completed?
             # Or maybe map to 'design' as in 'active'? 
             # Let's keep it as 'under construction' or 'design'? 
             # The hint says statuses are 'design', 'completed', 'not started'.
             # If it's not completed, it's strictly not 'completed' or 'not started'.
             # Maybe 'design' covers all active phases? Or I'll just say "under construction".
             data['status'] = "under construction"

# Function to check if project is related to emergency or FEMA
def is_related(project_name, topic_text):
    keywords = ['emergency', 'fema']
    text_lower = (project_name + " " + topic_text).lower()
    for k in keywords:
        if k in text_lower:
            return True
    return False

# Join with Funding
results = []
# We iterate extracted projects to find matches in funding, 
# AND iterate funding to find matches in extracted (because of suffixes)

# Create a map of normalized extracted names
extracted_map = {name.lower(): data for name, data in extracted_projects.items()}

for index, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_amount = row['Amount']
    f_source = row['Funding_Source']
    
    # Try exact match
    match = extracted_map.get(f_name.lower())
    
    # Try suffix removal
    if not match:
        # Suffixes to remove
        suffixes = ["(FEMA Project)", "(CalOES Project)", "(FEMA/CalOES Project)", "(FEMA)", "(CalJPIA Project)"]
        base_name = f_name
        for s in suffixes:
            if base_name.endswith(s):
                base_name = base_name.replace(s, "").strip()
        match = extracted_map.get(base_name.lower())
    
    if match:
        status = match['status']
        text = match['text']
        
        # Check relevance
        if is_related(f_name, text):
            results.append({
                "Project_Name": f_name,
                "Funding_Source": f_source,
                "Amount": f_amount,
                "Status": status
            })
    else:
        # If no match in docs, we can't determine status from docs. 
        # But if the project name itself contains FEMA/Emergency, maybe we should include it with "Unknown" status?
        # The prompt asks for "statuses". If status is unknown, maybe exclude? 
        # Or extracted from documents *is* the way to get status.
        # Check if project name implies relevance
        if "fema" in f_name.lower() or "emergency" in f_name.lower():
             results.append({
                "Project_Name": f_name,
                "Funding_Source": f_source,
                "Amount": f_amount,
                "Status": "Unknown" # Or "not started" default? Safer to say Unknown or try to infer.
            })

# Print result
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11967641288845648595': ['Funding'], 'var_function-call-11967641288845651132': ['civic_docs'], 'var_function-call-400742028544773800': 'file_storage/function-call-400742028544773800.json', 'var_function-call-400742028544771257': 'file_storage/function-call-400742028544771257.json'}

exec(code, env_args)
