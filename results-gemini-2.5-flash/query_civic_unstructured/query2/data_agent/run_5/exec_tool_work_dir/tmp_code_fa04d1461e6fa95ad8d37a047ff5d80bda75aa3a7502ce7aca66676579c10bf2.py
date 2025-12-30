code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

project_name_indicator_keywords = ["Project", "Program", "Improvements", "Study", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment", "Road", "Drainage", "Storm Drain", "PCH", "Malibu", "Civic Center", "Bluffs", "Trancas Canyon", "Point Dume", "Marie Canyon", "Broad Beach", "Encinal Canyon", "Kanan Dume", "City Traffic Signals", "Outdoor Warning Signs", "Traffic Study", "Clover Heights", "Latigo Canyon", "Westward Beach", "Morning View"]
park_specific_keywords = ["park", "playground", "bluffs park", "trancas canyon park"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')

    current_project_name = None
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for project name line: starts with capital, contains a project keyword, not too short/long
        # Removed single quote from character class to avoid syntax error in Python string literal within tool call
        if re.match(r'^[A-Z][a-zA-Z0-9 &\-/]{5,99}$', stripped_line) and any(kw in stripped_line for kw in project_name_indicator_keywords):
            temp_project_name = stripped_line.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip()
            
            if any(park_kw in temp_project_name.lower() for park_kw in park_specific_keywords):
                current_project_name = temp_project_name

                # Look in subsequent lines for completion in 2022
                for j in range(i + 1, min(i + 10, len(lines))):
                    subsequent_line = lines[j].strip()
                    if ("completed" in subsequent_line.lower() or "complete construction" in subsequent_line.lower()) and "2022" in subsequent_line:
                        project_info = {'Project_Name': current_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                        if project_info not in park_projects_2022_completed:
                            park_projects_2022_completed.append(project_info)
                        current_project_name = None # Reset for next project
                        break # Stop looking for completion for this project

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json'}

exec(code, env_args)
