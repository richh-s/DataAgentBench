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
print("Total funding records: " + str(len(funding_df)))

# Process civic documents to extract project information
print("Processing civic documents to extract project information...")

# Look specifically for completed projects in 2022 with park topic
park_projects_2022 = []

for doc in civic_docs_data:
    text = doc['text']
    
    # Look for park-related projects that were completed in 2022
    # Pattern: project name, then later "completed" and "2022" or "November 2022"
    
    # First, find sections that mention both "park" and completion in 2022
    if 'park' in text.lower() and ('2022' in text or 'November 2022' in text):
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Look for project names (not headers)
            if (line and len(line) > 5 and not line.startswith('(') and 
                not any(header in line for header in ['Agenda', 'Public Works', 'Commission', 
                                                     'Capital Improvement', 'Page', 'Item', 'To:', 'From:'])):
                
                # Look ahead for completion status and year
                context = '\n'.join(lines[i:i+15])
                
                # Check if this is a park project completed in 2022
                if ('park' in context.lower() and 
                    ('completed' in context.lower() or 'construction was completed' in context.lower()) and
                    ('2022' in context or 'November 2022' in context)):
                    
                    # Look for funding amount patterns
                    amount_match = re.search(r'\$([\d,]+)', context)
                    budget_match = re.search(r'(?:budget|cost|amount).*?\$([\d,]+)', context, re.IGNORECASE)
                    
                    park_projects_2022.append({
                        'Project_Name': line,
                        'Context': context[:200]
                    })

print("Park projects completed in 2022 found in documents:")
for proj in park_projects_2022:
    print("Project: " + proj['Project_Name'])
    print("Context preview: " + proj['Context'][:150] + "...")
    print("---")

print("\nTotal projects found: " + str(len(park_projects_2022)))

# Now, let's get more systematic and look for specific projects mentioned
print("\nLooking for specific park projects in funding data...")

# Check for park-related projects in funding data
park_funding = funding_df[funding_df['Project_Name'].str.contains('park|Park', case=False, na=False)]
print("\nPark-related funding records:")
print(park_funding[['Project_Name', 'Amount']].to_string())

# Create a list of specific projects to search for
specific_projects = [
    'Bluffs Park Shade Structure',
    'Bluffs Park Workout Station',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
    'Malibu Bluffs Park Roof Replacement Project',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Trancas Canyon Park Upper and Lower Slopes Repair'
]

print("\nChecking for these specific park projects in our data:")
for project_name in specific_projects:
    matching = funding_df[funding_df['Project_Name'] == project_name]
    if not matching.empty:
        amount = matching.iloc[0]['Amount']
        print(project_name + ": $" + str(amount))
    else:
        # Check for partial matches
        partial_matches = funding_df[funding_df['Project_Name'].str.contains(project_name.split()[0], case=False, na=False)]
        if not partial_matches.empty:
            for _, row in partial_matches.iterrows():
                print("Potential match for " + project_name + ": " + row['Project_Name'] + " ($" + str(row['Amount']) + ")")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
