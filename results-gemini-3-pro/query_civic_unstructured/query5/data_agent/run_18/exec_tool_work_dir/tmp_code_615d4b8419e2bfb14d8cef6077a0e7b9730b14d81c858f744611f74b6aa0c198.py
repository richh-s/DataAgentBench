code = """import json
import re

with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-9845122995383564769'], 'r') as f:
    funding_data = json.load(f)

def normalize(name):
    return re.sub(r'\s*\((?:FEMA|CalOES|CalJPIA).*?\)$', '', name, flags=re.IGNORECASE).strip()

funding_base_names = set()
for row in funding_data:
    funding_base_names.add(normalize(row['Project_Name']))

# We want to find:
# 1. Projects that started in 2022.
# 2. Projects that are disaster related.

# Info storage
project_info = {} # base_name -> {disaster_marks: [], start_marks: []}

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_proj = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        found = None
        # Heuristic matching
        for base in funding_base_names:
            if base in line_clean and len(line_clean) < len(base) + 15:
                found = base
                break
        
        if found:
            current_proj = found
            if current_proj not in project_info:
                project_info[current_proj] = {'disaster': False, 'started_2022': False, 'logs': []}
            continue
            
        if current_proj:
            # Check for Disaster keywords
            if any(x in line_clean for x in ["FEMA", "CalOES", "CalJPIA", "Woolsey", "Disaster"]):
                project_info[current_proj]['disaster'] = True
                project_info[current_proj]['logs'].append(f"Disaster KW in {doc['filename']}: {line_clean}")

            # Check for Start Date
            # Explicit Start
            if "Begin Construction" in line_clean or "Start Construction" in line_clean:
                if "2022" in line_clean:
                    project_info[current_proj]['started_2022'] = True
                    project_info[current_proj]['logs'].append(f"Start 2022 in {doc['filename']}: {line_clean}")
            
            # Award
            if "Awarded" in line_clean and "2022" in line_clean:
                project_info[current_proj]['started_2022'] = True
                project_info[current_proj]['logs'].append(f"Award 2022 in {doc['filename']}: {line_clean}")
                
            # Completed 2022
            if "Construction was completed" in line_clean and "2022" in line_clean:
                 # Check if it was early 2022 (likely started 2021) or late 2022 (likely started 2022)
                 # Jan/Feb 2022 -> likely 2021 start
                 # Nov/Dec 2022 -> likely 2022 start
                 if any(m in line_clean for m in ["November", "December", "October", "September", "August", "July", "June", "May", "April", "March"]):
                      # Excluding January/February? "March" is border.
                      # "Marie Canyon Green Streets" completed Jan 2023. Started 2022.
                      # "Broad Beach" completed Nov 2022. Started 2022.
                      # "2021 Annual Street" completed Jan 2022. Started 2021.
                      # So "Completed Jan 2022" -> Start 2021.
                      # "Completed Nov 2022" -> Start 2022.
                      project_info[current_proj]['started_2022'] = True
                      project_info[current_proj]['logs'].append(f"Completed late 2022 in {doc['filename']}: {line_clean}")

# Now match with Funding
final_projects = set()
total_amount = 0

for row in funding_data:
    raw_name = row['Project_Name']
    base = normalize(raw_name)
    
    # Is Disaster?
    is_disaster = False
    if re.search(r'\((?:FEMA|CalOES|CalJPIA).*?\)', raw_name, re.IGNORECASE):
        is_disaster = True
    elif base in project_info and project_info[base]['disaster']:
        is_disaster = True
        
    # Started 2022?
    started_2022 = False
    if base in project_info and project_info[base]['started_2022']:
        started_2022 = True
    
    # Check "2021 Annual Street Maintenance" exclusion explicitly
    if "2021" in base and "Annual" in base:
        started_2022 = False
        
    if is_disaster and started_2022:
        final_projects.add(raw_name)
        total_amount += int(row['Amount'])

print("__RESULT__:")
print(json.dumps({'total_funding': total_amount, 'projects': list(final_projects)}))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}, 'var_function-call-2894122064455046474': ['HEADER: Malibu Park Drainage Improvements', '', '(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview', 'Avenue. This project is scheduled to be accepted by the Council at the', 'January 24, 2022 meeting.', '', 'Clover Heights Storm Drain (FEMA Project)', '', '(cid:190) Project Description: This project consists of design and construction of a few', 'storm drains on Clover Heights. The existing storm drain facility ends at the', 'intersection of Clover Heights and Harvester Road. During storms, this', 'intersection floods and causes debris to block the road. An extended storm', 'drain towards the end of Clover Heights will help eliminate this issue.', '', '(cid:190) Updates:', '', '(cid:131) Staff is currently preparing consultant proposals for the design of this', '', 'project. Proposals will be due in February/March.'], 'var_function-call-12702603295060938783': ['HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project is scheduled to be accepted by the Council', 'at the January 24, 2022 meeting.', '', 'HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project was accepted by the Council at the January', '24, 2022 meeting.', ''], 'var_function-call-3103396639481338997': ['HEADER: Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'HEADER: Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', 'is finalizing the bid documents.'], 'var_function-call-12570495032935847245': ['--- Document: malibucity_agenda_03222023-2060.txt ---', 'Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '...', '--- Document: malibucity_agenda__01262022-1835.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', '...', '--- Document: malibucity_agenda__01272021-1626.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of the project.', '', '...', '--- Document: malibucity_agenda__03022021-1648.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of the project.', '', '...', '--- Document: malibucity_agenda__03232022-1869.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', '...']}

exec(code, env_args)
