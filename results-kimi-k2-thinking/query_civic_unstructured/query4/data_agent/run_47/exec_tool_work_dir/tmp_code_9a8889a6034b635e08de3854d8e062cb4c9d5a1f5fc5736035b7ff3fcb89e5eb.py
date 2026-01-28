code = """import json
import re

# Read the full result from the MongoDB query
result_file = '/tmp/results/20250219_143343_mongodb_civic_docs_database_query_0.json'
with open(result_file, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents retrieved: {len(civic_docs)}")

# Function to extract projects with Spring 2022 start dates
def extract_spring_2022_projects(text):
    """Extract projects that started in Spring 2022"""
    projects = []
    
    # Look for date patterns indicating Spring 2022
    spring_patterns = [
        r'(?:begin|start|commence|initiated).{0,100}2022[\-\s]?(?:Spring|Mar|Apr|May|03|04|05)',
        r'2022[\-\s]?(?:Spring|Mar|Apr|May|03|04|05).{0,100}(?:begin|start|commence|initiated)',
        r'(?:st:|start:).{0,50}2022[\-\s]?(?:Spring|Mar|Apr|May|03|04|05)',
        r'Advertise:\s*(?:Spring|Mar|Apr|May|03|04|05)[\s\-\_]2022',
        r'Begin[^:]{0,50}:\s*(?:Spring|Mar|Apr|May|03|04|05)[\s\-\_]2022',
    ]
    
    # Also look for "2022-Spring" format
    spring_patterns.append(r'2022\s*-\s*Spring')
    
    # Combine patterns
    pattern = re.compile('|'.join(spring_patterns), re.IGNORECASE | re.DOTALL)
    
    # Project name patterns - look for common project name formats
    # This is more complex as we need to find project names before the date
    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Look for potential project names (typically title case or uppercase lines)
        line = line.strip()
        if (len(line) > 10 and 
            (line.isupper() or (line.istitle() and not line.startswith('Page'))) and
            not any(keyword in line.lower() for keyword in ['agenda', 'item', 'public works', 'commission', 'meeting', 'subject:', 'recommended action:'])):
            
            # Check if this project has Spring 2022 dates in following lines
            following_text = '\n'.join(lines[i:i+20])
            if pattern.search(following_text):
                projects.append(line)
    
    return list(set(projects))

# Extract all projects that started in Spring 2022
all_spring_2022_projects = []
for doc in civic_docs:
    projects = extract_spring_2022_projects(doc.get('text', ''))
    all_spring_2022_projects.extend(projects)

# Remove duplicates while preserving order
unique_projects = []
seen = set()
for proj in all_spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print(f"Projects starting in Spring 2022: {len(unique_projects)}")
print("Project names found:")
for proj in unique_projects:
    print(f"  - {proj}")

# Store results
result = {
    'count': len(unique_projects),
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
