code = """import json
import pandas as pd
import re
from datetime import datetime

# Load data
p1 = locals()["var_function-call-11755073423388004543"]
p2 = locals()["var_function-call-11755073423388006536"]

with open(p1, "r") as f:
    docs = json.load(f)
with open(p2, "r") as f:
    fund = json.load(f)

# Get valid projects
df_fund = pd.DataFrame(fund)
valid_projs = set(df_fund["Project_Name"].unique())

# Helper to parse date from filename
def get_doc_date(filename):
    # format: malibucity_agenda_03222023-2060.txt
    match = re.search(r'_(\d{8})', filename)
    if match:
        return datetime.strptime(match.group(1), "%m%d%Y")
    return datetime.min

# Sort docs by date
docs.sort(key=lambda x: get_doc_date(x['filename']))

# Tracking projects
# projects[name] = {'status': 'Unknown', 'start_date': None, 'doc_date': datetime.min}
project_state = {}

# Regex
pat_start = re.compile(r"(Start|Begin Construction)[:\s]+(.*?20\d{2})", re.IGNORECASE)
pat_status_header = re.compile(r"Capital Improvement Projects \((.*?)\)", re.IGNORECASE)

for doc in docs:
    d_date = get_doc_date(doc['filename'])
    text = doc['text']
    lines = text.splitlines()
    
    current_section_status = None
    current_proj = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Check for section header
        # e.g. Capital Improvement Projects (Design)
        # Note: headers might not be exactly these lines, checking partial match
        status_match = pat_status_header.search(line)
        if status_match:
            current_section_status = status_match.group(1).lower() # design, construction, not started
            current_proj = None
            continue
            
        # Check for project name
        if line in valid_projs:
            current_proj = line
            # Initialize or update status
            if current_proj not in project_state:
                project_state[current_proj] = {'status': None, 'start_date': None, 'doc_date': d_date}
            
            # Update status if we have a section header
            if current_section_status:
                project_state[current_proj]['status'] = current_section_status
                project_state[current_proj]['doc_date'] = d_date
            continue
        
        # Parse start date if inside project
        if current_proj:
            # Look for start date in this line
            # We want to capture the value
            s_match = pat_start.search(line)
            if s_match:
                date_str = s_match.group(2).strip()
                # Update start date
                project_state[current_proj]['start_date'] = date_str

# Filter projects started in Spring 2022
# Criteria:
# 1. Start Date string matches Spring/March/April/May 2022
# 2. Status is NOT 'design' or 'not started' IF the doc date is AFTER Spring 2022 (e.g. late 2022 or 2023).
#    If the last doc is from Feb 2022 and says Start Spring 2022, we count it (as we don't know it failed).
#    But if we have a 2023 doc saying "Design", then it didn't start.

final_projects = []
spring_2022_regex = re.compile(r"(Spring|March|April|May).*?2022", re.IGNORECASE)

for p, state in project_state.items():
    s_date = state['start_date']
    status = state['status']
    d_date = state['doc_date']
    
    if s_date and spring_2022_regex.search(s_date):
        # We found a Spring 2022 start date.
        # Check if it was cancelled/delayed
        # If latest doc is > May 2022 and status is 'design' or 'not started', reject.
        # Spring 2022 ends May 31, 2022.
        limit_date = datetime(2022, 6, 1)
        
        if d_date > limit_date:
            if status and ('design' in status or 'not started' in status):
                # Valid evidence it didn't start
                continue
        
        final_projects.append(p)

# Calculate funding
df_final = df_fund[df_fund["Project_Name"].isin(final_projects)]
total_funding = df_final["Amount"].astype(int).sum()

print("__RESULT__:")
print(json.dumps({"count": len(final_projects), "total_funding": int(total_funding), "projects": final_projects}))"""

env_args = {'var_function-call-11755073423388006536': 'file_storage/function-call-11755073423388006536.json', 'var_function-call-11755073423388004543': 'file_storage/function-call-11755073423388004543.json', 'var_function-call-9326283723142284407': {'count': 13, 'total_funding': 658000, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Civic Center Water Treatment Facility Phase 2', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}}

exec(code, env_args)
