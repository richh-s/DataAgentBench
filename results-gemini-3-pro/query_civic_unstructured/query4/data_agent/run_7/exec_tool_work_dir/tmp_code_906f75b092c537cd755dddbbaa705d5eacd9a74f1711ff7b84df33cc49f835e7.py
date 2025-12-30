code = """import json
import pandas as pd
import re
from datetime import datetime

# Files
funding_path = locals()['var_function-call-11339180666459361146']
docs_path = locals()['var_function-call-9305854370968533096']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_map = {}
for name in funding_df['Project_Name']:
    project_map[name.lower().strip()] = name

# Parse doc dates
doc_dates = {}
for doc in civic_docs:
    fname = doc['filename']
    # simple regex for date in filename
    # assuming format like ...01262022...
    # avoiding re.search if possible to minimize complexity? No, re is fine.
    # use explicit raw string
    match = re.search(r'(\d{8})', fname)
    if match:
        dt_str = match.group(1)
        try:
            doc_dates[fname] = datetime.strptime(dt_str, '%m%d%Y')
        except:
            doc_dates[fname] = datetime.min
    else:
        doc_dates[fname] = datetime.min

matched_projects = set()

# We need to store all start mentions: Project -> [(Date, Line)]
project_mentions = {}

start_keywords = ['begin', 'start', 'advertise', 'award']

for doc in civic_docs:
    fname = doc['filename']
    d_date = doc_dates[fname]
    text = doc['text']
    lines = text.splitlines()
    current_project = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        line_lower = line_clean.lower()
        if line_lower in project_map:
            current_project = project_map[line_lower]
        
        if current_project:
            # Check for year to identify date-related lines
            if '202' in line_lower: # 2021, 2022, 2023, 2024
                # Check for start keywords
                is_start = False
                for kw in start_keywords:
                    if kw in line_lower:
                        is_start = True
                        break
                if 'construction' in line_lower and 'complete' not in line_lower:
                    is_start = True
                
                if is_start:
                    if current_project not in project_mentions:
                        project_mentions[current_project] = []
                    project_mentions[current_project].append((d_date, line_lower))

# Analyze latest mentions
for proj, mentions in project_mentions.items():
    # Sort by date descending
    mentions.sort(key=lambda x: x[0], reverse=True)
    
    # Take latest
    latest_date, line = mentions[0]
    
    # Check if Spring 2022
    is_spring_2022 = False
    if '2022' in line:
        if 'spring' in line: is_spring_2022 = True
        elif 'march' in line: is_spring_2022 = True
        elif 'april' in line: is_spring_2022 = True
        elif 'may' in line: is_spring_2022 = True
    
    if is_spring_2022:
        matched_projects.add(proj)

final_projects = list(matched_projects)
total_amount = funding_df[funding_df['Project_Name'].isin(final_projects)]['Amount'].astype(int).sum()

print('__RESULT__:')
print(json.dumps({'count': len(final_projects), 'total_funding': int(total_amount), 'names': final_projects}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json', 'var_function-call-12135098682891406353': 'file_storage/function-call-11339180666459361146.json', 'var_function-call-2490926604457630911': {'count': 14, 'total_funding': 748000, 'names': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH at Trancas Canyon Road Right Turn Lane', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'PCH Median Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}, 'var_function-call-9305854370968533096': 'file_storage/function-call-9305854370968533096.json'}

exec(code, env_args)
