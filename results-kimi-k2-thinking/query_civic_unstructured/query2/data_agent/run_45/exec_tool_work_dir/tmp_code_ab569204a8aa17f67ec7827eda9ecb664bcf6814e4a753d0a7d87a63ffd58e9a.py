code = """import json
import re

# Load the civic documents from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data from the file
funding_file_path = var_functions.query_db:2
with open(funding_file_path, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into sections to find project information
    # Look for patterns like project names followed by updates
    lines = text.split('\n')
    
    current_project = None
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Look for project name patterns (often on their own line or as headings)
        # Common patterns: project names that are title case and don't start with bullet points
        if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('-') and not line.startswith('□'):
            # Check if this line looks like a project name (length check, contains words like "Project", "Improvements", etc.)
            if len(line) > 10 and ('Project' in line or 'Improvements' in line or 'Repairs' in line or 'Replacement' in line):
                # This might be a project name
                project_name = line
                
                # Look ahead for status and date information
                j = i + 1
                status = None
                completion_date = None
                topic_keywords = []
                
                # Scan next few lines for status and completion info
                while j < min(i + 20, len(lines)):
                    next_line = lines[j].strip()
                    
                    # Look for completion status
                    if 'completed' in next_line.lower():
                        status = 'completed'
                        # Look for date in same line or next few lines
                        if '2022' in next_line:
                            completion_date = '2022'
                        elif j + 1 < len(lines) and '2022' in lines[j + 1]:
                            completion_date = '2022'
                    
                    # Look for topic keywords (park, road, etc.)
                    if 'park' in next_line.lower():
                        topic_keywords.append('park')
                    if 'road' in next_line.lower():
                        topic_keywords.append('road')
                    if 'drainage' in next_line.lower() or 'storm drain' in next_line.lower():
                        topic_keywords.append('drainage')
                    
                    j += 1
                
                # If we found a completion date and park topic, add it
                if status == 'completed' and completion_date == '2022':
                    if 'park' in project_name.lower() or 'park' in ' '.join(topic_keywords):
                        projects.append({
                            'Project_Name': project_name,
                            'topic': 'park',
                            'status': 'completed',
                            'et': '2022',
                            'source_file': filename
                        })
        
        i += 1

# Also look for more structured patterns like "Construction was completed November 2022"
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find all occurrences of completion statements
    completion_patterns = [
        r'Construction was completed[\s,]*([^\.\n]+2022)',
        r'completed[\s,]*([^\.\n]+2022)',
    ]
    
    for pattern in completion_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Look backwards to find project name
            start_pos = max(0, match.start() - 500)  # Look up to 500 chars before
            context = text[start_pos:match.start()]
            
            # Try to extract project name from context
            lines = context.split('\n')
            project_name = None
            
            # Look for project name in the preceding lines (usually a heading)
            for line in reversed(lines[-10:]):  # Check last 10 lines
                line = line.strip()
                if line and len(line) > 10 and not line.startswith('(') and not line.startswith('•'):
                    if 'Project' in line or 'Improvements' in line or 'Repairs' in line or 'Replacement' in line:
                        project_name = line
                        break
            
            if project_name:
                # Check if it's park-related
                if 'park' in project_name.lower() or 'park' in text.lower():
                    projects.append({
                        'Project_Name': project_name,
                        'topic': 'park',
                        'status': 'completed',
                        'et': '2022',
                        'source_file': filename
                    })

print(f"Found {len(projects)} park-related projects completed in 2022")
for p in projects:
    print(f"  - {p['Project_Name']}")

# Convert to JSON-serializable string
result = json.dumps(projects)
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
