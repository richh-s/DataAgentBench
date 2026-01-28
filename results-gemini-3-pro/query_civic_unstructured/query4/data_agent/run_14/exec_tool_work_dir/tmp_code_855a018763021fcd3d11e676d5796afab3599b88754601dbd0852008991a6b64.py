code = """import json
import pandas as pd

# Load civic docs
civic_key = 'var_function-call-14257733574021227783'
funding_key = 'var_function-call-12616807807824493399'

with open(locals()[civic_key], 'r') as f:
    civic_docs = json.load(f)

with open(locals()[funding_key], 'r') as f:
    funding_data = json.load(f)
    
funding_df = pd.DataFrame(funding_data)
# Convert Amount to int
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0)

extracted_projects = {} # Name -> list of dates

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
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
                # Filter out headers and noise
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

# Filter for Spring 2022
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

# Clean names
def clean_name(n):
    # Remove bullet points if any
    n = n.replace('(cid:190)', '').replace('(cid:131)', '').strip()
    return " ".join(n.split())

cleaned_spring_projects = {clean_name(p) for p in spring_projects}
funding_df['Clean_Project_Name'] = funding_df['Project_Name'].apply(clean_name)

# Attempt fuzzy matching or manual alignment
# Let's verify matches
matched = funding_df[funding_df['Clean_Project_Name'].isin(cleaned_spring_projects)]

# Check unmatched
matched_names = set(matched['Clean_Project_Name'])
unmatched = cleaned_spring_projects - matched_names

# Try to find partial matches for unmatched
additional_matches = []
for u in unmatched:
    # Try to find u in funding names or funding name in u
    for idx, row in funding_df.iterrows():
        fname = row['Clean_Project_Name']
        # Simple containment
        if u in fname or fname in u:
             # Avoid matching generic terms
             if len(fname) > 10 and len(u) > 10:
                 additional_matches.append(row)

if additional_matches:
    additional_df = pd.DataFrame(additional_matches)
    # Remove duplicates
    additional_df = additional_df.drop_duplicates(subset=['Funding_ID'])
    # Combine
    matched = pd.concat([matched, additional_df]).drop_duplicates(subset=['Funding_ID'])

print("__RESULT__:")
print(json.dumps({
    "matched_count": len(matched),
    "matched_projects": matched['Project_Name'].tolist(),
    "total_funding": matched['Amount'].sum()
}))"""

env_args = {'var_function-call-1020154492988582043': 'file_storage/function-call-1020154492988582043.json', 'var_function-call-14257733574021227783': 'file_storage/function-call-14257733574021227783.json', 'var_function-call-12616807807824493399': 'file_storage/function-call-12616807807824493399.json', 'var_function-call-7747155797650451357': {'found_projects_names': ['shade structures at Malibu Bluffs Park.', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'damaged by the Woolsey Fire.', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Marie Canyon Green Streets', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'], 'matched_count': 9, 'matched_amount': 810004500094000360004400091000500004400043000}}

exec(code, env_args)
