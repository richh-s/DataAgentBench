code = """import json
import os

# Get the file paths from the stored variables
civic_file = str(var_functions.query_db_10)
funding_file = str(var_functions.query_db_11)

# Read civic documents
civic_docs = []
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Read funding data
funding = []
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Build funding lookup map
funding_map = {}
for r in funding:
    funding_map[r['Project_Name']] = int(r['Amount'])

# Find Spring 2022 projects
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if this document mentions Spring 2022
    has_2022 = '2022' in text_lower
    has_spring = 'spring' in text_lower or 'march' in text_lower or 'april' in text_lower or 'may' in text_lower
    
    if has_2022 and has_spring:
        lines = text.split('\n')
        in_project_section = False
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty or very short lines
            if len(line) < 5:
                continue
            
            # Skip bullet points and special characters
            if line[0] in ['(', '•', '-', '■', '□', '▪', '*']:
                continue
            
            # Look for project names (capitalized, reasonable length)
            if (line[0].isalpha() and 
                line[0].isupper() and 
                ':' not in line and 
                len(line.split()) <= 20):
                
                # Skip metadata lines
                if any(x in line.lower() for x in ['capital improvement', 'disaster recovery', 'project update', 'status report']):
                    continue
                
                # Check if this project has Spring 2022 in nearby context
                context_lines = lines[i:min(i+6, len(lines))]
                context = ' '.join(context_lines).lower()
                
                if '2022' in context and any(m in context for m in ['spring', 'march', 'april', 'may']):
                    if line not in spring_projects:
                        spring_projects.append(line)

print(f"Found {len(spring_projects)} potential Spring 2022 projects")

# Match with funding and calculate total
total_funding = 0
matched = []
project_names_checked = set()

for proj in spring_projects:
    # Direct match
    if proj in funding_map:
        if proj not in project_names_checked:
            total_funding += funding_map[proj]
            matched.append({'name': proj, 'funding': funding_map[proj]})
            project_names_checked.add(proj)
    else:
        # Try fuzzy match by base name
        proj_base = proj.split('(')[0].strip().lower()
        
        for fund_name, amount in funding_map.items():
            if fund_name in project_names_checked:
                continue
                
            fund_base = fund_name.split('(')[0].strip().lower()
            
            if (proj_base in fund_base or 
                fund_base in proj_base or 
                proj_base == fund_base):
                
                total_funding += amount
                matched.append({'name': fund_name, 'funding': amount})
                project_names_checked.add(fund_name)
                break

result = {
    'project_count': len(matched),
    'total_funding': total_funding,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
