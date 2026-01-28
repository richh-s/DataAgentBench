code = """import json
import re

# Read files
funding_file = locals()['var_functions.query_db:12']
civic_file = locals()['var_functions.query_db:10']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_data = json.load(f)

# Filter funding for projects related to emergency/FEMA
# Look for projects with FEMA in name or emergency-related sources
emergency_patterns = ['FEMA', 'emergency', 'disaster', 'fire', 'warning']

filtered_funding = []
for record in funding_data:
    project_name = record['Project_Name'].lower()
    funding_source = record['Funding_Source'].lower()
    
    # Check if any pattern matches
    matches = any(pattern in project_name or pattern in funding_source 
                  for pattern in emergency_patterns)
    
    # Also check related project patterns
    if not matches:
        # Check for related project types
        if any(term in project_name for term in ['siren', 'warning', 'guardrail', 'culvert', 'storm drain']):
            matches = True
    
    if matches:
        filtered_funding.append(record)

# Count FEMA-specific vs emergency-related
fema_funding = [r for r in funding_data if 'fema' in r['Project_Name'].lower() or 'fema' in r['Funding_Source'].lower()]
emergency_funding = [r for r in funding_data if 'emergency' in r['Project_Name'].lower() or 'emergency' in r['Funding_Source'].lower()]

result = {
    'emergency_related_count': len(filtered_funding),
    'fema_count': len(fema_funding),
    'emergency_count': len(emergency_funding),
    'fema_projects': fema_funding,
    'emergency_projects': emergency_funding,
    'combined_related': filtered_funding[:20]  # First 20 for preview
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.execute_python:5': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'funding_count': 500, 'civic_count': 5, 'sample_funding': [{'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}], 'sample_civic_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current an'}}

exec(code, env_args)
