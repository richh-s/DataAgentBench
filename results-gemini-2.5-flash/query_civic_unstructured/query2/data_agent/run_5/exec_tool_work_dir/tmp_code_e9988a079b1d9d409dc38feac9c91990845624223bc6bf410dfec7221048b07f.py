code = """import json
import re

with open(locals()['var_function-call-18430938180689412795'], 'r') as f:
    civic_docs = json.load(f)

park_projects_2022_completed = []

for doc in civic_docs:
    text = doc['text']
    # Split the document by project
    project_sections = re.split(r'\n\n[A-Z][a-zA-Z0-9 ]+ Project\n', text) # This regex needs to be more robust

    # A more robust way to find projects and their details
    # Look for patterns of project names followed by details
    # This is a heuristic and might need refinement based on actual document structure
    project_pattern = re.compile(r'([A-Z][a-zA-Z0-9 &\-/]+(?: Project| Program| Improvements| Study| Repairs| Facility| System| Wall| Signals| Lane| Screens| Structures| Trails| Park| Playground)?)\n(?:\(cid:190\) [^\n]+\n)*(?:\(cid:190\) Updates:[^\n]*\n)*(?:\(cid:190\) Project Schedule:[^\n]*\n)*(?:\(cid:131\) Complete Construction: (?:Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)? ?(2022))', re.IGNORECASE)
    
    # Let's try to extract project name, status, and completion date using a more general approach
    # Looking for 'Project Name' and then 'Updates' or 'Schedule' and 'completed' or 'Complete Construction' and '2022'
    
    # This is a simplified regex, it may not capture all cases.
    # It looks for a project name followed by updates/schedule containing 'completed' or 'Complete Construction' and '2022'.
    # It also checks for "park" in the project name or the surrounding text.
    
    # First, identify potential project blocks. A project block usually starts with a project name and contains 'Updates' and 'Schedule'.
    
    # Let's refine this. Iterate through lines and try to identify project names and their associated status and dates.
    
    lines = text.split('\n')
    project_name = None
    status = None
    end_date = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Heuristic to identify a project name line - it's usually capitalized and followed by description or updates
        if re.match(r'^[A-Z][a-zA-Z0-9 &\-/]+\s(?:Project|Program|Improvements|Study|Repairs|Facility|System|Wall|Signals|Lane|Screens|Structures|Trails|Park|Playground|Treatment)$', line):
            project_name = line.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip()
            status = None
            end_date = None

        if project_name:
            if "park" in project_name.lower() or "playground" in project_name.lower(): # Checking for park-related projects
                if "completed" in line.lower() or "complete construction" in line.lower():
                    if "2022" in line:
                        status = "completed"
                        end_date = "2022" # We just need to confirm it's 2022, exact date not required for this query.
                        if project_name not in [p['Project_Name'] for p in park_projects_2022_completed]:
                            park_projects_2022_completed.append({'Project_Name': project_name, 'status': status, 'et': end_date, 'topic': 'park'})
            
            # Reset project_name if a new major section begins (heuristic)
            if re.match(r'^Capital Improvement Projects \((?:Design|Construction|Not Started)\)$', line) or \
               re.match(r'^Disaster Recovery Projects \((?:Design|Construction|Not Started)\)$', line):
                project_name = None # Start looking for a new project
                
# A more robust regex approach for extracting:
# Project_Name: ...
# Updates: ...
# Project Schedule: ...
# Complete Construction: YYYY
# or Construction was completed Month YYYY

extracted_projects = []
project_blocks = re.split(r'(?=
[A-Z][a-zA-Z0-9 ]+(?: Project| Program| Improvements| Study| Repairs| Facility| System| Wall| Signals| Lane| Screens| Structures| Trails| Park| Playground| Treatment| Road| Drainage| Storm Drain| PCH| Malibu| Civic Center| Bluffs| Trancas Canyon| Point Dume| Marie Canyon| Broad Beach| Encinal Canyon| Kanan Dume| City Traffic Signals| Outdoor Warning Signs| Traffic Study| Clover Heights| Latigo Canyon| Westward Beach| Morning View)
)', text)

for block in project_blocks:
    project_name_match = re.search(r'\n([A-Z][a-zA-Z0-9 &\-/]+(?: Project| Program| Improvements| Study| Repairs| Facility|System|Wall|Signals|Lane|Screens|Structures|Trails|Park|Playground|Treatment|Road|Drainage|Storm Drain|PCH|Malibu|Civic Center|Bluffs|Trancas Canyon|Point Dume|Marie Canyon|Broad Beach|Encinal Canyon|Kanan Dume|City Traffic Signals|Outdoor Warning Signs|Traffic Study|Clover Heights|Latigo Canyon|Westward Beach|Morning View))\n', block)
    if project_name_match:
        project_name = project_name_match.group(1).strip()
        
        # Check for completion in 2022
        completed_2022_match = re.search(r'(?:completed|Complete Construction):?(?:.*?)?(?:2022|November 2022|December 2022|October 2022|September 2022|August 2022|July 2022|June 2022|May 2022|April 2022|March 2022|February 2022|January 2022)', block, re.IGNORECASE)
        
        if completed_2022_match:
            # Check if it's park related
            if "park" in project_name.lower() or "playground" in project_name.lower() or "bluffs park" in project_name.lower() or "trancas canyon park" in project_name.lower():
                extracted_projects.append({'Project_Name': project_name.replace('(FEMA Project)', '').replace('(CalJPIA Project)', '').replace('(CalOES Project)', '').strip(), 'status': 'completed', 'et': '2022', 'topic': 'park'})

final_park_projects = []
# Remove duplicates
for project in extracted_projects:
    if project not in final_park_projects:
        final_park_projects.append(project)

print("__RESULT__:")
print(json.dumps(final_park_projects))"""

env_args = {'var_function-call-1711494461326809984': ['civic_docs'], 'var_function-call-18430938180689412795': 'file_storage/function-call-18430938180689412795.json'}

exec(code, env_args)
