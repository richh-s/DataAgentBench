code = """import json
import re

with open(locals()['var_function-call-9124692178282648902'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    name = record['Project_Name'].strip().lower()
    high_funding_projects.add(name)

with open(locals()['var_function-call-10183875392572160973'], 'r') as f:
    civic_docs = json.load(f)

found_projects = set()

section_start_regex = r"Capital Improvement Projects\s*\(Design\)"
section_end_regex = r"(?:Capital Improvement Projects|Disaster Recovery Projects|Agenda Item)"

for doc in civic_docs:
    text = doc['text']
    parts = re.split(section_start_regex, text, flags=re.IGNORECASE)
    
    for part in parts[1:]:
        end_match = re.search(section_end_regex, part, flags=re.IGNORECASE)
        if end_match:
            section_content = part[:end_match.start()]
        else:
            section_content = part
        
        lines = section_content.split('\n')
        for i in range(len(lines) - 1):
            line = lines[i].strip()
            next_line = lines[i+1].strip()
            
            if not line:
                continue
            
            # Check keywords in next line that indicate the previous line was a header
            # "Updates:", "Project Schedule:", "Project Description:", or the bullet "cid:190"
            if "Updates:" in next_line or "cid:190" in next_line or "Project Schedule" in next_line:
                found_projects.add(line.lower())

count = 0
matches = []
for p in found_projects:
    # Exact match check
    if p in high_funding_projects:
        count += 1
        matches.append(p)
    else:
        # Check for fuzzy match
        # If p is "project x" and high_funding has "project x (something)"
        # or vice versa
        # The prompt says project names in SQLite match those extracted.
        # But let's be careful.
        pass

print("__RESULT__:")
print(json.dumps({"count": count, "matches": matches, "extracted_example": list(found_projects)[:5]}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json'}

exec(code, env_args)
