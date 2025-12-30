code = """import json
import re

path_fund = locals()['var_function-call-9124692178282648902']
path_docs = locals()['var_function-call-10183875392572160973']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    high_funding_projects.add(record['Project_Name'].strip().lower())

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

extracted_names = []
debug_sections = []

section_start_regex = r"Capital Improvement Projects\s*\(Design\)"
# Be strict about the end. It should be the start of a line probably?
section_end_regex = r"(?:Capital Improvement Projects|Disaster Recovery Projects|Agenda Item)"

for doc in civic_docs:
    text = doc['text']
    parts = re.split(section_start_regex, text, flags=re.IGNORECASE)
    
    for i, part in enumerate(parts[1:]):
        # Find end
        end_match = re.search(section_end_regex, part, flags=re.IGNORECASE)
        if end_match:
            section_content = part[:end_match.start()]
            suffix = part[end_match.start():end_match.start()+50] # Debug what ended it
        else:
            section_content = part
            suffix = "EOF"
        
        if len(debug_sections) < 3:
            debug_sections.append({"content_start": section_content[:200], "ended_by": suffix})

        lines = section_content.splitlines()
        for j in range(len(lines) - 1):
            line = lines[j].strip()
            next_line = lines[j+1].strip()
            
            if not line:
                continue
            
            # Using partial match for bullet or keywords
            if 'Updates:' in next_line or 'Project Schedule' in next_line or 'cid:190' in next_line:
                extracted_names.append(line.lower())

print("__RESULT__:")
print(json.dumps({
    "extracted_sample": extracted_names[:10],
    "funding_sample": list(high_funding_projects)[:10],
    "debug_sections": debug_sections
}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json', 'var_function-call-5838596585415121062': {'count': 0, 'matches': [], 'extracted_example': ['marie canyon green streets']}}

exec(code, env_args)
