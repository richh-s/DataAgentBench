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

# Regex to find project blocks
# Looking for a line that is followed by double newline and then (cid:190) (or unicode char) followed by Updates or Project Description
# The preview shows: "Project Name\n\n(cid:190) Updates:"
# Note: (cid:190) might be represented differently in the string or just as characters.
# Let's inspect the actual string in the python code first to be sure about the bullet character.
# But assuming the pattern holds.

for doc in civic_data:
    text = doc['text']
    
    # We'll split the text by the project title pattern.
    # Pattern: a line of text, followed by \n\n, followed by the bullet and a keyword.
    # The bullet in the preview is (cid:190). In regex, we might just match the text literals if possible, or use a general pattern.
    # Let's try to match "\n\n(cid:190) " or similar.
    
    # Let's find all start indices of project blocks
    # We assume a project starts with a name line.
    # It's hard to regex the name line directly because it's just text.
    # Instead, we regex the *start of the metadata* and take the preceding line as the name.
    
    # Markers usually start with (cid:190) or similar.
    # Let's look for the pattern: `\n(.+)\n\n\(cid:190\) (Updates|Project Description|Project Schedule)`
    # This captures the line before the marker.
    
    matches = list(re.finditer(r'\n(.+?)\n\n\(cid:190\) (Updates|Project Description|Project Schedule|Project Updates)', text))
    
    for i, match in enumerate(matches):
        project_name = match.group(1).strip()
        start_index = match.start()
        
        # End index is the start of the next match or end of text
        if i < len(matches) - 1:
            end_index = matches[i+1].start()
        else:
            end_index = len(text)
            
        project_text = text[start_index:end_index]
        
        # Check for "park" in project name (case insensitive)
        is_park = "park" in project_name.lower()
        
        # Check for completed status and date in 2022
        # We look for "completed" in the text
        # And check if the date associated is 2022
        # Example: "Construction was completed November 2022"
        # Example: "Construction was completed, November 2022"
        # We'll look for "completed" and then scan for a year nearby?
        # Or specifically "completed" followed by date.
        
        status = "unknown"
        completion_year = None
        
        if "completed" in project_text.lower():
            # Extract the sentence or context around "completed"
            # Regex to find "completed" followed by date
            # Patterns: "completed[,] <Month> <Year>" or "completed <Month> <Year>"
            date_match = re.search(r'completed,?\s+([A-Za-z]+)\s+(\d{4})', project_text, re.IGNORECASE)
            if date_match:
                completion_year = int(date_match.group(2))
                status = "completed"
            else:
                 # Try finding just the year if strictly close?
                 # Maybe "completed in 2022"
                 date_match_2 = re.search(r'completed\s+(?:in\s+)?(\d{4})', project_text, re.IGNORECASE)
                 if date_match_2:
                     completion_year = int(date_match_2.group(1))
                     status = "completed"

        projects.append({
            "Project_Name": project_name,
            "is_park": is_park,
            "status": status,
            "completion_year": completion_year,
            "raw_text_preview": project_text[:100]
        })

# Filter projects
target_projects = [
    p for p in projects 
    if p['is_park'] and p['status'] == 'completed' and p['completion_year'] == 2022
]

# Create DataFrame for target projects
target_df = pd.DataFrame(target_projects)

# Merge with funding
# We need to match Project_Name. 
# Let's strip and lower case for matching just in case, though usually exact match is expected.
# But let's check exact match first.

if not target_df.empty:
    merged = pd.merge(target_df, funding_df, on='Project_Name', how='inner')
    
    # Calculate total funding
    # Amount is string in JSON, need to convert to int/float
    merged['Amount'] = pd.to_numeric(merged['Amount'])
    total_funding = merged['Amount'].sum()
    
    result = {
        "target_projects": target_df['Project_Name'].tolist(),
        "matched_projects": merged['Project_Name'].tolist(),
        "total_funding": total_funding
    }
else:
    result = {
        "target_projects": [],
        "matched_projects": [],
        "total_funding": 0
    }

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8628233454064463530': 'file_storage/function-call-8628233454064463530.json', 'var_function-call-8628233454064463845': 'file_storage/function-call-8628233454064463845.json'}

exec(code, env_args)
