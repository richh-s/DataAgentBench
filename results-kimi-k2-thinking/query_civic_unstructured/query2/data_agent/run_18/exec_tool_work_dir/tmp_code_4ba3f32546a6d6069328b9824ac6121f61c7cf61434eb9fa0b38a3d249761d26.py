code = """import json
import pandas as pd
import re

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
print('Total funding records: ' + str(len(funding_df)))

# Look for park-related projects in funding data
park_funding = funding_df[funding_df['Project_Name'].str.contains('park|Park', case=False, na=False)]
print('\nPark-related funding records found:')
print(park_funding[['Project_Name', 'Amount']].to_string())

# Check which of these might be completed in 2022
print('\nAnalyzing civic documents for park projects completed in 2022...')

# Process documents to find park projects completed in 2022
completed_2022_projects = []

for doc in civic_docs_data:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project name indicators
        if (line and len(line) > 5 and not line.startswith('(') and 
            not any(header in line for header in ['Agenda', 'Public Works', 'Commission', 'Capital Improvement'])):
            
            # Check context for park, completion, and 2022
            context_start = max(0, i-2)
            context_end = min(len(lines), i+20)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if ('park' in context and 
                ('completed' in context or 'complete construction' in context) and
                ('2022' in context or 'november 2022' in context or 'december 2022' in context)):
                
                completed_2022_projects.append(line)

print('\nPark projects completed in 2022 found in documents:')
for proj in completed_2022_projects:
    print('- ' + proj)

# Now match these with funding data
print('\nMatching with funding data...')
total_funding = 0
funded_projects = []

for project_name in completed_2022_projects:
    # Try exact match first
    match = funding_df[funding_df['Project_Name'] == project_name]
    if not match.empty:
        amount = int(match.iloc[0]['Amount'])
        total_funding += amount
        funded_projects.append((project_name, amount))
    else:
        # Try partial match
        words = project_name.split()
        if len(words) > 1:
            # Use first few words for matching
            search_term = ' '.join(words[:3])
            partial_matches = funding_df[funding_df['Project_Name'].str.contains(search_term, case=False, na=False)]
            if not partial_matches.empty:
                for _, row in partial_matches.iterrows():
                    amount = int(row['Amount'])
                    total_funding += amount
                    funded_projects.append((row['Project_Name'], amount))

print('\nFunded park projects completed in 2022:')
for name, amount in funded_projects:
    print(f'- {name}: ${amount:,}')

print('\nTotal funding for park projects completed in 2022: ${:,}'.format(total_funding))

# Also check funding data directly for patterns indicating 2022 completion
print('\nChecking funding table for additional park projects...')
for _, row in funding_df.iterrows():
    project_name = row['Project_Name']
    if 'Park' in project_name or 'park' in project_name:
        # Some projects might have year in name
        if '2022' in project_name:
            amount = int(row['Amount'])
            total_funding += amount
            funded_projects.append((project_name, amount))
            print(f'Found year-specific project: {project_name}: ${amount:,}')

print('\nFinal total funding for park-related projects completed in 2022: ${:,}'.format(total_funding))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
