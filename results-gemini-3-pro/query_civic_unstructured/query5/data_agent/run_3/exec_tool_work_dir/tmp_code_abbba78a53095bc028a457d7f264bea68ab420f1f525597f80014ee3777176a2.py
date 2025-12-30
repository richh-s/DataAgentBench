code = """import json
import pandas as pd
import os

civic_docs_var = locals()['var_function-call-72276613876208038']
funding_var = locals()['var_function-call-9094127879311422561']

if isinstance(civic_docs_var, str) and os.path.exists(civic_docs_var):
    with open(civic_docs_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_docs_var

if isinstance(funding_var, str) and os.path.exists(funding_var):
    with open(funding_var, 'r') as f:
        funding_data = json.load(f)
else:
    funding_data = funding_var

funding_df = pd.DataFrame(funding_data)

projects = []

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_section = 'Unknown'
    current_project = None
    project_buffer = [] 
    
    def save_project(name, buffer, section):
        if not name: return
        full_text = ' '.join(buffer)
        
        st = None
        # String find for date
        keys = ['Begin Construction:', 'Start:', 'Commence Construction:', 'Begin construction:', 'start:', 'Advertise:', 'Complete Design:'] 
        # Added Advertise/Design as fallbacks if start not found? No, query asks for "started". 
        # "Started" usually means construction start. But "st" field in description.
        # "Dates (st, et fields) use flexible formats...".
        # I'll stick to "Begin Construction" or "Start" as primary.
        # But wait, maybe "started in 2022" refers to the project *initiation*? 
        # "design" status projects might have started design in 2022.
        # "st" usually implies Start Time. 
        # Hints say "Projects have three statuses: 'design', 'completed', 'not started'".
        # If a project is in design, did it "start"?
        # Usually "started" means the project phase begins.
        # I will look for any date associated with 2022 in the schedule if "Begin Construction" is not found?
        # No, risk of picking End Date.
        # I will stick to "Begin Construction" or "Start".
        
        target_keys = ['Begin Construction:', 'Start:', 'Commence Construction:']
        for k in target_keys:
            idx = full_text.find(k)
            if idx != -1:
                sub = full_text[idx + len(k):]
                st_cand = sub[:50].strip()
                st = st_cand
                break
        
        p_type = 'capital'
        if 'Disaster' in section:
            p_type = 'disaster'
        elif any(s in name for s in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']):
            p_type = 'disaster'
        elif 'Woolsey Fire' in full_text:
            p_type = 'disaster'
            
        projects.append({
            'Project_Name': name,
            'type': p_type,
            'st': st,
            'section': section
        })

    for i, line in enumerate(lines):
        line = line.strip()
        if not line: continue
        
        if 'Capital Improvement Projects' in line:
            current_section = 'Capital Improvement Projects'
        if 'Disaster Recovery Projects' in line:
            current_section = 'Disaster Recovery Projects'
        
        is_project_name = False
        if not line.startswith('(') and not line.startswith('(cid'):
            if i + 1 < len(lines):
                next_line = lines[i+1].strip()
                if next_line.startswith('(cid') and ('Updates' in next_line or 'Description' in next_line):
                     if len(line) > 5 and len(line) < 150 and 'Page' not in line and 'Agenda' not in line:
                         is_project_name = True
        
        if is_project_name:
            if current_project:
                save_project(current_project, project_buffer, current_section)
            current_project = line
            project_buffer = []
        else:
            if current_project:
                project_buffer.append(line)
    
    if current_project:
        save_project(current_project, project_buffer, current_section)

projects_df = pd.DataFrame(projects)

# Clean Project Name
def clean_name(n):
    for s in ['(FEMA Project)', '(CalJPIA Project)', '(CalOES Project)']:
        n = n.replace(s, '')
    return n.strip()

projects_df['clean_name'] = projects_df['Project_Name'].apply(clean_name)

# Filter
projects_df['is_disaster'] = projects_df['type'] == 'disaster'
projects_df['started_2022'] = projects_df['st'].fillna('').str.contains('2022')

target_projects = projects_df[projects_df['is_disaster'] & projects_df['started_2022']].copy()

# Deduplicate
target_projects = target_projects.drop_duplicates(subset=['clean_name'])

# Join
funding_df['Project_Name'] = funding_df['Project_Name'].str.strip()
merged = pd.merge(target_projects, funding_df, left_on='clean_name', right_on='Project_Name', how='inner')

funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
# Make sure merged has numeric Amount
merged['Amount'] = pd.to_numeric(merged['Amount'])

total = int(merged['Amount'].sum())

print('__RESULT__:')
print(json.dumps({
    'total_funding': total,
    'merged_list': merged[['Project_Name_y', 'Amount', 'st']].to_dict(orient='records'),
    'debug_targets': target_projects[['clean_name', 'st']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-9094127879311422366': 'file_storage/function-call-9094127879311422366.json', 'var_function-call-9094127879311422561': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-72276613876208038': 'file_storage/function-call-72276613876208038.json', 'var_function-call-4777212261606908531': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Fall 2023', 'type': 'capital', 'st': 'Fall 2023 PCH Median Improvements Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Repair Project'}, {'Project_Name': '(cid:131) Complete Design: Summer 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Westward Beach Road Drainage Improvement'}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Clover Heights Storm Drainage Improvemen'}, {'Project_Name': '(cid:131) Final Design: Summer, 2023', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Summer 2023', 'type': 'capital', 'st': 'Fall 2023 Latigo Canyon Road Retaining Wall Repair'}, {'Project_Name': '(cid:131) Plans and specifications have been completed', 'type': 'capital', 'st': None}, {'Project_Name': '(cid:131) Advertise: Spring 2023', 'type': 'capital', 'st': 'Summer 2023 Storm Drain Master Plan'}]}, 'var_function-call-11494957844232901297': {'total_funding': 0, 'merged_projects': [], 'projects_dump': [{'Project_Name': 'Trancas Canyon Park Playground', 'type': 'capital', 'st': 'April 2023 (cid:131) Complete Construction: Summe'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'capital', 'st': None}, {'Project_Name': 'Point Dume Walkway Repairs', 'type': 'capital', 'st': None}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Spring 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': 'April 2022 Encinal Canyon Road Drainage Improveme'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2021 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Marie Canyon Green Streets', 'type': 'disaster', 'st': 'Summer 2022 PCH Median Improvements Project (cid:'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'type': 'disaster', 'st': None}]}}

exec(code, env_args)
