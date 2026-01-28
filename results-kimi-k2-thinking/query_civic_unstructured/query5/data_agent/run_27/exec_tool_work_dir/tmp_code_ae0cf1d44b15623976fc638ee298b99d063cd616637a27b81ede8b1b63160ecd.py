code = """import json
import re

# Read funding data
funding_file = open('file_storage/functions.query_db:5.json', 'r')
funding_data = json.load(funding_file)
funding_file.close()

# Read all civic documents
civic_file = open('file_storage/functions.query_db:6.json', 'r')
civic_docs = json.load(civic_file)
civic_file.close()

print("Funding records:", len(funding_data))
print("Civic documents:", len(civic_docs))

# Create a mapping of project names to funding amounts
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

print("\nSample funding map entries:")
for i, (name, amount) in enumerate(list(funding_map.items())[:5]):
    print(f"  {name}: ${amount:,}")

# Parse civic documents to find disaster projects that started in 2022
disaster_projects_2022 = []

# Patterns to identify disaster-related projects
disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'disaster', 'fire', 'emergency warning']
disaster_pattern = re.compile(r'\b(' + '|'.join(disaster_keywords) + r')\b', re.IGNORECASE)

# Pattern to find project names and dates
# Look for lines that start with project names (often capitalized, may contain year)
project_line_pattern = re.compile(r'^([A-Z][^\n]{5,150})$', re.MULTILINE)

for doc in civic_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Find all potential project names in the text
    # Projects often appear as title lines
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and very short lines
        if not line or len(line) < 10:
            continue
            
        # Look for project names that might indicate disaster projects
        # Check if line contains disaster keywords OR ends with disaster suffixes
        has_disaster_suffix = any(suffix in line for suffix in ['(FEMA Project)', '(CalOES Project)', '(CalJPIA Project)'])
        has_disaster_keyword = bool(disaster_pattern.search(line))
        
        # Also check if it's a disaster project by context (near disaster keywords)
        if has_disaster_suffix or has_disaster_keyword:
            # This is likely a disaster project, check for 2022 start date
            # Start date might be in the project name itself or in following lines
            if '2022' in line:
                # Extract project name (clean it up)
                project_name = line.strip()
                disaster_projects_2022.append(project_name)
            else:
                # Check next few lines for date information
                context = '\n'.join(lines[i:i+10])
                if '2022' in context:
                    # The project might have started in 2022, include it
                    project_name = line.strip()
                    disaster_projects_2022.append(project_name)

print(f"\nFound {len(disaster_projects_2022)} potential disaster projects:")
for proj in disaster_projects_2022[:20]:
    print(f"  - {proj}")

result = {
    "funding_count": len(funding_data),
    "civic_count": len(civic_docs),
    "disaster_projects_2022_count": len(disaster_projects_2022),
    "disaster_projects_2022": disaster_projects_2022[:20]
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
