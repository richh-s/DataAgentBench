code = """import json
import re

file_path = locals()['var_function-call-8179248509000558122']
with open(file_path, 'r') as f:
    data = json.load(f)

spring_2022_projects = []

# Markers that typically indicate a line is NOT a project name, or a general section header
known_non_project_markers = [
    "Updates:", "Project Schedule:", "Estimated Schedule:", "Subject:", 
    "DISCUSSION:", "RECOMMENDED ACTION:", "Date prepared:", "Meeting date:", 
    "Prepared by:", "Approved by:", "To:", "Page ", "Item ", "Table of Contents",
    "BACKGROUND", "FINDINGS", "FISCAL IMPACT", "ATTACHMENTS", "Project Description",
    "Public Works Commission", "Capital Improvement Projects", "Disaster Recovery Projects",
    "(cid:", # Common bullet point indicator
    "Agenda Report", "Public Works", "Capital Improvement Program"
]

for doc in data:
    text_content = doc['text']
    lines = text_content.split('\n')
    
    current_project_name = None
    is_looking_for_schedule_date = False

    for i, line in enumerate(lines):
        cleaned_line = line.strip()

        # Check if the line is a non-project marker
        is_marker = any(marker.lower() in cleaned_line.lower() for marker in known_non_project_markers)
        
        # Heuristic to identify potential project names:
        # - non-empty
        # - not a known marker
        # - not a date in 'MM-DD-YYYY' format (e.g., '03-22-2023')
        # - reasonable length (to avoid capturing very short, uninformative lines)
        if cleaned_line and not is_marker and not re.match(r'^\d{2}-\d{2}-\d{4}$', cleaned_line) and len(cleaned_line) > 5:
            current_project_name = cleaned_line
            is_looking_for_schedule_date = False # Reset if a new project candidate is found
        
        # If we see a schedule indicator, set flag to start looking for dates in subsequent lines
        if 'Project Schedule:' in cleaned_line or 'Estimated Schedule:' in cleaned_line:
            is_looking_for_schedule_date = True
            continue # Skip to the next line to check for dates, current line is just the header
        
        # If we are currently in a schedule block, check for Spring 2022 dates
        if is_looking_for_schedule_date:
            if re.search(r'(Spring|March|April|May)\s*2022', cleaned_line, re.IGNORECASE):
                if current_project_name:
                    spring_2022_projects.append(current_project_name)
                is_looking_for_schedule_date = False # Date found, exit schedule block
                current_project_name = None # Reset project name after finding its date

# Remove duplicates and ensure no common headers remain
unique_spring_2022_projects = list(set(spring_2022_projects))

# Final filtering to remove any remaining known general headers that might have been picked up
final_filtered_projects = []
common_general_headers = [
    "Capital Improvement Projects (Design)",
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]
for project_name in unique_spring_2022_projects:
    is_general_header = False
    for header in common_general_headers:
        if header.lower() in project_name.lower():
            is_general_header = True
            break
    if not is_general_header:
        final_filtered_projects.append(project_name)

print("__RESULT__:")
print(json.dumps(final_filtered_projects)))"""

env_args = {'var_function-call-8179248509000558122': 'file_storage/function-call-8179248509000558122.json'}

exec(code, env_args)
