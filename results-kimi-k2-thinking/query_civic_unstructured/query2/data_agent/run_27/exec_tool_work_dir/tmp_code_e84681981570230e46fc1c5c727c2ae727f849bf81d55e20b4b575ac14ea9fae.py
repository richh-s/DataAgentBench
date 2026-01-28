code = """import json
import re

civic_docs_path = locals()['var_functions.query_db:16']
funding_path = locals()['var_functions.query_db:17']

with open(civic_docs_path) as f:
    civic_docs = json.load(f)

with open(funding_path) as f:
    funding_data = json.load(f)

print("Processing civic documents...")

park_projects_2022 = []

# Process all text from all documents
all_text = ""
for doc in civic_docs:
    all_text += doc['text'] + "\n"

# Look for park projects completed in 2022
lines = all_text.split('\n')

for i, line in enumerate(lines):
    line_lower = line.lower()
    
    # Check if this line indicates completion in 2022
    if '2022' in line and ('completed' in line_lower or 'completion' in line_lower):
        # Look backwards for project name (especially park-related)
        project_name = None
        
        # Search up to 5 lines back
        for j in range(i-1, max(0, i-6), -1):
            prev_line = lines[j].strip()
            if not prev_line or prev_line.startswith('('):
                continue
                
            # Check if this line looks like a project name
            if len(prev_line) > 5 and 'Updates:' not in prev_line and 'Project Schedule' not in prev_line:
                project_name = prev_line
                break
        
        if project_name:
            # Clean up the project name
            clean_name = project_name.replace('•', '').replace('◦', '').strip()
            
            # Check if it's park-related
            if 'park' in clean_name.lower():
                # Avoid duplicates
                if clean_name not in park_projects_2022:
                    park_projects_2022.append(clean_name)
                    print(f"Found: {clean_name}")

# Also look for patterns like "Construction was completed [date] [project name]"
completion_patterns = [
    r'Construction was completed[^\n]*?([A-Za-z][^.]*?Park[A-Za-z\s]*)',
    r'completed[^\n]*?2022[^\n]*?([A-Za-z][^.]*?Park[A-Za-z\s]*)'
]

for pattern in completion_patterns:
    matches = re.findall(pattern, all_text, re.IGNORECASE)
    for match in matches:
        clean_match = match.strip()
        # Remove trailing punctuation and common words
        clean_match = re.sub(r'[\.,;]$', '', clean_match)
        clean_match = re.sub(r'\b(and|the|with|for|in|on)\b.*$', '', clean_match, flags=re.IGNORECASE).strip()
        
        if clean_match and len(clean_match) > 5 and 'park' in clean_match.lower():
            if clean_match not in park_projects_2022:
                park_projects_2022.append(clean_match)
                print(f"Found via pattern: {clean_match}")

print(f"\nTotal park projects completed in 2022: {len(park_projects_2022)}")

# Calculate total funding
total_funding = 0
matched_funding = []

for park_name in park_projects_2022:
    park_simple = park_name.lower().replace(' ', '').replace('-', '').replace('_', '')
    
    for fund in funding_data:
        fund_name = fund['Project_Name']
        fund_simple = fund_name.lower().replace(' ', '').replace('-', '').replace('_', '')
        
        # Check if park name is contained in fund name or vice versa
        if (park_simple in fund_simple or fund_simple in park_simple):
            amount = int(fund['Amount'])
            total_funding += amount
            matched_funding.append({
                'project': park_name,
                'funded_as': fund_name,
                'amount': amount
            })
            print(f"Matched funding: {park_name} -> ${amount:,}")
            break

result = {
    'total_funding_dollars': total_funding,
    'number_of_park_projects': len(park_projects_2022),
    'funding_details': matched_funding
}

print(f"\nTotal funding: ${total_funding:,}")
print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:56': {'test': 'success'}}

exec(code, env_args)
