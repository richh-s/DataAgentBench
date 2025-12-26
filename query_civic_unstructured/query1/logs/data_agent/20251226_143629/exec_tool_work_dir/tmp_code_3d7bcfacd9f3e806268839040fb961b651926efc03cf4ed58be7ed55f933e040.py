code = """import json
import pandas as pd

# Read large funding data
with open(var_call_M2zAyhrxkS1VB9fKwpDfXmSc, 'r') as f:
    funding_records = json.load(f)

# Extract names of funded projects
funded_projects = set([rec['Project_Name'] for rec in funding_records])

# Read large civic docs data
with open(var_call_MqiKPpIdCDvQhAaEypHXKu4u, 'r') as f:
    docs = json.load(f)

# This will store relevant (capital, design) projects
relevant_projects = set()

# Extract info about capital projects with design status from civic docs text
for doc in docs:
    txt = doc.get('text','').lower()
    # Rough matching for projects mentioned in 'Capital Improvement Projects (Design)' sections
    # Look for each funded project's name in the text near 'design' and 'capital'
    for pname in funded_projects:
        pname_ln = pname.lower()
        if pname_ln in txt:
            # find occurrences
            idx = txt.find(pname_ln)
            # Check local window for 'design' and 'capital'
            window = txt[max(0,idx-150):idx+len(pname_ln)+150]
            if 'design' in window and 'capital' in window:
                relevant_projects.add(pname)

result = len(relevant_projects)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_M2zAyhrxkS1VB9fKwpDfXmSc': 'file_storage/call_M2zAyhrxkS1VB9fKwpDfXmSc.json', 'var_call_MqiKPpIdCDvQhAaEypHXKu4u': 'file_storage/call_MqiKPpIdCDvQhAaEypHXKu4u.json'}

exec(code, env_args)
