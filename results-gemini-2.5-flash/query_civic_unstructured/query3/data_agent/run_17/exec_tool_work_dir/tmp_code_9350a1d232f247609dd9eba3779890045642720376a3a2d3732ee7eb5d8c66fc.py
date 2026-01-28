code = """import json
import re

# Load the full result from the file
with open(locals()['var_function-call-14735836657967561594'], 'r') as f:
    documents = json.load(f)

extracted_projects = []

for doc in documents:
    text = doc['text']
    
    # Identify project sections and their general type/status
    lines = text.split('\n')
    
    current_section_type = None
    current_section_status = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        if "Capital Improvement Projects (Design)" in line:
            current_section_type = "capital"
            current_section_status = "design"
        elif "Capital Improvement Projects (Construction)" in line:
            current_section_type = "capital"
            current_section_status = "construction"
        elif "Capital Improvement Projects (Not Started)" in line:
            current_section_type = "capital"
            current_section_status = "not started"
        elif "Disaster Recovery Projects" in line:
            current_section_type = "disaster"
            current_section_status = "various" # Status will be more specific per project
        
        # Look for project names
        # Project names are often followed by (cid:190) Updates: or (cid:190) Project Schedule:
        # Or they are listed directly under a section heading.
        
        project_name_match = re.search(r'\n\n([A-Za-z0-9][A-Za-z0-9 &-,/\']+(?: Project)?(?: Phase \d)?)(?:\n\(cid:190) Updates:|\n\(cid:190) Project Description:|\n\(cid:190) Estimated Schedule:)', text[text.find(line):])
        
        if project_name_match:
            project_name = project_name_match.group(1).strip()
            
            # Extract status (if not explicitly set by section)
            status = current_section_status
            if "(Updates: Project is currently under construction)" in text[text.find(project_name):] or "(Updates: Project is currently out to bid)" in text[text.find(project_name):]:
                status = "construction"
            elif "Construction was completed" in text[text.find(project_name):] or "Notice of completion filed" in text[text.find(project_name):]:
                status = "completed"
            elif "Project is in the preliminary design phase" in text[text.find(project_name):] or "Staff is working with the consultant to finalize the design plans" in text[text.find(project_name):]:
                status = "design"
            
            # Extract topic
            topic_keywords = []
            if "emergency" in project_name.lower() or "emergency" in text[text.find(project_name):].lower():
                topic_keywords.append("emergency")
            if "FEMA" in project_name or "FEMA" in text[text.find(project_name):]:
                topic_keywords.append("FEMA")
            if "storm drain" in project_name.lower() or "storm drain" in text[text.find(project_name):].lower():
                topic_keywords.append("storm drain")
            if "fire" in project_name.lower() or "fire" in text[text.find(project_name):].lower():
                topic_keywords.append("fire")
            if "drainage" in project_name.lower() or "drainage" in text[text.find(project_name):].lower():
                topic_keywords.append("drainage")
            if "disaster" in project_name.lower() or "disaster" in text[text.find(project_name):].lower():
                topic_keywords.append("disaster")

            # Extract type
            project_type = current_section_type
            if "Disaster Recovery Projects" in text[text.find(project_name):text.find(project_name) + 200] and project_type != "disaster": # Check nearby text for type if not set by section
                project_type = "disaster"
            elif "Capital Improvement Projects" in text[text.find(project_name):text.find(project_name) + 200] and project_type != "capital":
                project_type = "capital"
            
            # Remove duplicates and join
            topic = ", ".join(sorted(list(set(topic_keywords))))
            
            extracted_projects.append({
                "Project_Name": project_name,
                "topic": topic if topic else None,
                "type": project_type,
                "status": status
            })

# Filter for unique projects (name, type, status, topic)
unique_projects = []
seen_projects = set()

for project in extracted_projects:
    project_tuple = (project["Project_Name"], project["type"], project["status"], project["topic"])
    if project_tuple not in seen_projects:
        unique_projects.append(project)
        seen_projects.add(project_tuple)


# Further refine and filter for 'emergency' or 'FEMA' in topic
final_projects = []
for project in unique_projects:
    if project["topic"] and ("emergency" in project["topic"].lower() or "fema" in project["topic"].lower()):
        final_projects.append(project)

print("__RESULT__:")
print(json.dumps(final_projects)))"""

env_args = {'var_function-call-15574106946328272683': ['civic_docs'], 'var_function-call-14735836657967561594': 'file_storage/function-call-14735836657967561594.json'}

exec(code, env_args)
