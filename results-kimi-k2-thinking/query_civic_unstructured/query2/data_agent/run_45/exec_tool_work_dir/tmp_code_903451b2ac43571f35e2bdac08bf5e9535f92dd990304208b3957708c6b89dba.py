code = """import json
import re

# Access the civic documents result from the previous tool call
civic_docs_key = 'var_functions.query_db:0'
civic_docs_file = locals()[civic_docs_key]

# Load civic documents from file
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Access the funding data result from the previous tool call
funding_key = 'var_functions.query_db:2'
funding_file = locals()[funding_key]

# Load funding data from file
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(civic_docs), 'civic documents and', len(funding_data), 'funding records')

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements mentioning 2022
    patterns = [
        r'Construction was completed[^\n]*2022[^\n]*',
        r'\bcompleted[^\n]*2022[^\n]*',
        r'Complete Construction[^\n]*2022[^\n]*'
    ]
    
    for pattern in patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            # Get context to find project name
            start_pos = max(0, match.start() - 800)
            context = text[start_pos:match.start()]
            
            # Look for project name
            lines = context.split('\n')
            project_name = None
            
            for line in reversed(lines):
                line = line.strip()
                if not line or len(line) < 5:
                    continue
                if line.startswith(('(', '•', '-', '□', '■')):
                    continue
                if any(x in line for x in ['Updates:', 'Schedule:', 'To:', 'Prepared by:', 'Date:']):
                    continue
                
                # Check if line looks like a project name
                indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Structure', 'Walkway', 'Park', 'Playground', 'Facility', 'System', 'Roof']
                
                if any(indicator in line for indicator in indicators):
                    if 10 < len(line) < 200:
                        project_name = line
                        break
            
            if project_name:
                # Check if it's park-related
                park_keywords = ['park', 'Park', 'playground', 'Playground']
                is_park = any(kw in project_name for kw in park_keywords)
                
                if is_park:
                    park_projects_2022.append({
                        'Project_Name': project_name,
                        'source_file': filename
                    })

# Remove duplicates
unique = {}
for p in park_projects_2022:
    name = p['Project_Name']
    if name not in unique:
        unique[name] = p

park_projects_2022 = list(unique.values())

print('Found', len(park_projects_2022), 'park projects completed in 2022')

# Match with funding data
total_funding = 0
matched_count = 0

# Create funding lookup
funding_lookup = {}
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    
    if fund_name not in funding_lookup:
        funding_lookup[fund_name] = []
    funding_lookup[fund_name].append(amount)

# Try to match projects
for park_project in park_projects_2022:
    park_name = park_project['Project_Name']
    
    # Direct match
    if park_name in funding_lookup:
        amount = sum(funding_lookup[park_name])
        total_funding += amount
        matched_count += 1
        print('Matched:', park_name, '-', amount)
        continue
    
    # Try variations
    found = False
    park_lower = park_name.lower()
    
    for fund_name in funding_lookup:
        fund_lower = fund_name.lower()
        
        if park_lower in fund_lower or fund_lower in park_lower:
            amount = sum(funding_lookup[fund_name])
            total_funding += amount
            matched_count += 1
            print('Matched partial:', park_name, '->', fund_name, '-', amount)
            found = True
            break
    
    if not found:
        print('No funding found for:', park_name)

print('Matched', matched_count, 'projects with funding')
print('Total funding for park projects completed in 2022:', total_funding)

result = {
    'total_funding': total_funding,
    'matched_projects': matched_count,
    'total_projects_found': len(park_projects_2022)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
