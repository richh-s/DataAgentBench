code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-2910026112661516748'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10585127880706054254'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Keywords
keywords = ['emergency', 'fema']

# Extracted projects
projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_status = None
    current_project_name = None
    current_project_text = []
    
    # Flags and buffers
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect Status Headers
        if "Capital Improvement Projects (Design)" in line:
            current_status = "design"
            i += 1
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_status = "construction" # Will refine later
            i += 1
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_status = "not started"
            i += 1
            continue
        elif "Disaster Recovery Projects" in line:
            # Check if it has status in parens?
            # In the snippet: "Capital Improvement Projects and Disaster Recovery Projects Status Report"
            # It seems they might be mixed or have their own headers. 
            # Let's assume the status headers apply to following projects until a new header.
            pass

        # Identify Project Start
        # Projects seem to be followed by "(cid:190) Updates:" or "(cid:190) Project Description:" or "(cid:190) Project Schedule:"
        # The line before is the project name.
        
        # Look ahead for (cid:190)
        # Note: (cid:190) might be encoded differently or just text.
        # In the preview it was "(cid:190)".
        
        is_project_start = False
        # Check next few lines for start markers
        j = i + 1
        while j < len(lines) and j < i + 5:
            if "(cid:190)" in lines[j] or "Updates:" in lines[j] or "Project Description:" in lines[j] or "Project Schedule:" in lines[j]:
                # Found a marker.
                # The project name should be at line i (or i combined with previous if wrapped)
                # But let's assume one line for now.
                if "(cid:190)" in lines[j]:
                     is_project_start = True
                break
            j += 1
        
        # However, checking every line is inefficient/tricky.
        # Better approach: Iterate and buffer.
        
        # Alternative:
        # Split by `(cid:190)`? No, that's inside the block.
        
        # Let's use the marker `(cid:190)` to identify that the *previous* non-empty line was the title.
        if "(cid:190)" in line:
            # The previous non-empty line stored in `last_line` was the title.
            # But we need to have processed it.
            # Let's restart logic: iterate lines, keep track of last non-empty line.
            # When we hit `(cid:190)`, the `last_non_empty_line` is the project name.
            # The text following `(cid:190)` until the next project name is the description.
            pass
        
        i+=1

