code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

project_name_keywords = ["Project", "Program", "Improvements", "Study", "Repairs", "Facility", "System", "Wall", "Signals", "Lane", "Screens", "Structures", "Trails", "Park", "Playground", "Treatment", "Road", "Drainage", "Storm Drain", "PCH", "Malibu", "Civic Center", "Bluffs", "Trancas Canyon", "Point Dume", "Marie Canyon", "Broad Beach", "Encinal Canyon", "Kanan Dume", "City Traffic Signals", "Outdoor Warning Signs", "Traffic Study", "Clover Heights", "Latigo Canyon", "Westward Beach", "Morning View"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = {'Project_Name': None, 'status': None, 'et': None, 'topic': None}
    
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        
        # Heuristic to identify a project name line: starts with a capital letter and contains a project keyword
        if re.match(r'^[A-Z][a-zA-Z0-9 &\\-/\']+', stripped_line) and any(keyword in stripped_line for keyword in project_name_keywords):
            current_project['Project_Name'] = stripped_line.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip()
            current_project['status'] = None
            current_project['et'] = None
            current_project['topic'] = None

            # Check if it's a park-related project
            if any(keyword in current_project['Project_Name'].lower() for keyword in ["park", "playground", "bluffs park", "trancas canyon park"]):
                current_project['topic'] = 'park'
                
                # Look in the next few lines for completion status and year
                for j in range(i + 1, min(i + 10, len(lines))):
                    subsequent_line = lines[j].strip()
                    if "completed" in subsequent_line.lower() or "complete construction" in subsequent_line.lower():
                        if "2022" in subsequent_line:
                            current_project['status'] = 'completed'
                            current_project['et'] = '2022'
                            if current_project['Project_Name'] not in [p['Project_Name'] for p in park_projects_2022_completed]:
                                park_projects_2022_completed.append(current_project.copy()) # Append a copy to avoid reference issues
                            break # Found status and year, move to next project candidate
            current_project = {'Project_Name': None, 'status': None, 'et': None, 'topic': None}
            
print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json'}

exec(code, env_args)
