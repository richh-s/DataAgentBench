code = """import json

with open(locals()['var_function-call-2661118915962742960'], 'r') as f:
    civic_docs = json.load(f)

check_projects = [
    "Legacy Park Benches and Arbors Renovation"
]

results = []
for doc in civic_docs:
    text = doc['text']
    for proj in check_projects:
        if proj in text:
            idx = text.find(proj)
            snippet = text[idx:idx+400]
            results.append({
                "project": proj,
                "snippet": snippet
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2661118915962742960': 'file_storage/function-call-2661118915962742960.json', 'var_function-call-2661118915962742543': 'file_storage/function-call-2661118915962742543.json', 'var_function-call-16651809271219312034': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-13865229525523709225': [{'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}, {'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}], 'var_function-call-16357069807311124111': [{'project': 'Trancas Canyon Park Playground', 'snippet': 'Trancas Canyon Park Playground\n(cid:190) Updates:\n\n(cid:131) Staff is currently working on the final design plans\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n\nMalibu Canyon Road Traffic Study\n\n(cid:190) Project Description: This project will consist of a traffic study on Malibu\nCanyon Road near Harbor Vista Drive and Potter Lane to determ'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2023\n(cid:131) Begin Construction: Winter 2024\n\nPCH at Trancas Canyon Road Right Turn Lane\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to Caltrans for review and expecting comments in\n\nthe Sp'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes the designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for addit'}, {'project': 'Bluffs Park Workout Station', 'snippet': 'Bluffs Park Workout Station\n\n(cid:190) Updates: The contractor is waiting for the delivery of the new workout\n\nstation equipment.\n\n(cid:190) Project Schedule: November 2020 – March 2021\n\nCivic Center Way Improvements\n\n(cid:190) Updates:\n\n(cid:131) Work Hours: Monday through Friday 7:00AM to 4:00PM, Saturdays\n\n7:00AM to 4:00PM\n\n(cid:131) The contractor is currently working at the section between Vi'}, {'project': 'Bluffs Park Workout Station', 'snippet': 'Bluffs Park Workout Station\n\n(cid:190) Updates: The contractor is waiting for the delivery of the new workout\nstation equipment. The equipment is anticipated to be delivered at the end\nof February.\n\n(cid:190) Project Schedule: November 2020 – March 2021\n\nCivic Center Way Improvements\n\n(cid:190) Updates:\n\n(cid:131) Work Hours: Monday through Friday 7:00AM to 4:00PM, Saturdays\n\n7:00AM to 4:00PM\n\n(ci'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for additiona'}]}

exec(code, env_args)
