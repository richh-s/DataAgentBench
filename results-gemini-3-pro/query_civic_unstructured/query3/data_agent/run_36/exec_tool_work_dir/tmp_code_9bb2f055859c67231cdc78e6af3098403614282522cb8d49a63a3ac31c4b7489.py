code = """import json

with open(locals()['var_function-call-15070344879824368069'], 'r') as f:
    civic_docs = json.load(f)

text = civic_docs[0]['text']
indices = []
start = 0
while True:
    idx = text.find("Disaster Recovery Projects", start)
    if idx == -1: break
    indices.append(idx)
    start = idx + 1

snippets = []
for i in indices:
    snippets.append(text[i:i+300])

print("__RESULT__:")
print(json.dumps(snippets))"""

env_args = {'var_function-call-18371054564754366390': 'file_storage/function-call-18371054564754366390.json', 'var_function-call-18371054564754362375': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_function-call-15070344879824368496': 'file_storage/function-call-15070344879824368496.json', 'var_function-call-15070344879824368069': 'file_storage/function-call-15070344879824368069.json', 'var_function-call-2633647079085397024': [], 'var_function-call-8767218630817718124': {'parsed_count': 45, 'sample_parsed': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'or phasing out the project', 'Westward Beach Road Repair Project'], 'funding_count': 500, 'sample_funding': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements']}, 'var_function-call-9458519939930987624': [], 'var_function-call-7913651078523279337': {'parsed_fema_related': ['Outdoor Warning Signs'], 'funding_fema_related': ['Birdview Avenue Improvements (FEMA/CalOES Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)']}, 'var_function-call-4055307384925035367': 'Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor pha'}

exec(code, env_args)
