code = """import json
import pandas as pd
import re

# Load
with open(locals()['var_function-call-10631543890590275884'], 'r') as f:
    civic_docs = json.load(f)
with open(locals()['var_function-call-10631543890590275137'], 'r') as f:
    funding_data = json.load(f)

df_funding = pd.DataFrame(funding_data)
df_funding['Amount'] = pd.to_numeric(df_funding['Amount'])

projects_found = []

for doc in civic_docs:
    lines = [l.strip() for l in doc['text'].split(chr(10)) if l.strip()]
    
    # 1. Identify start indices of projects
    project_indices = [] # (line_index, project_name)
    
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        # Check if next line is a project section starter
        # (cid:190) Updates... or (cid:190) Project Description...
        if next_line.startswith('(') and 'cid' in next_line and '190' in next_line:
            if 'updates' in next_line.lower() or 'project description' in next_line.lower():
                # This line 'line' is likely the project name
                # Clean it
                name = line.strip()
                # Filter out garbage
                if len(name) < 5 or "Page" in name or "Agenda" in name or name.endswith('.'):
                    continue
                
                project_indices.append((i, name))
    
    # 2. Extract content for each project
    for k in range(len(project_indices)):
        start_idx, name = project_indices[k]
        end_idx = project_indices[k+1][0] if k + 1 < len(project_indices) else len(lines)
        
        # content
        content_lines = lines[start_idx:end_idx]
        full_text = " ".join(content_lines).lower()
        t = re.sub(r'\s+', ' ', full_text)
        
        # 3. Check for Spring 2022
        # We need "Advertise: Spring 2022" or "Begin Construction: Spring 2022"
        # Or "Start... Spring 2022"
        if re.search(r'(advertise|begin construction|start).*spring 2022', t):
            projects_found.append(name)
        elif re.search(r'(advertise|begin construction|start).*spring, 2022', t):
            projects_found.append(name)

# Dedupe
projects_found = list(set(projects_found))

# Join
matched_count = 0
matched_funding = 0
matched_names = []
unmatched = []

df_funding['norm'] = df_funding['Project_Name'].str.lower().str.strip()

for p in projects_found:
    p_norm = p.lower().strip()
    match = df_funding[df_funding['norm'] == p_norm]
    if not match.empty:
        matched_count += 1
        matched_funding += match['Amount'].sum()
        matched_names.append(p)
    else:
        unmatched.append(p)

print("__RESULT__:")
print(json.dumps({
    "count": int(matched_count),
    "total_funding": int(matched_funding),
    "projects": matched_names,
    "unmatched": unmatched
}))"""

env_args = {'var_function-call-16904404130023659614': 'file_storage/function-call-16904404130023659614.json', 'var_function-call-16904404130023657657': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-10631543890590275137': 'file_storage/function-call-10631543890590275137.json', 'var_function-call-10631543890590275884': 'file_storage/function-call-10631543890590275884.json', 'var_function-call-1178814106683189136': {'count': 2, 'total_funding': 87000, 'projects': ['Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)']}, 'var_function-call-9469292868970053981': [{'name': 'advertised for construction bids shortly after this date.', 'context': '(cid:190) project schedule: (cid:131) complete design: march 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'Project Schedule:', 'context': '(cid:131) complete final design: spring 2022 (cid:131) advertise: spring/summer 2022 (cid:131) award contract and begin construction: spring/summer 2022...'}, {'name': 'to review', 'context': '(cid:190) project schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: summer/winter 2022...'}, {'name': 'sending this project out to bid during the Spring of 2022.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'review by the Council.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: to be determined...'}, {'name': 'March 2022', 'context': '(cid:190) estimated schedule: (cid:131) begin design: spring 2022 capital improvement projects (construction) the city does not have projects in construction at this time. page 3 of 8 agenda item # 4....'}, {'name': 'is finalizing the bid documents.', 'context': '(cid:190) project schedule: (cid:131) complete design: february 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'context': '(cid:190) updates: (cid:131) the project consultant has started the design of this project. (cid:190) project schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'context': '(cid:190) updates: (cid:131) the project consultant has started the design of this project. (cid:190) project schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'A kick-off meeting was held in late December.', 'context': '(cid:190) estimated schedule: (cid:131) completion date: spring 2022...'}, {'name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'context': '(cid:190) updates: (cid:131) the project design will commence during the spring 2022. (cid:190) estimated schedule: tbd...'}, {'name': 'started and is anticipated to be completed by the Spring of 2022.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: fall 2022...'}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: summer 2022...'}, {'name': 'that was damaged by the Woolsey Fire.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: winter 2021 (cid:131) begin construction: spring 2022...'}, {'name': 'Fire.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: winter 2021 (cid:131) begin construction: spring 2022...'}, {'name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: summer 2022...'}, {'name': 'that was damaged by the Woolsey Fire.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: winter 2021 (cid:131) begin construction: spring 2022...'}, {'name': 'Fire.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: winter 2021 (cid:131) begin construction: spring 2022...'}, {'name': 'within the City.', 'context': '(cid:190) estimated schedule: (cid:131) completion date: spring 2022 page 6 of 6 agenda item # 4.a....'}, {'name': 'will begin in conjunction with the PCH Median Improvement', 'context': '(cid:190) project schedule: (cid:131) complete final design: spring 2022 (cid:131) advertise: summer 2022 (cid:131) award contract and begin construction: summer 2022...'}, {'name': 'scheduled for the April 11, 2022 Council meeting.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: february 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'review by the Council.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: to be determined page 3 of 8 agenda item # 4.a....'}, {'name': 'Metro.', 'context': '(cid:190) estimated schedule: (cid:131) begin design: late spring 2022 capital improvement projects (construction)...'}, {'name': 'is finalizing the bid documents.', 'context': '(cid:190) project schedule: (cid:131) complete design: march 2022 (cid:131) advertise: spring 2022 (cid:131) begin construction: summer 2022...'}, {'name': 'timber with non-combustible materials.', 'context': '(cid:190) project schedule (cid:131) complete design: april 2022 (cid:131) advertise: spring 2022 (cid:131) begin construction: spring 2022 page 5 of 8 agenda item # 4.a....'}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'context': '(cid:190) updates: (cid:131) the project consultant has started the design of this project. (cid:190) project schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: summer 2022...'}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'context': '(cid:190) updates: (cid:131) the project consultant has started the design of this project. (cid:190) project schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: summer 2022...'}, {'name': 'A kick-off meeting was held in late December.', 'context': '(cid:190) estimated schedule: (cid:131) completion date: spring 2022...'}, {'name': 'beginning in Spring 2022.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: march 2022 (cid:131) begin construction: spring 2022...'}, {'name': 'of 2022.', 'context': '(cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: fall 2022...'}]}

exec(code, env_args)
