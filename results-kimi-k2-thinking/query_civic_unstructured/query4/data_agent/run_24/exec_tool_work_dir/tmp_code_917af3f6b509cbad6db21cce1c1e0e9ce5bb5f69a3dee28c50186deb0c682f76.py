code = """import json

# Load Spring 2022 documents
spring_docs_file = var_functions.query_db:38
with open(spring_docs_file, 'r') as f:
    spring_docs = json.load(f)

print('Spring 2022 documents count:', len(spring_docs))

# Process documents to extract project names
project_list = []

for doc in spring_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    if not text:
        continue
    
    lines = text.split('\n')
    
    # Extract potential project names
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty or very short lines
        if len(line) < 10:
            continue
        
        # Check if line starts with uppercase (potential project name)
        if line[0].isupper():
            # Check for project-related keywords
            keywords = ['project', 'improvements', 'repairs', 'drainage', 'road', 'park', 'bridge']
            if any(kw in line.lower() for kw in keywords):
                # Check surrounding context for Spring 2022 timing
                start_idx = max(0, i - 2)
                end_idx = min(len(lines), i + 8)
                context = '\n'.join(lines[start_idx:end_idx])
                
                spring_patterns = ['2022-Spring', 'Spring 2022', 'spring 2022', '2022-March', '2022-April', '2022-May']
                timing_words = ['Advertise', 'Begin', 'Start', 'Construction', 'Complete']
                
                has_spring = any(p in context for p in spring_patterns)
                has_timing = any(t in context for t in timing_words)
                
                if has_spring or has_timing:
                    # Clean project name
                    clean_name = line.replace('(cid:190)', '').strip()
                    if clean_name and clean_name not in project_list:
                        project_list.append(clean_name)

print('Total unique projects found:', len(project_list))
print('Projects:', project_list)

result = json.dumps({'count': len(project_list), 'project_names': project_list})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
