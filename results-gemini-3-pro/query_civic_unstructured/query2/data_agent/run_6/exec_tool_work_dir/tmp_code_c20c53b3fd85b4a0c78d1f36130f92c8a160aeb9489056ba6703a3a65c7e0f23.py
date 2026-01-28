code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-11119621278912765381'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-10468269192346586678'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)

# Helper to identify projects
projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    # Iterate lines to find project blocks
    # Logic: A line is a project name if the next non-empty line starts with (cid:190)
    # Actually, the marker is (cid:190). In python string it might be a specific char.
    # From the output preview: "(cid:190) Updates:"
    # This (cid:190) is likely the string representation of a character. 
    # Let's assume the text literally contains "(cid:190)" or the character it represents.
    # I will look for lines starting with "(cid:190)" or containing "Updates:".
    
    # Let's clean lines first (strip whitespace)
    clean_lines = [l.strip() for l in lines]
    
    i = 0
    while i < len(clean_lines):
        line = clean_lines[i]
        
        # Check if this line is a start of a project description (Updates marker)
        # The marker in the preview is "(cid:190)". 
        # But looking at the preview text, it shows "(cid:190) Updates:".
        # Let's check for "Updates:" at the start or following a marker.
        if "Updates:" in line or line.startswith("(cid:190)"):
            # The PREVIOUS non-empty line should be the Project Name.
            # Let's look back.
            j = i - 1
            while j >= 0 and clean_lines[j] == "":
                j -= 1
            
            if j >= 0:
                project_name = clean_lines[j]
                # Now extract the full text block for this project.
                # It goes until the next Project Name.
                # How to find the next project name? 
                # It will be a line followed by "Updates:" or "(cid:190)".
                # So I can just capture text until the next "Updates:" block's predecessor.
                # Easier: just capture until end or next "Updates:" and assume the lines before it belong to the next project.
                
                # Actually, let's capture everything from line i (Updates) until the next time we identify a project start.
                # But the project name is at j.
                # So the block is from j to ...
                
                # Let's change strategy: Identify all indices of "Updates:" lines.
                # Then for each index, find the name before it.
                # The text is between this Name (exclusive) and the Next Name (exclusive).
                pass
        i += 1

# Revised extraction strategy
extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    clean_lines = [l.strip() for l in lines]
    
    # Find indices of lines containing "Updates:"
    update_indices = [idx for idx, line in enumerate(clean_lines) if "Updates:" in line or "(cid:190) Updates" in line]
    
    for k, idx in enumerate(update_indices):
        # Find name
        name_idx = idx - 1
        while name_idx >= 0 and clean_lines[name_idx] == "":
            name_idx -= 1
        
        if name_idx < 0:
            continue
            
        project_name = clean_lines[name_idx]
        
        # Determine end of this block
        # It ends at the start of the next project name.
        # The next project name is before the next update_idx.
        if k + 1 < len(update_indices):
            next_update_idx = update_indices[k+1]
            # Find name of next project
            next_name_idx = next_update_idx - 1
            while next_name_idx >= 0 and clean_lines[next_name_idx] == "":
                next_name_idx -= 1
            block_end = next_name_idx # exclusive
        else:
            block_end = len(clean_lines)
        
        # Extract block text
        # Join lines from name_idx to block_end
        block_text = "\n".join(clean_lines[name_idx:block_end])
        
        extracted_projects.append({
            "name": project_name,
            "text": block_text
        })

# Filter projects
matched_projects = []
for proj in extracted_projects:
    text_lower = proj['text'].lower()
    name_lower = proj['name'].lower()
    
    # Check Topic: "park"
    # Search in name or text.
    if "park" in name_lower or "park" in text_lower:
        is_park = True
    else:
        is_park = False
        
    if not is_park:
        continue
        
    # Check Status: "completed" in 2022
    # Look for "completed" and "2022"
    # Specific phrases: "construction was completed", "construction completed", "project completed"
    # And "2022"
    
    if "completed" in text_lower and "2022" in text_lower:
        # Refine check
        # Check if "complete design" is the only match.
        # If "construction" is in text, and "completed" is near "2022".
        
        # Simple heuristic:
        # If "construction was completed" or "construction completed" appears.
        if "construction was completed" in text_lower or "construction completed" in text_lower:
             # Check if 2022 is mentioned in the completion context.
             # e.g. "november 2022"
             if "2022" in text_lower: 
                 matched_projects.append(proj['name'])
        # Also check just "completed ... 2022" if specific phrase missing but context implies.
        # But let's stick to the specific ones found in the sample for high precision.
        # "Construction was completed November 2022" -> Matches.
        # "Construction was completed, January 2023" -> Matches "Construction was completed" but 2023.
        # So I need to parse the date associated with completion.
        
        # Let's use regex to find the date near "completed".
        # Pattern: completed.*?2022
        elif re.search(r"completed.*?2022", text_lower):
             # Exclude if it says "complete design"
             if "complete design" not in text_lower or "construction" in text_lower:
                 matched_projects.append(proj['name'])

# Remove duplicates
matched_projects = list(set(matched_projects))

# Filter funding
# Project names in Funding might be slightly different or exact.
# I will try exact match first.
# Clean matched_projects names (remove extra spaces, symbols if any)
# The sample name "Bluffs Park Shade Structure" is clean.
# Some names in text might have * or bullets? 
# The logic `project_name = clean_lines[name_idx]` should capture the line.

# Normalize names for matching
def normalize(s):
    return s.strip()

matched_projects_norm = [normalize(n) for n in matched_projects]

# Filter Funding
funding_matched = df_funding[df_funding['Project_Name'].apply(normalize).isin(matched_projects_norm)]

# Calculate total
total_funding = pd.to_numeric(funding_matched['Amount']).sum()

print("__RESULT__:")
print(json.dumps({
    "matched_projects": matched_projects_norm,
    "funding_rows": funding_matched.to_dict(orient='records'),
    "total_funding": total_funding
}))"""

env_args = {'var_function-call-5712816459567478650': ['civic_docs'], 'var_function-call-5712816459567478655': ['Funding'], 'var_function-call-13090257420212352430': 'file_storage/function-call-13090257420212352430.json', 'var_function-call-13090257420212352471': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11119621278912765381': 'file_storage/function-call-11119621278912765381.json', 'var_function-call-10468269192346586678': 'file_storage/function-call-10468269192346586678.json'}

exec(code, env_args)
