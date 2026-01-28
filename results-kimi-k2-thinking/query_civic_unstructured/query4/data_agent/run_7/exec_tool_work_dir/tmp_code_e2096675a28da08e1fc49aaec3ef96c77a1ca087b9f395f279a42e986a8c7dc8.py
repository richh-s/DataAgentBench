code = """import json
import re

# Load the data from the stored file paths
civic_docs_file = '/tmp/query_result_694eef5c4ec675b6b5f5a285.json'
funding_file = '/tmp/query_result_funding_database_Funding.json'

# Read civic documents
civic_docs_data = []
try:
    with open(civic_docs_file, 'r') as f:
        civic_docs_data = json.load(f)
except:
    # Try alternative - the variable should contain the path
    try:
        civic_docs_file = str(var_functions.query_db_10)
        with open(civic_docs_file, 'r') as f:
            civic_docs_data = json.load(f)
    except:
        pass

# Read funding data  
funding_data = []
try:
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)
except:
    try:
        funding_file = str(var_functions.query_db_11)
        with open(funding_file, 'r') as f:
            funding_data = json.load(f)
    except:
        pass

print(f"Loaded {len(civic_docs_data)} documents and {len(funding_data)} funding records")

# Create funding map for lookup
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Find projects started in Spring 2022
spring_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document mentions 2022 Spring timeframe
    has_2022 = '2022' in text
    has_spring_months = any(m in lower_text for m in ['spring', 'march', 'april', 'may'])
    
    if has_2022 and has_spring_months:
        # Extract project sections
        # Look for patterns typical of project descriptions
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines and common markers
            if len(line) < 5:
                continue
            
            # Skip bullet points and parenthetical lines
            first_char = line[0] if len(line) > 0 else ''
            if first_char in ['(', '•', '-', '■', '□', '▪']:
                continue
            
            # Look for project names (usually start with capital letter, reasonable length, not metadata)
            if (first_char.isalpha() and first_char.isupper() and 
                ':' not in line and '!' not in line and '?' not in line and
                len(line) <= 100 and len(line.split()) <= 20 and
                'project' not in line.lower() and 'capital improvement' not in line.lower()):
                
                # Check if this project name or nearby text contains Spring 2022 info
                # Look ahead a few lines
                lookahead_end = min(i + 5, len(lines))
                nearby_text = ' '.join(lines[i:lookahead_end])
                nearby_lower = nearby_text.lower()
                
                if '2022' in nearby_text and any(m in nearby_lower for m in ['spring', 'march', 'april', 'may']):
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))

print(f"Found {len(spring_projects)} potential Spring 2022 projects")

# Match projects with funding data
total_funding = 0
matched_projects = []

for proj_name in spring_projects:
    # Direct match with funding database
    if proj_name in funding_map:
        funding_amount = funding_map[proj_name]
        total_funding += funding_amount
        matched_projects.append({
            'name': proj_name,
            'funding': funding_amount
        })
    else:
        # Try to find a match by comparing base names (before parentheses)
        proj_base = proj_name.split('(')[0].strip().lower()
        
        for fund_name, fund_amount in funding_map.items():
            # Skip if already found
            if any(m['name'] == fund_name for m in matched_projects):
                continue
                
            fund_base = fund_name.split('(')[0].strip().lower()
            
            # Check for substantial name overlap
            if (proj_base in fund_base or 
                fund_base in proj_base or
                proj_base == fund_base):
                
                total_funding += fund_amount
                matched_projects.append({
                    'name': fund_name,
                    'funding': fund_amount
                })
                break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
