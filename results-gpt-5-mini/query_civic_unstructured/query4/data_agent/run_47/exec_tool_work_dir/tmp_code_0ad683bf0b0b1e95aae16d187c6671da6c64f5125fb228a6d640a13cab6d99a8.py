code = """import json
import re

# Load the civic docs result (file path stored in var_call_dpIJq3GC3JHbvONv2OP2EYlp)
with open(var_call_dpIJq3GC3JHbvONv2OP2EYlp, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Load the funding table result (file path stored in var_call_IRAIHIQxpFwOjP5L1iucGzIo)
with open(var_call_IRAIHIQxpFwOjP5L1iucGzIo, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Prepare patterns for Spring 2022 (Spring = March-May)
spring_patterns = [
    'Spring 2022', '2022 Spring', '2022-Spring',
    'March 2022', 'Apr 2022', 'April 2022', 'May 2022', 'Mar 2022',
    '2022-March', '2022-April', '2022-May',
    '03-2022', '04-2022', '05-2022'
]

# Normalize patterns to lowercase for case-insensitive search
spring_patterns = [p.lower() for p in spring_patterns]

# Combine all civic doc texts into a single string for easier searching, but keep document boundaries
texts = [doc.get('text','') for doc in civic_docs]

matched_projects = []
matched_records = []

for row in funding_rows:
    proj_name = row.get('Project_Name','')
    if not proj_name:
        continue
    proj_name_lower = proj_name.lower()
    found = False
    for text in texts:
        text_lower = text.lower()
        idx = text_lower.find(proj_name_lower)
        if idx != -1:
            # take a window around the occurrence
            start = max(0, idx-400)
            end = min(len(text_lower), idx+400)
            window = text_lower[start:end]
            # Check if any spring pattern appears in the window or nearby lines
            if any(p in window for p in spring_patterns):
                found = True
                break
            # also check a slightly larger nearby context
            start2 = max(0, idx-2000)
            end2 = min(len(text_lower), idx+2000)
            window2 = text_lower[start2:end2]
            if any(p in window2 for p in spring_patterns):
                found = True
                break
    if found:
        matched_projects.append(proj_name)
        # convert amount to int safely
        try:
            amount = int(row.get('Amount',0))
        except:
            try:
                amount = int(float(row.get('Amount',0)))
            except:
                amount = 0
        matched_records.append({'Project_Name': proj_name, 'Amount': amount})

# Deduplicate projects by name
unique_projects = {}
for rec in matched_records:
    name = rec['Project_Name']
    amt = rec['Amount']
    if name in unique_projects:
        unique_projects[name] += amt
    else:
        unique_projects[name] = amt

count = len(unique_projects)
total_funding = sum(unique_projects.values())
project_list = sorted([{"Project_Name": k, "Total_Amount": v} for k,v in unique_projects.items()], key=lambda x: x['Project_Name'])

result = {
    'count': count,
    'total_funding': total_funding,
    'projects': project_list
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_CKtpo9pHhmHQNLchYr9UHcgK': ['civic_docs'], 'var_call_e1tRcrXJqWwbZQHoIrpyHxrF': ['Funding'], 'var_call_dpIJq3GC3JHbvONv2OP2EYlp': 'file_storage/call_dpIJq3GC3JHbvONv2OP2EYlp.json', 'var_call_IRAIHIQxpFwOjP5L1iucGzIo': 'file_storage/call_IRAIHIQxpFwOjP5L1iucGzIo.json'}

exec(code, env_args)
