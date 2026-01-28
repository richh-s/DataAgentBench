code = """import json
import re

# Load the two data files
funding_file = locals()['var_functions.query_db:0']
civic_file = locals()['var_functions.query_db:2']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print('Loaded {} funding records and {} civic documents'.format(len(funding_data), len(civic_docs)))

# Step 1: Filter FEMA/emergency projects from funding data
fema_funding = []
for record in funding_data:
    project_name = record.get('Project_Name', '').lower()
    if 'fema' in project_name or 'emergency' in project_name:
        fema_funding.append({
            'Project_Name': record.get('Project_Name'),
            'Funding_Source': record.get('Funding_Source'),
            'Amount': int(record.get('Amount', 0))
        })

print('Found {} FEMA/emergency funding records'.format(len(fema_funding)))

# Step 2: Extract project status information from civic documents
project_statuses = {}
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_project = None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Detect project names (heuristic: lines that look like titles)
        if len(line) > 10 and not line.startswith('(') and not line.startswith('Page'):
            if any(word in line.lower() for word in ['project', 'improvements', 'repairs', 'replacement']):
                current_project = line
                if current_project not in project_statuses:
                    project_statuses[current_project] = {'status': 'unknown', 'topics': []}
        
        # Extract status information
        if current_project:
            lower_line = line.lower()
            if any(phrase in lower_line for phrase in ['construction was completed', 'notice of completion filed']):
                project_statuses[current_project]['status'] = 'completed'
            elif 'design' in lower_line:
                project_statuses[current_project]['status'] = 'design'
            elif 'construction' in lower_line and 'not started' not in lower_line:
                project_statuses[current_project]['status'] = 'in_progress'
            
            # Extract topics
            if 'fema' in lower_line:
                project_statuses[current_project]['topics'].append('fema')
            if 'storm' in lower_line and 'drain' in lower_line:
                project_statuses[current_project]['topics'].append('storm drain')

print('Extracted {} project status records'.format(len(project_statuses)))

# Step 3: Match funding data with status information
final_results = []
for funding_proj in fema_funding:
    proj_name = funding_proj['Project_Name']
    
    # Try to find matching status info
    status = 'unknown'
    topics = []
    
    # First try exact match
    if proj_name in project_statuses:
        status = project_statuses[proj_name]['status']
        topics = project_statuses[proj_name]['topics']
    else:
        # Try fuzzy matching
        for key, info in project_statuses.items():
            # Check if project names share significant words
            proj_words = set(proj_name.lower().split())
            key_words = set(key.lower().split())
            # Remove common words
            common = {'project', 'improvements', 'repairs', 'and', 'the', 'road'}
            proj_words = proj_words - common
            key_words = key_words - common
            
            if len(proj_words.intersection(key_words)) >= 2:
                status = info['status']
                topics = info['topics']
                break
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding_proj['Funding_Source'],
        'Amount': funding_proj['Amount'],
        'Status': status,
        'Topics': ', '.join(topics) if topics else 'None'
    })

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

print('\nFINAL RESULTS:')
print('=' * 80)
for i, proj in enumerate(final_results[:15], 1):
    amt_str = '${:,}'.format(proj['Amount'])
    print('{}. {}'.format(i, proj['Project_Name']))
    print('   Funding Source: {}'.format(proj['Funding_Source']))
    print('   Amount: {}'.format(amt_str))
    print('   Status: {}'.format(proj['Status']))
    print('   Topics: {}'.format(proj['Topics']))
    print()

print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [{'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 92000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 91000}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': 84000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': 81000}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 80000}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': 78000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': 44000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 43000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': 27000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}]}

exec(code, env_args)
