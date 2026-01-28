code = """import json
import re

file_path = locals()['var_function-call-8179248509000558122']
with open(file_path, 'r') as f:
    data = json.load(f)

spring_2022_projects = []

# Markers that typically indicate a line is NOT a project name
known_non_project_markers = [
    "Updates:", "Project Schedule:", "Estimated Schedule:", "Subject:", 
    "DISCUSSION:", "RECOMMENDED ACTION:", "Date prepared:", "Meeting date:", 
    "Prepared by:", "Approved by:", "To:", "Page ", "Item ", "Table of Contents",
    "BACKGROUND", "FINDINGS", "FISCAL IMPACT", "ATTACHMENTS", "Project Description",
    "Public Works Commission", "Capital Improvement Projects", "Disaster Recovery Projects",
    "(cid:" # Common bullet point indicator
]

for doc in data:
    text_content = doc['text']
    lines = text_content.split('\n')
    
    current_project_name = None
    is_in_schedule_block = False

    for i, line in enumerate(lines):
        cleaned_line = line.strip()

        # Check if the line is a non-project marker
        is_marker = any(marker in cleaned_line for marker in known_non_project_markers)
        
        # Heuristic to identify project names: non-empty, not a marker, and a reasonable length
        if cleaned_line and not is_marker and len(cleaned_line) > 5 and not re.match(r'^\d{2}-\d{2}-\d{4}$', cleaned_line):
            current_project_name = cleaned_line
            is_in_schedule_block = False # Reset when a new project candidate is found
        
        # If we see a schedule indicator, set flag to start looking for dates
        if 'Project Schedule:' in cleaned_line or 'Estimated Schedule:' in cleaned_line:
            is_in_schedule_block = True
            continue # Skip to the next line to check for dates
        
        # If we are in a schedule block, check for Spring 2022 dates
        if is_in_schedule_block:
            if re.search(r'(Spring|March|April|May)\s*2022', cleaned_line, re.IGNORECASE):
                if current_project_name:
                    spring_2022_projects.append(current_project_name)
                is_in_schedule_block = False # Date found, exit schedule block
                current_project_name = None # Reset project name after finding its date

# Remove duplicates
unique_spring_2022_projects = list(set(spring_2022_projects))

print("__RESULT__:")
print(json.dumps(unique_spring_2022_projects)))"""

env_args = {'var_function-call-8179248509000558122': 'file_storage/function-call-8179248509000558122.json'}

exec(code, env_args)
