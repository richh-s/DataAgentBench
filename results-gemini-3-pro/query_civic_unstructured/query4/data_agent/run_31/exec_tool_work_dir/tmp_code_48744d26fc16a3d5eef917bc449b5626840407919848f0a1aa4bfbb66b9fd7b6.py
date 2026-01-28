code = """import json

path_funding = locals()['var_function-call-8803859908455603463']
with open(path_funding, 'r') as f:
    funding_data = json.load(f)

valid_names = set(x['Project_Name'] for x in funding_data)
latigo_names = [n for n in valid_names if "Latigo" in n]

print('__RESULT__:')
print(json.dumps(latigo_names))"""

env_args = {'var_function-call-6062983773300407174': ['civic_docs'], 'var_function-call-8587075472335102739': 'file_storage/function-call-8587075472335102739.json', 'var_function-call-4603789047444994898': ['Funding'], 'var_function-call-8803859908455603463': 'file_storage/function-call-8803859908455603463.json', 'var_function-call-4031632959131545213': ['scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'damaged by the Woolsey Fire.', 'beginning in April 2022.', 'March 2022', 'beginning in Spring 2022.', '(cid:131) The project consultant has started the design of this project.', 'assessment district will be created.', 'advertised for construction bids shortly after this date.', 'timber with non-combustible materials.', 'Fire.', '(cid:131) Next public community meeting is scheduled for March 25th.', 'is finalizing the bid documents.', 'that was damaged by the Woolsey Fire.', 'Metro.'], 'var_function-call-2765771842290335904': [], 'var_function-call-1028562691190283738': 'Done', 'var_function-call-2831729942517060244': {'db_names_sample': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements'], 'marker_count': 268, 'snippet': 'mer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have been completed\n(cid:131) Awaiting final FEMA/CalOES approval for scope modification\n\n(cid:'}}

exec(code, env_args)
