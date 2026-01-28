code = """import json
import re

# Load civic documents from file path stored in the variable
civic_docs_file = var_functions.query_db:0
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data from file path stored in the variable
funding_file = var_functions.query_db:2
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs)} civic documents and {len(funding_data)} funding records")

# Extract park projects completed in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for completion statements mentioning 2022
    # Pattern 1: "Construction was completed, [Month] 2022"
    pattern1 = r'Construction was completed[^\n]*2022[^\n]*'
    matches1 = re.finditer(pattern1, text, re.IGNORECASE)
    
    # Pattern 2: "completed [Month] 2022"
    pattern2 = r'\bcompleted[^\n]*2022[^\n]*'
    matches2 = re.finditer(pattern2, text, re.IGNORECASE)
    
    all_matches = list(matches1) + list(matches2)
    
    for match in all_matches:
        # Get context to find project name
        start_pos = max(0, match.start() - 800)
        context = text[start_pos:match.start()]
        
        # Look for project name (usually a heading or bold line)
        lines = context.split('\n')
        project_name = None
        
        for line in reversed(lines):
            line = line.strip()
            # Skip empty lines, bullet points, metadata
            if not line or len(line) < 5:
                continue
            if line.startswith(('(', '•', '-', '□', '■', '♦', '◊')):
                continue
            if any(x in line for x in ['Updates:', 'Schedule:', 'PROJECTS', 'To:', 'Prepared by:', 'Date:']):
                continue
            
            # Check if line looks like a project name
            project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 'Structure', 
                                 'Walkway', 'Park', 'Playground', 'Facility', 'System', 'Roof', 'Paver']
            
            if any(indicator in line for indicator in project_indicators):
                if 10 < len(line) < 200:  # Reasonable length for project name
                    project_name = line
                    break
        
        if project_name:
            # Check if it's park-related
            park_keywords = ['park', 'Park', 'playground', 'Playground', 'Park Shade', 'Park Workout']
            is_park = any(kw in project_name for kw in park_keywords)
            
            if is_park:
                park_projects_2022.append({
                    'Project_Name': project_name,
                    'source_file': filename
                })

# Remove duplicates
unique_projects = {}
for p in park_projects_2022:
    name = p['Project_Name']
    if name not in unique_projects:
        unique_projects[name] = p

park_projects_2022 = list(unique_projects.values())

print(f"Found {len(park_projects_2022)} park projects completed in 2022")
for p in park_projects_2022:
    print(f"  - {p['Project_Name']}")

# Match with funding data
project_names = [p['Project_Name'] for p in park_projects_2022]
total_funding = 0
matched_count = 0

# Create lookup for funding by project name
funding_lookup = {}
for fund in funding_data:
    fund_name = fund.get('Project_Name', '').strip()
    amount = int(fund.get('Amount', 0))
    
    if fund_name not in funding_lookup:
        funding_lookup[fund_name] = []
    funding_lookup[fund_name].append(amount)

# Try to match each park project with funding
for park_project in park_projects_2022:
    park_name = park_project['Project_Name']
    
    # Direct match
    if park_name in funding_lookup:
        amount = sum(funding_lookup[park_name])
        total_funding += amount
        matched_count += 1
        print(f"  Matched: {park_name} - ${amount:,}")
        continue
    
    # Try variations (case insensitive, partial)
    found = False
    park_lower = park_name.lower()
    
    for fund_name in funding_lookup:
        fund_lower = fund_name.lower()
        
        # Check if one is contained in the other
        if park_lower in fund_lower or fund_lower in park_lower:
            amount = sum(funding_lookup[fund_name])
            total_funding += amount
            matched_count += 1
            print(f"  Matched (partial): {park_name} -> {fund_name} - ${amount:,}")
            found = True
            break
    
    if not found:
        print(f"  No funding found for: {park_name}")

print(f"\nMatched {matched_count} projects with funding")
print(f"Total funding for park projects completed in 2022: ${total_funding:,}")

# Return result
result = {
    'total_funding': total_funding,
    'matched_projects': matched_count,
    'total_projects_found': len(park_projects_2022)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
