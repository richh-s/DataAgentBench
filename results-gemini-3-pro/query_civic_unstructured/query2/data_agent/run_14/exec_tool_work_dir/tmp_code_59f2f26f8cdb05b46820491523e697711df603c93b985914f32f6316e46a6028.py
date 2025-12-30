code = """import json
import re

funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

all_text = ""
for d in civic_data:
    all_text += d.get('text', '') + ' '

total_funding = 0
confirmed_projects = []

for item in funding_data:
    p_name = item['Project_Name']
    amount = int(item['Amount'])
    
    # Check topic: park or playground
    name_lower = p_name.lower()
    if 'park' not in name_lower and 'playground' not in name_lower:
        continue

    # Normalize name for search (remove parens)
    # e.g. "Project (FEMA)" -> "Project"
    base_name = p_name.split('(')[0].strip()
    
    # Find all occurrences
    # search base_name in all_text
    matches = [m.start() for m in re.finditer(re.escape(base_name), all_text, re.IGNORECASE)]
    
    is_completed = False
    for start in matches:
        # Look at next 500 chars
        snippet = all_text[start:start+500].lower()
        
        # Criteria: 'completed' AND '2022'
        if 'completed' in snippet and '2022' in snippet:
            # Check for negative indicators
            if 'will be completed' in snippet or 'scheduled' in snippet or 'expected' in snippet:
                continue
            
            # Check for past tense indicators or direct statement
            if 'was completed' in snippet or 'construction completed' in snippet or 'has been completed' in snippet:
                is_completed = True
                break
            
            # Additional check: 'notice of completion filed ... 2023' implies completion in 2022 usually?
            # Text: "Construction was completed November 2022. Notice of completion filed January 2023"
            # This contains "completed November 2022".
            
            # If we see "completed, november 2022", that's good.
    
    if is_completed:
        total_funding += amount
        confirmed_projects.append(p_name)

print('__RESULT__:')
print(json.dumps({'confirmed_projects': confirmed_projects, 'total_funding': total_funding}))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json'}

exec(code, env_args)
