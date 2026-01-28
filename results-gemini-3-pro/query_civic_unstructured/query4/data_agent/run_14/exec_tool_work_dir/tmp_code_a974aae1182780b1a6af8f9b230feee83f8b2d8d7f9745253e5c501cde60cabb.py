code = """import json
import pandas as pd
import string

# Load civic docs
civic_key = 'var_function-call-14257733574021227783'
funding_key = 'var_function-call-12616807807824493399'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)
    
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0)

extracted_projects = {} 

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    recent_lines = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if 'Updates:' in line or 'Project Description:' in line:
            if recent_lines:
                possible_name = recent_lines[-1]
                if "Capital Improvement Projects" not in possible_name and "Agenda Item" not in possible_name:
                    if len(possible_name) > 5 and not possible_name.startswith("Page"):
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

spring_projects = set()
for proj, dates in extracted_projects.items():
    for d in dates:
        d_lower = d.lower()
        if 'spring 2022' in d_lower or 'spring, 2022' in d_lower:
            spring_projects.add(proj)
            continue
        if '2022' in d_lower:
            if 'march' in d_lower or 'april' in d_lower or 'may' in d_lower:
                spring_projects.add(proj)

def clean_name(n):
    n = n.replace('(cid:190)', '').replace('(cid:131)', '').strip()
    return " ".join(n.split())

cleaned_spring_projects = {clean_name(p) for p in spring_projects}
funding_df['Clean_Project_Name'] = funding_df['Project_Name'].apply(clean_name)

matched = funding_df[funding_df['Clean_Project_Name'].isin(cleaned_spring_projects)]

# Fuzzy match
matched_ids = set(matched['Funding_ID'])
matched_names = set(matched['Clean_Project_Name'])
unmatched = cleaned_spring_projects - matched_names

def tokenize(s):
    # Remove punctuation
    s = s.translate(str.maketrans('', '', string.punctuation))
    return set(s.lower().split())

additional_matches = []
for u in unmatched:
    for idx, row in funding_df.iterrows():
        if row['Funding_ID'] in matched_ids:
            continue
        fname = row['Clean_Project_Name']
        
        u_tokens = tokenize(u)
        f_tokens = tokenize(fname)
        common = u_tokens.intersection(f_tokens)
        
        # Check similarity
        # If tokens match substantially
        if len(common) >= 3:
             # Ensure generic terms don't drive the match
             # Generic: park, road, improvements, project, repair, construction
             # Specific: malibu, bluffs, canyon, latigo, broad, beach, etc.
             
             # If common tokens are only generic, skip
             # But "Bluffs Park Shade Structure" - Bluffs is specific.
             if 'bluffs' in common or 'canyon' in common or 'beach' in common or 'civic' in common:
                 additional_matches.append(row)

if additional_matches:
    additional_df = pd.DataFrame(additional_matches)
    matched = pd.concat([matched, additional_df]).drop_duplicates(subset=['Funding_ID'])

print("__RESULT__:")
print(json.dumps({
    "matched_count": int(len(matched)),
    "matched_projects": matched['Project_Name'].tolist(),
    "total_funding": int(matched['Amount'].sum())
}))"""

env_args = {'var_function-call-1020154492988582043': 'file_storage/function-call-1020154492988582043.json', 'var_function-call-14257733574021227783': 'file_storage/function-call-14257733574021227783.json', 'var_function-call-12616807807824493399': 'file_storage/function-call-12616807807824493399.json', 'var_function-call-7747155797650451357': {'found_projects_names': ['shade structures at Malibu Bluffs Park.', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'damaged by the Woolsey Fire.', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Marie Canyon Green Streets', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'], 'matched_count': 9, 'matched_amount': 810004500094000360004400091000500004400043000}, 'var_function-call-16181361196311269015': {'matched_count': 9, 'matched_projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)'], 'total_funding': 528000}}

exec(code, env_args)
