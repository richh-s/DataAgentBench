code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3769111620830882253'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-3769111620830881668'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_funding = dict(zip(funding_df['Project_Name'], funding_df['Amount']))
project_names = list(project_funding.keys())
project_names.sort(key=len, reverse=True)

matches = []

# Date regex for Spring 2022
# Spring = March, April, May
date_regex = r"(Spring 2022|Spring, 2022|March 2022|April 2022|May 2022|March, 2022|April, 2022|May, 2022|03/\d{2}/2022|04/\d{2}/2022|05/\d{2}/2022)"

start_indicators = ["Begin Construction", "Construction Start", "Start Date", "Mobilization", "Advertise"] 
# "Advertise" is sometimes the start of the procurement phase, but usually "Begin Construction" is the project start.
# However, let's capture the line and decide.
# The hint says "st: Start time/date". 
# The text has "(cid:131) Begin Construction: ...". This is the most likely candidate.
# Let's also look for "Start:"

for doc in civic_docs:
    text = doc['text']
    # Find positions
    positions = []
    for name in project_names:
        start_search = 0
        while True:
            idx = text.find(name, start_search)
            if idx == -1:
                break
            # Verify it's not part of another word? (Optional but good)
            positions.append((idx, name))
            start_search = idx + len(name)
    
    positions.sort()
    
    # Analyze sections
    for i in range(len(positions)):
        start_idx, name = positions[i]
        if i < len(positions) - 1:
            end_idx = positions[i+1][0]
        else:
            end_idx = len(text)
        
        section = text[start_idx:end_idx]
        
        # Look for dates
        lines = section.split('\n')
        for line in lines:
            if re.search(date_regex, line, re.IGNORECASE):
                # Found the date. Check context.
                # If the line contains "Begin Construction" or similar
                if any(ind.lower() in line.lower() for ind in ["Construction", "Begin", "Start"]):
                     matches.append({
                        "Project": name,
                        "Line": line.strip(),
                        "Funding": project_funding.get(name, 0)
                     })

# Remove duplicates (same project might be mentioned multiple times or in multiple docs)
# We want unique projects.
unique_matches = {}
for m in matches:
    unique_matches[m['Project']] = m

result_list = list(unique_matches.values())

print("__RESULT__:")
print(json.dumps(result_list, indent=2))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json'}

exec(code, env_args)
