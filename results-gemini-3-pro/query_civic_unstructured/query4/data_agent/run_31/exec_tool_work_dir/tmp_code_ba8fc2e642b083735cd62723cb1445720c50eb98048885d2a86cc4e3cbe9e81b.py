code = """import json

path_funding = locals()['var_function-call-8803859908455603463']
path_docs = locals()['var_function-call-8587075472335102739']

with open(path_funding, 'r') as f:
    funding_data = json.load(f)

with open(path_docs, 'r') as f:
    docs = json.load(f)

valid_names = set(x['Project_Name'] for x in funding_data)
marker = 'cid:190'
bullet = 'cid:131'

identified = []

for doc in docs:
    lines = doc['text'].splitlines()
    curr_name = None
    buf = []
    
    for line in lines:
        s = line.strip()
        if not s: continue
        
        if marker in s:
            # Clean buf
            clean = []
            for b in buf:
                if 'Agenda' in b or 'Page ' in b or 'Public Works' in b or 'Capital Improvement' in b: continue
                if bullet in b: continue
                clean.append(b)
            
            if clean:
                cand = clean[-1]
                if cand in valid_names:
                    curr_name = cand
                else:
                    # Try joining last 2 lines
                    if len(clean) >= 2:
                        cand2 = clean[-2] + " " + clean[-1]
                        if cand2 in valid_names:
                            curr_name = cand2
            buf = []
        else:
            buf.append(s)
            if curr_name:
                low = s.lower()
                # Check for Spring 2022
                is_spring = False
                if 'spring 2022' in low: is_spring = True
                if 'march 2022' in low: is_spring = True
                if 'april 2022' in low: is_spring = True
                if 'may 2022' in low: is_spring = True
                
                if is_spring:
                    # Check for start phase
                    # "Begin Construction", "Start", "Commence"
                    # What if it says "Project Start: Spring 2022"?
                    # "Estimated Schedule: ... Start: Spring 2022"
                    if 'begin' in low or 'start' in low or 'commence' in low:
                        identified.append(curr_name)

final_list = list(set(identified))
print('__RESULT__:')
print(json.dumps(final_list))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json', 'var_function-call-4031632959131545213': ['scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'damaged by the Woolsey Fire.', 'beginning in April 2022.', 'March 2022', 'beginning in Spring 2022.', '(cid:131) The project consultant has started the design of this project.', 'assessment district will be created.', 'advertised for construction bids shortly after this date.', 'timber with non-combustible materials.', 'Fire.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'is finalizing the bid documents.', 'that was damaged by the Woolsey Fire.', 'Metro.'], 'var_function-call-2765771842290335904': [], 'var_function-call-1028562691190283738': 'Done', 'var_function-call-2831729942517060244': {'db_names_sample': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements'], 'marker_count': 268, 'snippet': 'mer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:'}, 'var_function-call-12524213056519618730': ['Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)']}

exec(code, env_args)
