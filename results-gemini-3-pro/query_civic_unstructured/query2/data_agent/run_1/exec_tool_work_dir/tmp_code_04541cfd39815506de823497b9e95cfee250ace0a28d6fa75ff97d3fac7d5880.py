code = """import json
import re

# Load data
with open(locals()['var_function-call-11007729145767623025'], 'r') as f:
    funding_data = json.load(f)
with open(locals()['var_function-call-2656858989978563996'], 'r') as f:
    civic_docs_data = json.load(f)

# Process Funding
project_funding = {}
for record in funding_data:
    p_name = record['Project_Name']
    if p_name in project_funding:
        project_funding[p_name] += int(record['Amount'])
    else:
        project_funding[p_name] = int(record['Amount'])

project_names = list(project_funding.keys())
total_text = chr(10).join([doc['text'] for doc in civic_docs_data])

def find_projects(text, p_names):
    occurrences = []
    for p_name in p_names:
        start = 0
        while True:
            idx = text.find(p_name, start)
            if idx == -1:
                break
            occurrences.append((idx, p_name))
            start = idx + len(p_name)
    occurrences.sort()
    segments = []
    for i in range(len(occurrences)):
        start, name = occurrences[i]
        end = occurrences[i+1][0] if i+1 < len(occurrences) else len(text)
        segments.append((name, text[start:end]))
    return segments

segments = find_projects(total_text, project_names)

debug_matches = []
completed_projects = set()

for p_name, segment in segments:
    if 'park' in p_name.lower():
        match = re.search(r'completed.{0,50}2022', segment, re.IGNORECASE)
        if match:
            completed_projects.add(p_name)
            s = match.start()
            e = match.end()
            snippet = segment[max(0, s-20):min(len(segment), e+20)]
            snippet = snippet.replace(chr(10), ' ')
            debug_matches.append({'name': p_name, 'match': match.group(0), 'snippet': snippet})

print("__RESULT__:")
print(json.dumps({'debug': debug_matches}))"""

env_args = {'var_function-call-4881455227376236038': ['civic_docs'], 'var_function-call-4881455227376238215': ['Funding'], 'var_function-call-11007729145767623596': 'file_storage/function-call-11007729145767623596.json', 'var_function-call-11007729145767623025': 'file_storage/function-call-11007729145767623025.json', 'var_function-call-12661878134790433858': 'file_storage/function-call-12661878134790433858.json', 'var_function-call-2656858989978563996': 'file_storage/function-call-2656858989978563996.json', 'var_function-call-3675807921624241983': {'total': 118000, 'projects': ['Permanent Skate Park', 'Bluffs Park Shade Structure'], 'debug': ['Bluffs Park Shade Structure', 'Permanent Skate Park', 'Permanent Skate Park']}}

exec(code, env_args)
