code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Find all potential project lines and their following content
    # This regex tries to capture a project name line and everything until the next project line or end of document.
    # Using a slightly simplified character set for project names to avoid potential escaping issues.
    project_blocks = re.findall(r'([A-Z][a-zA-Z0-9 &\'\-,\.\(\)]+\s(?:Project|Projects)?)(.*?)(?=\n[A-Z][a-zA-Z0-9 &\'\-,\.\(\)]+\s(?:Project|Projects)?|\Z)', text, re.DOTALL)
    
    for project_name_raw, project_details in project_blocks:
        project_name = project_name_raw.strip()

        # Filter for relevant projects based on keywords in name or details
        if re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning signs|traffic signals backup power', project_name, re.IGNORECASE) or \
           re.search(r'emergency|FEMA|disaster|CalOES', project_details, re.IGNORECASE):
            
            status = "unknown"
            if re.search(r'status:\s*design|in preliminary design phase|complete design:|awaiting final FEMA/CalOES approval', project_details, re.IGNORECASE):
                status = "design"
            elif re.search(r'status:\s*completed|construction was completed|notice of completion filed', project_details, re.IGNORECASE):
                status = "completed"
            elif re.search(r'status:\s*not started|not begun', project_details, re.IGNORECASE):
                status = "not started"
            elif re.search(r'under construction|project is currently out to bid|begin construction:', project_details, re.IGNORECASE):
                status = "construction"

            project_type = "unknown"
            if re.search(r'disaster recovery projects|disaster', project_name + project_details, re.IGNORECASE):
                project_type = "disaster"
            elif re.search(r'capital improvement projects|capital', project_name + project_details, re.IGNORECASE):
                project_type = "capital"
            
            topic_keywords = []
            if re.search(r'park', project_name + project_details, re.IGNORECASE): topic_keywords.append("park")
            if re.search(r'road', project_name + project_details, re.IGNORECASE): topic_keywords.append("road")
            if re.search(r'FEMA', project_name + project_details, re.IGNORECASE): topic_keywords.append("FEMA")
            if re.search(r'fire', project_name + project_details, re.IGNORECASE): topic_keywords.append("fire")
            if re.search(r'emergency warning|outdoor warning signs', project_name + project_details, re.IGNORECASE): topic_keywords.append("emergency warning")
            if re.search(r'drainage|storm drain', project_name + project_details, re.IGNORECASE): topic_keywords.append("drainage")
            if re.search(r'capital', project_name + project_details, re.IGNORECASE): topic_keywords.append("capital")
            if re.search(r'disaster', project_name + project_details, re.IGNORECASE): topic_keywords.append("disaster")
            if re.search(r'traffic signals|backup power', project_name + project_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
            if re.search(r'CalOES', project_name + project_details, re.IGNORECASE): topic_keywords.append("CalOES")
            if re.search(r'retaining wall', project_name + project_details, re.IGNORECASE): topic_keywords.append("retaining wall")

            topic = ", ".join(sorted(list(set(topic_keywords))))
            if not topic: topic = "general"

            projects.append({
                "Project_Name": project_name,
                "topic": topic,
                "type": project_type,
                "status": status
            })

# Filter out duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json'}

exec(code, env_args)
