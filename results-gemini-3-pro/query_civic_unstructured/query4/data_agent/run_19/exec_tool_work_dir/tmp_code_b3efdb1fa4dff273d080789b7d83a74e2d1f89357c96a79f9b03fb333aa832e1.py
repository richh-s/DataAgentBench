code = """import json
import re

# Load data
with open(locals()['var_function-call-6833374196738575429'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-2571732605933953840'], 'r') as f:
    civic_docs = json.load(f)

projects_started_spring_2022 = set()

# Helper to check if date is Spring 2022
def is_spring_2022(date_str):
    if not date_str:
        return False
    ds = date_str.lower()
    if 'spring 2022' in ds or 'spring, 2022' in ds:
        return True
    # Check months
    if '2022' in ds:
        if 'march' in ds or 'april' in ds or 'may' in ds:
            return True
    return False

# Parse documents
for doc in civic_docs:
    text = doc['text']
    # Split by lines
    lines = text.split('\n')
    
    current_project = None
    project_buffer = []
    
    # We'll try to identify project blocks. 
    # Structure often: Project Name \n ... \n (cid:190) ...
    # We can use regex to find project starts.
    # Or simple line iteration looking for the markers.
    
    # Let's try a regex approach on the whole text to find blocks
    # Looking for a line that is not empty, followed eventually by (cid:190)
    # This might be tricky. Let's iterate.
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Check if this line is a project name
        # Heuristic: The next non-empty line starts with (cid:190) or is "Updates:"
        # Or checking if line is in our known funding project names? 
        # But we need to extract from text first to be safe.
        
        # Let's look ahead
        is_project_header = False
        for j in range(i+1, min(i+5, len(lines))):
            next_l = lines[j].strip()
            if not next_l:
                continue
            if next_l.startswith('(cid:190)') or next_l.startswith('Updates:') or 'Project Description:' in next_l:
                is_project_header = True
            break
        
        if is_project_header:
            if current_project:
                # Process previous project
                full_block = "\n".join(project_buffer)
                # Extract start date
                # Look for Begin Construction
                start_match = re.search(r'Begin [Cc]onstruction:?\s*(.*)', full_block, re.IGNORECASE)
                if start_match:
                    date_val = start_match.group(1).strip()
                    if is_spring_2022(date_val):
                        projects_started_spring_2022.add(current_project)
                else:
                    # Maybe "Advertise" if construction info is missing? No, query says "started".
                    # Check for "Start Date:" or "Schedule:" lines?
                    # The sample had: "(cid:131) Begin Construction: Fall 2023"
                    pass

            current_project = line
            project_buffer = []
        else:
            if current_project:
                project_buffer.append(line)
    
    # Process last project
    if current_project:
        full_block = "\n".join(project_buffer)
        start_match = re.search(r'Begin [Cc]onstruction:?\s*(.*)', full_block, re.IGNORECASE)
        if start_match:
            date_val = start_match.group(1).strip()
            if is_spring_2022(date_val):
                projects_started_spring_2022.add(current_project)

# Now calculate funding
total_funding = 0
funded_projects = []

# Normalize project names for matching
# Remove special chars, lower case?
# Funding table names seem clean. Doc names might have extra spaces.
def clean_name(n):
    return re.sub(r'\s+', ' ', n).strip().lower()

funding_map = {clean_name(r['Project_Name']): int(r['Amount']) for r in funding_data}

matched_count = 0
for p_name in projects_started_spring_2022:
    cn = clean_name(p_name)
    # Try exact match
    if cn in funding_map:
        total_funding += funding_map[cn]
        funded_projects.append(p_name)
        matched_count += 1
    else:
        # Try finding as substring or fuzzy?
        # Hint says names "match".
        # Let's print unmatched to debug if needed.
        pass

result = {
    "count": len(funded_projects),
    "total_funding": total_funding,
    "projects": funded_projects,
    "debug_all_found_projects": list(projects_started_spring_2022)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3413924578737441379': ['civic_docs'], 'var_function-call-3413924578737439684': ['Funding'], 'var_function-call-6833374196738575429': 'file_storage/function-call-6833374196738575429.json', 'var_function-call-6833374196738572946': 'file_storage/function-call-6833374196738572946.json', 'var_function-call-2571732605933953840': 'file_storage/function-call-2571732605933953840.json'}

exec(code, env_args)
