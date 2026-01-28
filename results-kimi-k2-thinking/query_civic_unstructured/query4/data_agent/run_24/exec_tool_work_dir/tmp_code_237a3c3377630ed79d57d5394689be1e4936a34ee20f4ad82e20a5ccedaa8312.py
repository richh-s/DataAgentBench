code = """import json

# Load the filtered documents that mention Spring 2022
file_path = var_functions.query_db:38
with open(file_path, 'r') as f:
    documents = json.load(f)

print('Found', len(documents), 'documents mentioning Spring 2022')

# Extract project names and Spring 2022 start dates
spring_2022_projects = []

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty or short lines
        if not line or len(line) < 10:
            continue
        
        # Look for project names (capitalized lines with project-related terms)
        if line[0].isupper():
            project_terms = ['Project', 'Improvements', 'Repairs', 'Facility', 'Park', 'Road', 'Drainage', 'Bridge', 'Playground', 'Treatment', 'Wall', 'Study', 'System', 'Lane', 'Structure', 'Biofilter']
            has_indicator = any(term.lower() in line.lower() for term in project_terms)
            
            if has_indicator:
                # Look for Spring 2022 timing in the surrounding context (up to 10 lines)
                context_start = max(0, i-1)
                context_end = min(len(lines), i+10)
                context = '\n'.join(lines[context_start:context_end])
                
                # Check for Spring 2022 and project timing keywords
                has_spring_2022 = '2022' in context and ('Spring' in context or 'spring' in context)
                has_timing = any(word in context for word in ['Advertise', 'Begin', 'Start', 'Construction', 'Complete', 'Design'])
                
                if has_spring_2022 and has_timing:
                    # Clean up the project name
                    project_name = line.replace('(cid:190)', '').strip()
                    if project_name and project_name not in [p['name'] for p in spring_2022_projects]:
                        # Determine if it's a capital or disaster project
                        project_type = None
                        if 'FEMA' in project_name or 'Disaster' in project_name or 'CalJPIA' in project_name or 'CalOES' in project_name:
                            project_type = 'disaster'
                        elif 'Improvement' in project_name or any(term.lower() in project_name.lower() for term in ['Road', 'Park', 'Drainage', 'Bridge', 'Facility']):
                            project_type = 'capital'
                        
                        spring_2022_projects.append({
                            'name': project_name,
                            'type': project_type
                        })
                        print(f"Found project: {project_name} ({project_type})")

print(f"\nTotal unique Spring 2022 projects: {len(spring_2022_projects)}")

result = json.dumps(spring_2022_projects, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
