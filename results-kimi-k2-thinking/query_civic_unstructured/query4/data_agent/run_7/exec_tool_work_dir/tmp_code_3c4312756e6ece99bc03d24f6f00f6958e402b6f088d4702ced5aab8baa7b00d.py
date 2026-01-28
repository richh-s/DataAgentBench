code = """import json
import re

# File paths from the query results
civic_docs_file = var_functions.query_db:10
funding_file = var_functions.query_db:11

# Read the actual data from files
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} civic documents and {len(funding_data)} funding records")

# Create funding lookup map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Spring 2022 date patterns
spring_patterns = [
    r'2022[-\s]?Spring',
    r'2022[-\s]?March', 
    r'2022[-\s]?April',
    r'2022[-\s]?May',
    r'2022[-\s]?03',
    r'2022[-\s]?04', 
    r'2022[-\s]?05'
]

# Extract projects with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines, bullets, parentheticals
        if len(line) < 5 or line.startswith(('(', '•', '-', '–', '—', '●', '○', '■')):
            continue
            
        # Look for project names (title case, reasonable length, not metadata)
        if (line[0].isalpha() and 
            line[0].isupper() and 
            ':' not in line and 
            not any(skip in line.lower() for skip in ['subject:', 'recommended action', 'discussion:', 'update', 'schedule']) and
            len(line.split()) <= 20):
            
            current_project = line
            continue
        
        # Check if current or upcoming lines have Spring 2022 dates
        if current_project:
            # Check this line
            combined_text = line
            
            # Also check next couple lines for context
            if i < len(lines) - 2:
                combined_text += ' ' + ' '.join(lines[i+1:i+3])
            
            for pattern in spring_patterns:
                if re.search(pattern, combined_text, re.IGNORECASE):
                    spring_2022_projects.append(current_project)
                    current_project = None
                    break
    
    # Also try finding projects via regex patterns in the text
    # Look for patterns like "Project Name\nUpdates:" or "Project Name\nProject Schedule:"
    project_sections = re.findall(r'([A-Z][a-zA-Z0-9\s\-\(\)]+?)\s*(?=\n\s*(?:Updates?|Project Schedule|Estimated Schedule))', text, re.MULTILINE)
    
    for section in project_sections:
        section = section.strip()
        if (len(section) > 10 and 
            not any(skip in section.lower() for skip in ['capital improvement', 'disaster recovery', 'public works']) and
            len(section.split()) <= 15):
            
            # Check nearby text for Spring 2022
            section_pos = text.find(section)
            nearby = text[section_pos:section_pos + 500]
            
            for pattern in spring_patterns:
                if re.search(pattern, nearby, re.IGNORECASE):
                    if section not in spring_2022_projects:
                        spring_2022_projects.append(section)
                    break

# Remove duplicates while preserving order
spring_2022_projects = list(dict.fromkeys(spring_2022_projects))

print(f"\nFound {len(spring_2022_projects)} unique Spring 2022 projects")

# Match with funding data
total_funding = 0
matched_projects = []

for proj_name in spring_2022_projects:
    # Direct match
    if proj_name in funding_map:
        funding = funding_map[proj_name]
        total_funding += funding
        matched_projects.append({'name': proj_name, 'funding': funding})
    else:
        # Fuzzy match - check base names without suffixes
        base_name = proj_name.split('(')[0].strip()
        
        for fund_name, fund_amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip()
            
            # Check for meaningful overlap
            if (base_name in fund_name or 
                fund_base in proj_name or 
                base_name.lower() == fund_base.lower()):
                
                total_funding += fund_amount
                matched_projects.append({'name': fund_name, 'funding': fund_amount})
                break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print(f'__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
