code = """import json
import pandas as pd

# Load funding data
with open(locals()['var_function-call-7295023987179093116'], 'r') as f:
    funding_data = json.load(f)

# Load civic docs
with open(locals()['var_function-call-10283202643711845823'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_section = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Identify sections
        if "Capital Improvement Projects (Design)" in line:
            current_section = "CAP_DESIGN"
            i += 1
            continue
        elif "Capital Improvement Projects" in line and "(Construction)" in line:
            current_section = "OTHER"
            i += 1
            continue
        elif "Capital Improvement Projects" in line and "(Not Started)" in line:
            current_section = "OTHER"
            i += 1
            continue
        elif "Disaster Recovery Projects" in line:
            current_section = "OTHER"
            i += 1
            continue
            
        if current_section == "CAP_DESIGN":
            # Potential project name
            if not line:
                i += 1
                continue
            
            # Skip page headers/footers
            if "Page" in line and "Agenda Item" in line:
                i += 1
                continue
            if line.startswith("Page ") or line.startswith("Agenda Item"):
                i += 1
                continue
                
            # Check for the update marker in subsequent lines to confirm this is a header
            # Markers from preview: (cid:190) which often decodes to a bullet. 
            # In the raw text provided in preview, it shows as "(cid:190)".
            
            is_project = False
            # check next few lines
            for j in range(i+1, min(i+5, len(lines))):
                nxt = lines[j].strip()
                if not nxt:
                    continue
                if "(cid:190)" in nxt or "Updates:" in nxt or "Project Description:" in nxt:
                    is_project = True
                    break
                else:
                    # If the next non-empty line is not a marker, then this line is probably not a project header
                    # OR the marker is further down.
                    # But usually the structure is Header -> Updates.
                    break
            
            if is_project:
                projects.append(line)
        
        i += 1

extracted_df = pd.DataFrame(projects, columns=['Project_Name'])
# Remove duplicates if any (same project mentioned in multiple docs or multiple times?)
# Assuming one doc is the "Status Report", we might process just one. 
# But let's keep all and distinct later.

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
funding_target = funding_df[funding_df['Amount'] > 50000]

# Merge
# Normalize names: strip, maybe lower case for matching?
# The prompt implies names match exactly or close.
merged = pd.merge(extracted_df, funding_target, on='Project_Name', how='inner')

# Get unique matched projects
unique_matches = merged['Project_Name'].unique()

print("__RESULT__:")
print(json.dumps(list(unique_matches)))"""

env_args = {'var_function-call-7295023987179093116': 'file_storage/function-call-7295023987179093116.json', 'var_function-call-10283202643711845823': 'file_storage/function-call-10283202643711845823.json'}

exec(code, env_args)
