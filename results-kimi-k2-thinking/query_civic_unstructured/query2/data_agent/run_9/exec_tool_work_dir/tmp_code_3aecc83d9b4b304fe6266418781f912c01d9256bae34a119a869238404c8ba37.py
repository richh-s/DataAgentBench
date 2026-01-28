code = """import json
import re

# Access the file path from the query result
file_path = locals()['var_functions.query_db:10']
print(f"Reading from file: {file_path}")

# Load the complete data
with open(file_path, 'r', encoding='utf-8') as f:
    all_docs = json.load(f)

print(f"Total documents loaded: {len(all_docs)}")

# Search for park projects completed in 2022
park_projects_2022 = []

for doc_idx, doc in enumerate(all_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', f'doc_{doc_idx}')
    
    # Look for patterns that indicate park projects completed in 2022
    # Pattern: Project name (often in title case or uppercase) containing Park/Playground
    # followed by completion information in 2022
    
    # First, find all occurrences of "Park" in the text
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip short or obviously not-project lines
        if len(line) < 10:
            continue
        
        # Look for lines that likely contain park project names
        # These often contain "Park" plus other keywords
        has_park_keywords = 'Park' in line or 'Playground' in line
        has_project_keywords = any(kw in line for kw in ['Repair', 'Improvement', 'Project', 'Structure', 'Walkway', 'Shade', 'Recreation'])
        
        if has_park_keywords or (has_park_keywords and has_project_keywords):
            # Look ahead in subsequent lines (up to 15 lines) for completion info
            for j in range(i+1, min(i+20, len(lines))):
                future_text = '\n'.join(lines[i:j+1]).lower()
                
                # Check if completed in 2022
                if '2022' in '\n'.join(lines[i:j+1]) and any(marker in future_text for marker in ['completed', 'construction was completed', 'notice of completion']):
                    # This is likely a park project completed in 2022
                    project_name = line
                    
                    # Clean up the project name
                    project_name = re.sub(r'^[\d\s\.]+', '', project_name)  # Remove leading numbers/dots
                    project_name = project_name.strip()
                    
                    # Avoid obviously non-project lines
                    if project_name and len(project_name) > 5 and not project_name.startswith('Page'):
                        park_projects_2022.append({
                            'Project_Name': project_name,
                            'source_file': filename,
                            'completion_year': '2022'
                        })
                        break  # Don't check further lines for this project

# Remove duplicates
unique_projects = {}
for proj in park_projects_2022:
    name = proj['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = proj

final_projects = list(unique_projects.values())

print(f"\nFound {len(final_projects)} unique park projects completed in 2022:")
for proj in final_projects:
    print(f"- {proj['Project_Name']} (from {proj['source_file']})")

# Prepare result for next step - just the project names as a simple list
project_names = [p['Project_Name'] for p in final_projects]

result = {
    'count': len(final_projects),
    'project_names': project_names,
    'projects': final_projects
}

# Use simple string concatenation instead of json.dumps for the result
import json as js
result_json = js.dumps(result)

print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
