code = """import json
import re

with open(locals()['var_function-call-2661118915962742960'], 'r') as f:
    civic_docs = json.load(f)

check_projects = [
    "Legacy Park Paver Repair Project",
    "Legacy Park Benches and Arbors Renovation",
    "Malibu Bluffs Park Roof Replacement Project",
    "Malibu Park Resurfacing Project"
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

env_args = {'var_function-call-2661118915962742960': 'file_storage/function-call-2661118915962742960.json', 'var_function-call-2661118915962742543': 'file_storage/function-call-2661118915962742543.json', 'var_function-call-16651809271219312034': {'total_funding': 21000, 'projects': ['Bluffs Park Shade Structure']}}

exec(code, env_args)
