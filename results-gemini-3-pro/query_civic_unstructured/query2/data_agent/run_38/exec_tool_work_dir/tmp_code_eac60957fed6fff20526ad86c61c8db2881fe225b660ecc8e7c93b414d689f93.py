code = """import json
import re

with open(locals()['var_function-call-2661118915962742960'], 'r') as f:
    civic_docs = json.load(f)

park_projects = [
    # Manually list some or just re-derive? Re-derive is safer.
    "Bluffs Park Shade Structure",
    "Legacy Park Benches and Arbors Renovation",
    "Legacy Park Paver Repair Project",
    "Malibu Bluffs Park Roof Replacement Project",
    "Malibu Bluffs Park South Walkway",
    "Malibu Bluffs Park South Walkway Repairs",
    "Malibu Park Drainage Improvements",
    "Malibu Park Resurfacing Project",
    "Malibu Park Storm Drain Repairs",
    "Permanent Skate Park",
    "Trancas Canyon Park Playground",
    "Trancas Canyon Park Upper and Lower Slopes Repair",
    "Bluffs Park Workout Station"
]

results = []

for doc in civic_docs:
    text = doc['text']
    for proj in park_projects:
        if proj in text:
            # Get snippets
            matches = [m.start() for m in re.finditer(re.escape(proj), text)]
            for start in matches:
                snippet = text[start:start+600].lower()
                # Check for 2022 and completion indicators
                if '2022' in snippet and ('completed' in snippet or 'completion' in snippet or 'complete' in snippet):
                     results.append({
                         "project": proj,
                         "snippet": snippet
                     })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2661118915962742960': 'file_storage/function-call-2661118915962742960.json', 'var_function-call-2661118915962742543': 'file_storage/function-call-2661118915962742543.json', 'var_function-call-16651809271219312034': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-13865229525523709225': [{'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}, {'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}], 'var_function-call-16357069807311124111': [{'project': 'Trancas Canyon Park Playground', 'snippet': 'Trancas Canyon Park Playground\n(cid:190) Updates:\n\n(cid:131) Staff is currently working on the final design plans\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n\nMalibu Canyon Road Traffic Study\n\n(cid:190) Project Description: This project will consist of a traffic study on Malibu\nCanyon Road near Harbor Vista Drive and Potter Lane to determ'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2023\n(cid:131) Begin Construction: Winter 2024\n\nPCH at Trancas Canyon Road Right Turn Lane\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to Caltrans for review and expecting comments in\n\nthe Sp'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes the designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for addit'}, {'project': 'Bluffs Park Workout Station', 'snippet': 'Bluffs Park Workout Station\n\n(cid:190) Updates: The contractor is waiting for the delivery of the new workout\n\nstation equipment.\n\n(cid:190) Project Schedule: November 2020 – March 2021\n\nCivic Center Way Improvements\n\n(cid:190) Updates:\n\n(cid:131) Work Hours: Monday through Friday 7:00AM to 4:00PM, Saturdays\n\n7:00AM to 4:00PM\n\n(cid:131) The contractor is currently working at the section between Vi'}, {'project': 'Bluffs Park Workout Station', 'snippet': 'Bluffs Park Workout Station\n\n(cid:190) Updates: The contractor is waiting for the delivery of the new workout\nstation equipment. The equipment is anticipated to be delivered at the end\nof February.\n\n(cid:190) Project Schedule: November 2020 – March 2021\n\nCivic Center Way Improvements\n\n(cid:190) Updates:\n\n(cid:131) Work Hours: Monday through Friday 7:00AM to 4:00PM, Saturdays\n\n7:00AM to 4:00PM\n\n(ci'}, {'project': 'Permanent Skate Park', 'snippet': 'Permanent Skate Park\n\n(cid:190) Project Description: This project includes designing and constructing a\npermanent skate park located on the Crummer/Case Court parcel adjacent\nto Malibu Bluffs Park. The project would include parking and additional site\namenities such as trash cans, benches, tables, and restrooms.\n\n(cid:190) Updates:\n(cid:131)\n\nIn May 2021, the Council approved funding for additiona'}], 'var_function-call-5262641157031457708': []}

exec(code, env_args)
