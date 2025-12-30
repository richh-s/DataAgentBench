code = """import json

with open(locals()['var_function-call-6964896026869671245'], 'r') as f:
    civic_docs = json.load(f)

full_text = chr(10).join([doc['text'] for doc in civic_docs])

park_projects = [
    "Bluffs Park Workout Station",
    "Legacy Park Benches and Arbors Renovation",
    "Legacy Park Paver Repair Project",
    "Malibu Bluffs Park Roof Replacement Project",
    "Malibu Bluffs Park South Walkway",
    "Malibu Park Drainage Improvements",
    "Malibu Park Resurfacing Project",
    "Malibu Park Storm Drain Repairs",
    "Trancas Canyon Park Planting and Irrigation Repairs",
    "Trancas Canyon Park Slope Stabilization Project"
]

results = {}
for name in park_projects:
    idx = full_text.find(name)
    if idx != -1:
        results[name] = full_text[idx:idx+400].replace(chr(10), " ")
    else:
        results[name] = "Not Found in Text"

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6964896026869671245': 'file_storage/function-call-6964896026869671245.json', 'var_function-call-16721484954554461294': ['Funding'], 'var_function-call-867828661549977430': 'file_storage/function-call-867828661549977430.json', 'var_function-call-7895803557599904901': {'total_funding': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}, 'var_function-call-15919782058148255785': {'Permanent Skate Park': 'Permanent Skate Park\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2023\n(cid:131) Begin Construction: Winter 2024\n\nPCH at Trancas Canyon Road Right Turn Lane\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to Caltrans for review and expecting comments in\n\nthe Spring 2023.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Fall 2023\n(cid:131) Begin Cons', 'Bluffs Park Shade Structure': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi', 'Point Dume Walkway Repairs': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study\nand includes installing new raised medians and improvements. New raised\nmedians are proposed east and west of PCH and Paradise Cove Road. The\nproposed improvemen', 'Broad Beach Road Water Quality Repair': 'Broad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoint Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study'}, 'var_function-call-12275065709945997960': {'total_funding': 21000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000, 'reason': 'Found park and construction completed 2022'}]}}

exec(code, env_args)
