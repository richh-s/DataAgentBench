code = """import json
import pandas as pd
import re

# Load civic docs
with open(locals()['var_function-call-14257733574021227783'], 'r') as f:
    civic_docs = json.load(f)

# Load funding data
with open(locals()['var_function-call-12616807807824493399'], 'r') as f:
    funding_data = json.load(f)
    
funding_df = pd.DataFrame(funding_data)

extracted_projects = {} # Name -> list of dates

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    current_project = None
    recent_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Heuristic for project name: Line before "Updates:"
        if 'Updates:' in line or 'Project Description:' in line:
            if recent_lines:
                possible_name = recent_lines[-1]
                # Filter out headers
                if "Capital Improvement Projects" not in possible_name and "Agenda Item" not in possible_name:
                    current_project = possible_name
        
        if current_project:
            if 'Begin Construction:' in line:
                val = line.split('Begin Construction:', 1)[1].strip()
                extracted_projects[current_project] = extracted_projects.get(current_project, []) + [val]
            elif 'Start:' in line:
                val = line.split('Start:', 1)[1].strip()
                extracted_projects[current_project] = extracted_projects.get(current_project, []) + [val]
        
        recent_lines.append(line)
        if len(recent_lines) > 5:
            recent_lines.pop(0)

# Filter for Spring 2022
spring_projects = set()
for proj, dates in extracted_projects.items():
    for d in dates:
        d_lower = d.lower()
        if 'spring 2022' in d_lower or 'spring, 2022' in d_lower:
            spring_projects.add(proj)
            continue
        # Check specific months
        if '2022' in d_lower:
            if 'march' in d_lower or 'april' in d_lower or 'may' in d_lower:
                spring_projects.add(proj)

# Clean names
def clean_name(n):
    return " ".join(n.split())

cleaned_spring_projects = {clean_name(p) for p in spring_projects}
funding_df['Clean_Project_Name'] = funding_df['Project_Name'].apply(clean_name)

matched = funding_df[funding_df['Clean_Project_Name'].isin(cleaned_spring_projects)]

# Result
print("__RESULT__:")
print(json.dumps({
    "found_projects_count": len(cleaned_spring_projects),
    "found_projects_names": list(cleaned_spring_projects),
    "matched_count": len(matched),
    "matched_amount": int(matched['Amount'].sum()),
    "matched_details": matched[['Project_Name', 'Amount']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-1020154492988582043': 'file_storage/function-call-1020154492988582043.json', 'var_function-call-14257733574021227783': 'file_storage/function-call-14257733574021227783.json', 'var_function-call-12616807807824493399': 'file_storage/function-call-12616807807824493399.json'}

exec(code, env_args)
