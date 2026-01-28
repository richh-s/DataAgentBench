code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# Heuristics for identifying project titles. Avoiding complex regex for the initial scan.
project_title_indicators = ['Project', 'Projects', 'Plan', 'Improvements', 'Study', 'Program', 'Report', 'Update', 'Master Plan', 'Repair', 'Resurfacing', 'Drainage', 'Traffic Study', 'Slopes Repair', 'Water Treatment Facility', 'Skate Park', 'Walkway Repairs', 'Slope Repairs', 'Signals Backup Power', 'Storm Drain Trash Screens']

# Keywords for filtering projects relevant to 'emergency' or 'FEMA'
relevant_keywords_filter = ['emergency', 'fema', 'disaster', 'caloes', 'outdoor warning', 'traffic signals backup', 'fire']

# Keyword maps for extracting status, type, and topics
status_keywords = {
    'design': ['design', 'preliminary design', 'complete design', 'awaiting approval', 'planning phase'],
    'completed': ['completed', 'construction was completed', 'notice of completion filed', 'finished'],
    'not started': ['not started', 'not begun', 'identified but not begun'],
    'construction': ['under construction', 'out to bid', 'begin construction', 'underway']
}
type_keywords = {
    'disaster': ['disaster recovery projects', 'disaster', 'fema', 'caloes', 'fire recovery'],
    'capital': ['capital improvement projects', 'capital', 'infrastructure', 'road', 'park']
}
topic_keywords_map = {
    'park': ['park', 'playground', 'bluffs'],
    'road': ['road', 'highway', 'street', 'avenue', 'traffic', 'lane', 'resurfacing'],
    'FEMA': ['fema'],
    'fire': ['fire', 'woolsey fire'],
    'emergency warning': ['emergency warning', 'outdoor warning signs', 'sirens'],
    'drainage': ['drainage', 'storm drain', 'culvert', 'biofilter'],
    'capital': ['capital', 'infrastructure'],
    'disaster': ['disaster', 'recovery'],
    'traffic signals & backup power': ['traffic signals', 'backup power'],
    'CalOES': ['caloes'],
    'retaining wall': ['retaining wall', 'slope repair'],
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

        # Check if the line is a potential project title using basic heuristics
        is_project_title = False
        if line[0].isupper() and any(indicator.lower() in line.lower() for indicator in project_title_indicators):
            # Further filter out common non-project titles or general section headers
            if not (line.startswith('To:') or line.startswith('Prepared by:') or line.startswith('Approved by:') or \
                    line.startswith('Date prepared:') or line.startswith('Meeting date:') or line.startswith('Subject:') or \
                    line.startswith('RECOMMENDED ACTION:') or line.startswith('DISCUSSION:') or \
                    'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line or \
                    re.match(r'^Agenda Item # \d.\w.$|^Page \d of \d$', line)):
                 is_project_title = True
        
        # Add specific project titles that might not fit the general pattern but are known to be projects
        # These are explicit checks for project names seen in the document
        if "Latigo Canyon Road Retaining Wall Repair Project" == line: is_project_title = True
        if "Outdoor Warning Signs" == line: is_project_title = True
        if "City Traffic Signals Backup Power" == line: is_project_title = True
        if "2022 Morning View Resurfacing & Storm Drain Improvements" == line: is_project_title = True
        if "PCH Median Improvements Project" == line: is_project_title = True
        if "Trancas Canyon Park Upper and Lower Slopes Repair" == line: is_project_title = True

        if is_project_title:
            # If we were collecting details for a previous project, process it
            if current_project_name:
                full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
                
                if any(keyword in full_project_text for keyword in relevant_keywords_filter):
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
            current_project_name = line
            current_project_details = []
        elif current_project_name: # Accumulate details if a project is currently being tracked
            current_project_details.append(line)
            
    # After the loop, process the very last project if it was being tracked
    if current_project_name:
        full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
        if any(keyword in full_project_text for keyword in relevant_keywords_filter):
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


# Deduplicate projects based on Project_Name (normalized)
unique_projects = []
seen_project_names = set()
for p in projects_data:
    normalized_name = re.sub(r'\s*(?:Project|Projects|Plan|Improvements|Study|Program|Report|Update|Master Plan)$', '', p['Project_Name'], flags=re.IGNORECASE).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(normalized_name)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding'], 'var_function-call-18081243149010549445': 'file_storage/function-call-18081243149010549445.json'}

exec(code, env_args)
