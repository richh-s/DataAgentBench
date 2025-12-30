code = """import json
import sqlite3
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-5188433826363097598']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
docs_path = locals()['var_function-call-7088797317398377498']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

projects = []

def parse_date(line):
    # Extract date from lines like "(cid:131) Complete Design: Summer 2023"
    if ":" in line:
        return line.split(":", 1)[1].strip()
    return None

for doc in docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_project = None
    project_buffer = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect Section Headers
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "construction" # Will refine later
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not started"
            continue
        elif "Disaster Recovery Projects" in line:
            # Could be a header, but let's see. The text had "Capital Improvement Projects and Disaster Recovery Projects Status Report"
            pass
            
        # Heuristic for project name:
        # It is not a bullet point (starts with (cid:...) or (cid:190))
        # It is not a common keyword like "Updates:", "Project Schedule:"
        # It is followed by a line that starts with (cid:190) or "Updates:"
        # And we are in a valid section
        
        is_bullet = line.startswith("(cid:") or line.startswith("\u2013") or line.startswith("-")
        is_keyword = line.startswith("Updates:") or line.startswith("Project Schedule:") or line.startswith("Estimated Schedule:")
        
        # Look ahead for next non-empty line
        next_line = None
        for j in range(i + 1, len(lines)):
            if lines[j].strip():
                next_line = lines[j].strip()
                break
        
        is_project_start = False
        if current_status and not is_bullet and not is_keyword:
            if next_line and (next_line.startswith("(cid:190)") or next_line.startswith("Updates:") or next_line.startswith("Project Description:")):
                is_project_start = True
                # Special case: "Page X of Y" or "Agenda Item" headers
                if "Page" in line and "of" in line: is_project_start = False
                if "Agenda Item" in line: is_project_start = False
                
        if is_project_start:
            # Save previous project
            if current_project:
                projects.append(current_project)
            
            current_project = {
                "Project_Name": line,
                "status": current_status,
                "text_lines": [],
                "st": None,
                "et": None
            }
        elif current_project:
            current_project["text_lines"].append(line)

    # Append last project
    if current_project:
        projects.append(current_project)

# Process extracted projects to find details
final_projects = []
for p in projects:
    full_text = " ".join(p['text_lines'])
    
    # Refine status
    status = p['status']
    if "Construction was completed" in full_text:
        status = "completed"
    
    # Extract dates
    st = None
    et = None
    
    for line in p['text_lines']:
        if "Begin Construction:" in line or "Begin construction:" in line:
            st = line.split(":", 1)[1].strip()
        if "Complete Construction:" in line or "Complete construction:" in line:
            et = line.split(":", 1)[1].strip()
        # Fallback if no construction dates? 
        # The prompt says "st: Start time/date, et: End time/date".
        # Maybe "Advertise" is start? I'll stick to Construction if avail.
        
    p['st'] = st
    p['et'] = et
    p['status'] = status
    p['full_text'] = full_text
    
    # Check for keywords
    # "related to 'emergency' or 'FEMA'"
    # Check Project_Name and full_text
    is_related = False
    name_upper = p['Project_Name'].upper()
    text_upper = full_text.upper()
    
    if "EMERGENCY" in name_upper or "FEMA" in name_upper:
        is_related = True
    elif "EMERGENCY" in text_upper or "FEMA" in text_upper:
        is_related = True
        
    if is_related:
        final_projects.append(p)

# Create DataFrame for extracted projects
extracted_df = pd.DataFrame(final_projects)

# Merge with Funding
# Try exact match on Project_Name
# Note: Funding table names might have suffixes like "(FEMA Project)" which extracted names might not have
# Or extracted names might be clean.
# Let's inspect a few extracted names vs funding names
# extracted: "Latigo Canyon Road Retaining Wall Repair Project"
# funding: "Latigo Canyon Road Retaining Wall Repair Project" -> Match
# funding: "Latigo Canyon Road Culvert Repairs (FEMA Project)" -> Might be different project
# Let's clean names for merging if needed.
# For now, merge on Project_Name

if not extracted_df.empty:
    merged = pd.merge(extracted_df, funding_df, on="Project_Name", how="inner")
    
    # Select columns
    result_df = merged[["Project_Name", "Funding_Source", "Amount", "status", "st", "et"]]
    result = result_df.to_dict(orient="records")
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1936795018027182717': ['Funding'], 'var_function-call-1936795018027181912': 'file_storage/function-call-1936795018027181912.json', 'var_function-call-5188433826363097598': 'file_storage/function-call-5188433826363097598.json', 'var_function-call-7088797317398377498': 'file_storage/function-call-7088797317398377498.json'}

exec(code, env_args)
