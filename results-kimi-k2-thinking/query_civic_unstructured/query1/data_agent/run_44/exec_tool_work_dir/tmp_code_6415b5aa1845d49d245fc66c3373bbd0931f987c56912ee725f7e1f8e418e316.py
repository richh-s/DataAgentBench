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

# Extract capital projects in design status from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Simple approach: find the Design section and extract project names
    design_start = text.find('Capital Improvement Projects (Design)')
    construction_start = text.find('Capital Improvement Projects (Construction)')
    
    if design_start > 0:
        if construction_start > design_start:
            design_section = text[design_start:construction_start]
        else:
            design_section = text[design_start:design_start + 3000]  # Limit length
        
        # Split into lines and look for project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines, bullet points, and common non-project lines
            if (line and 
                not line.startswith('(') and 
                not line.startswith('•') and 
                'Project Schedule' not in line and 
                'Updates:' not in line and
                'Estimated Schedule' not in line and
                'RECOMMENDED ACTION' not in line and
                len(line) > 10 and
                len(line) < 120):  # Reasonable project name length
                
                # Remove leading numbering/lettering
                clean_line = re.sub(r'^[A-Za-z0-9]+[.)]\s*', '', line)
                
                # Skip lines that are all uppercase (likely headings)
                if not (clean_line.isupper() and ' ' not in clean_line):
                    # Check if it looks like a project name (contains nouns, not just status words)
                    if any(keyword in clean_line.lower() for keyword in 
                           ['project', 'road', 'beach', 'park', 'storm', 'drain', 'improvement', 
                            'repair', 'structure', 'facility', 'system', 'bridge', 'culvert', 
                            'retaining', 'signal', 'crosswalk', 'median']):
                        design_projects.append(clean_line.strip())

# Remove duplicates while preserving order
design_projects_unique = []
for proj in design_projects:
    if proj not in design_projects_unique:
        design_projects_unique.append(proj)

# Get projects with funding > $50,000
high_funding_projects = []
for item in funding_data:
    if int(item['Amount']) > 50000:
        high_funding_projects.append({
            'Project_Name': item['Project_Name'],
            'Amount': int(item['Amount'])
        })

print('__RESULT__:')
print(json.dumps({
    'design_projects_count': len(design_projects_unique),
    'high_funding_count': len(high_funding_projects),
    'design_projects': design_projects_unique,
    'high_funding_projects': high_funding_projects[:20]  # Sample
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
