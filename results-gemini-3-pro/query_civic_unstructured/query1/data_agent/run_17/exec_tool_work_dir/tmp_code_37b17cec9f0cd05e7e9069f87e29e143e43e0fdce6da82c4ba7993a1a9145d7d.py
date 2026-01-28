code = """import json

# Load funding data
with open(locals()['var_function-call-16838995843230881233'], 'r') as f:
    funding_data = json.load(f)

# Filter for > 50000 (already done in SQL, but just to be sure/consistent)
high_funding_projects = {item['Project_Name'] for item in funding_data if float(item['Amount']) > 50000}

# Load civic docs
with open(locals()['var_function-call-13293051466899965091'], 'r') as f:
    civic_docs = json.load(f)

# Section headers
target_header = "Capital Improvement Projects (Design)"
other_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects",
    "Disaster Recovery Projects (Design)",
    "Disaster Recovery Projects (Construction)",
    "Disaster Recovery Projects (Not Started)"
]

found_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all occurrences of the target header (though usually one per doc)
    start_idx = text.find(target_header)
    while start_idx != -1:
        # Determine the end of this section
        section_start = start_idx + len(target_header)
        section_end = len(text)
        
        # Find the nearest next header
        for header in other_headers:
            idx = text.find(header, section_start)
            if idx != -1 and idx < section_end:
                section_end = idx
        
        section_text = text[section_start:section_end]
        
        # Check for projects in this section
        for project in high_funding_projects:
            if project in section_text:
                found_projects.add(project)
        
        # Look for next occurrence of target header
        start_idx = text.find(target_header, section_start)

result = len(found_projects)
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16838995843230881233': 'file_storage/function-call-16838995843230881233.json', 'var_function-call-16838995843230880788': 'file_storage/function-call-16838995843230880788.json', 'var_function-call-13293051466899965091': 'file_storage/function-call-13293051466899965091.json'}

exec(code, env_args)
