code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# A more robust pattern to capture project name and its content
# It tries to find a project name line, then captures everything until the next project name or end of relevant section
# Using raw string literals for regex to avoid issues with backslashes
project_section_regex = r'(\n(?:[A-Z][a-zA-Z0-9 &\'\-,.\(\)]*\s(?:Project|Projects|Plan|Improvements|Study))(?=\n|\s*\(cid:190\).*?|\s*(?:Project|Updates|Schedule|Description):.*?))((?:.|\n)*?)(?=\n(?:[A-Z][a-zA-Z0-9 &\'\-,.\(\)]*\s(?:Project|Projects|Plan|Improvements|Study))(?=\n|\s*\(cid:190\).*?|\s*(?:Project|Updates|Schedule|Description):.*?)|Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|\Z)'

for doc in civic_docs:
    text = doc['text']
    
    # Use re.finditer to get all matches with start and end positions
    # This helps in splitting the document into logical project blocks
    matches = re.finditer(project_section_regex, text, re.DOTALL | re.IGNORECASE)

    for match in matches:
        project_name = match.group(1).strip()
        project_details = match.group(2).strip()
        
        # Filter for relevant projects based on keywords
        if (re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', project_name + " " + project_details, re.IGNORECASE)):
            
            status = "unknown"
            if re.search(r'design|preliminary design|complete design|awaiting.*?approval', project_details, re.IGNORECASE):
                status = "design"
            elif re.search(r'completed|construction was completed|notice of completion filed', project_details, re.IGNORECASE):
                status = "completed"
            elif re.search(r'not started|not begun', project_details, re.IGNORECASE):
                status = "not started"
            elif re.search(r'under construction|out to bid|begin construction', project_details, re.IGNORECASE):
                status = "construction"

            project_type = "unknown"
            if re.search(r'disaster recovery projects|disaster', project_name + " " + project_details, re.IGNORECASE):
                project_type = "disaster"
            elif re.search(r'capital improvement projects|capital', project_name + " " + project_details, re.IGNORECASE):
                project_type = "capital"
            
            topic_keywords = []
            if re.search(r'park', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("park")
            if re.search(r'road', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("road")
            if re.search(r'FEMA', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("FEMA")
            if re.search(r'fire', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("fire")
            if re.search(r'emergency warning|outdoor warning signs', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("emergency warning")
            if re.search(r'drainage|storm drain', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("drainage")
            if re.search(r'capital', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("capital")
            if re.search(r'disaster', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("disaster")
            if re.search(r'traffic signals|backup power', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
            if re.search(r'CalOES', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("CalOES")
            if re.search(r'retaining wall', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("retaining wall")
            if re.search(r'emergency', project_name + " " + project_details, re.IGNORECASE): topic_keywords.append("emergency")

            topic = ", ".join(sorted(list(set(topic_keywords))))
            if not topic: topic = "general"

            projects_data.append({
                "Project_Name": project_name.replace("(cid:190)", "").strip(), # Clean up (cid:190) which sometimes appears in project name due to bad parsing
                "topic": topic,
                "type": project_type,
                "status": status
            })

# Deduplicate projects based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects_data:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json'}

exec(code, env_args)
