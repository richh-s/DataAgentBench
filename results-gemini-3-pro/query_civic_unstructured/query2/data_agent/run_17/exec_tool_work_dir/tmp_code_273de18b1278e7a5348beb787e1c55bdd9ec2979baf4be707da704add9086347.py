code = """import json
import re

with open(locals()['var_function-call-10057184920144794313'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-10057184920144796126'], 'r') as f:
    civic_docs = json.load(f)

qualifying_projects = set()
construction_completed_re = re.compile(r'(construction\s+was\s+completed|complete\s+construction)[:\s\w,]*?(\d{4})', re.IGNORECASE | re.DOTALL)

for project in funding_data:
    p_name = project['Project_Name']
    p_amount = int(project['Amount'])
    
    # Check park keywords in name
    name_lower = p_name.lower()
    tokens = re.split(r'[^a-z0-9]', name_lower)
    is_park = "park" in tokens or "playground" in tokens
    
    if is_park:
        completed_2022 = False
        for doc in civic_docs:
            text = doc['text']
            # Find all occurrences in this doc? Or just presence?
            # A doc might mention it multiple times.
            # Let's search for the name.
            idx = text.find(p_name)
            while idx != -1:
                context = text[idx:idx+800] # Get generous context
                
                match = construction_completed_re.search(context)
                if match:
                    year = match.group(2)
                    if year == "2022":
                        completed_2022 = True
                
                if completed_2022: break
                
                # Find next occurrence in same doc
                idx = text.find(p_name, idx + 1)
            
            if completed_2022: break
        
        if completed_2022:
            qualifying_projects.add((p_name, p_amount))

total_funding = sum(amount for _, amount in qualifying_projects)

print("__RESULT__:")
print(json.dumps({"total": total_funding, "projects": list(qualifying_projects)}))"""

env_args = {'var_function-call-10057184920144794313': 'file_storage/function-call-10057184920144794313.json', 'var_function-call-10057184920144796126': 'file_storage/function-call-10057184920144796126.json', 'var_function-call-16463367332335965304': {'total_funding': 0, 'projects': [], 'debug': []}, 'var_function-call-12562812388912151187': {'found': True, 'context': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi'}, 'var_function-call-4420774818653847510': {'total_funding': 0, 'projects': [], 'logs': ['Checking Bluffs Park Shade Structure, is_park=False', 'Found completion in doc: Construction was completed November 2022', 'Failed to qualify. Found in docs: True, Completed 2022: True']}, 'var_function-call-15478542269899668790': {'name': 'Bluffs Park Shade Structure', 'match': 'None', 'bool': False}, 'var_function-call-5050739371739425431': {'total_funding': 21000, 'projects': [['Bluffs Park Shade Structure', 21000]]}, 'var_function-call-5078256386249604020': [{'name': 'Bluffs Park Shade Structure', 'status': 'Completed', 'year': '2022'}, {'name': 'Bluffs Park Workout Station', 'status': 'Found', 'year': None}, {'name': 'Legacy Park Paver Repair Project', 'status': 'Found', 'year': None}, {'name': 'Malibu Bluffs Park South Walkway', 'status': 'Found', 'year': None}, {'name': 'Malibu Bluffs Park South Walkway Repairs', 'status': 'Found', 'year': None}, {'name': 'Malibu Park Drainage Improvements', 'status': 'Found', 'year': None}, {'name': 'Malibu Park Storm Drain Repairs', 'status': 'Found', 'year': None}, {'name': 'Permanent Skate Park', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Playground', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'status': 'Found', 'year': None}, {'name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'status': 'Found', 'year': None}, {'name': 'Trancas Playground Resurfacing', 'status': 'Found', 'year': None}], 'var_function-call-758903624864135206': {'Bluffs Park Workout Station': 'Bluffs Park Workout Station  (cid:190) Updates: The contractor is waiting for the delivery of the new workout  station equipment.  (cid:190) Project Schedule: November 2020 – March 2021  Civic Center Way Improvements  (cid:190) Updates:  (cid:131) Work Hours: Monday through Friday 7:00AM to 4:00PM, Saturdays  7:00AM to 4:00PM  (cid:131) The contractor is currently working at the section between Vista Pacifica and the condos on Civic Center Way. This phase of work will require the temporary closu', 'Legacy Park Paver Repair Project': 'Legacy Park Paver Repair Project  (cid:190) Project Description: This project will consist of removing and repairing a large section of pavers in Legacy Park. The pavers have become uneven and damaged in several areas  Malibu Bluffs Park South Walkway  (cid:190) Project Description: This project will include replacing the existing sidewalk  located on the south side of Malibu Bluffs Park.  Trancas Playground Resurfacing  (cid:190) Project Description: The project will include removing and replac'}, 'var_function-call-1573118444026308391': {'Point Dume Walkway Repairs': 'Point Dume Walkway Repairs (cid:190) Updates:  (cid:131) Construction was completed, November 2022 (cid:131) Notice of completion filed January 2023  Capital Improvement Projects (Not Started)  PCH Median Improvements at Paradise Cove and Zuma Beach  (cid:190) Project Description: This project was identified in the 2015 PCH Safety Study and includes installing new raised medians and improvements. New raised medians are proposed east and west of PCH and Paradise Cove Road. The proposed improvemen'}}

exec(code, env_args)
