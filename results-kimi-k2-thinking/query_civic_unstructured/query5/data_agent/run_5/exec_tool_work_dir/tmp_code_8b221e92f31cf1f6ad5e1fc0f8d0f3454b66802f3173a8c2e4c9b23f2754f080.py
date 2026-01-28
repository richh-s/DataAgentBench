code = """import json
import re

# Load funding data
with open(locals()['var_functions.query_db:6'], 'r') as f:
    funding_records = json.load(f)

# Load civic documents
with open(locals()['var_functions.query_db:8'], 'r') as f:
    civic_docs = json.load(f)

# Define disaster indicators
DISASTER_SUFFIXES = [
    '(FEMA Project)',
    '(FEMA/CalOES Project)',
    '(CalOES Project)',
    '(CalJPIA Project)',
    '(FEMA)',
    '(FEMA/CalOES)'
]

# Create mapping of base project names to full disaster project names and amounts
# This handles cases where multiple disaster variants exist for same base project
base_to_disaster = {}
for record in funding_records:
    proj_name = record['Project_Name']
    if any(proj_name.endswith(suffix) for suffix in DISASTER_SUFFIXES):
        base_name = proj_name
        for suffix in DISASTER_SUFFIXES:
            base_name = base_name.replace(suffix, '').strip()
        base_lower = base_name.lower()
        
        if base_lower not in base_to_disaster:
            base_to_disaster[base_lower] = []
        
        base_to_disaster[base_lower].append({
            'full_name': proj_name,
            'amount': int(record['Amount'])
        })

# Function to check if project started in 2022
def project_started_in_2022(base_name, civic_docs):
    base_lower = base_name.lower()
    
    for doc in civic_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Check if base project name appears in document
        if base_lower in text.lower():
            # Check if any date with 2022 appears near the project or in filename
            if '2022' in filename:
                return True
                
            # Check surrounding context for date mentions
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if base_lower in line.lower():
                    # Look in surrounding lines for 2022 date
                    context_window = lines[max(0, i-3):min(len(lines), i+10)]
                    context = ' '.join(context_window).lower()
                    
                    # Look for 2022 with time-related words
                    if '2022' in context:
                        # Check for start/duration words
                        time_keywords = ['begin', 'start', 'advertise', 'initiate', 'complete', 'end', 'construction', 'design']
                        if any(kw in context for kw in time_keywords):
                            return True
    
    return False

# Find all disaster projects that started in 2022
funded_projects_2022 = []
total_funding = 0

for base_name, disaster_list in base_to_disaster.items():
    if project_started_in_2022(base_name, civic_docs):
        # All disaster variants for this base project started in 2022
        for disaster_proj in disaster_list:
            funded_projects_2022.append(disaster_proj)
            total_funding += disaster_proj['amount']

# Prepare result
result = {
    'total_funding': total_funding,
    'project_count': len(funded_projects_2022),
    'projects': funded_projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'funding_records_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:20': {'funding_records_count': 500, 'civic_docs_count': 5, 'first_funding_record': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'first_civic_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_length': 9796}}, 'var_functions.execute_python:22': {'disaster_projects_count': 26, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 85000, 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Base_Name': 'Birdview Avenue Improvements', 'Amount': 14000, 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Base_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Amount': 81000, 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Base_Name': 'Clover Heights Storm Drain', 'Amount': 21000, 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 43000, 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Culvert Repairs', 'Amount': 15000, 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 25000, 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Base_Name': 'Corral Canyon Road Bridge Repairs', 'Amount': 58000, 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 18000, 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Base_Name': 'Encinal Canyon Road Drainage Improvements', 'Amount': 94000, 'Funding_Source': 'Private Sponsor'}]}}

exec(code, env_args)
