code = """import json

# Read the full MongoDB query result
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    mongo_docs = json.load(f)

print("Documents found:", len(mongo_docs))

projects = []
keywords = ['fema', 'emergency', 'disaster', 'recovery', 'caloes', 'caljpia', 'warning sirens', 'outdoor warning']

for doc in mongo_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Split text into lines
    lines = text.splitlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for keywords
        has_keyword = any(kw in line.lower() for kw in keywords)
        
        # Check if it looks like a project name
        is_project_name = (line.isupper() or '(' in line or 'Project' in line or 
                          'Improvements' in line or 'Repairs' in line or 'Replacement' in line)
        
        if has_keyword and is_project_name:
            topics = []
            if 'fema' in line.lower():
                topics.append('FEMA')
            if 'emergency' in line.lower():
                topics.append('emergency')
            if 'disaster' in line.lower():
                topics.append('disaster')
            if 'warning' in line.lower() or 'siren' in line.lower():
                topics.append('emergency warning')
            
            projects.append({
                'Project_Name': line,
                'topics': ','.join(topics),
                'status': 'design',
                'type': 'disaster'
            })

print("Extracted projects:", len(projects))
for i, proj in enumerate(projects[:5]):
    print(i+1, proj['Project_Name'][:80])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
