code = """import re
import json

docs = json.load(open(locals()['var_function-call-9774842745181215014'], 'r'))
disaster_projects_2022 = []

for doc in docs:
    text = doc['text']
    # Split the document into potential project blocks
    # Projects are usually introduced by a name followed by "(cid:190) Updates:", "(cid:190) Project Schedule:" or similar.
    # The regex aims to capture the project name and its subsequent details until the next project or a major section heading.
    
    # Using a more robust regex to split projects
    # This pattern looks for a project name followed by updates/schedule/description and captures the content until the next such pattern or end of relevant sections.
    project_blocks = re.split(r'\n\n(?:Capital Improvement Projects \((?:Design|Construction|Not Started)\)|Disaster Recovery Projects\n\n)', text)

    for block in project_blocks:
        # Each block might contain multiple projects or just one.
        # Let's try to extract project name and its immediate details.
        
        # This regex attempts to get the project name and all following details until a new project name or end of block.
        # It's looking for a line starting with a project name (often capitalized)
        # followed by (cid:190) or (Updates: or (Project Description: 
        # and then captures everything until the next similar project pattern or the end of the block.
        for match in re.finditer(r'^(?P<project_name>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)\n(?:\(cid:190\)|\(Updates:|\(Project Description:)(?P<details>.+?)(?=\n[A-Za-z0-9][A-Za-z0-9\s&,-]+?\n(?:\(cid:190\)|\(Updates:|\(Project Description:))|\Z)', block, re.DOTALL | re.MULTILINE):
            project_name = match.group('project_name').strip()
            details = match.group('details')
            
            project_type = "capital" # Default type
            if "Disaster" in project_name or "Disaster" in details or "FEMA" in details or "CalOES" in details:
                project_type = "disaster"
            
            start_date_found = False
            # Check for 2022 in various schedule related phrases
            if re.search(r'(?:Begin Construction|Advertise|Complete Design|Final Design|Project Schedule:|Estimated Schedule:|Scheduled for|expected|target|anticipated|planning)[:-]?\s*(?:[A-Za-z]+\s+)?(?:2022|Fall\s*2022|Spring\s*2022|Summer\s*2022|Winter\s*2022|early\s*2022|mid\s*2022|late\s*2022)', details, re.IGNORECASE):
                start_date_found = True
            
            if project_type == "disaster" and start_date_found:
                disaster_projects_2022.append(project_name)

print('__RESULT__:')
print(json.dumps(list(set(disaster_projects_2022)))) # Remove duplicates and print"""

env_args = {'var_function-call-3153928930254216863': ['civic_docs'], 'var_function-call-9774842745181215014': 'file_storage/function-call-9774842745181215014.json'}

exec(code, env_args)
