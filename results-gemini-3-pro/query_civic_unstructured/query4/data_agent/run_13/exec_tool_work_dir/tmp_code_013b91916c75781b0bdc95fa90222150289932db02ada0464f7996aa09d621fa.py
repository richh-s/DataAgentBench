code = """import json
import re
import pandas as pd

with open(locals()['var_function-call-4190880947126154290'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2571507213258603600'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

spring_regex = re.compile(r'(Spring|March|April|May|Mar|Apr).*2022', re.IGNORECASE)

found_projects = set()

for doc in civic_docs:
    lines = doc['text'].split('\n')
    current_project = None
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check ahead for "Updates:"
        # If the NEXT non-empty line contains "Updates:", then THIS line is likely the project name
        is_header = False
        k = i + 1
        while k < len(lines) and k < i + 5:
            nl = lines[k].strip()
            if not nl:
                k += 1
                continue
            if "Updates:" in nl:
                is_header = True
            break
        
        if is_header:
            current_project = line
            
        if current_project:
            # Check for start date
            l_lower = line.lower()
            if "begin construction" in l_lower or "construction started" in l_lower or "start" in l_lower:
                if spring_regex.search(line):
                    found_projects.add(current_project)

# Matching
funding_df['Project_Name_Clean'] = funding_df['Project_Name'].str.strip().str.lower()
cleaned_projects_lower = {p.lower() for p in found_projects}

matched = funding_df[funding_df['Project_Name_Clean'].isin(cleaned_projects_lower)]

res = {
    "count": len(matched),
    "total_funding": matched['Amount'].astype(float).sum(),
    "projects": matched['Project_Name'].tolist()
}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-2571507213258604103': ['civic_docs'], 'var_function-call-2571507213258603600': 'file_storage/function-call-2571507213258603600.json', 'var_function-call-4959924631149924151': 'file_storage/function-call-4959924631149924151.json', 'var_function-call-4190880947126154290': 'file_storage/function-call-4190880947126154290.json'}

exec(code, env_args)
