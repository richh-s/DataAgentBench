code = """import json
import re

funding_path = locals()['var_function-call-2809487722948638107']
civic_docs_path = locals()['var_function-call-2809487722948637720']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

project_names = set(item['Project_Name'] for item in funding_data)
sorted_project_names = sorted(list(project_names), key=len, reverse=True)

target_projects = ["Permanent Skate Park", "Bluffs Park Shade Structure"]

print("__RESULT__:")
results = []

for doc in civic_docs:
    text = doc['text']
    found_projects = []
    for name in sorted_project_names:
        start = 0
        while True:
            idx = text.find(name, start)
            if idx == -1: break
            found_projects.append((idx, name))
            start = idx + len(name)
    found_projects.sort(key=lambda x: x[0])
    
    for i in range(len(found_projects)):
        start_idx, name = found_projects[i]
        if name in target_projects:
            if i + 1 < len(found_projects):
                end_idx = found_projects[i+1][0]
            else:
                end_idx = len(text)
            segment = text[start_idx:end_idx]
            # Clean up newlines for printing
            clean_segment = segment.replace('\n', ' ')
            results.append(f"Project: {name} | Segment: {clean_segment[:200]}...")

print(json.dumps(results))"""

env_args = {'var_function-call-2809487722948638107': 'file_storage/function-call-2809487722948638107.json', 'var_function-call-2809487722948637720': 'file_storage/function-call-2809487722948637720.json', 'var_function-call-2577172791415288121': {'total_funding': 118000, 'projects': [{'name': 'Permanent Skate Park', 'amount': 97000}, {'name': 'Bluffs Park Shade Structure', 'amount': 21000}]}}

exec(code, env_args)
