code = """import json
import re

# Load data
funding_path = locals()['var_function-call-13164751492978107468']
civic_path = locals()['var_function-call-9869211362583101527']

with open(funding_path, 'r') as f:
    funding_data = json.load(f)

with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Combine text from all docs
all_text = ""
for doc in civic_data:
    all_text += doc.get('text', '') + "\n\n"

total_funding = 0
confirmed_projects = []

for item in funding_data:
    p_name = item['Project_Name']
    p_amount = int(item['Amount'])
    
    # Check if park related
    # "park", "playground"
    if "park" not in p_name.lower() and "playground" not in p_name.lower():
        continue
        
    # Search for p_name in text
    # We use re.escape to handle special chars like parens in project names e.g. "(FEMA Project)"
    # But wait, the name in text might be "Bluffs Park Shade Structure" without the "(FEMA Project)" part?
    # The Funding DB has "Project Name (FEMA Project)". 
    # The text likely says "Project Name".
    # So we should match the base name.
    # Let's clean the project name by removing content in parens for searching in text.
    
    base_name = re.sub(r'\s*\(.*?\)', '', p_name).strip()
    
    # Simple find
    # We iterate to find all occurrences
    matches = [m.start() for m in re.finditer(re.escape(base_name), all_text, re.IGNORECASE)]
    
    project_completed = False
    for start_idx in matches:
        # Check snippet after the name
        snippet = all_text[start_idx:start_idx+600]
        snippet_lower = snippet.lower()
        
        # Check for completion in 2022
        # Look for "completed" and "2022"
        # And ensure "completed" is associated with "2022"
        # Pattern: "completed... 2022" or "completed, ... 2022"
        
        if "completed" in snippet_lower and "2022" in snippet_lower:
            # Check for "was completed" or context
            if "was completed" in snippet_lower:
                project_completed = True
                break
            # Or "completion filed ... 2022" (meaning completed in 2022 or late 2022)
            # Or just "completed, november 2022"
            # Let's be a bit generous but careful about "will be completed"
            if "will be completed" not in snippet_lower and "scheduled to be completed" not in snippet_lower:
                project_completed = True
                break
    
    if project_completed:
        total_funding += p_amount
        confirmed_projects.append(p_name)

print("__RESULT__:")
print(json.dumps({"confirmed_projects": confirmed_projects, "total_funding": total_funding}))"""

env_args = {'var_function-call-13164751492978107468': 'file_storage/function-call-13164751492978107468.json', 'var_function-call-13164751492978107155': 'file_storage/function-call-13164751492978107155.json', 'var_function-call-9869211362583101527': 'file_storage/function-call-9869211362583101527.json'}

exec(code, env_args)
