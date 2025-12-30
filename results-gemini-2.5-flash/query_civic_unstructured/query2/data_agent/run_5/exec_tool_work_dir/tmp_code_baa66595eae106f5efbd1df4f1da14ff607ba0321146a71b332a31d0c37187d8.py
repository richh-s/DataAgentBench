code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs", "trancas canyon"]
completion_phrases = ["completed", "complete construction"]

for doc in civic_docs:
    text = doc['text']
    
    # Split text into sections that might represent projects or project status updates
    # Use section headers like 'Capital Improvement Projects (Design)' or 'Project Schedule:' as delimiters
    sections = re.split(r'\n(?=(?:Capital Improvement Projects|Disaster Recovery Projects) \(|Project Schedule:)', text, flags=re.IGNORECASE)
    
    current_project_name = None
    
    for section in sections:
        # Try to find a project name within the section
        # A project name is typically a capitalized phrase, potentially followed by 'Project', 'Improvements', etc.
        project_name_match = re.search(r'^[A-Z][a-zA-Z0-9 &\-/]+\s(?:Project|Program|Improvements|Study|Repairs|Facility|System|Wall|Signals|Lane|Screens|Structures|Trails|Park|Playground|Treatment|Road|Drainage|Storm Drain|PCH|Malibu|Civic Center|Bluffs|Trancas Canyon|Point Dume|Marie Canyon|Broad Beach|Encinal Canyon|Kanan Dume|City Traffic Signals|Outdoor Warning Signs|Traffic Study|Clover Heights|Latigo Canyon|Westward Beach|Morning View)\b', section, re.MULTILINE)
        
        if project_name_match:
            current_project_name = project_name_match.group(0).strip()
            
            # Check if this project name is park-related
            if any(pk in current_project_name.lower() for pk in park_keywords):
                
                # Now check if this section contains completion in 2022
                if any(cp in section.lower() for cp in completion_phrases) and "2022" in section:
                    cleaned_project_name = re.sub(r'\s*\(FEMA Project\)|\s*\(CalJPIA Project\)|\s*\(CalOES Project\)', '', current_project_name).strip()
                    project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
                    if project_info not in park_projects_2022_completed:
                        park_projects_2022_completed.append(project_info)
            current_project_name = None # Reset for the next section

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
