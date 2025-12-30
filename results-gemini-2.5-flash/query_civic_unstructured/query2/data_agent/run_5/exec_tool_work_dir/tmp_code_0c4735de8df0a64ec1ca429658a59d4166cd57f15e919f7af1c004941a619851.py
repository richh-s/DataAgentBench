code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    
    # A more general pattern to capture project names that are typically capitalized
    # and might be followed by terms like 'Project', 'Improvements', etc.
    project_name_pattern = re.compile(r'([A-Z][a-zA-Z0-9 &\\-/\']+(?: Project| Program| Improvements| Study| Repairs| Facility| System| Wall| Signals| Lane| Screens| Structures| Trails| Park| Playground| Treatment| Road| Drainage| Storm Drain| PCH| Malibu| Civic Center| Bluffs| Trancas Canyon| Point Dume| Marie Canyon| Broad Beach| Encinal Canyon| Kanan Dume| City Traffic Signals| Outdoor Warning Signs| Traffic Study| Clover Heights| Latigo Canyon| Westward Beach| Morning View)?)\n', re.MULTILINE)
    
    # Pattern to find completion status and year 2022 within a reasonable proximity of a project name
    completion_2022_status_pattern = re.compile(r'(?:completed|Complete Construction)(?:[^\n]*?)(?:2022|November 2022|December 2022|October 2022|September 2022|August 2022|July 2022|June 2022|May 2022|April 2022|March 2022|February 2022|January 2022)', re.IGNORECASE)
    
    # Split the text into potential project blocks based on project name appearance
    # This is a heuristic and might need adjustment based on the document structure
    project_blocks = re.split(r'\n(?=[A-Z][a-zA-Z0-9 ]+(?: Project| Program| Improvements| Study| Repairs| Facility| System| Wall| Signals| Lane| Screens| Structures| Trails| Park| Playground| Treatment| Road| Drainage| Storm Drain| PCH| Malibu| Civic Center| Bluffs| Trancas Canyon| Point Dume| Marie Canyon| Broad Beach| Encinal Canyon| Kanan Dume| City Traffic Signals| Outdoor Warning Signs| Traffic Study| Clover Heights| Latigo Canyon| Westward Beach| Morning View))\n', text)

    for block in project_blocks:
        project_name_match = project_name_pattern.search(block)
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Check if the project is park-related
            if any(keyword in project_name.lower() for keyword in ["park", "playground", "bluffs", "trancas canyon"]):
                
                # Check for completion in 2022 within the block
                if completion_2022_status_pattern.search(block):
                    project_info = {'Project_Name': project_name.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip(), 'status': 'completed', 'et': '2022', 'topic': 'park'}
                    if project_info not in park_projects_2022_completed:
                        park_projects_2022_completed.append(project_info)

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json'}

exec(code, env_args)
