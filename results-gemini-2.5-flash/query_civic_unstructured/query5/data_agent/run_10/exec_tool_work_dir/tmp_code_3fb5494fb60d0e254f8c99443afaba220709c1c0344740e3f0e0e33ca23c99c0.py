code = """import re
import json

docs = json.load(open(locals()['var_function-call-9774842745181215014'], 'r'))
disaster_projects_2022 = []

for doc in docs:
    text = doc['text']
    
    # The goal is to extract projects that are 'disaster' type and start in 2022.
    # Projects are often listed with a name, followed by '(cid:190) Updates:', '(cid:190) Project Schedule:', etc.
    # We need to capture the project name and all its associated details to check for type and start date.
    
    # This regex attempts to find project names and their details. 
    # It looks for a project name (typically starts with a capital letter or number) followed by a newline and then (cid:190) or (Updates: or (Project Description: 
    # It captures everything until another similar project pattern or the end of a section.
    # The negative lookahead `(?!PCH Median Improvements Project)` is to prevent matching the section title as a project name if it is followed by another project title. 
    # It's a complex regex, so will try to simplify it, focusing on key terms.
    
    # Simplified approach: Look for lines that contain 'Project' or 'Projects' and then try to extract names and details from around them.
    
    # Let's try to extract project blocks based on common headings like 'Capital Improvement Projects' and 'Disaster Recovery Projects'.
    # This might help in segmenting the document better.
    
    # Split the document into sections based on major headings for project types
    sections = re.split(r'\n\n(Capital Improvement Projects \((?:Design|Construction|Not Started)\)|Disaster Recovery Projects)\n\n', text)
    
    current_section_type = "Unknown"
    for i, section in enumerate(sections):
        if i % 2 == 1: # These are the section titles captured by the split
            current_section_type = section
        else:
            # Process the content within each section
            # Now within each section, try to find individual projects.
            # Projects usually have a name followed by details.
            for match in re.finditer(r'(?P<project_name>[A-Za-z0-9][A-Za-z0-9\s&,-]+?)(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))(?P<details>.+?)(?=\n\n[A-Za-z0-9][A-Za-z0-9\s&,-]+?(?:\s+\(cid:190\)|\s*\(Updates:|\s*\(Project Description:))|\Z)', section, re.DOTALL):
                project_name = match.group('project_name').strip()
                details = match.group('details')
                
                project_type = "capital" # Default type
                # If the section title explicitly mentions 'Disaster Recovery Projects', or keywords are in project name/details
                if "Disaster Recovery Projects" in current_section_type or \
                   "Disaster" in project_name or "Disaster" in details or \
                   "FEMA" in details or "CalOES" in details or "CalJPIA" in details:
                    project_type = "disaster"
                
                start_date_in_2022 = False
                # Look for start date indicators mentioning '2022'
                # Keywords like 'Begin Construction', 'Advertise', 'Project Schedule', 'Estimated Schedule', 'Scheduled for'
                # followed by a year '2022' or a season 'Spring 2022', etc.
                if re.search(r'(?:Begin Construction|Advertise|Project Schedule|Estimated Schedule|Scheduled for|planning)[:-]?\s*(?:[A-Za-z]+\s+)?(?:2022|Fall\s*2022|Spring\s*2022|Summer\s*2022|Winter\s*2022|early\s*2022|mid\s*2022|late\s*2022)', details, re.IGNORECASE):
                    start_date_in_2022 = True
                
                if project_type == "disaster" and start_date_in_2022:
                    disaster_projects_2022.append(project_name)

print('__RESULT__:')
print(json.dumps(list(set(disaster_projects_2022)))) # Remove duplicates and print"""

env_args = {'var_function-call-3153928930254216863': ['civic_docs'], 'var_function-call-9774842745181215014': 'file_storage/function-call-9774842745181215014.json'}

exec(code, env_args)
