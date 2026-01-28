code = """import json

# Load MongoDB documents
mongo_file = locals()['var_functions.query_db:2']
with open(mongo_file, 'r') as f:
    docs = json.load(f)

# Load all funding records
funding_file = locals()['var_functions.query_db:48']
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Documents loaded:', len(docs))
print('Funding records loaded:', len(funding_records))

# Simple extraction: look for common patterns in text
spring_2022_projects = []

for doc in docs:
    text = doc.get('text', '').lower()
    
    # Look for spring 2022 indicators
    has_spring = ('spring 2022' in text or 
                  '2022-spring' in text or 
                  'march 2022' in text or
                  'april 2022' in text or
                  'may 2022' in text or
                  '2022-march' in text or
                  '2022-april' in text or
                  '2022-may' in text)
    
    if not has_spring:
        continue
        
    # Split by common separators
    segments = text.split('\n\n')
    
    for segment in segments:
        segment = segment.strip()
        if len(segment) < 50:  # Too short to be a project description
            continue
            
        # Extract first line as potential project name
        lines = segment.split('\n')
        for line in lines:
            line = line.strip()
            if line and len(line) > 10:
                # Skip headers
                lower = line.lower()
                if any(skip in lower for skip in ['public works', 'agenda report', 'item ', 'to:', 'prepared by', 'approved by', 'date ', 'meeting date', 'subject:', 'page ']):
                    continue
                
                # Check if this segment mentions spring 2022
                if has_spring:
                    spring_2022_projects.append(line)
                    break

# Remove duplicates
unique_projects = []
seen = set()
for proj in spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print('Unique projects found:', len(unique_projects))

# Create normalized lookup for funding
funding_lookup = {}
for fund in funding_records:
    # Normalize by lowercasing and removing extra spaces
    name = ' '.join(fund['Project_Name'].lower().split())
    funding_lookup[name] = fund

# Match projects to funding
matched_projects = []
for proj in unique_projects:
    proj_norm = ' '.join(proj.lower().split())
    
    # Direct match
    if proj_norm in funding_lookup:
        matched_projects.append({
            'project_name': proj,
            'funding': funding_lookup[proj_norm]
        })
    else:
        # Try removing parentheses content for FEMA projects
        clean_proj = proj_norm.split('(')[0].strip()
        if clean_proj in funding_lookup:
            matched_projects.append({
                'project_name': proj,
                'funding': funding_lookup[clean_proj]
            })
        else:
            # Check for partial matches
            for fund_name, fund_record in funding_lookup.items():
                if clean_proj in fund_name or fund_name in clean_proj:
                    if abs(len(clean_proj) - len(fund_name)) < 30:  # Similar length
                        matched_projects.append({
                            'project_name': proj,
                            'funding': fund_record
                        })
                        break

# Calculate totals
total_funding = sum(int(p['funding']['Amount']) for p in matched_projects)

# Prepare results
result = {
    'spring_2022_project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': [
        {
            'name': p['project_name'],
            'funded_name': p['funding']['Project_Name'],
            'amount': int(p['funding']['Amount']),
            'source': p['funding']['Funding_Source']
        }
        for p in matched_projects
    ]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:16': {'key': 'var_functions.query_db:2', 'type': "<class 'str'>", 'length': 38}, 'var_functions.execute_python:18': {'total_docs': 5, 'sample_keys': ['_id', 'filename', 'text'], 'doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 202'}, 'var_functions.query_db:20': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.execute_python:36': {'doc_count': 5}, 'var_functions.execute_python:38': {'spring_2022_docs': 4, 'total_docs': 5}, 'var_functions.execute_python:42': {'spring_2022_projects_count': 0, 'total_funding': 0}, 'var_functions.execute_python:44': {'funding_records': 10, 'sample': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}, 'var_functions.query_db:46': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
