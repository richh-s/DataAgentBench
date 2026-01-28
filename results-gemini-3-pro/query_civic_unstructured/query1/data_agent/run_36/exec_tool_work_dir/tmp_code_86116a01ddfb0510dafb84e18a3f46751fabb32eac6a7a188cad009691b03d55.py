code = """import json

p1 = locals()["var_function-call-5247396609485473632"]
with open(p1, "r") as f:
    funding_list = json.load(f)

# Filter > 50000
valid_funding_names = set()
for x in funding_list:
    try:
        if float(x['Amount']) > 50000:
            valid_funding_names.add(x['Project_Name'].strip().lower())
    except:
        pass

p2 = locals()["var_function-call-633765740054289148"]
with open(p2, "r") as f:
    dl = json.load(f)

# Get latest doc content
latest_filename = "malibucity_agenda_03222023-2060.txt"
target_doc = None
for d in dl:
    if d["filename"] == latest_filename:
        target_doc = d
        break

found_projects = set()

if target_doc:
    lines = target_doc['text'].splitlines()
    mode = 0 # 0: none, 1: design
    
    for l in lines:
        lc = l.strip().lower()
        if not lc: continue
        
        if "capital improvement projects (design)" in lc:
            mode = 1
            continue
        if "capital improvement projects" in lc and "(design)" not in lc:
            mode = 0
            continue
        if "disaster recovery projects" in lc:
            mode = 0
            continue
            
        if mode == 1:
            if lc in valid_funding_names:
                found_projects.add(lc)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-5247396609485473632': 'file_storage/function-call-5247396609485473632.json', 'var_function-call-633765740054289148': 'file_storage/function-call-633765740054289148.json', 'var_function-call-9077877662949363263': ['malibu canyon road traffic study', 'civic center stormwater diversion structure', 'pch median improvements project', 'westward beach road drainage improvements project', 'latigo canyon road retaining wall repair project', 'malibu bluffs park south walkway repairs', 'pch at trancas canyon road right turn lane', 'outdoor warning signs', 'permanent skate park', 'storm drain master plan'], 'var_function-call-15990990681837136322': [], 'var_function-call-17594359016080085678': [{'Project_Name': 'Clover Heights Storm Drain', 'Amount': '53000'}], 'var_function-call-8434699775002976394': [{'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 343, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 327, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'index': 317, 'context': ['(cid:190) Project Schedule', '', '(cid:131) Complete Design: Spring 2021', '(cid:131) Begin Construction: Summer 2021', '', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}, {'line': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'index': 371, 'context': ['', '', '', '', '', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', '', '(cid:190) Updates:', '', '(cid:131) The project consultant has started the design of this project.']}], 'var_function-call-3536160269563716772': ['Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Found in section: Not Started, Line: Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)'], 'var_function-call-9370289276184492999': [], 'var_function-call-10845941831033251560': ['Found in section: Construction, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Design, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Design, Line: Civic Center Stormwater Diversion Structure', 'Found in section: Construction, Line: Civic Center Stormwater Diversion Structure'], 'var_function-call-4048575078283089782': {'filename': 'malibucity_agenda_03222023-2060.txt', 'date': '20230322'}}

exec(code, env_args)
