code = """import json
import re
import os

# Load funding data
with open('/root/shared_data/var_functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data  
with open('/root/shared_data/var_functions.query_db:2.json', 'r') as f:
    civic_docs = json.load(f)

print("Loaded", len(funding_data), "funding records and", len(civic_docs), "civic documents")

# Extract Spring 2022 projects from civic documents
spring_2022_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    # Check for Spring 2022 indicators
    if 'Spring 2022' in text or '2022-Spring' in text or re.search('2022-(03|04|05|March|April|May)', text, re.IGNORECASE):
        # Split into lines to find project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            # Look for lines mentioning Spring 2022
            if re.search('Spring 2022|2022-Spring|2022-(03|04|05|March|April|May)', line, re.IGNORECASE):
                # Look backwards up to 5 lines to find project name
                for j in range(i-1, max(0, i-6), -1):
                    prev_line = lines[j].strip()
                    # Heuristic: project names are typically capitalized, not bullet points, and longer than 10 chars
                    if (prev_line and 
                        len(prev_line) > 10 and 
                        not prev_line.startswith(('(', '•', '-', 'Page', 'Item')) and
                        not 'commission' in prev_line.lower() and
                        not 'public works' in prev_line.lower()):
                        spring_2022_project_names.append(prev_line)
                        break

print("Found", len(spring_2022_project_names), "potential Spring 2022 projects")

# Match projects with funding records
total_funding = 0
matched_projects = set()

for funding_record in funding_data:
    funding_name = funding_record['Project_Name']
    funding_amount = int(funding_record['Amount'])
    
    # Try to match with any of the spring 2022 project names
    for project_name in spring_2022_project_names:
        # Check if funding_name matches or contains project_name or vice versa
        if (funding_name == project_name or 
            funding_name in project_name or 
            project_name in funding_name or
            any(word.strip() in funding_name for word in project_name.split() if len(word.strip()) > 4)):
            
            if funding_name not in matched_projects:
                matched_projects.add(funding_name)
                total_funding += funding_amount
                break

result = {"project_count": len(matched_projects), "total_funding": total_funding}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
