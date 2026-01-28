code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-13609634735217417921'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-13507259868243532000'], 'r') as f:
    civic_docs = json.load(f)

# Unique known projects
known_projects = funding_df['Project_Name'].unique().tolist()
# Sort by length descending to match longest first
known_projects.sort(key=len, reverse=True)

found_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # Find positions of all known projects
    occurrences = []
    for proj in known_projects:
        start = 0
        while True:
            idx = text.find(proj, start)
            if idx == -1:
                break
            occurrences.append((idx, proj))
            start = idx + len(proj)
            
    # Sort by position
    occurrences.sort(key=lambda x: x[0])
    
    # Iterate and check segments
    for i in range(len(occurrences)):
        pos, proj_name = occurrences[i]
        
        # Define segment end
        if i < len(occurrences) - 1:
            end_pos = occurrences[i+1][0]
        else:
            end_pos = len(text)
            
        segment = text[pos:end_pos]
        
        # Search for start date
        # Pattern: Begin Construction: <Date>
        # Escaping backslashes: \\s, \\-
        match = re.search(r"(?:Begin|Start) [Cc]onstruction:?\s*([A-Za-z0-9, \-]+)", segment)
        
        if match:
            date_str = match.group(1).strip()
            
            d = date_str.lower()
            if "2022" in d:
                if "spring" in d:
                    found_projects.add(proj_name)
                elif "march" in d or "april" in d or "may" in d:
                    found_projects.add(proj_name)

# Calculate total funding
# Filter funding_df
result_df = funding_df[funding_df['Project_Name'].isin(found_projects)]

total_funding = pd.to_numeric(result_df['Amount']).sum()
# Count distinct projects found (the query asks "How many projects")
count = result_df['Project_Name'].nunique()

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_funding, "projects": list(found_projects)}))"""

env_args = {'var_function-call-17342646837596843535': 'file_storage/function-call-17342646837596843535.json', 'var_function-call-13609634735217417921': 'file_storage/function-call-13609634735217417921.json', 'var_function-call-13507259868243532000': 'file_storage/function-call-13507259868243532000.json'}

exec(code, env_args)
