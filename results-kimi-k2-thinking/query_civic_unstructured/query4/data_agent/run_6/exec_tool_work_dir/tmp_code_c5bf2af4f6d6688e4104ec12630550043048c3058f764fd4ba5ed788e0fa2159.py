code = """import json
import re

# Load the civic documents data
civic_docs_path = locals().get('var_functions.query_db:6', 'var_functions.query_db:2')
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals()['var_functions.query_db:2']

# Print debug info about the data
print('__RESULT__:')
print(f"Number of documents: {len(civic_docs)}")
print(f"First document keys: {civic_docs[0].keys() if civic_docs else 'No documents'}")

# Look for Spring 2022 patterns in the text
spring_2022_patterns = [
    '2022-Spring',
    '2022-March',
    '2022-April', 
    '2022-Apr',
    '2022-May'
]

projects_with_spring_2022 = []

# Parse each document
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    current_schedule = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (they often appear before project schedule sections)
        # Project names are typically at the start of a section or after a bullet point
        
        # Check if this line contains a spring 2022 date
        if any(pattern in line for pattern in spring_2022_patterns):
            # If we have a current project name from context, use it
            # For now, let's extract all project names from the text
            
            # Look backwards for project name
            # Project names often appear before the schedule
            
            # Extract all project names that appear in the document
            # Projects often appear with names like "PCH Median Improvements Project"
            # or "2022 Morning View Resurfacing & Storm Drain Improvements"
            
            # Let's look for common patterns that indicate project names
            project_patterns = [
                r'([A-Z][^.]*?Project)',
                r'([A-Z][^.]*?Improvements)',
                r'([A-Z][^.]*?Repair)',
                r'([A-Z][^.]*?Replacement)',
                r'([A-Z][^.]*?Study)',
                r'([A-Z][^.]*?Facility)',
                r'([A-Z][^.]*?Park)',
                r'([A-Z][^.]*?Road[^.]*)',
                r'(Kanan Dume Biofilter)',
                r'(Outdoor Warning Signs)',
                r'(City Traffic Signals Backup Power)',
                r'(Malibu Bluffs Park[^.]*)',
                r'(Malibu Canyon Road[^.]*)'
            ]
            
            # Search the entire text for project names that have spring 2022 dates
            combined_text = text
            
            # Find all potential project sections
            sections = re.split(r'\n\s*\n', combined_text)
            
            for section in sections:
                if any(pattern in section for pattern in spring_2022_patterns):
                    # Extract project name from this section
                    # Look for the main project title (usually first bold line or uppercase)
                    section_lines = section.split('\n')
                    for sect_line in section_lines[:5]:  # Check first few lines
                        sect_line = sect_line.strip()
                        if sect_line and not sect_line.startswith('(') and len(sect_line) > 10:
                            # Skip lines that are clearly not project names
                            if not any(x in sect_line.lower() for x in ['page', 'agenda item', 'updates:', 'project schedule:', 'project description:', 'estimated schedule:']):
                                if len(sect_line) < 150:  # Reasonable length for a project name
                                    projects_with_spring_2022.append({
                                        'Project_Name': sect_line,
                                        'Source': doc.get('filename', ''),
                                        'Snippet': line[:100]
                                    })
                                    break

# Remove duplicates based on project name
unique_projects = []
seen_names = set()
for proj in projects_with_spring_2022:
    name = proj['Project_Name']
    # Normalize the name (remove common suffixes/prefixes that might vary)
    normalized_name = re.sub(r'\s*\(.*?\)\s*$', '', name)  # Remove parenthetical suffixes
    normalized_name = normalized_name.strip()
    
    if normalized_name not in seen_names:
        seen_names.add(normalized_name)
        unique_projects.append(proj)

print(f"Found {len(unique_projects)} projects with Spring 2022 dates:")
for proj in unique_projects[:10]:
    print(f"- {proj['Project_Name']}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
