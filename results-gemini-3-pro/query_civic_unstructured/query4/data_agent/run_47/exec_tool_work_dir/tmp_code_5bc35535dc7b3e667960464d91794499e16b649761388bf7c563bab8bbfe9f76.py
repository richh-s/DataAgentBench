code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3769111620830882253'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-3769111620830881668'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
# Create a mapping
project_funding = {}
for i, row in funding_df.iterrows():
    project_funding[row['Project_Name']] = row['Amount']

project_names = list(project_funding.keys())
project_names.sort(key=len, reverse=True)

matches = []

# Regex patterns
pats = [
    "Spring 2022", "Spring, 2022",
    "March 2022", "April 2022", "May 2022",
    "March, 2022", "April, 2022", "May, 2022",
    "03/\\d{2}/2022", "04/\\d{2}/2022", "05/\\d{2}/2022"
]
date_regex = "(" + "|".join(pats) + ")"

for doc in civic_docs:
    text = doc['text']
    # Find project positions
    positions = []
    for name in project_names:
        start_search = 0
        while True:
            idx = text.find(name, start_search)
            if idx == -1:
                break
            positions.append((idx, name))
            start_search = idx + len(name)
    
    positions.sort()
    
    for i in range(len(positions)):
        start_idx, name = positions[i]
        if i < len(positions) - 1:
            end_idx = positions[i+1][0]
        else:
            end_idx = len(text)
        
        section = text[start_idx:end_idx]
        
        # Check lines
        for line in section.split('\n'):
            if re.search(date_regex, line, re.IGNORECASE):
                # Check for start indicators
                lower_line = line.lower()
                # We want "Started" -> "Begin Construction" or similar.
                # Avoid "Complete"
                if "complete" in lower_line:
                    continue
                    
                if "begin" in lower_line or "start" in lower_line or "construction" in lower_line or "advertise" in lower_line:
                    matches.append({
                        "Project": name,
                        "Line": line.strip(),
                        "Funding": project_funding.get(name, 0)
                    })

# Unique
unique_matches = {}
for m in matches:
    unique_matches[m['Project']] = m

print("__RESULT__:")
print(json.dumps(list(unique_matches.values()), indent=2))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json'}

exec(code, env_args)
