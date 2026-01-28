code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-7295023987179093116'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10283202643711845823'], 'r') as f:
    civic_docs = json.load(f)

# Extract projects from text
projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_type = None
    current_status = None
    
    # We iterate through lines
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect Section Headers
        if "Capital Improvement Projects (Design)" in line:
            current_type = "capital"
            current_status = "design"
            i += 1
            continue
        elif "Capital Improvement Projects" in line and "(Construction)" in line:
            current_type = "capital"
            current_status = "construction" # Not what we want, but good to track to stop 'design' capturing
            i += 1
            continue
        elif "Capital Improvement Projects" in line and "(Not Started)" in line:
            current_type = "capital"
            current_status = "not_started"
            i += 1
            continue
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster" # Stop capturing capital
            current_status = None
            i += 1
            continue
            
        # If we are in the target section
        if current_type == "capital" and current_status == "design":
            # Heuristic to find Project Name
            # Project names in the preview seem to be lines that are not empty, 
            # and are followed (eventually, skipping empty lines) by a line starting with "(cid:190)" or "Updates:"
            
            # Skip empty lines or page numbers
            if not line or line.startswith("Page ") or line.startswith("Agenda Item"):
                i += 1
                continue
            
            # Check if this line is a project name
            # Look ahead for confirmation
            is_project = False
            for j in range(i + 1, min(i + 10, len(lines))):
                next_line = lines[j].strip()
                if not next_line:
                    continue
                if "(cid:190)" in next_line or "Updates:" in next_line or "Project Description:" in next_line:
                    is_project = True
                    break
                # If we hit another likely project name or header, stop (this heuristic is tricky without the marker)
                # But based on preview, the marker (bullet) is consistent.
                break 
            
            if is_project:
                # Clean up the name
                p_name = line.strip()
                # Sometimes headers are split across lines? 
                # Preview: "2022 Morning View Resurfacing & Storm Drain Improvements" is one line.
                projects.append(p_name)
        
        i += 1

# Create DataFrame for extracted projects
extracted_projects_df = pd.DataFrame(projects, columns=['Project_Name'])
extracted_projects_df['extracted'] = True

# Funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = funding_df['Amount'].astype(float)
funding_filtered = funding_df[funding_df['Amount'] > 50000]

# Join
# We need to match Project_Name. 
# Let's check for exact matches first.
merged = pd.merge(extracted_projects_df, funding_filtered, on='Project_Name', how='inner')

# Result count
count = len(merged)
unique_projects = merged['Project_Name'].unique()

print("__RESULT__:")
print(json.dumps({
    "count": count, 
    "unique_projects_count": len(unique_projects),
    "unique_projects": list(unique_projects),
    "extracted_samples": projects[:5],
    "funding_samples": funding_filtered['Project_Name'].head().tolist()
}))"""

env_args = {'var_function-call-7295023987179093116': 'file_storage/function-call-7295023987179093116.json', 'var_function-call-10283202643711845823': 'file_storage/function-call-10283202643711845823.json'}

exec(code, env_args)
