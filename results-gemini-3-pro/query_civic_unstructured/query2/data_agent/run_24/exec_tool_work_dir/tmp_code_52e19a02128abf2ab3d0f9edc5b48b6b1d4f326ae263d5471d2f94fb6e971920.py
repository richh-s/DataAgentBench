code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-10729501578572278771'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-14279954887626903002'], 'r') as f:
    civic_docs = json.load(f)

extracted_projects = []

for doc in civic_docs:
    lines = doc['text'].splitlines()
    lines = [l.strip() for l in lines if l.strip()]
    
    # Identify project start indices
    project_indices = []
    for i, line in enumerate(lines):
        if "Updates:" in line:
            if i > 0:
                project_indices.append(i-1)
    
    for k in range(len(project_indices)):
        start_idx = project_indices[k]
        name = lines[start_idx]
        
        # Determine end index
        if k < len(project_indices) - 1:
            end_idx = project_indices[k+1]
        else:
            end_idx = min(len(lines), start_idx + 30) # Safe upper bound
            
        # Get text block (stop before next project name, which is at end_idx)
        # Actually end_idx is the start of next project.
        # But we must be careful: the next project starts at end_idx.
        # So we take up to end_idx.
        chunk_lines = lines[start_idx+1:end_idx]
        chunk = " ".join(chunk_lines).lower()
        
        extracted_projects.append({
            "Project_Name": name,
            "text_chunk": chunk
        })

matched_projects = []
for p in extracted_projects:
    name = p['Project_Name']
    chunk = p['text_chunk']
    full_str = (name + " " + chunk).lower()
    
    if "park" in full_str:
        # Check completion date in 2022
        # Use regex to find "completed" followed by date
        # Pattern: "completed" ... "november 2022"
        # We need to ensure the date is 2022.
        
        # Find all dates associated with completed
        # "construction was completed november 2022"
        # "construction was completed, november 2022"
        # "notice of completion filed january 2023" (ignore this one)
        
        # Regex: look for "completed" then capture the next month/year
        # Be careful not to capture "january 2023" if it's far away.
        # Usually dates are close.
        
        dates = re.findall(r'completed.*?([a-z]+\s+202\d)', chunk)
        
        # Check if any date is 2022
        valid_2022 = False
        for d in dates:
            if "2022" in d:
                valid_2022 = True
                break
        
        if valid_2022:
            matched_projects.append(p)

# Merge
total = 0
project_names = []

if matched_projects:
    df_match = pd.DataFrame(matched_projects)
    df_match['join_key'] = df_match['Project_Name'].apply(lambda x: x.lower().strip())
    
    # Funding
    funding_df['join_key'] = funding_df['Project_Name'].apply(lambda x: x.lower().strip())
    funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])
    
    merged = pd.merge(df_match, funding_df, on='join_key', how='inner')
    merged = merged.drop_duplicates(subset=['Project_Name_y'])
    
    total = int(merged['Amount'].sum())
    project_names = merged['Project_Name_y'].tolist()

