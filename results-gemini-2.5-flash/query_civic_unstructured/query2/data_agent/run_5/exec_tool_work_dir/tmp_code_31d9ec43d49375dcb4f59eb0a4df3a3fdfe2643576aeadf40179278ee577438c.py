code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs", "trancas canyon"]
project_indicator_keywords = ["Project", "Program", "Improvements", "Study", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment", "Road", "Drainage", "Storm Drain", "PCH", "Malibu", "Civic Center", "Bluffs", "Trancas Canyon", "Point Dume", "Marie Canyon", "Broad Beach", "Encinal Canyon", "Kanan Dume", "City Traffic Signals", "Outdoor Warning Signs", "Traffic Study", "Clover Heights", "Latigo Canyon", "Westward Beach", "Morning View"]
completion_keywords = ["completed", "complete construction"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_candidate = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for potential project name: capitalized, contains a project indicator, not too short/long
        if re.match(r'^[A-Z][a-zA-Z0-9 &\-/\']{5,99}$', stripped_line) and any(kw in stripped_line for kw in project_indicator_keywords):
            current_project_candidate = stripped_line
        
        # If we have a project candidate, check for completion in 2022 in the current line
        if current_project_candidate:
            if any(comp_kw in stripped_line.lower() for comp_kw in completion_keywords) and "2022" in stripped_line:
                # Verify if the candidate project name is park-related
                if any(park_kw in current_project_candidate.lower() for park_kw in park_keywords):
                    cleaned_project_name = re.sub(r'\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', current_project_candidate).strip()
                    project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                    if project_info not in park_projects_2022_completed:
                        park_projects_2022_completed.append(project_info)
                    current_project_candidate = None # Reset for next project search
            elif stripped_line.lower().startswith("capital improvement projects") or stripped_line.lower().startswith("disaster recovery projects"):
                # Reset candidate if a new section header is encountered, as it likely signifies a new project context
                current_project_candidate = None

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
