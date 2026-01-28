code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_related_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]
completion_indicators = ["completed", "complete construction"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for project name: capitalized, contains 'Project' or similar, reasonably long
        if re.match(r'^[A-Z][a-zA-Z0-9 &\-/\']{5,100}$', stripped_line) and any(kw in stripped_line for kw in ["Project", "Improvements", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment"]):
            current_project_candidate = stripped_line
        
        # Check if the current line indicates completion in 2022 and if there's a recent project candidate
        if current_project_candidate and "2022" in stripped_line.lower() and any(indicator in stripped_line.lower() for indicator in completion_indicators):
            # Verify if the candidate project name is park-related
            if any(park_kw in current_project_candidate.lower() for park_kw in park_related_keywords):
                cleaned_project_name = re.sub(r'\s*\(FEMA Project\)|\s*\(CalJPIA Project\)|\s*\(CalOES Project\)', '', current_project_candidate).strip()
                project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                if project_info not in park_projects_2022_completed:
                    park_projects_2022_completed.append(project_info)
            current_project_candidate = None # Reset for next project
        elif stripped_line.lower().startswith("capital improvement projects") or stripped_line.lower().startswith("disaster recovery projects"):
            current_project_candidate = None # Reset if a section header is encountered

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
