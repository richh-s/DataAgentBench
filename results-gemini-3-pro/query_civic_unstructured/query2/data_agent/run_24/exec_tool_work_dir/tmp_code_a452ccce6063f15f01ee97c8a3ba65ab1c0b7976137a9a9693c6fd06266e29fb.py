code = """import json
import re
import pandas as pd

# Load funding data
with open(locals()['var_function-call-10729501578572278771'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Load civic docs
with open(locals()['var_function-call-14279954887626903002'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    text = doc['text']
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    
    # Iterate through lines to find project blocks
    # Heuristic: A line followed immediately by a line containing "(cid:190) Updates:" is a Project Name.
    # We will gather the text following it until the next Project Name is found.
    
    indices = []
    for i, line in enumerate(lines):
        if "(cid:190) Updates:" in line or "Updates:" in line and "(cid:190)" in line:
            # The project name is at i-1
            if i > 0:
                indices.append(i-1)
    
    for k in range(len(indices)):
        start_idx = indices[k]
        name = lines[start_idx]
        
        # Determine end index
        if k < len(indices) - 1:
            end_idx = indices[k+1]
        else:
            end_idx = len(lines)
            
        # Get full text block for this project
        block_lines = lines[start_idx:end_idx]
        full_text = " ".join(block_lines)
        
        extracted_projects.append({
            "Project_Name": name,
            "full_text": full_text
        })

# Analyze extracted projects
target_projects = []

for p in extracted_projects:
    name = p['Project_Name']
    full_text = p['full_text']
    lower_text = full_text.lower()
    
    # Check topic "park"
    # Check in Name or Text. User said "topic field contains... keywords", implies I should look for keywords.
    if "park" not in lower_text:
        continue
        
    # Check status "completed" and year "2022"
    # Look for patterns like "Construction was completed November 2022"
    # or "Complete Construction: November 2022"
    
    # Normalize spaces
    clean_text = re.sub(r'\s+', ' ', lower_text)
    
    # Check for completion in 2022
    # Regex to find "completed" followed by "2022" within reasonable distance
    # e.g. "completed november 2022" or "completed: nov 2022"
    
    # Patterns to look for:
    # 1. "completed <month> 2022"
    # 2. "complete construction: <month> 2022"
    # 3. "completed, <month> 2022"
    
    # Let's search for "2022" and see if "completed" is near it.
    
    is_2022_completed = False
    
    # Specific extraction logic
    # Find all dates associated with "completed" or "complete construction"
    matches = re.findall(r'(?:completed|complete construction).*?(\w+ 202\d)', clean_text)
    
    for match in matches:
        if "2022" in match:
            is_2022_completed = True
            break
            
    if is_2022_completed:
        target_projects.append(p)

# Create DataFrame
target_df = pd.DataFrame(target_projects)

if not target_df.empty:
    # Merge with funding
    # Normalize names
    target_df['norm_name'] = target_df['Project_Name'].str.lower().str.strip()
    funding_df['norm_name'] = funding_df['Project_Name'].str.lower().str.strip()
    
    # We might need fuzzy matching or strict. Let's try exact match first on normalized string.
    merged = pd.merge(target_df, funding_df, on='norm_name', how='inner')
    
    # Calculate sum
    total = merged['Amount'].sum()
    
    result = {
        "total_funding": total,
        "projects": merged['Project_Name_x'].tolist(),
        "amounts": merged['Amount'].tolist()
    }
else:
    result = {"total_funding": 0, "projects": []}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json'}

exec(code, env_args)
