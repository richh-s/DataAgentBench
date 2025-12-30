code = """import json
import re
import pandas as pd

# Load previous results
with open(locals()['var_function-call-4190880947126154290'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-2571507213258603600'], 'r') as f:
    funding_data = json.load(f)

funding_df = pd.DataFrame(funding_data)

# Regex for Spring 2022
# Spring 2022 = March, April, May 2022
spring_2022_regex = re.compile(r'(Spring|March|April|May|Mar|Apr)\s*,?\s*2022', re.IGNORECASE)

found_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if line is a project name
        # Look ahead for (cid:190)
        is_project = False
        j = i + 1
        while j < len(lines) and j < i + 5:
            next_line = lines[j].strip()
            if not next_line:
                j += 1
                continue
            if "(cid:190)" in next_line or "Updates:" in next_line:
                # If we see the bullet or "Updates:", the previous non-empty line was likely the header
                is_project = True
            break
        
        if is_project:
            current_project = line
        
        if current_project:
            # Check for start date
            l_lower = line.lower()
            if "begin construction" in l_lower or "construction started" in l_lower or "construction began" in l_lower or "start" in l_lower:
                if spring_2022_regex.search(line):
                    found_projects.add(current_project)
        
        i += 1

# Clean extracted project names
cleaned_projects = set()
for p in found_projects:
    # Sometimes header has extra noise, but based on preview it looks clean enough
    cleaned_projects.add(p.strip())

# Funding matching
funding_df['Project_Name_Clean'] = funding_df['Project_Name'].str.strip().str.lower()
# Create a set of lower case project names from extraction
cleaned_projects_lower = {p.lower() for p in cleaned_projects}

# Filter
matched = funding_df[funding_df['Project_Name_Clean'].isin(cleaned_projects_lower)]

count = len(matched)
total_amount = matched['Amount'].astype(float).sum()

result = {
    "count": count,
    "total_funding": total_amount,
    "projects": list(matched['Project_Name'].unique())
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2571507213258604103': ['civic_docs'], 'var_function-call-2571507213258603600': 'file_storage/function-call-2571507213258603600.json', 'var_function-call-4959924631149924151': 'file_storage/function-call-4959924631149924151.json', 'var_function-call-4190880947126154290': 'file_storage/function-call-4190880947126154290.json'}

exec(code, env_args)
