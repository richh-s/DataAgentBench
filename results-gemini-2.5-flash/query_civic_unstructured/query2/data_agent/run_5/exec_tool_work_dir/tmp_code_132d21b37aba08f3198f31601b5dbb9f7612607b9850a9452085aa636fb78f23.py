code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

park_keywords = ["park", "playground", "bluffs", "trancas canyon"]

for doc in civic_docs:
    text = doc['text']
    
    # This regex attempts to find a project name and its completion status within a block.
    # It looks for a line starting with a capital letter (potential project name),
    # followed by any content, then a completion phrase that includes '2022'.
    # The project name pattern has been simplified and carefully escaped.
    project_completion_pattern = re.compile(
        r'([A-Z][a-zA-Z0-9 &\-/\']{5,99}(?: Project| Program| Improvements| Study| Repairs| Facility| System| Wall| Signals| Lane| Screens| Structures| Trails| Park| Playground| Treatment| Road| Drainage| Storm Drain| PCH| Malibu| Civic Center| Bluffs| Trancas Canyon| Point Dume| Marie Canyon| Broad Beach| Encinal Canyon| Kanan Dume| City Traffic Signals| Outdoor Warning Signs| Traffic Study|Clover Heights|Latigo Canyon|Westward Beach|Morning View))' # Project Name
        r'.*?' # Non-greedy match for any characters in between
        r'(?:completed|Complete Construction):?(?:.*?)(?:2022|November 2022|December 2022|October 2022|September 2022|August 2022|July 2022|June 2022|May 2022|April 2022|March 2022|February 2022|January 2022)', # Completion in 2022
        re.IGNORECASE | re.DOTALL
    )

    for match in project_completion_pattern.finditer(text):
        project_name = match.group(1).strip()
        
        # Filter for park-related projects
        if any(keyword in project_name.lower() for keyword in park_keywords):
            cleaned_project_name = re.sub(r'\\s*\\(FEMA Project\\)|\\s*\\(CalJPIA Project\\)|\\s*\\(CalOES Project\\)', '', project_name).strip()
            project_info = {'Project_Name': cleaned_project_name, 'status': 'completed', 'et': '2022', 'topic': 'park'}
            if project_info not in park_projects_2022_completed:
                park_projects_2022_completed.append(project_info)

print("__RESULT__:")
print(json.dumps(park_projects_2022_completed))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json', 'var_function-call-4442267602916977481': 'file_storage/function-call-4442267602916977481.json'}

exec(code, env_args)
