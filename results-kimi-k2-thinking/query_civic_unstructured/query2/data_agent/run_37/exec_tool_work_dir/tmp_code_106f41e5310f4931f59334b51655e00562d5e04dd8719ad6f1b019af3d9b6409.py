code = """import json
import re
import pandas as pd

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Function to extract project information from civic documents
def extract_projects_from_docs(docs):
    projects = []
    
    for doc in docs:
        text = doc.get('text', '')
        # Split by project sections
        sections = re.split(r'\n\([cid:]+\d+\)', text)
        
        for section in sections:
            if not section.strip():
                continue
                
            # Look for project name patterns
            project_match = re.search(r'^\s*([A-Z][A-Za-z0-9\s&\-\(\)]+)\s*$', section, re.MULTILINE)
            if not project_match:
                continue
                
            project_name = project_match.group(1).strip()
            
            # Skip common headers
            if any(header in project_name for header in [
                'Capital Improvement Projects', 'Disaster Recovery Projects', 
                'Public Works Commission', 'RECOMMENDED ACTION', 'DISCUSSION'
            ]):
                continue
            
            # Extract status
            status = None
            if 'completed' in section.lower():
                status = 'completed'
            elif 'design' in section.lower() or 'planning' in section.lower():
                status = 'design'
            elif 'not started' in section.lower() or 'identified' in section.lower():
                status = 'not started'
            
            # Extract topic keywords
            topics = []
            lower_section = section.lower()
            if 'park' in lower_section:
                topics.append('park')
            if 'road' in lower_section:
                topics.append('road')
            if 'fema' in lower_section:
                topics.append('FEMA')
            if 'drainage' in lower_section or 'storm drain' in lower_section:
                topics.append('drainage')
            if 'bridge' in lower_section:
                topics.append('bridge')
            if 'playground' in lower_section:
                topics.append('playground')
            if 'fire' in lower_section:
                topics.append('fire')
            if 'warning' in lower_section or 'siren' in lower_section:
                topics.append('emergency warning')
            
            # Extract dates
            st = None
            et = None
            
            # Look for completion/completed dates
            complete_match = re.search(r'(?:Complete[sd]?|Completed)[\s:]+([A-Za-z\d\-\s]+)', section, re.IGNORECASE)
            if complete_match:
                et = complete_match.group(1).strip()
            
            # Look for schedule patterns
            schedule_patterns = [
                (r'Complete[\w\s]*:\s*([A-Za-z\d\-\s]+)', 'et'),
                (r'Completed[\w\s]*:\s*([A-Za-z\d\-\s]+)', 'et'),
                (r'Construction[\w\s]*:\s*([A-Za-z\d\-\s]+)', 'et'),
                (r'Begin[\w\s]*:\s*([A-Za-z\d\-\s]+)', 'st')
            ]
            
            for pattern, date_type in schedule_patterns:
                matches = re.finditer(pattern, section, re.IGNORECASE)
                for match in matches:
                    date_val = match.group(1).strip()
                    if date_type == 'et' and not et:
                        et = date_val
                    elif date_type == 'st' and not st:
                        st = date_val
            
            projects.append({
                'Project_Name': project_name,
                'topic': ', '.join(topics) if topics else None,
                'status': status,
                'st': st,
                'et': et,
                'source_doc': doc.get('filename')
            })
    
    return projects

# Extract projects from civic documents
extracted_projects = extract_projects_from_docs(civic_docs_data)

# Create DataFrames
df_projects = pd.DataFrame(extracted_projects)

# Clean and normalize project names for matching
def normalize_name(name):
    if not name:
        return ''
    # Remove common suffixes and normalize
    name = re.sub(r'\s*\(FEMA[^\)]*\)\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalOES[^\)]*\)\s*$', '', name, flags=re.IGNORECASE)
    name = re.sub(r'\s*\(CalJPIA[^\)]*\)\s*$', '', name, flags=re.IGNORECASE)
    return name.strip().lower()

# Also create a version for the funding data matching
df_funding = pd.DataFrame(funding_data)
df_funding['normalized_name'] = df_funding['Project_Name'].apply(normalize_name)

# Normalize extracted project names
df_projects['normalized_name'] = df_projects['Project_Name'].apply(normalize_name)

print('__RESULT__:')
print(json.dumps({
    'extracted_projects_count': len(extracted_projects),
    'sample_projects': extracted_projects[:10],
    'funding_records_count': len(funding_data),
    'unique_normalized_funding_names': len(df_funding['normalized_name'].unique())
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json'}

exec(code, env_args)
