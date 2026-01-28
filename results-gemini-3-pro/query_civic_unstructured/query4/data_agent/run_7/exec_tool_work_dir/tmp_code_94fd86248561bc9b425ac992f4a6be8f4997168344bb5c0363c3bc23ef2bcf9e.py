code = """import json
import pandas as pd
import re
from datetime import datetime

# Files
funding_path = locals()['var_function-call-11339180666459361146']
docs_path = locals()['var_function-call-11339180666459360437']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

funding_df = pd.DataFrame(funding_data)
project_map = {}
for name in funding_df['Project_Name']:
    project_map[name.lower().strip()] = name

# Parse doc dates
doc_dates = {} # filename -> datetime
for doc in civic_docs:
    fname = doc['filename']
    # search for 8 digits
    match = re.search(r'(\d{8})', fname)
    if match:
        dt_str = match.group(1)
        try:
            dt = datetime.strptime(dt_str, "%m%d%Y")
            doc_dates[fname] = dt
        except:
            doc_dates[fname] = datetime.min
    else:
        doc_dates[fname] = datetime.min

# Extract segments per project
project_segments = {} # Project -> [(date, segment_lines)]

for doc in civic_docs:
    fname = doc['filename']
    date = doc_dates[fname]
    text = doc['text']
    lines = text.splitlines()
    
    # Identify project locations
    # We'll use a simplified approach: Iterate lines, if header match, start collecting.
    current_project = None
    buffer = []
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        
        line_lower = line_clean.lower()
        
        # Check for new project
        if line_lower in project_map:
            # Save previous buffer
            if current_project:
                if current_project not in project_segments:
                    project_segments[current_project] = []
                project_segments[current_project].append((date, buffer))
            
            current_project = project_map[line_lower]
            buffer = []
        else:
            if current_project:
                buffer.append(line_clean)
    
    # Save last buffer
    if current_project and buffer:
        if current_project not in project_segments:
            project_segments[current_project] = []
        project_segments[current_project].append((date, buffer))

# Analyze latest segment for each project
matched_projects = set()
start_keywords = ['begin', 'start', 'advertise', 'award']

for proj, segments in project_segments.items():
    # Sort by date descending
    segments.sort(key=lambda x: x[0], reverse=True)
    
    # Check the latest segment first. 
    # If the project is "completed", the schedule might say "Completed: Date".
    # We check if the Start was Spring 2022 based on the latest info.
    # Note: If the latest doc is from 2023, and it says "Begin Construction: Spring 2022", that's confirmed.
    # If the latest doc is from 2021, and says "Begin: Spring 2022", it's a plan (but maybe the best we have).
    # We'll trust the latest available document.
    
    latest_date, lines = segments[0]
    
    # Check for Spring 2022 start in these lines
    for line in lines:
        line_lower = line.lower()
        
        has_date = False
        if '2022' in line_lower:
            if 'spring' in line_lower: has_date = True
            elif 'march' in line_lower: has_date = True
            elif 'april' in line_lower: has_date = True
            elif 'may' in line_lower: has_date = True
            
        if has_date:
            is_start = False
            for kw in start_keywords:
                if kw in line_lower:
                    is_start = True
                    break
            if 'construction' in line_lower and 'complete' not in line_lower:
                is_start = True
            
            if is_start:
                matched_projects.add(proj)
                break # Found for this project

final_projects = list(matched_projects)
total_amount = funding_df[funding_df['Project_Name'].isin(final_projects)]['Amount'].astype(int).sum()

print('__RESULT__:')
print(json.dumps({'count': len(final_projects), 'total_funding': int(total_amount), 'names': final_projects}))"""

env_args = {'var_function-call-2238045295135148005': ['civic_docs'], 'var_function-call-2238045295135146372': 'file_storage/function-call-2238045295135146372.json', 'var_function-call-2238045295135148835': ['Funding'], 'var_function-call-2238045295135147202': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-11339180666459360437': 'file_storage/function-call-11339180666459360437.json', 'var_function-call-11339180666459361146': 'file_storage/function-call-11339180666459361146.json', 'var_function-call-12135098682891406353': 'file_storage/function-call-11339180666459361146.json', 'var_function-call-2490926604457630911': {'count': 14, 'total_funding': 748000, 'names': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH at Trancas Canyon Road Right Turn Lane', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Bluffs Park Shade Structure', 'PCH Median Improvements Project', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)']}}

exec(code, env_args)