print("__RESULT__:")
print(json.dumps({"total": total, "projects": project_names}))"""

env_args = {'var_function-call-10729501578572278771': 'file_storage/function-call-10729501578572278771.json', 'var_function-call-14279954887626903002': 'file_storage/function-call-14279954887626903002.json', 'var_function-call-17936722017621136426': {'total': 152000, 'projects': ['Malibu Road Slope Repairs', 'Encinal Canyon Road Repairs', 'PCH Signal Synchronization System Improvements Project', 'Storm Drain Trash Screens Phase Two', 'Bluffs Park Shade Structure']}, 'var_function-call-8977789345911997912': {'total': 0, 'projects': []}, 'var_function-call-17316988873757343714': [{'name': 'Malibu Bluffs Park South Walkway Repairs', 'chunk': '(cid:190) updates: (cid:131) city to request proposal from consultant for design services (cid:190) estimated schedule: (cid:131) complete design: summer 2023 page 3 of 6 agenda item # 4.b. trancas canyon park playground (cid:190) updates: (cid:131) staff is currently working on the final design plans (cid:190) estimated schedule: (cid:131) complete design: summer 2023 (cid:131) advertise: summer 2023 malibu canyon road traffic study (cid:190) project description: this project will consist of a traffic study on malibu canyon road near harbor vista drive and potter lane to determine if any'}, {'name': 'Bluffs Park Shade Structure', 'chunk': '(cid:190) updates: construction was completed november 2022. notice of completion filed january 2023 page 4 of 6 agenda item # 4.b. marie canyon green streets (cid:190) updates: (cid:131) construction was completed, january 2023 (cid:131) scheduled for council acceptance on april 24, 2023 broad beach road water quality repair (cid:190) updates: (cid:131) construction was completed, november 2022 (cid:131) notice of completion filed january 2023 point dume walkway repairs (cid:190) updates: (cid:131) construction was completed, november 2022'}, {'name': 'shade structures at Malibu Bluffs Park.', 'chunk': '(cid:190) updates: (cid:131) staff is currently working on the design of the project and anticipates sending this project out to bid during the spring of 2022. (cid:190) estimated schedule: (cid:131) complete design: spring 2022 (cid:131) begin construction: spring 2022 permanent skate park (cid:190) project description: this project includes the designing and constructing a permanent skate park located on the crummer/case court parcel adjacent to malibu bluffs park. the project would include parking and additional site amenities such as trash cans, benches, tables, and restrooms. (cid:190) updates: (cid:131) in may 2021, the council approved funding for additional engineering work related to the project. staff has worked with the consultant over'}, {'name': 'Bluffs Park Workout Station', 'chunk': '(cid:190) updates: the contractor is waiting for the delivery of the new workout station equipment. (cid:190) project schedule: november 2020 – march 2021 civic center way improvements (cid:190) updates: (cid:131) work hours: monday through friday 7:00am to 4:00pm, saturdays 7:00am to 4:00pm (cid:131) the contractor is currently working at the section between vista pacifica and the condos on civic center way. this phase of work will require the temporary closure of civic center way. portions of the curb and gutter have been placed and the contactor is working on the proposed retaining wall. this portion of work is anticipated to be completed in early february 2021. (cid:131) the contractor is also working on the curb, gutter and storm drain installation on civic center way from webb way to the condos. this'}, {'name': 'Bluffs Park Workout Station', 'chunk': '(cid:190) updates: the contractor is waiting for the delivery of the new workout station equipment. the equipment is anticipated to be delivered at the end of february. (cid:190) project schedule: november 2020 – march 2021 civic center way improvements (cid:190) updates: (cid:131) work hours: monday through friday 7:00am to 4:00pm, saturdays 7:00am to 4:00pm (cid:131) the contractor is currently working at the section between vista pacifica and the condos on civic center way. this phase of work will require the temporary closure of civic center way. portions of the curb and gutter have been placed and the contactor is working on the proposed retaining wall. this portion of work is anticipated to be completed in early february 2021. (cid:131) the contractor is also working on the curb, gutter and storm drain'}, {'name': 'shade structures at Malibu Bluffs Park.', 'chunk': '(cid:190) updates: (cid:131) staff received bids on february 24, 2022. award of contract is scheduled for the april 11, 2022 council meeting. (cid:190) estimated schedule: (cid:131) complete design: february 2022 (cid:131) begin construction: spring 2022 permanent skate park (cid:190) project description: this project includes designing and constructing a permanent skate park located on the crummer/case court parcel adjacent to malibu bluffs park. the project would include parking and additional site amenities such as trash cans, benches, tables, and restrooms. (cid:190) updates: (cid:131) in may 2021, the council approved funding for additional engineering work related to the project. staff has worked with the consultant over'}]}

exec(code, env_args)
