code = """import json
import re

# Load funding data
with open(locals()['var_function-call-16838995843230881233'], 'r') as f:
    funding_data = json.load(f)

# Filter for > 50000
high_funding_projects = {item['Project_Name'] for item in funding_data if float(item['Amount']) > 50000}

# Load civic docs
with open(locals()['var_function-call-13293051466899965091'], 'r') as f:
    civic_docs = json.load(f)

target_header = "Capital Improvement Projects (Design)"
other_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects" # Covers all disaster recovery subsections if they start with this
]

found_projects = set()

def normalize(s):
    return " ".join(s.split())

for doc in civic_docs:
    text = doc.get('text', '')
    
    start_idx = text.find(target_header)
    while start_idx != -1:
        section_start = start_idx + len(target_header)
        section_end = len(text)
        
        for header in other_headers:
            idx = text.find(header, section_start)
            if idx != -1 and idx < section_end:
                section_end = idx
        
        section_text = text[section_start:section_end]
        normalized_section_text = normalize(section_text)
        
        for project in high_funding_projects:
            # Check normalized project name against normalized section text
            # This handles line breaks in the document text
            if normalize(project) in normalized_section_text:
                found_projects.add(project)
        
        start_idx = text.find(target_header, section_start)

print("__RESULT__:")
print(json.dumps(list(found_projects)))"""

env_args = {'var_function-call-16838995843230881233': 'file_storage/function-call-16838995843230881233.json', 'var_function-call-16838995843230880788': 'file_storage/function-call-16838995843230880788.json', 'var_function-call-13293051466899965091': 'file_storage/function-call-13293051466899965091.json', 'var_function-call-16442694046434714773': 12}

exec(code, env_args)
