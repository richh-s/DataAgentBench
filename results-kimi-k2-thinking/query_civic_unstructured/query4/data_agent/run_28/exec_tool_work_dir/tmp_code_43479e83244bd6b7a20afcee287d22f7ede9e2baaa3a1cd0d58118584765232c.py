code = """import json
import re

# Load all MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load all funding records
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print(f"Loaded {len(docs)} documents and {len(funding_records)} funding records")

# Patterns for Spring 2022
date_patterns = [
    r'(?:spring\s*2022|2022\s*spring)',
    r'(?:march\s*2022|2022\s*march)',
    r'(?:april\s*2022|2022\s*april)',
    r'(?:may\s*2022|2022\s*may)',
    r'2022-0[3-5]',  # 2022-03, 2022-04, 2022-05
]

date_regex = re.compile('|'.join(date_patterns), re.IGNORECASE)

# Function to extract projects with Spring 2022 start dates
def extract_spring_2022_projects(doc_text, filename):
    projects = []
    text = doc_text
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers and metadata
        skip_patterns = [
            'public works', 'agenda', 'item', 'to:', 'prepared by', 'approved by',
            'date prepared', 'meeting date', 'subject:', 'recommended action',
            'discussion:', 'updates:', 'project schedule', 'page', '•', '□', '○', '●'
        ]
        
        if any(pattern in line.lower() for pattern in skip_patterns):
            continue
        
        # Look for lines that might be project names
        # Typically longer than 10 chars, shorter than 100, contain some capital letters
        if 10 < len(line) < 100 and any(c.isupper() for c in line):
            # Check if this project has a Spring 2022 date in following lines
            subsequent_text = '\n'.join(lines[i:i+15])
            
            if date_regex.search(subsequent_text):
                # Clean up project name
                project_name = line.strip()
                
                # Extract the actual date mentioned
                date_match = date_regex.search(subsequent_text)
                matched_date = date_match.group() if date_match else 'Spring 2022'
                
                projects.append({
                    'project_name': project_name,
                    'date_info': matched_date,
                    'source_file': filename
                })
    
    return projects

# Extract all Spring 2022 projects
all_spring_2022_projects = []
for doc in docs:
    projects = extract_spring_2022_projects(doc.get('text', ''), doc.get('filename', ''))
    all_spring_2022_projects.extend(projects)

print(f"Found {len(all_spring_2022_projects)} potential Spring 2022 project mentions")

# Remove duplicates based on project name
unique_projects = {}
for proj in all_spring_2022_projects:
    name = proj['project_name']
    if name not in unique_projects:
        unique_projects[name] = proj

spring_2022_project_names = list(unique_projects.keys())
print(f"Unique Spring 2022 projects: {len(spring_2022_project_names)}")
print("Projects:", spring_2022_project_names[:10])

# Normalize project names for matching
def normalize_name(name):
    # Remove common suffixes and convert to lowercase for matching
    name = name.lower().strip()
    name = re.sub(r'\s+', ' ', name)  # Normalize whitespace
    name = re.sub(r'\s*\(fema[^)]*\)\s*', '', name)  # Remove FEMA suffixes
    name = re.sub(r'\s*\(caloes[^)]*\)\s*', '', name)  # Remove CalOES suffixes
    name = re.sub(r'\s*\(caljpia[^)]*\)\s*', '', name)  # Remove CalJPIA suffixes
    return name.strip()

# Create index of funding records by normalized name
funding_by_name = {}
for record in funding_records:
    proj_name = record['Project_Name']
    norm_name = normalize_name(proj_name)
    funding_by_name[norm_name] = record

# Match Spring 2022 projects with funding records
matched_projects = []
for proj_name in spring_2022_project_names:
    norm_proj_name = normalize_name(proj_name)
    
    # Direct match
    if norm_proj_name in funding_by_name:
        matched_projects.append({
            'project_name': proj_name,
            'funding_record': funding_by_name[norm_proj_name]
        })
    else:
        # Fuzzy match - check if any funding name contains the project name
        for fund_name, record in funding_by_name.items():
            if (norm_proj_name in fund_name or fund_name in norm_proj_name) and abs(len(norm_proj_name) - len(fund_name)) < 20:
                matched_projects.append({
                    'project_name': proj_name,
                    'funding_record': record
                })
                break

print(f"Matched {len(matched_projects)} projects with funding records")

# Calculate total funding
total_funding = sum(int(proj['funding_record']['Amount']) for proj in matched_projects)

# Create detailed results
detailed_results = []
for proj in matched_projects:
    detailed_results.append({
        'project_name': proj['project_name'],
        'funded_name': proj['funding_record']['Project_Name'],
        'amount': int(proj['funding_record']['Amount']),
        'funding_source': proj['funding_record']['Funding_Source']
    })

result = {
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': detailed_results
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
