code = """import json
import re
import pandas as pd

# Load funding data
funding_path = locals()['var_function-call-8628233454064463530']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

# Load civic docs
civic_path = locals()['var_function-call-8628233454064463845']
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

projects = []

for doc in civic_data:
    text = doc['text']
    
    # Regex: match newline, capture line, newline, newline, (cid:190)
    # Note: we need to escape backslashes for the python string, and parentheses for regex
    # Pattern in python string: r'\n(.+?)\n\n\(cid:190\)'
    matches = list(re.finditer(r'\n(.+?)\n\n\(cid:190\)', text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.start()
        
        if i < len(matches) - 1:
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
            
        project_text = text[start_index:end_index]
        
        # Check "park"
        is_park = "park" in project_name.lower()
        
        # Check "completed" and date
        status = "not completed"
        completion_year = None
        
        # Look for "completed"
        if "completed" in project_text.lower():
            # Look for year 2022 near "completed"
            # Pattern: completed ... 2022
            # We'll just check if "2022" is in the text? No, must be the completion date.
            # Example: "Construction was completed November 2022"
            # Let's verify the text segment.
            
            # Simple check: if "completed" and "2022" are in the same sentence or close proximity?
            # Or regex specific formats seen in preview.
            # "completed, <Month> <Year>" or "completed <Month> <Year>"
            
            date_match = re.search(r'completed,?\s+([A-Za-z]+)\s+(\d{4})', project_text, re.IGNORECASE)
            if date_match:
                year = int(date_match.group(2))
                status = "completed"
                completion_year = year
            else:
                 # Try "completed" followed by just year or something similar
                 pass

        projects.append({
            "Project_Name": project_name,
            "is_park": is_park,
            "status": status,
            "completion_year": completion_year
        })

# Filter
target_projects = [
    p for p in projects 
    if p['is_park'] and p['status'] == 'completed' and p['completion_year'] == 2022
]

target_df = pd.DataFrame(target_projects)

if not target_df.empty:
    # Merge
    # Ensure exact match. 
    # Check if we need to clean project names?
    # The extracted name might have extra spaces? strip() was used.
    
    merged = pd.merge(target_df, funding_df, on='Project_Name', how='inner')
    merged['Amount'] = pd.to_numeric(merged['Amount'])
    total_funding = merged['Amount'].sum()
    
    result = {
        "projects": merged['Project_Name'].tolist(),
        "total_funding": total_funding
    }
else:
    result = {
        "projects": [],
        "total_funding": 0
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8628233454064463530': 'file_storage/function-call-8628233454064463530.json', 'var_function-call-8628233454064463845': 'file_storage/function-call-8628233454064463845.json'}

exec(code, env_args)
