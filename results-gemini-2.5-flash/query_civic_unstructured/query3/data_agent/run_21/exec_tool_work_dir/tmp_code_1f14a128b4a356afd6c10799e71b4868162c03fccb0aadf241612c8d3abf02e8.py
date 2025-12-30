code = """import json
import re

with open(locals()['var_function-call-2241076992410809533'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']

    # Function to extract projects from a given text block and status
    def extract_projects_from_block(block_text, status_type, topic_prefix=""):
        extracted = []
        # Using raw string literals with double quotes for regex to handle single quotes in project names easily
        # The project name pattern allows letters, numbers, spaces, hyphens, ampersands, commas, dots, single quotes, and escaped square brackets.
        project_name_chars = r"[A-Za-z0-9 \-&,.'\[\]]"
        
        project_pattern = re.compile(
            r"(" + project_name_chars + "+? (?:Project|Plan))" # Project Name
            r"(?:\n\n\(cid:190\) Updates:(.*?)(?="
            r"\n\n" + project_name_chars + "+? (?:Project|Plan)|" # Next project
            r"\n\n\(cid:190\) Project Schedule:|\n\n\(cid:190\) Project Description:|$)"
            r"|\n\n\(cid:190\) Project Schedule:(.*?)(?="
            r"\n\n" + project_name_chars + "+? (?:Project|Plan)|"
            r"\n\n\(cid:190\) Project Schedule:|\n\n\(cid:190\) Project Description:|$)"
            r"|\n\n\(cid:190\) Project Description:(.*?)(?="
            r"\n\n" + project_name_chars + "+? (?:Project|Plan)|"
            r"\n\n\(cid:190\) Project Schedule:|\n\n\(cid:190\) Project Description:|$)"
            r")",
            re.DOTALL
        )

        for match in project_pattern.finditer(block_text):
            project_name = match.group(1).strip()
            details = ''.join(filter(None, match.groups()[1:]))
            
            current_status = status_type
            current_topic = topic_prefix

            if re.search(r'completed', details, re.IGNORECASE):
                current_status = 'completed'
            elif re.search(r'construction|begin construction', details, re.IGNORECASE):
                current_status = 'construction'
            elif re.search(r'design|preliminary design|FEMA/CalOES approval', details, re.IGNORECASE):
                current_status = 'design'
            elif re.search(r'not started', details, re.IGNORECASE):
                current_status = 'not started'

            if re.search(r'emergency|FEMA', project_name + details, re.IGNORECASE):
                if current_topic:
                    current_topic += '/emergency/FEMA'
                else:
                    current_topic = 'emergency/FEMA'
                extracted.append({"Project_Name": project_name, "status": current_status, "topic": current_topic})
        return extracted

    # Extract Disaster Recovery Projects
    disaster_section_match = re.search(r'Disaster Recovery Projects\n\n(.*?)(?=(?:\n\nCapital Improvement Projects|\n\nPage \d+ of \d+|$))', text, re.DOTALL)
    if disaster_section_match:
        disaster_text = disaster_section_match.group(1)
        projects_data.extend(extract_projects_from_block(disaster_text, "unknown", "disaster"))

    # Extract Capital Improvement Projects
    capital_sections = {
        'design': r'Capital Improvement Projects \\(Design\\)\n\n(.*?)(?=(?:\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nPage \d+ of \d+|$))',
        'construction': r'Capital Improvement Projects \\(Construction\\)\n\n(.*?)(?=(?:\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nPage \d+ of \d+|$))',
        'not started': r'Capital Improvement Projects \\(Not Started\\)\n\n(.*?)(?=(?:\n\nCapital Improvement Projects|\n\nDisaster Recovery Projects|\n\nPage \d+ of \d+|$))',
    }

    for status_key, pattern in capital_sections.items():
        section_match = re.search(pattern, text, re.DOTALL)
        if section_match:
            section_text = section_match.group(1)
            projects_data.extend(extract_projects_from_block(section_text, status_key, "capital"))

    # Specific project extractions mentioned in hints that might be missed by general patterns
    # Outdoor Warning Signs
    if re.search(r'Outdoor Warning Signs', text) and re.search(r'emergency', text, re.IGNORECASE):
        projects_data.append({"Project_Name": "Outdoor Warning Signs", "status": "design", "topic": "emergency"})

    # Latigo Canyon Road Retaining Wall Repair Project
    if re.search(r'Latigo Canyon Road Retaining Wall Repair Project', text) and re.search(r'FEMA/CalOES approval', text):
        projects_data.append({"Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "status": "design", "topic": "FEMA"})

    # City Traffic Signals Backup Power
    traffic_signals_match = re.search(r'City Traffic Signals Backup Power\n\n\(cid:190\) Project Description:(.*?)\n\n\(cid:190\) Updates:(.*?)\n\n\(cid:190\) Project Schedule:(.*?)(?=\n\n.+?$)', text, re.DOTALL)
    if traffic_signals_match:
        description = traffic_signals_match.group(1)
        updates = traffic_signals_match.group(2)
        if re.search(r'emergency', description, re.IGNORECASE) or re.search(r'emergency', updates, re.IGNORECASE):
            projects_data.append({"Project_Name": "City Traffic Signals Backup Power", "status": "preliminary design", "topic": "emergency"})


# Remove duplicates
unique_projects = []
seen_projects = set()
for project in projects_data:
    project_tuple = (project['Project_Name'], project['status'], project['topic'])
    if project_tuple not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project_tuple)


print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-16338752333912652679': ['civic_docs'], 'var_function-call-2241076992410809533': 'file_storage/function-call-2241076992410809533.json'}

exec(code, env_args)
