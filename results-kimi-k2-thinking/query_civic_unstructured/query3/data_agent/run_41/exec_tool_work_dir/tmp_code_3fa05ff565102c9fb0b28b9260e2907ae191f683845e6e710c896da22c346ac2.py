code = """import json
import re

# Load the MongoDB query result
mongo_result = locals()['var_functions.query_db:0']

# Parse the result
if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        documents = json.load(f)
else:
    documents = mongo_result

print(f"Number of documents found: {len(documents)}")
print(f"First document filename: {documents[0].get('filename')}")

# Extract project information
def extract_emergency_projects(doc):
    """Extract emergency/FEMA projects from a document"""
    text = doc.get('text', '')
    projects = []
    lower_text = text.lower()
    
    # Find all occurrences of key emergency-related terms
    emergency_terms = ['fema', 'emergency', 'warning siren', 'warning sign', 'disaster recovery']
    
    for term in emergency_terms:
        if term in lower_text:
            term_positions = [m.start() for m in re.finditer(term, lower_text)]
            
            for pos in term_positions:
                # Look for project name patterns around this position
                # Try to capture the project name (usually capitalized or on its own line)
                context = text[max(0, pos-200):min(len(text), pos+300)]
                
                # Try to find project name in the context
                # Common patterns: Title (FEMA Project), Title (CalOES Project)
                lines = context.split('\n')
                for line in lines:
                    line = line.strip()
                    if (term.split()[0].upper() in line or  # FEMA or EMERGENCY in caps
                        '(' in line and 'Project)' in line or  # e.g., (FEMA Project)
                        'warning' in term.lower() and 'warning' in line.lower()):
                        
                        # Skip very short lines or lines that are just status updates
                        if len(line) < 10 or line.startswith('(') or line.startswith(')') or line.startswith('?'):
                            continue
                            
                        # Check if this looks like a project name
                        project_name = line
                        
                        # Try to find status in nearby text
                        status = None
                        if 'completed' in lower_text or 'complete construction' in lower_text:
                            status = 'completed'
                        elif 'design' in lower_text or 'planning' in lower_text:
                            status = 'design'
                        elif 'not started' in lower_text:
                            status = 'not started'
                        else:
                            status = 'unknown'
                        
                        # Try to find more specific info
                        topic = 'emergency, FEMA'
                        if 'fire' in lower_text:
                            topic += ', fire'
                        elif 'drainage' in lower_text or 'storm' in lower_text:
                            topic += ', drainage'
                        elif 'warning' in lower_text or 'siren' in lower_text:
                            topic = 'emergency warning'
                        
                        projects.append({
                            'Project_Name': project_name,
                            'topic': topic,
                            'type': 'disaster',
                            'status': status,
                            'source_file': doc.get('filename')
                        })
                        break  # Take the first relevant line
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in documents:
    doc_projects = extract_emergency_projects(doc)
    all_projects.extend(doc_projects)

# Remove duplicates based on project name (normalized)
unique_projects = {}
for proj in all_projects:
    # Normalize project name for deduplication
    norm_name = proj['Project_Name'].strip()
    if norm_name and norm_name not in unique_projects:
        unique_projects[norm_name] = proj

result_list = list(unique_projects.values())

print(f"\nExtracted {len(result_list)} unique emergency/FEMA projects")
print(f"Sample projects: {result_list[:2]}")

result = json.dumps(result_list)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
