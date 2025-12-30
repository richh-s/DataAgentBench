code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# Regex to identify potential project name lines. More restrictive to avoid capturing general text.
# It looks for lines that start with a capital letter and likely contain "Project", "Plan", etc.
project_name_regex = re.compile(r'^[A-Z][a-zA-Z0-9 &\'\-,.\(\)]*(?:\s(?:Project|Projects|Plan|Improvements|Study))\s*$', re.MULTILINE)

# Regex for major section headers that delimit projects
section_header_regex = re.compile(r'^(?:Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)$', re.MULTILINE)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details = []

    for line in lines:
        line = line.strip()

        # Skip empty lines and purely bullet point lines
        if not line or re.match(r'^(?:\(cid:\d+\)|\*|-)\s*$', line):
            continue

        # Check if the line is a major section header
        if section_header_regex.match(line):
            # If a project was being tracked, process it before resetting
            if current_project_name:
                full_details = ' '.join(current_project_details)
                if re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', current_project_name + ' ' + full_details, re.IGNORECASE):
                    # Extract status, type, topic
                    status = "unknown"
                    if re.search(r'design|preliminary design|complete design|awaiting.*?approval', full_details, re.IGNORECASE):
                        status = "design"
                    elif re.search(r'completed|construction was completed|notice of completion filed', full_details, re.IGNORECASE):
                        status = "completed"
                    elif re.search(r'not started|not begun', full_details, re.IGNORECASE):
                        status = "not started"
                    elif re.search(r'under construction|out to bid|begin construction', full_details, re.IGNORECASE):
                        status = "construction"

                    project_type = "unknown"
                    if re.search(r'disaster recovery projects|disaster', current_project_name + ' ' + full_details, re.IGNORECASE):
                        project_type = "disaster"
                    elif re.search(r'capital improvement projects|capital', current_project_name + ' ' + full_details, re.IGNORECASE):
                        project_type = "capital"
                    
                    topic_keywords = []
                    if re.search(r'park', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("park")
                    if re.search(r'road', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("road")
                    if re.search(r'FEMA', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("FEMA")
                    if re.search(r'fire', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("fire")
                    if re.search(r'emergency warning|outdoor warning signs', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency warning")
                    if re.search(r'drainage|storm drain', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("drainage")
                    if re.search(r'capital', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("capital")
                    if re.search(r'disaster', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("disaster")
                    if re.search(r'traffic signals|backup power', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
                    if re.search(r'CalOES', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("CalOES")
                    if re.search(r'retaining wall', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("retaining wall")
                    if re.search(r'emergency', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency")

                    topic = ", ".join(sorted(list(set(topic_keywords))))
                    if not topic: topic = "general"

                    projects_data.append({
                        "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                        "topic": topic,
                        "type": project_type,
                        "status": status
                    })
            current_project_name = None
            current_project_details = []
            continue

        # Check if the line is a potential project name (starts a new project block)
        name_match = project_name_regex.match(line)
        if name_match:
            # If a project was being tracked, process it before starting a new one
            if current_project_name:
                full_details = ' '.join(current_project_details)
                if re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', current_project_name + ' ' + full_details, re.IGNORECASE):
                    # Extract status, type, topic
                    status = "unknown"
                    if re.search(r'design|preliminary design|complete design|awaiting.*?approval', full_details, re.IGNORECASE):
                        status = "design"
                    elif re.search(r'completed|construction was completed|notice of completion filed', full_details, re.IGNORECASE):
                        status = "completed"
                    elif re.search(r'not started|not begun', full_details, re.IGNORECASE):
                        status = "not started"
                    elif re.search(r'under construction|out to bid|begin construction', full_details, re.IGNORECASE):
                        status = "construction"

                    project_type = "unknown"
                    if re.search(r'disaster recovery projects|disaster', current_project_name + ' ' + full_details, re.IGNORECASE):
                        project_type = "disaster"
                    elif re.search(r'capital improvement projects|capital', current_project_name + ' ' + full_details, re.IGNORECASE):
                        project_type = "capital"
                    
                    topic_keywords = []
                    if re.search(r'park', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("park")
                    if re.search(r'road', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("road")
                    if re.search(r'FEMA', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("FEMA")
                    if re.search(r'fire', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("fire")
                    if re.search(r'emergency warning|outdoor warning signs', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency warning")
                    if re.search(r'drainage|storm drain', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("drainage")
                    if re.search(r'capital', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("capital")
                    if re.search(r'disaster', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("disaster")
                    if re.search(r'traffic signals|backup power', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
                    if re.search(r'CalOES', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("CalOES")
                    if re.search(r'retaining wall', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("retaining wall")
                    if re.search(r'emergency', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency")

                    topic = ", ".join(sorted(list(set(topic_keywords))))
                    if not topic: topic = "general"

                    projects_data.append({
                        "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                        "topic": topic,
                        "type": project_type,
                        "status": status
                    })
            
            current_project_name = name_match.group(1).strip()
            current_project_details = []
        elif current_project_name: # Accumulate details if a project is being tracked
            current_project_details.append(line)
            
    # Process the last project after the loop ends
    if current_project_name:
        full_details = ' '.join(current_project_details)
        if re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', current_project_name + ' ' + full_details, re.IGNORECASE):
            # Extract status, type, topic
            status = "unknown"
            if re.search(r'design|preliminary design|complete design|awaiting.*?approval', full_details, re.IGNORECASE):
                status = "design"
            elif re.search(r'completed|construction was completed|notice of completion filed', full_details, re.IGNORECASE):
                status = "completed"
            elif re.search(r'not started|not begun', full_details, re.IGNORECASE):
                status = "not started"
            elif re.search(r'under construction|out to bid|begin construction', full_details, re.IGNORECASE):
                status = "construction"

            project_type = "unknown"
            if re.search(r'disaster recovery projects|disaster', current_project_name + ' ' + full_details, re.IGNORECASE):
                project_type = "disaster"
            elif re.search(r'capital improvement projects|capital', current_project_name + ' ' + full_details, re.IGNORECASE):
                project_type = "capital"
            
            topic_keywords = []
            if re.search(r'park', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("park")
            if re.search(r'road', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("road")
            if re.search(r'FEMA', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("FEMA")
            if re.search(r'fire', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("fire")
            if re.search(r'emergency warning|outdoor warning signs', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency warning")
            if re.search(r'drainage|storm drain', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("drainage")
            if re.search(r'capital', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("capital")
            if re.search(r'disaster', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("disaster")
            if re.search(r'traffic signals|backup power', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
            if re.search(r'CalOES', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("CalOES")
            if re.search(r'retaining wall', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("retaining wall")
            if re.search(r'emergency', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency")

            topic = ", ".join(sorted(list(set(topic_keywords))))
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
    normalized_name = re.sub(r'\s*(?:Project|Projects|Plan|Improvements|Study)$', '', p['Project_Name'], flags=re.IGNORECASE).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(normalized_name)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding']}

exec(code, env_args)
