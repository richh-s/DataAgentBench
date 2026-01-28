code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# Regex to identify a project title line. This should be a distinct line.
# Using a more robust pattern to catch variations and avoid over-matching.
# \\s* ensures optional whitespace around the title.
project_title_pattern = re.compile(r'^\\s*([A-Z][a-zA-Z0-9 &'\-,.\(\)\\xC2\\xA0]*(?:Project|Projects|Plan|Improvements|Study|Program|Report|Improvements|Update|Master Plan|Study))\\s*$', re.MULTILINE)

# Keywords to filter projects and extract topics/types/statuses
relevant_keywords = ['emergency', 'fema', 'disaster', 'caloes', 'outdoor warning', 'traffic signals backup']
status_keywords = {
    'design': ['design', 'preliminary design', 'complete design', 'awaiting approval'],
    'completed': ['completed', 'construction was completed', 'notice of completion filed'],
    'not started': ['not started', 'not begun'],
    'construction': ['under construction', 'out to bid', 'begin construction']
}
type_keywords = {
    'disaster': ['disaster recovery projects', 'disaster'],
    'capital': ['capital improvement projects', 'capital']
}
topic_keywords_map = {
    'park': ['park'],
    'road': ['road'],
    'FEMA': ['fema'],
    'fire': ['fire'],
    'emergency warning': ['emergency warning', 'outdoor warning signs'],
    'drainage': ['drainage', 'storm drain'],
    'capital': ['capital'],
    'disaster': ['disaster'],
    'traffic signals & backup power': ['traffic signals', 'backup power'],
    'CalOES': ['caloes'],
    'retaining wall': ['retaining wall'],
    'emergency': ['emergency']
}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details = []

    for line in lines:
        line = line.strip()
        if not line: # Skip empty lines
            continue

        # Check if the line is a potential project title
        title_match = project_title_pattern.match(line)
        if title_match:
            # If we were tracking a previous project, process it
            if current_project_name:
                full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
                
                if any(keyword in full_project_text for keyword in relevant_keywords):
                    status = "unknown"
                    for s_key, s_terms in status_keywords.items():
                        if any(term in full_project_text for term in s_terms):
                            status = s_key
                            break

                    project_type = "unknown"
                    for t_key, t_terms in type_keywords.items():
                        if any(term in full_project_text for term in t_terms):
                            project_type = t_key
                            break
                    
                    topics_found = []
                    for topic_name, topic_terms in topic_keywords_map.items():
                        if any(term in full_project_text for term in topic_terms):
                            topics_found.append(topic_name)
                    topic = ", ".join(sorted(list(set(topics_found))))
                    if not topic: topic = "general"

                    projects_data.append({
                        "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                        "topic": topic,
                        "type": project_type,
                        "status": status
                    })
            
            # Start a new project
            current_project_name = title_match.group(1).strip() # Extract cleaned title
            current_project_details = []
        elif current_project_name: # Accumulate details if a project is being tracked
            current_project_details.append(line)
            
    # Process the last project after the loop ends
    if current_project_name:
        full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
        if any(keyword in full_project_text for keyword in relevant_keywords):
            status = "unknown"
            for s_key, s_terms in status_keywords.items():
                if any(term in full_project_text for term in s_terms):
                    status = s_key
                    break

            project_type = "unknown"
            for t_key, t_terms in type_keywords.items():
                if any(term in full_project_text for term in t_terms):
                    project_type = t_key
                    break
            
            topics_found = []
            for topic_name, topic_terms in topic_keywords_map.items():
                if any(term in full_project_text for term in topic_terms):
                    topics_found.append(topic_name)
            topic = ", ".join(sorted(list(set(topics_found))))
            if not topic: topic = "general"

            projects_data.append({
                "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                "topic": topic,
                "type": project_type,
                "status": status
            })


# Deduplicate projects based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects_data:
    # Normalize project name for deduplication (e.g., remove trailing 'Project' if it's inconsistent)
    normalized_name = re.sub(r'\\s*(?:Project|Projects|Plan|Improvements|Study|Program|Report|Update|Master Plan|Study)$', '', p['Project_Name'], flags=re.IGNORECASE).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(normalized_name)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding']}

exec(code, env_args)
