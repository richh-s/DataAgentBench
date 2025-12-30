code = """import re
import json

data_path = locals()['var_function-call-2718406926601295619']

with open(data_path, 'r') as f:
    data = json.load(f)

projects = []
for doc in data:
    text = doc['text']
    # Regex to find project names and their details. This pattern is based on the structure observed in the text.
    # It looks for lines starting with '(cid:190) ' which usually precede project updates or descriptions.
    # It then tries to capture the Project Name, and look for keywords like "Disaster Recovery Projects" for type,
    # and "st" or "begin construction" for start dates.
    # This is a simplified regex, as the text is unstructured and may require more robust NLP for higher accuracy.

    # This regex is simplified and specifically targets the format found in the example text where 'Disaster Recovery Projects' is mentioned
    # and project names are followed by sections like '(cid:190) Updates:' and '(cid:190) Project Schedule:'.

    # We are looking for "Disaster Recovery Projects" section and then listing projects under it, or project names that clearly indicate disaster.
    
    # Extracting Project Names and associated details
    # The current approach is to identify sections that discuss "Capital Improvement Projects" or "Disaster Recovery Projects"
    # and then parse the project details listed under these headings.

    # Example pattern for project extraction:
    # Project_Name\n\n(cid:190) Updates: ... (cid:190) Project Schedule: ... (cid:131) Begin Construction: Fall 2023
    
    # A more robust approach would involve iterating through lines and using context.
    
    # For now, let's try a simpler approach by splitting the text by major headings
    
    
    
    
    
    
    
    
    # Initial attempt to find disaster projects and their start dates in 2022
    disaster_projects_pattern = r"Disaster Recovery Projects\\n\\n(.+?)(?=\\n\\nCapital Improvement Projects|$)"
    disaster_projects_section_match = re.search(disaster_projects_pattern, text, re.DOTALL)

    if disaster_projects_section_match:
        disaster_section_text = disaster_projects_section_match.group(1)
        
        # Now, within this section, try to find individual projects and their schedules
        project_pattern = r"([A-Za-z0-9&,\\s'-]+)(?=\\n\\n\(cid:190) Updates:|\(cid:190) Updates:|\n\nAgenda Item #|\n\nPage \d of \d)"
        
        project_names_in_section = re.findall(project_pattern, disaster_section_text)
        
        
        for project_name in project_names_in_section:
            # Clean up the project name
            project_name = project_name.strip()
            if project_name and len(project_name) < 100: # Heuristic to avoid matching too long strings
                
                # Now, try to find the project's details, specifically 'st' (start date)
                # Look for 'Begin Construction:' or 'Advertise:' or 'Project Schedule:'
                
                # Construct a more specific pattern to find the schedule for *this* project
                # We need to find the text block for the specific project. This is tricky with unstructured text.
                
                # A better approach might be to split the entire document into project blocks first
                # and then process each block.
                
                # For now, let's try to find start dates for disaster projects generally in the text,
                # and then filter by project name later, assuming 'disaster' type is implicit in the section.
                
                # Looking for start dates in 2022 for any project for now, then filter by project name later.
                start_date_pattern = r"(?:Begin Construction|Advertise|Complete Design|Project Schedule):\s*(.*?2022.*?)(?=\\n|\s*\(cid:131)|\s*\(cid:190))"
                start_date_matches = re.findall(start_date_pattern, disaster_section_text)
                
                for date_str in start_date_matches:
                    date_str = date_str.strip()
                    if "2022" in date_str:
                        projects.append({'Project_Name': project_name, 'type': 'disaster', 'st': date_str})


    # Additionally, look for specific project names that clearly indicate 'disaster' type from previous observations
    # For instance, projects with "(FEMA Project)" suffix.
    
    # We will refine the extraction to include "disaster" projects more broadly.
    # Let's try to extract all projects and then filter for disaster and 2022 start date.
    
    
    # A more general pattern to capture projects and their subsequent details (status, schedule)
    # This pattern attempts to capture a project name followed by updates and schedule.
    # It assumes project names are typically at the start of a line and followed by bullet points.
    
    project_block_pattern = r"([A-Za-z0-9&,\\s'-]+)\\n\\n\(cid:190) Updates:(.*?)(?=(?:\n\n[A-Za-z0-9&,\\s'-]+\\n\\n\(cid:190) Updates:)|$)"
    
    all_project_blocks = re.findall(project_block_pattern, text, re.DOTALL)
    
    for project_name, details_block in all_project_blocks:
        project_name = project_name.strip()
        project_type = "capital" # Default type
        
        if "disaster" in details_block.lower() or "fema" in details_block.lower() or "(fema project)" in project_name.lower():
            project_type = "disaster"
        
        start_date = None
        start_date_match = re.search(r"(?:Begin Construction|Advertise|Complete Design):\s*(.*?2022.*?)(?=\\n|\s*\(cid:131)|\s*\(cid:190))", details_block, re.IGNORECASE)
        if start_date_match:
            start_date = start_date_match.group(1).strip()
            
        if start_date and "2022" in start_date:
            projects.append({'Project_Name': project_name, 'type': project_type, 'st': start_date})


# Further refining the project extraction to capture "Disaster Recovery Projects" section more explicitly.
# Look for a common header like "Capital Improvement Projects and Disaster Recovery Projects Status Report"
# or directly "Disaster Recovery Projects"

    
    
    
    
    
    
    # Final attempt: A more robust project extraction based on common patterns for project listings
    # We need to find project names and their attributes (type, start date).
    
    # Look for project name followed by schedule, updates etc.
    # We will iterate through lines and try to identify projects.
    
    lines = text.split('\\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Project names are often followed by '(cid:190) Updates:' or are part of a list
        # Let's try to find project names that seem to be headers
        
        # Heuristic: A line that looks like a project name, not too short, not too long, and not just punctuation
        if len(line) > 5 and len(line) < 100 and not re.match(r'^[\(\)\d\W]+$', line):
            
            # Check if the next few lines contain project schedule or updates, to confirm it's a project
            next_lines_sample = "\\n".join(lines[i+1:i+5])
            
            if "(cid:190) Updates:" in next_lines_sample or "(cid:190) Project Schedule:" in next_lines_sample or "(cid:190) Estimated Schedule:" in next_lines_sample:
                current_project = {'Project_Name': line, 'type': 'unknown', 'st': None}
                
                # Determine project type
                if "disaster" in next_lines_sample.lower() or "fema" in next_lines_sample.lower() or "(fema project)" in line.lower():
                    current_project['type'] = 'disaster'
                elif "capital" in next_lines_sample.lower():
                    current_project['type'] = 'capital'
                
                # Extract start date
                start_date_match = re.search(r"(?:Begin Construction|Advertise|Complete Design):\s*(.*?2022.*?)(?=\\n|\s*\(cid:131)|\s*\(cid:190))", next_lines_sample, re.IGNORECASE)
                if start_date_match:
                    start_date_str = start_date_match.group(1).strip()
                    if "2022" in start_date_str:
                        current_project['st'] = start_date_str
                
                if current_project['type'] == 'disaster' and current_project['st']:
                    projects.append(current_project)
                
                current_project = None # Reset for next project
                
            # Special case for "Disaster Recovery Projects" heading explicitly
            elif "Disaster Recovery Projects" in line:
                for j in range(i + 1, len(lines)):
                    sub_line = lines[j].strip()
                    if sub_line.startswith("(cid:190)"): # End of sub-projects list under this heading
                        break
                    
                    if len(sub_line) > 5 and len(sub_line) < 100 and not re.match(r'^[\(\)\d\W]+$', sub_line):
                        
                        # Assuming projects listed directly under "Disaster Recovery Projects" are of type disaster
                        project_name = sub_line
                        
                        # Look for start date in the following lines for this sub_line project
                        sub_project_details_sample = "\\n".join(lines[j+1:j+5])
                        start_date_match = re.search(r"(?:Begin Construction|Advertise|Complete Design):\s*(.*?2022.*?)(?=\\n|\s*\(cid:131)|\s*\(cid:190))", sub_project_details_sample, re.IGNORECASE)
                        if start_date_match:
                            start_date_str = start_date_match.group(1).strip()
                            if "2022" in start_date_str:
                                projects.append({'Project_Name': project_name, 'type': 'disaster', 'st': start_date_str})

# Remove duplicates if any
unique_projects = []
seen_project_names = set()
for p in projects:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-18410950440773738686': ['civic_docs'], 'var_function-call-2718406926601295619': 'file_storage/function-call-2718406926601295619.json'}

exec(code, env_args)
