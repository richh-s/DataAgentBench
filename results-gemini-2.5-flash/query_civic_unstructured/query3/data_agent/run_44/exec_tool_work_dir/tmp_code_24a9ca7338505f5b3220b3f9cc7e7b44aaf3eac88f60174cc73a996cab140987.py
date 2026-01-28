code = """import json
import re

def parse_civic_document_v6(text):
    projects = []
    lines = text.split('\\n')
    current_type = None
    current_status = None
    
    project_accumulator = None # Holds the current project being built
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Update section type and status
        if re.search(r'Capital Improvement Projects \\(Design\\)', line_stripped):
            current_type = 'capital'
            current_status = 'design'
            continue
        elif re.search(r'Capital Improvement Projects \\(Construction\\)', line_stripped):
            current_type = 'capital'
            current_status = 'under construction'
            continue
        elif re.search(r'Capital Improvement Projects \\(Not Started\\)', line_stripped):
            current_type = 'capital'
            current_status = 'not started'
            continue
        elif re.search(r'Disaster Recovery Projects', line_stripped):
            current_type = 'disaster'
            current_status = 'disaster recovery'
            continue

        # Project name identification heuristic:
        # A non-empty line, not a known header, and is potentially a project name if followed by '(cid:190)' in next lines.
        # Also, filter out lines that are too short to be a project name or known non-project phrases.
        is_potential_project_name = False
        if line_stripped and len(line_stripped) > 5 and not any(re.search(keyword, line_stripped, re.IGNORECASE) for keyword in [
            'Public Works Commission', 'Agenda Report', 'RECOMMENDED ACTION', 'Updates:', 'Project Description:', 'Project Schedule:', 'Estimated Schedule:', 'DISCUSSION:'
        ]):
            # Look ahead for a few lines to find a '(cid:190)' marker, indicating project details follow
            for j in range(i + 1, min(i + 5, len(lines))):
                if '(cid:190)' in lines[j]:
                    is_potential_project_name = True
                    break

        if is_potential_project_name and current_type and current_status:
            # If we were accumulating a previous project, finalize it
            if project_accumulator and 'Project_Name' in project_accumulator:
                project_topic = []
                details_text = '\\n'.join(project_accumulator['details'])
                if re.search(r'emergency', details_text, re.IGNORECASE):
                    project_topic.append('emergency')
                if re.search(r'FEMA', details_text, re.IGNORECASE):
                    project_topic.append('FEMA')
                
                if project_topic:
                    project_accumulator['topic'] = ', '.join(project_topic)
                    projects.append(project_accumulator)

            # Start a new project
            project_accumulator = {
                'Project_Name': line_stripped,
                'status': current_status,
                'type': current_type,
                'details': [] # To accumulate all lines related to this project until next project or section
            }
        elif project_accumulator:
            # Continue accumulating details for the current project
            project_accumulator['details'].append(line_stripped)
    
    # Add the last accumulated project if any
    if project_accumulator and 'Project_Name' in project_accumulator:
        project_topic = []
        details_text = '\\n'.join(project_accumulator['details'])
        if re.search(r'emergency', details_text, re.IGNORECASE):
            project_topic.append('emergency')
        if re.search(r'FEMA', details_text, re.IGNORECASE):
            project_topic.append('FEMA')
        
        if project_topic:
            project_accumulator['topic'] = ', '.join(project_topic)
            projects.append(project_accumulator)

    # Filter for projects with emergency or FEMA topic only
    return [p for p in projects if 'topic' in p and ('emergency' in p['topic'] or 'FEMA' in p['topic'])]

all_projects = []
with open(locals()['var_function-call-5052213206219168496'], 'r') as f:
    docs = json.load(f)

for doc in docs:
    all_projects.extend(parse_civic_document_v6(doc['text']))

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in all_projects:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-5052213206219168496': 'file_storage/function-call-5052213206219168496.json'}

exec(code, env_args)
