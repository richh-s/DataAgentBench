code = """import json
import pandas as pd
import re

# Load Funding Data
funding_path = locals()['var_function-call-9960923256029121607']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load Civic Docs
docs_path = locals()['var_function-call-9960923256029120432']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    # Possible statuses from hint: design, completed, not started
    # Headers in text: "Capital Improvement Projects (Design)", "(Construction)", "(Not Started)"
    
    # We need to iterate and identify sections and projects
    # Heuristic:
    # 1. Identify Section Header
    # 2. Identify Project Name (Line before "(cid:190) Updates:" or similar)
    # 3. Collect text until next project or section
    
    # Let's verify the marker for Updates. In the preview it was "(cid:190) Updates:"
    # This might differ in other files or be decoded differently.
    # We will look for a line containing "Updates:" and a preceding line.
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check Section
        if "Capital Improvement Projects" in line:
            if "(Design)" in line:
                current_status = "design"
            elif "(Construction)" in line:
                current_status = "construction_section" # To be refined
            elif "(Not Started)" in line:
                current_status = "not started"
            i += 1
            continue
            
        # Check Project Start
        # Look ahead for "Updates:"
        # The pattern seems to be:
        # Project Name
        # (cid:190) Updates:
        # OR
        # (cid:190) Project Description:
        
        if i + 1 < len(lines):
            next_line = lines[i+1].strip()
            # Check for markers
            marker_found = False
            if "Updates:" in next_line and ("(cid:190)" in next_line or len(next_line) < 20):
                marker_found = True
            elif "Project Description:" in next_line and ("(cid:190)" in next_line or len(next_line) < 30):
                marker_found = True
            
            if marker_found and line:
                # Found a project
                project_name = line
                
                # Extract full block
                block_lines = [line, next_line]
                j = i + 2
                while j < len(lines):
                    l = lines[j].strip()
                    # Stop if new section or new project
                    # New section
                    if "Capital Improvement Projects" in l:
                        break
                    # New project (look ahead again)
                    if j + 1 < len(lines):
                        nl = lines[j+1].strip()
                        if ("Updates:" in nl or "Project Description:" in nl) and ("(cid:190)" in nl or len(nl) < 30):
                             # Only if l is a potential project name (non-empty)
                             if l:
                                 break
                    block_lines.append(l)
                    j += 1
                
                full_text = "\n".join(block_lines)
                
                # Determine Status
                p_status = current_status
                if p_status == "construction_section":
                    # Check if completed
                    if "completed" in full_text.lower() and "construction was completed" in full_text.lower():
                        p_status = "completed"
                    elif "under construction" in full_text.lower():
                         p_status = "design" # Map to design as it's active? Or keep as construction?
                         # Hint says "Projects have three statuses: 'design', 'completed', 'not started'".
                         # If I report "construction", it might be wrong.
                         # "design" = in planning/design phase.
                         # Maybe "under construction" is separate. 
                         # However, usually Construction is the phase after Design.
                         # I will store "construction" for now and decide later or show it.
                         p_status = "construction"
                    else:
                        p_status = "construction" # Default for this section

                projects.append({
                    "Project_Name": project_name,
                    "text": full_text,
                    "status": p_status
                })
                
                i = j
                continue
        
        i += 1

# Filter Projects
related_projects = []
for p in projects:
    # Check for keywords
    keywords = ["emergency", "fema", "fire", "disaster"] # Added fire/disaster as per hint, but query said 'emergency' or 'FEMA'.
    # Query: "projects related to 'emergency' or 'FEMA'"
    # I should strictly follow query but hint says "Disaster project names often include..." and "Common topics include... FEMA, fire, emergency warning..."
    # I'll stick to 'emergency' or 'FEMA' as primary filter.
    text_lower = p['text'].lower()
    name_lower = p['Project_Name'].lower()
    
    if "emergency" in text_lower or "fema" in text_lower or \
       "emergency" in name_lower or "fema" in name_lower:
        related_projects.append(p)

# Create DataFrame
related_df = pd.DataFrame(related_projects)

# Join with Funding
# We need to match Project_Name.
# Let's clean up Project_Name (strip spaces, etc)
if not related_df.empty:
    related_df['Project_Name'] = related_df['Project_Name'].str.strip()
    
    # Merge
    merged_df = pd.merge(related_df, funding_df, on='Project_Name', how='left')
    
    # Filter columns
    result = merged_df[['Project_Name', 'Funding_Source', 'Amount', 'status']]
    
    print("__RESULT__:")
    print(result.to_json(orient='records'))
else:
    print("__RESULT__:")
    print("[]")"""

env_args = {'var_function-call-7478273444201397872': ['Funding'], 'var_function-call-7478273444201397573': ['civic_docs'], 'var_function-call-9960923256029121607': 'file_storage/function-call-9960923256029121607.json', 'var_function-call-9960923256029120432': 'file_storage/function-call-9960923256029120432.json'}

exec(code, env_args)
