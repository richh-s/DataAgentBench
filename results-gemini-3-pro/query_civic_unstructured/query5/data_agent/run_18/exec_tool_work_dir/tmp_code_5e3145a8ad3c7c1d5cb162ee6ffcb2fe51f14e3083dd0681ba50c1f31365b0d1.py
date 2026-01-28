code = """import json

with open(locals()['var_function-call-6099601671334015320'], 'r') as f:
    civic_docs = json.load(f)

target = "Broad Beach Road Water Quality"
res = []

for doc in civic_docs:
    if target in doc['text']:
        res.append(f"--- Document: {doc['filename']} ---")
        lines = doc['text'].splitlines()
        for i, line in enumerate(lines):
            if target in line:
                res.append(line)
                # print next few lines
                for j in range(1, 6):
                    if i+j < len(lines):
                        res.append(lines[i+j])
                res.append("...")

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-18312166134834260107': 'file_storage/function-call-18312166134834260107.json', 'var_function-call-6099601671334015320': 'file_storage/function-call-6099601671334015320.json', 'var_function-call-9845122995383564769': 'file_storage/function-call-9845122995383564769.json', 'var_function-call-6347418710872321306': {'total_funding': 209000, 'matched_projects': ['2021 Annual Street Maintenance', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Malibu Park Drainage Improvements']}, 'var_function-call-2894122064455046474': ['HEADER: Malibu Park Drainage Improvements', '', '(cid:190) Updates: The Contractor completed the repairs to storm drains on Cuthbert', 'Road, Morning View Drive, Busch Drive, Harvester Road and Birdview', 'Avenue. This project is scheduled to be accepted by the Council at the', 'January 24, 2022 meeting.', '', 'Clover Heights Storm Drain (FEMA Project)', '', '(cid:190) Project Description: This project consists of design and construction of a few', 'storm drains on Clover Heights. The existing storm drain facility ends at the', 'intersection of Clover Heights and Harvester Road. During storms, this', 'intersection floods and causes debris to block the road. An extended storm', 'drain towards the end of Clover Heights will help eliminate this issue.', '', '(cid:190) Updates:', '', '(cid:131) Staff is currently preparing consultant proposals for the design of this', '', 'project. Proposals will be due in February/March.'], 'var_function-call-12702603295060938783': ['HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project is scheduled to be accepted by the Council', 'at the January 24, 2022 meeting.', '', 'HEADER: 2021 Annual Street Maintenance', '', '(cid:190) Updates: This project included resurfacing Malibu Road, Broad Beach Road,', 'Latigo Canyon Road, Corral Canyon Road, Webb Way, Rambla Pacifico', 'Street and Vista Pacifica with a slurry seal treatment and adding speed', 'humps to Birdview Avenue. This project was identified in the City’s Pavement', 'Management Plan. This project was accepted by the Council at the January', '24, 2022 meeting.', ''], 'var_function-call-3103396639481338997': ['HEADER: Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'HEADER: Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant prepared the specifications for the project. Staff', '', 'is finalizing the bid documents.']}

exec(code, env_args)
