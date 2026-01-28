code = """import json
import pandas as pd

with open(locals()['var_function-call-3769111620830882253'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-3769111620830881668'], 'r') as f:
    funding_data = json.load(f)

funding_map = {x['Project_Name']: x['Amount'] for x in funding_data}
project_names = list(funding_map.keys())
project_names.sort(key=len, reverse=True)

targets = ["Spring 2022", "Spring, 2022", "March 2022", "April 2022", "May 2022", "03/2022", "04/2022", "05/2022"]
matches = []

for doc in civic_docs:
    text = doc['text']
    
    for name in project_names:
        idx = text.find(name)
        if idx == -1:
            continue
            
        snippet = text[idx:idx+2000]
        
        for line in snippet.splitlines():
            line_lower = line.lower()
            # Check for date
            found_date = False
            for t in targets:
                if t.lower() in line_lower:
                    found_date = True
                    break
            
            if found_date:
                if "complete" in line_lower:
                    continue
                if "begin" in line_lower or "start" in line_lower or "advertise" in line_lower:
                    matches.append({
                        "Project": name,
                        "Line": line.strip(),
                        "Amount": funding_map[name]
                    })
                    break 

unique = {}
for m in matches:
    unique[m['Project']] = m

print("__RESULT__:")
print(json.dumps(list(unique.values())))"""

env_args = {'var_function-call-3769111620830882253': 'file_storage/function-call-3769111620830882253.json', 'var_function-call-3769111620830881668': 'file_storage/function-call-3769111620830881668.json', 'var_function-call-11366925193979982688': 'Hello', 'var_function-call-1063209578995606583': {'docs': 10, 'funding': 500}}

exec(code, env_args)
