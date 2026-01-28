code = """import json
import pandas as pd
import re
import os

# Load the data files
funding_file = locals()['var_functions.query_db:10']
civic_file = locals()['var_functions.query_db:6']

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project info from civic documents
# Looking for disaster projects with 2022 dates

potential_disaster_projects = set()
disaster_keywords = ['(fema', '(caloes', '(caljpia', 'emergency', 'fire', 'disaster', 'warning siren']
year_keywords = ['2022']

for doc in civic_docs:
    text = doc.get('text', '').lower()
    filename = doc.get('filename', '').lower()
    
    # Check if document is from 2022
    is_2022_file = '2022' in filename
    
    # Find all projects in the text
    # Projects usually appear at the start of lines or after bullet points
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) > 10 and not line.startswith(('page', 'agenda', 'to:', 'prepared', 'approved', 'date', 'meeting', 'subject', 'recommended', 'discussion')):
            # Check if this is a disaster project
            line_lower = line.lower()
            
            # Check for disaster keywords
            is_disaster = any(keyword in line_lower for keyword in disaster_keywords)
            
            if is_disaster:
                potential_disaster_projects.add(line)

# Match with funding records
total_funding = 0
match_details = []

for funding in funding_records:
    fund_name = funding.get('Project_Name', '').lower()
    fund_amount = float(funding.get('Amount', 0))
    
    # Check if this is a disaster/2022 project
    is_disaster_funding = any(keyword in fund_name for keyword in disaster_keywords)
    is_2022_funding = '2022' in fund_name
    
    if is_disaster_funding:
        total_funding += fund_amount
        match_details.append(funding)

result = {
    'total_funding': total_funding,
    'matching_records': len(match_details),
    'sample_matches': match_details[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:14': {'funding_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
