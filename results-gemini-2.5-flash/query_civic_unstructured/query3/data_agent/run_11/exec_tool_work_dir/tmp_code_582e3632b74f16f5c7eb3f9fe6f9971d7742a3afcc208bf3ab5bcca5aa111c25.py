code = """import json
import re

file_path = locals()['var_function-call-4455202454282602494']
with open(file_path, 'r') as f:
    civic_docs_results = json.load(f)

extracted_projects = []

for doc in civic_docs_results:
    text = doc['text']
    
    # Using standard string literal and explicit escaping for the regex
    project_pattern = re.compile("\n([A-Z][a-zA-Z0-9\\s&,-]*?(?:Project|Improvements|Study|Plan|Repairs|Facility|Lane|System|Power|Signs|Walkway|Playground|Road|Drainage|Filter|Signals|Treatment))\n\\(cid:190\\) Updates:", re.MULTILINE)
    
    # Find all potential project sections
    project_sections = project_pattern.split(text)
    
    # The split method will return a list where even indices are the text before the match, and odd indices are the captured groups.
    # The first element (index 0) will be the text before the first project, which we can ignore.
    for i in range(1, len(project_sections), 2):
        project_name = project_sections[i].strip()
        details_text = project_sections[i+1] if (i+1) < len(project_sections) else ""

        # Check for 'emergency' or 'FEMA' in the project name or its details
        if re.search(r'(emergency|FEMA)', project_name, re.IGNORECASE) or re.search(r'(emergency|FEMA)', details_text, re.IGNORECASE):
            
            status = "unknown"
            if re.search(r'status:\s*(.+?)(?:\n|;)', details_text, re.IGNORECASE):
                 status_match = re.search(r'status:\s*(.+?)(?:\n|;)', details_text, re.IGNORECASE)
                 status = status_match.group(1).strip()
            elif re.search(r'Updates:\s*Project is currently under construction', details_text, re.IGNORECASE):
                status = "under construction"
            elif re.search(r'Construction was completed', details_text, re.IGNORECASE):
                status = "completed"
            elif re.search(r'Project is delayed', details_text, re.IGNORECASE) or re.search(r'pending', details_text, re.IGNORECASE):
                status = "delayed"
            elif re.search(r'preliminary design phase', details_text, re.IGNORECASE) or re.search(r'Complete Design', details_text, re.IGNORECASE):
                status = "design"
            elif re.search(r'not started', details_text, re.IGNORECASE) or re.search(r'identified but not begun', details_text, re.IGNORECASE):
                status = "not started"

            
            project_type = "unknown"
            if re.search(r'Capital Improvement Projects', text, re.IGNORECASE) or re.search(r'CIP', text, re.IGNORECASE):
                project_type = "capital"
            if re.search(r'Disaster Recovery Projects', text, re.IGNORECASE):
                project_type = "disaster"

            topic = []
            if re.search(r'emergency', project_name + details_text, re.IGNORECASE):
                topic.append('emergency')
            if re.search(r'FEMA', project_name + details_text, re.IGNORECASE):
                topic.append('FEMA')
            if re.search(r'fire', project_name + details_text, re.IGNORECASE):
                topic.append('fire')
            if re.search(r'storm drain|drainage', project_name + details_text, re.IGNORECASE):
                topic.append('storm drain')
            if re.search(r'water treatment', project_name + details_text, re.IGNORECASE):
                topic.append('water treatment')
            if re.search(r'road', project_name + details_text, re.IGNORECASE):
                topic.append('road')
            if re.search(r'park', project_name + details_text, re.IGNORECASE):
                topic.append('park')
            if re.search(r'traffic', project_name + details_text, re.IGNORECASE):
                topic.append('traffic')
            if re.search(r'warning', project_name + details_text, re.IGNORECASE):
                topic.append('emergency warning')
            if re.search(r'slopes repair', project_name + details_text, re.IGNORECASE):
                topic.append('slopes repair')

            extracted_projects.append({
                'Project_Name': project_name,
                'status': status,
                'type': project_type,
                'topic': ', '.join(list(set(topic))) # Use set to avoid duplicate topics
            })

# Filter out projects without a clear name or that are too generic
filtered_projects = [p for p in extracted_projects if p['Project_Name'] and len(p['Project_Name']) > 5]


__RESULT__:
print(json.dumps(filtered_projects))"""

env_args = {'var_function-call-11970460531683141501': ['civic_docs'], 'var_function-call-4455202454282602494': 'file_storage/function-call-4455202454282602494.json'}

exec(code, env_args)
