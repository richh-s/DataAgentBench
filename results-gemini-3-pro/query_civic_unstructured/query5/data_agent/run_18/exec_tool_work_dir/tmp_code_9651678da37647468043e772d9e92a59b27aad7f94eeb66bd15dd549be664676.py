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

project_info = {} 

for doc in civic_docs:
    lines = doc['text'].splitlines()
    current_proj = None
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
            
        found = None
        for base in funding_base_names:
            if base in line_clean and len(line_clean) < len(base) + 15:
                found = base
                break
        
        if found:
            current_proj = found
            if current_proj not in project_info:
                project_info[current_proj] = {'logs': []}
            continue
            
        if current_proj:
            if "2022" in line_clean:
                 project_info[current_proj]['logs'].append(line_clean)

# Check specific projects
targets = ["Latigo Canyon Road Roadway/Retaining Wall Improvements", "Annual Street Maintenance", "Malibu Park Drainage Improvements"]

res = {}
for t in targets:
    norm = normalize(t)
    if norm in project_info:
        res[t] = project_info[norm]['logs']

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}, 'var_function-call-2894122064455046474': ['HEADER: Malibu Park Drainage Improvements', '', '(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview', 'Avenue. This project is scheduled to be accepted by the Council at the', 'January 24, 2022 meeting.', '', 'Clover Heights Storm Drain (FEMA Project)', '', '(cid:190) Project Description: This project consists of design and construction of a few', 'storm drains on Clover Heights. The existing storm drain facility ends at the', 'intersection of Clover Heights and Harvester Road. During storms, this', 'intersection floods and causes debris to block the road. An extended storm', 'drain towards the end of Clover Heights will help eliminate this issue.', '', '(cid:190) Updates:', '', '(cid:131) Staff is currently preparing consultant proposals for the design of this', '', 'project. Proposals will be due in February/March.'], 'var_function-call-12702603295060938783': ['HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project is scheduled to be accepted by the Council', 'at the January 24, 2022 meeting.', '', 'HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project was accepted by the Council at the January', '24, 2022 meeting.', ''], 'var_function-call-3103396639481338997': ['HEADER: Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'HEADER: Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', 'is finalizing the bid documents.'], 'var_function-call-12570495032935847245': ['--- Document: malibucity_agenda_03222023-2060.txt ---', 'Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '...', '--- Document: malibucity_agenda__01262022-1835.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', '...', '--- Document: malibucity_agenda__01272021-1626.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of the project.', '', '...', '--- Document: malibucity_agenda__03022021-1648.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of the project.', '', '...', '--- Document: malibucity_agenda__03232022-1869.txt ---', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', '...'], 'var_function-call-4538539031030602187': {'total_funding': 396000, 'projects': ['Annual Street Maintenance', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Malibu Park Drainage Improvements', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs']}}

exec(code, env_args)
