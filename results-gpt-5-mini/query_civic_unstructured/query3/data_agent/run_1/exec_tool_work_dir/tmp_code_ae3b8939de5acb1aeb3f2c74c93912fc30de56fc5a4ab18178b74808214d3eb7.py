code = """import json
import pandas as pd

# Load the query results from storage variables (file paths provided)
with open(var_call_IBkE6sETgIJUK7RBuQYNU2IP, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

with open(var_call_F5LZc7pWGPHZcH3cfkJsTRH0, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Convert funding to DataFrame
funding_df = pd.DataFrame(funding_records)

# Normalize amount to int
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Prepare civic docs texts
docs = []
for d in civic_docs:
    text = d.get('text','')
    docs.append(text)

# Helper function to extract status from text around a project mention
import re

def extract_status_for_mention(project_name, text):
    lt = text.lower()
    pn = project_name.lower()
    idx = lt.find(pn)
    if idx == -1:
        return None
    start = max(0, idx-400)
    end = min(len(lt), idx+400)
    window = lt[start:end]
    # look for keywords in order of priority
    if 'not started' in window:
        return 'not started'
    if 'design' in window or 'complete design' in window or 'final design' in window:
        return 'design'
    # construction related
    if 'under construction' in window or 'begin construction' in window or 'construction' in window:
        return 'construction'
    if 'complete construction' in window or 'completed' in window or 'complete' in window:
        return 'completed'
    # FEMA/emergency mention but no clear status
    return None

related_projects = []

for _, row in funding_df.iterrows():
    pname = row['Project_Name']
    p_lower = pname.lower()
    funding_source = row['Funding_Source']
    amount = int(row['Amount'])
    related = False
    status = None
    # direct indicators in project name or funding source
    if 'fema' in p_lower or 'fema' in str(funding_source).lower() or 'emergency' in p_lower or 'emergency' in str(funding_source).lower():
        related = True
    # check civic docs for mentions of the project name within docs that contain fema/emergency (docs already filtered)
    if not related:
        for doc in docs:
            if pname.lower() in doc.lower():
                # doc was matched by initial query so contains fema or emergency
                related = True
                st = extract_status_for_mention(pname, doc)
                if st:
                    status = st
                break
    else:
        # even if related by name/funding_source, try to find status in civic docs
        for doc in docs:
            if pname.lower() in doc.lower():
                st = extract_status_for_mention(pname, doc)
                if st:
                    status = st
                    break
    if related:
        related_projects.append({
            'Project_Name': pname,
            'Funding_Source': funding_source,
            'Amount': amount,
            'Status': status
        })

# As a final step, deduplicate by Project_Name keeping first
seen = set()
unique_projects = []
for r in related_projects:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique_projects.append(r)

result = unique_projects

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_F5LZc7pWGPHZcH3cfkJsTRH0': 'file_storage/call_F5LZc7pWGPHZcH3cfkJsTRH0.json', 'var_call_IBkE6sETgIJUK7RBuQYNU2IP': 'file_storage/call_IBkE6sETgIJUK7RBuQYNU2IP.json'}

exec(code, env_args)
