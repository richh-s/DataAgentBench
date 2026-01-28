code = """import json
import re

# Access the civic documents data
civic_docs_key = 'var_functions.query_db:5'
civic_docs_data = locals().get(civic_docs_key)

# If it's a file path, load the data
if isinstance(civic_docs_data, str) and '/tmp/' in civic_docs_data:
    with open(civic_docs_data, 'r') as f:
        civic_docs_data = json.load(f)

# Access the funding data
funding_key = 'var_functions.query_db:6'
funding_data = locals().get(funding_key)

# If it's a file path, load the data
if isinstance(funding_data, str) and '/tmp/' in funding_data:
    with open(funding_data, 'r') as f:
        funding_data = json.load(f)

# Function to extract projects from civic documents text
def extract_projects_from_text(text):
    projects = []
    
    # Patterns to identify project sections
    project_patterns = [
        r'([A-Z][^\n]+?)\n\s*\(cid:190\)\s*Updates:',
        r'([A-Z][^\n]+?)\n\s*\(cid:190\)\s*Project Description:',
        r'([A-Z][^\n]+?)\n\s*\(cid:190\)\s*Project Schedule:'
    ]
    
    for pattern in project_patterns:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_name = match.group(1).strip()
            
            # Find the text block for this project
            start_pos = match.start()
            # Look for the next project or end of text
            next_project_pos = len(text)
            for p in project_patterns:
                next_match = re.search(p, text[start_pos + 1:])
                if next_match:
                    potential_pos = start_pos + 1 + next_match.start()
                    if potential_pos < next_project_pos:
                        next_project_pos = potential_pos
            
            project_text = text[start_pos:next_project_pos]
            
            # Extract status information
            status = None
            if 'completed' in project_text.lower():
                status = 'completed'
            elif 'design' in project_text.lower() and 'complete design' not in project_text.lower():
                status = 'design'
            elif 'not started' in project_text.lower():
                status = 'not started'
            elif 'construction' in project_text.lower():
                # Check if it's completed or in progress
                if re.search(r'complete[d]? construction|construction was completed', project_text, re.I):
                    status = 'completed'
                else:
                    status = 'construction'
            
            # Extract dates
            dates = []
            date_patterns = [
                r'(\d{4})-Spring',
                r'(\d{4})-Fall',
                r'(\d{4})-Summer',
                r'(\d{4})[-\s](January|February|March|April|May|June|July|August|September|October|November|December)',
                r'(\d{4})[-\s](\d{1,2})',
                r'(January|February|March|April|May|June|July|August|September|October|November|December)[\s]+(\d{4})',
                r'(\d{4})'
            ]
            
            for dp in date_patterns:
                matches = re.finditer(dp, project_text)
                for m in matches:
                    dates.append(m.group(0))
            
            # Determine type (capital or disaster)
            project_type = 'capital'  # default
            if 'FEMA' in project_text or 'CalOES' in project_text or 'CalJPIA' in project_text:
                project_type = 'disaster'
            elif re.search(r'Park|road|drainage|streets|walkway|bridge|guardrail|traffic|signal|playground', project_name, re.I):
                project_type = 'capital'
            
            # Determine topic
            topic_parts = []
            if re.search(r'Park|park', project_name):
                topic_parts.append('park')
            if re.search(r'road|street|highway', project_name, re.I):
                topic_parts.append('road')
            if re.search(r'drainage|storm', project_name, re.I):
                topic_parts.append('drainage')
            if re.search(r'FEMA|fire', project_name, re.I):
                topic_parts.append('FEMA')
            if re.search(r'emergency|warning|siren', project_name, re.I):
                topic_parts.append('emergency warning')
            
            topic = ','.join(topic_parts) if topic_parts else 'general'
            
            projects.append({
                'Project_Name': project_name,
                'topic': topic,
                'status': status,
                'type': project_type,
                'dates': dates
            })
    
    return projects

# Extract all projects from all documents
all_projects = []
for doc in civic_docs_data:
    projects = extract_projects_from_text(doc.get('text', ''))
    all_projects.extend(projects)

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(all_projects),
    'sample_projects': all_projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'civic_docs_count': 38, 'funding_records_count': 38, 'status': 'Data loaded successfully'}}

exec(code, env_args)
