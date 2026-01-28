code = """import json

with open(locals()['var_function-call-2661118915962742960'], 'r') as f:
    civic_docs = json.load(f)

check_projects = [
    "Trancas Canyon Park Playground",
    "Permanent Skate Park",
    "Bluffs Park Workout Station"
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

env_args = {'var_function-call-2661118915962742960': 'file_storage/function-call-2661118915962742960.json', 'var_function-call-2661118915962742543': 'file_storage/function-call-2661118915962742543.json', 'var_function-call-16651809271219312034': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}, 'var_function-call-13865229525523709225': [{'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}, {'project': 'Legacy Park Paver Repair Project', 'snippet': 'Legacy Park Paver Repair Project\n\n(cid:190) Project Description: This project will consist of removing and repairing a large\nsection of pavers in Legacy Park. The pavers have become uneven and\ndamaged in several areas\n\nMalibu Bluffs Park South Walkway\n\n(cid:190) Project Description: This project will include replacing the existing sidewalk\n\nlocated on the south side of Malibu Bluffs Park.\n\nTrancas'}]}

exec(code, env_args)