# Refined Parsing Logic
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    # Normalize line endings
    lines = [l.strip() for l in text.split('\n')]
    
    current_status = "unknown"
    buffer_text = []
    potential_name = ""
    
    # We need to capture the name and the full block of text associated with it to check keywords.
    # We also need to capture the status section.
    
    # Let's iterate.
    # We will accumulate text for a project until we find a new project or section header.
    
    # Regex for headers
    # "Capital Improvement Projects (Design)"
    # "Capital Improvement Projects (Construction)"
    # "Capital Improvement Projects (Not Started)"
    
    # We can identify project boundaries by the project name line.
    # But project name lines don't have a distinct marker *except* being followed by `(cid:190)`.
    
    # So:
    # 1. Identify indices of lines starting with `(cid:190)`.
    # 2. The line before (ignoring empty lines) is the Project Name.
    # 3. Everything between Project Name and next Project Name (or Section Header) is the content.
    
    # Step 1: Map lines
    line_map = []
    for idx, line in enumerate(lines):
        if not line: continue
        
        type_line = "text"
        if "Capital Improvement Projects (Design)" in line:
            type_line = "header_design"
        elif "Capital Improvement Projects (Construction)" in line:
            type_line = "header_construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            type_line = "header_not_started"
        elif "(cid:190)" in line:
            type_line = "bullet"
        
        line_map.append({"idx": idx, "text": line, "type": type_line})
    
    # Step 2: Traverse map
    current_status = "unknown"
    
    # We need to group by project.
    # A project starts with a Name. A Name is a text line immediately followed by a bullet line (ignoring other text lines? No, usually Name is immediately followed by bullet or new line then bullet).
    # Actually, in the text:
    # "2022 Morning View Resurfacing & Storm Drain Improvements"
    # ""
    # "(cid:190) Updates:"
    
    # So Name is the text line before the bullet block.
    
    i = 0
    while i < len(line_map):
        item = line_map[i]
        
        if "header_" in item['type']:
            if "design" in item['type']: current_status = "design"
            elif "construction" in item['type']: current_status = "construction"
            elif "not_started" in item['type']: current_status = "not started"
            i += 1
            continue
        
        # Check if this line is a Project Name
        # It should be type 'text' and followed (eventually) by 'bullet' without intervening 'header' or other 'potential names'?
        # Actually, the pattern `Name -> ... -> Bullet` is strong.
        # But `Name` is just text. `Bullet` is `(cid:190)`.
        # So if `line_map[i]` is text, and `line_map[i+1]` is bullet, then `line_map[i]` is Name.
        
        if item['type'] == 'text':
            # Check next item
            if i + 1 < len(line_map) and line_map[i+1]['type'] == 'bullet':
                # Found a project
                p_name = item['text']
                p_start_idx = item['idx']
                
                # Collect text until next project name or header
                p_text = [p_name]
                
                # Advance to bullet
                j = i + 1
                while j < len(line_map):
                    next_item = line_map[j]
                    
                    # Stop if we hit a header
                    if "header_" in next_item['type']:
                        break
                    
                    # Stop if we hit next project (Text followed by Bullet)
                    if next_item['type'] == 'text' and j + 1 < len(line_map) and line_map[j+1]['type'] == 'bullet':
                        break
                    
                    p_text.append(next_item['text'])
                    j += 1
                
                full_text = " ".join(p_text)
                
                # Determine Status (refine 'construction')
                final_status = current_status
                if current_status == "construction":
                    if "completed" in full_text.lower():
                        final_status = "completed"
                    # Else remains "construction" (which likely maps to 'design' or 'active' in user's mind, but let's keep it or map to 'design' if needed? Prompt says 3 statuses: design, completed, not started. 'Construction' fits neither perfectly if it's not completed. But 'design' is 'in planning/design'. Construction is implementation. Maybe 'not started' is wrong. 'Completed' is wrong.
                    # Hint says: "Projects have three statuses: 'design', 'completed', 'not started'."
                    # Maybe 'Construction' -> 'design'? (Since it's active). 
                    # Or maybe I should check if the text says "Project is currently under construction".
                    # Let's output "construction" if strictly "under construction".
                    # But the Join will filter anyway.
                    pass
                
                extracted_projects.append({
                    "Project_Name": p_name,
                    "Status": final_status,
                    "Full_Text": full_text
                })
                
                # Move i to j
                i = j
                continue
        
        i += 1

# Filter projects by keywords
relevant_projects = []
for p in extracted_projects:
    text_lower = p['Full_Text'].lower()
    name_lower = p['Project_Name'].lower()
    
    # Check match
    match = False
    for kw in keywords:
        if kw in text_lower or kw in name_lower:
            match = True
            break
    
    if match:
        relevant_projects.append(p)

df_extracted = pd.DataFrame(relevant_projects)

# Join with Funding
# Clean Project Names? The DB names might be exact or close.
# Let's try exact merge first.
if not df_extracted.empty:
    merged = pd.merge(df_funding, df_extracted, on='Project_Name', how='inner')
else:
    merged = pd.DataFrame()

# If exact merge misses, we might need fuzzy or substring matching.
# But hint says "matches the project names that can be extracted".
# Let's check matching success.

# Select columns
if not merged.empty:
    result = merged[['Project_Name', 'Funding_Source', 'Amount', 'Status']].to_dict(orient='records')
else:
    result = []

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9102831309616723132': ['civic_docs'], 'var_function-call-9102831309616723245': ['Funding'], 'var_function-call-12492854141756139028': 'file_storage/function-call-12492854141756139028.json', 'var_function-call-7907601960746092281': 'file_storage/function-call-7907601960746092281.json', 'var_function-call-10585127880706054254': 'file_storage/function-call-10585127880706054254.json', 'var_function-call-2910026112661516748': 'file_storage/function-call-2910026112661516748.json'}

exec(code, env_args)
