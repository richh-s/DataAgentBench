code = """import json
import re

# Access the stored data
funding_json_path = locals()['var_functions.query_db:6']
civic_json_path = locals()['var_functions.query_db:2']

# Read the funding data
with open(funding_json_path, 'r') as f:
    funding_data = json.load(f)

# Read the civic documents
with open(civic_json_path, 'r') as f:
    civic_docs = json.load(f)

# Extract projects from civic documents
capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for capital projects in Design section
    # Pattern to match project names and status
    
    # Find "Capital Improvement Projects (Design)" section
    design_section_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|$)', 
                                      text, re.DOTALL | re.IGNORECASE)
    
    if design_section_match:
        design_section = design_section_match.group(1)
        
        # Extract project names - they typically appear as standalone lines
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Look for lines that are likely project names (not bullet points, not dates, not empty)
            if line and not line.startswith('(') and not line.startswith('•') and not line.startswith('■') \
               and not line.startswith('●') and not line.startswith('\u2022') \
               and not re.match(r'^(cid:|\d+\)|\d+\.)', line) \
               and 'Project Schedule' not in line and 'Updates' not in line \
               and 'Estimated Schedule' not in line and len(line) > 10:
                
                # Clean up the line
                project_name = re.sub(r'^[\dA-Za-z]\.\s*', '', line)
                project_name = project_name.strip()
                
                if project_name and not re.match(r'^(Page|Agenda|Item)', project_name):
                    # Check if this looks like a project name (not a heading)
                    if not re.match(r'^[A-Z\s]{3,}$', project_name) or len(project_name.split()) > 1:
                        capital_projects.append({
                            'Project_Name': project_name,
                            'type': 'capital',
                            'status': 'design',
                            'source_doc': doc['filename']
                        })

# Also look for patterns like "Capital Improvement Projects (Design)" followed by project names
# Alternative approach: find all project-like names in the design section
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|$)', 
                             text, re.DOTALL | re.IGNORECASE)
    
    if design_match:
        content = design_match.group(1)
        # Split by common project delimiters
        potential_projects = re.split(r'\n\s*\n', content)
        
        for proj in potential_projects:
            proj = proj.strip()
            if proj and len(proj) < 200:  # Likely a project name, not description
                # Extract first line as project name
                first_line = proj.split('\n')[0].strip()
                if first_line and not any(keyword in first_line.lower() for keyword in ['updates', 'schedule', 'project schedule']):
                    # Clean up
                    clean_name = re.sub(r'^[\dA-Za-z]\.\s*', '', first_line)
                    if clean_name and len(clean_name) > 10:
                        # Avoid duplicates
                        if not any(p['Project_Name'] == clean_name for p in capital_projects):
                            capital_projects.append({
                                'Project_Name': clean_name,
                                'type': 'capital',
                                'status': 'design',
                                'source_doc': doc['filename']
                            })

# Get projects with funding > $50,000
funded_projects = {item['Project_Name']: item for item in funding_data if int(item['Amount']) > 50000}

print('__RESULT__:')
print(json.dumps({
    'capital_design_projects': len(capital_projects),
    'high_funding_projects': len(funded_projects),
    'sample_design_projects': capital_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
