code = """import json

path_docs = locals()['var_function-call-8587075472335102739']
with open(path_docs, 'r') as f:
    docs = json.load(f)

for doc in docs:
    if "Bluffs Park Shade Structure" in doc['text']:
        lines = doc['text'].splitlines()
        for i, line in enumerate(lines):
            if "Bluffs Park Shade Structure" in line:
                # print context
                # check next 20 lines for Spring 2022 match
                for j in range(i, min(i+30, len(lines))):
                    l_low = lines[j].lower()
                    if ('spring 2022' in l_low or 'march 2022' in l_low or 'april 2022' in l_low or 'may 2022' in l_low) and \
                       ('begin' in l_low or 'start' in l_low or 'commence' in l_low):
                           print(f"Match found in: {lines[j]}")"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json', 'var_function-call-4031632959131545213': ['scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'damaged by the Woolsey Fire.', 'beginning in April 2022.', 'March 2022', 'beginning in Spring 2022.', '(cid:131) The project consultant has started the design of this project.', 'assessment district will be created.', 'advertised for construction bids shortly after this date.', 'timber with non-combustible materials.', 'Fire.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'is finalizing the bid documents.', 'that was damaged by the Woolsey Fire.', 'Metro.'], 'var_function-call-2765771842290335904': [], 'var_function-call-1028562691190283738': 'Done', 'var_function-call-2831729942517060244': {'db_names_sample': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements'], 'marker_count': 268, 'snippet': 'mer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:'}, 'var_function-call-12524213056519618730': ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)'], 'var_function-call-10233603179972647313': ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'PCH at Trancas Canyon Road Right Turn Lane', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Civic Center Water Treatment Facility Phase 2', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Marie Canyon Green Streets'], 'var_function-call-17771196675504247720': {'count': 10, 'total_funding': 1202000, 'projects': ['PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Culvert Repairs', 'Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Trancas Canyon Park Slope Stabilization Project', 'Marie Canyon Green Streets', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Civic Center Water Treatment Facility Phase 2', 'Encinal Canyon Road Drainage Improvements']}}

exec(code, env_args)
