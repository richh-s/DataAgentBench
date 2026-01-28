code = """import json
import re

# Load the civic documents from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print('Loaded', len(documents), 'documents')

# Let's analyze the text structure to find projects with Spring 2022 start dates
spring_2022_projects = []

# Search patterns for Spring 2022
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', 'Spring 2022', 'spring 2022']

for doc in documents:
    text = doc.get('text', '')
    if not text:
        continue
    
    # Split into lines and look for project information
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        
        # Skip empty or very short lines
        if not line or len(line) < 10:
            continue
        
        # Look for project names (typically capitalized, contains project-related terms)
        if line[0].isupper():
            project_terms = ['project', 'improvements', 'repairs', 'facility', 'park', 'road', 'drainage', 'bridge', 'playground', 'treatment', 'wall', 'study', 'system', 'lane', 'structure', 'maintenance']
            has_project_term = any(term in line.lower() for term in project_terms)
            
            if has_project_term:
                # Look for Spring 2022 references in the context
                context_window = lines[max(0, i-2):min(len(lines), i+10)]
                context_text = ' '.join(context_window)
                
                # Check if Spring 2022 appears in context
                has_spring_2022 = any(pattern in context_text for pattern in spring_patterns)
                
                # Also check if it's related to project timing (construction, begin, advertise, etc.)
                timing_keywords = ['Advertise', 'Begin', 'Start', 'Construction', 'Complete', 'Design']
                has_timing = any(keyword in context_text for keyword in timing_keywords)
                
                if has_spring_2022 and has_timing:
                    spring_2022_projects.append(line)

# Remove duplicates and count
unique_projects = list(set(spring_2022_projects))
print('Found', len(unique_projects), 'unique projects with Spring 2022 start')

# Save to JSON format
result = json.dumps({'count': len(unique_projects), 'projects': unique_projects}, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}]}

exec(code, env_args)
