code = """import json
import pandas as pd
import re

# Load data
# Using the keys from previous outputs
file_civic = locals()['var_function-call-2910026112661516748']
file_funding = locals()['var_function-call-10585127880706054254']

with open(file_civic, 'r') as f:
    civic_docs = json.load(f)

with open(file_funding, 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n')]
    
    # Map lines with types
    line_map = []
    for idx, line in enumerate(lines):
        if not line:
            continue
            
        ltype = "text"
        if "Capital Improvement Projects (Design)" in line:
            ltype = "header_design"
        elif "Capital Improvement Projects (Construction)" in line:
            ltype = "header_construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            ltype = "header_not_started"
        elif "Disaster Recovery Projects" in line:
            # Check if followed by status?
            # For now treat as header but status might persist from previous or be distinct
            # Let's see if we can infer status from context or if it's a main header
            # Often it's "Capital Improvement Projects and Disaster Recovery Projects Status Report"
            # which is a title, not a section header.
            # But inside the list, if there is "Disaster Recovery Projects (Design)", we catch it.
            if "(Design)" in line: ltype = "header_design"
            elif "(Construction)" in line: ltype = "header_construction"
            elif "(Not Started)" in line: ltype = "header_not_started"
            else: ltype = "header_general" # Might not change status if it's just a title
        elif "(cid:190)" in line:
            ltype = "bullet"
        
        line_map.append({"idx": idx, "text": line, "type": ltype})
        
    current_status = "unknown"
    i = 0
    while i < len(line_map):
        item = line_map[i]
        
        # Handle Headers
        if "header_" in item['type']:
            if item['type'] == "header_design":
                current_status = "design"
            elif item['type'] == "header_construction":
                current_status = "construction"
            elif item['type'] == "header_not_started":
                current_status = "not started"
            # if header_general, keep previous status or reset? Let's keep previous.
            i += 1
            continue
            
        # Handle Potential Project
        # Pattern: Text Line -> Bullet Line
        if item['type'] == 'text':
            if i + 1 < len(line_map) and line_map[i+1]['type'] == 'bullet':
                p_name = item['text']
                
                # Collect content
                content_parts = [p_name]
                j = i + 1
                while j < len(line_map):
                    next_item = line_map[j]
                    if "header_" in next_item['type']:
                        break
                    if next_item['type'] == 'text' and j + 1 < len(line_map) and line_map[j+1]['type'] == 'bullet':
                        break
                    content_parts.append(next_item['text'])
                    j += 1
                
                full_text = " ".join(content_parts)
                
                # Determine Status
                status = current_status
                if status == "construction":
                    if "completed" in full_text.lower():
                        status = "completed"
                    # Else check if explicitly "design" mentioned? Unlikely in Construction section.
                    # If strictly construction, keep as construction?
                    # Or map to 'design' if the user strictly wants 3 statuses.
                    # The prompt says: "Projects have three statuses: 'design', 'completed', 'not started'."
                    # I will map 'construction' to 'design' (as it's active) UNLESS it's completed.
                    # Wait, 'construction' is definitely not 'design' phase. It's execution.
                    # But if I have to choose from the 3, maybe 'design' is the closest 'active' status?
                    # Or maybe the prompt implies I should find the status in the text?
                    # Let's return the status I found ('construction' or 'completed'). The user can interpret.
                    # But "completed" is one of the 3.
                    pass

                extracted_projects.append({
                    "Project_Name": p_name,
                    "Status": status,
                    "Full_Text": full_text
                })
                
                i = j
                continue
        
        i += 1

# Filter
relevant = []
keywords = ['emergency', 'fema']
for p in extracted_projects:
    txt = p['Full_Text'].lower()
    if any(kw in txt for kw in keywords):
        relevant.append(p)

df_extracted = pd.DataFrame(relevant)

# Join
if not df_extracted.empty and not df_funding.empty:
    merged = pd.merge(df_funding, df_extracted, on='Project_Name', how='inner')
    result = merged[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9102831309616723132': ['civic_docs'], 'var_function-call-9102831309616723245': ['Funding'], 'var_function-call-12492854141756139028': 'file_storage/function-call-12492854141756139028.json', 'var_function-call-7907601960746092281': 'file_storage/function-call-7907601960746092281.json', 'var_function-call-10585127880706054254': 'file_storage/function-call-10585127880706054254.json', 'var_function-call-2910026112661516748': 'file_storage/function-call-2910026112661516748.json'}

exec(code, env_args)
