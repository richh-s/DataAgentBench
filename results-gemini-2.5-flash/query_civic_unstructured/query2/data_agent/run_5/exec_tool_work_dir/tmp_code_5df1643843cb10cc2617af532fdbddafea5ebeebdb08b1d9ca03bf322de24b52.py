code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_related_terms = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_terms = ["completed", "complete construction"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Check if the current line or a nearby line indicates completion in 2022
        if any(term in stripped_line.lower() for term in completion_terms) and "2022" in stripped_line:
            
            # Now look for a park-related project name in the preceding lines
            project_name = None
            for j in range(max(0, i - 5), i):
                prev_line = lines[j].strip()
                if re.match(r'^[A-Z][a-zA-Z0-9 &\-/\']{5,99}$', prev_line) and any(park_term in prev_line.lower() for park_term in park_related_terms):
                    project_name = prev_line.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip()
                    break
            
            if project_name:
                project_info = {'Project_Name': project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json'}

exec(code, env_args)
