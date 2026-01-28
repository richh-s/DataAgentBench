code = """import json
import re

# Load funding results
with open(locals()['var_function-call-2470903467818453572'], 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set(item['Project_Name'].strip() for item in funding_data)

# Load civic docs
with open(locals()['var_function-call-1752816955858049091'], 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Locate section
    start_match = re.search(r'Capital Improvement Projects\s*\(Design\)', text, re.IGNORECASE)
    if not start_match:
        continue
    
    start_index = start_match.end()
    
    # End section
    end_match = re.search(r'Capital Improvement Projects\s*\((?:Construction|Not Started)\)|Disaster Recovery Projects', text[start_index:], re.IGNORECASE)
    
    if end_match:
        end_index = start_index + end_match.start()
        section_text = text[start_index:end_index]
    else:
        section_text = text[start_index:]
        
    lines = [line.strip() for line in section_text.split('\n') if line.strip()]
    
    for i in range(len(lines) - 1):
        current_line = lines[i]
        next_line = lines[i+1]
        
        # Check markers
        # Using specific strings
        is_detail_start = next_line.startswith('(cid:') or \
                          'Updates:' in next_line or \
                          'Project Description:' in next_line or \
                          'Project Schedule:' in next_line
                          
        is_noise = current_line.startswith('Page ') or \
                   current_line.startswith('Agenda Item') or \
                   current_line.startswith('(cid:')
                   
        if is_detail_start and not is_noise:
            p_name = current_line.strip()
            # Clean up potential leading/trailing non-alphanum if necessary, but keep it simple
            capital_design_projects.add(p_name)

matched_projects = []
for p in capital_design_projects:
    if p in high_funding_projects:
        matched_projects.append(p)

result = {
    "extracted_capital_design_projects": list(capital_design_projects),
    "matched_projects": matched_projects,
    "count": len(matched_projects)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-2470903467818453572': 'file_storage/function-call-2470903467818453572.json', 'var_function-call-1752816955858049091': 'file_storage/function-call-1752816955858049091.json'}

exec(code, env_args)
