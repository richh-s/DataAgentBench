code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3769111620830882253'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-3769111620830881668'], 'r') as f:
    funding_data = json.load(f)

# Funding dict
project_funding = {item['Project_Name']: item['Amount'] for item in funding_data}
project_names = list(project_funding.keys())
project_names.sort(key=len, reverse=True)

matches = []
pats = ["Spring 2022", "Spring, 2022", "March 2022", "April 2022", "May 2022"]
# Simplified regex for testing
date_regex = "(Spring 2022|March 2022|April 2022|May 2022)"

for doc in civic_docs:
    text = doc['text']
    for name in project_names:
        idx = text.find(name)
        if idx != -1:
            # Look in a window after the name
            window = text[idx:idx+2000] # Assumption: project details are within 2000 chars
            
            if re.search(date_regex, window, re.IGNORECASE):
                # Found date
                lines = window.split('\n')
                for line in lines:
                    if re.search(date_regex, line, re.IGNORECASE):
                        lower = line.lower()
                        if "complete" in lower: continue
                        if "begin" in lower or "start" in lower or "advertise" in lower:
                            matches.append({"Project": name, "Line": line.strip(), "Amount": project_funding[name]})
                            break # Found one start date for this project in this doc

# Unique
unique = {}
for m in matches:
    unique[m['Project']] = m

print("__RESULT__:")
print(json.dumps(list(unique.values())))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json'}

exec(code, env_args)
