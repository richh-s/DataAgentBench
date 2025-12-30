code = """import json

funding_path = locals()['var_function-call-5441404039575521335']
docs_path = locals()['var_function-call-5441404039575519310']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for item in funding_data:
    try:
        if int(item['Amount']) > 50000:
            high_funding_projects.add(item['Project_Name'].strip())
    except:
        continue

with open(docs_path, 'r') as f:
    docs = json.load(f)

target_header = "Capital Improvement Projects (Design)"
stop_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

extracted_projects = set()

for doc in docs:
    text = doc['text']
    start_idx = text.find(target_header)
    if start_idx == -1:
        continue
    
    content_start = start_idx + len(target_header)
    end_idx = len(text)
    
    for stop in stop_headers:
        idx = text.find(stop, content_start)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_content = text[content_start:end_idx]
    
    lines = section_content.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Check for bullets (cid:190) etc or dates/pages
        if line.startswith('(') or line.startswith('Page') or line.startswith('Agenda'):
            continue
        if "Updates:" in line or "Project Schedule:" in line:
            continue
            
        extracted_projects.add(line)

matches = []
for proj in extracted_projects:
    if proj in high_funding_projects:
        matches.append(proj)

result = {
    "count": len(matches),
    "matches": matches,
    "extracted_sample": list(extracted_projects)[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-5441404039575521335': 'file_storage/function-call-5441404039575521335.json', 'var_function-call-5441404039575519310': 'file_storage/function-call-5441404039575519310.json'}

exec(code, env_args)
