code = """import json, re

# Read civic documents
civic_docs = []
with open('var_functions.query_db:16.json', 'r') as f:
    civic_docs = json.load(f)

# Read funding data  
funding_data = []
with open('var_functions.query_db:17.json', 'r') as f:
    funding_data = json.load(f)

print("Loaded data files")

park_projects_2022 = []

# Process documents to find park projects completed in 2022
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for park projects with completion in 2022
    patterns = [
        r'([A-Za-z\s]+Park[A-Za-z\s]*)[^.]*completed[^.]*2022',
        r'([A-Za-z\s]+Playground[A-Za-z\s]*)[^.]*completed[^.]*2022',
        r'Construction was completed[^\n]*2022[^\n]*([A-Za-z\s]+Park[A-Za-z\s]*)'
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            clean_match = match.strip()
            if clean_match and len(clean_match) > 5:
                park_projects_2022.append(clean_match)

# Also look for lines with completion dates
lines_all = []
for doc in civic_docs:
    lines_all.extend(doc.get('text', '').split('\n'))

for i, line in enumerate(lines_all):
    if '2022' in line and ('completed' in line.lower() or 'completion' in line.lower()):
        # Look back for project name
        for j in range(i-1, max(0, i-3), -1):
            prev = lines_all[j].strip()
            if prev and 'park' in prev.lower() and not prev.startswith('('):
                clean_name = re.sub(r'^[A-Z]\s+', '', prev)
                park_projects_2022.append(clean_name.strip())
                break

# Remove duplicates
park_projects_2022 = list(set(park_projects_2022))

print("Found park projects:", len(park_projects_2022))
for p in park_projects_2022:
    print("-", p)

# Calculate total funding
total_funding = 0
for park in park_projects_2022:
    park_lower = park.lower()
    
    for fund in funding_data:
        fund_name = fund['Project_Name'].lower()
        # Check if park name matches funding record
        if (park_lower in fund_name or fund_name in park_lower or
            park_lower.replace(' ', '') in fund_name.replace(' ', '')):
            total_funding += int(fund['Amount'])
            break

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
