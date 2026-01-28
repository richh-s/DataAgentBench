code = """import json

# Read civic documents
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Create funding dictionary by project name
funding_dict = {}
for item in funding_data:
    name = item['Project_Name'].lower().replace('  ', ' ').strip()
    funding_dict[name] = int(item['Amount'])

# Find park projects completed in 2022 based on the document text
park_projects_2022 = []

# From the sample preview, we saw these projects completed in November 2022:
# - Bluffs Park Shade Structure
# - Marie Canyon Green Streets  
# - Broad Beach Road Water Quality Repair
# - Point Dume Walkway Repairs

# Check which of these are park-related and find their funding
potential_projects = [
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets',
    'Broad Beach Road Water Quality Repair', 
    'Point Dume Walkway Repairs',
    'Legacy Park Benches and Arbors Renovation',
    'Legacy Park Paver Repair Project',
    'Malibu Bluffs Park Roof Replacement Project',
    'Malibu Bluffs Park South Walkway',
    'Malibu Bluffs Park South Walkway Repairs',
    'Malibu Park Drainage Improvements',
    'Malibu Park Resurfacing Project',
    'Malibu Park Storm Drain Repairs'
]

# Check each document for 2022 completions and collect matching projects
projects_with_funding = []
total_funding = 0

for doc in civic_docs_data:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check if this document mentions 2022 completions
    if '2022' in text and 'completed' in text_lower:
        for proj_name in potential_projects:
            proj_lower = proj_name.lower()
            if proj_lower in text_lower:
                # Check if the context mentions completion in 2022
                # Find the position of the project name
                proj_pos = text_lower.find(proj_lower)
                # Get surrounding text
                context = text_lower[max(0, proj_pos-200):proj_pos+200]
                if '2022' in context and 'completed' in context:
                    # Found a match - get funding
                    if proj_lower in funding_dict:
                        amount = funding_dict[proj_lower]
                        total_funding += amount
                        projects_with_funding.append({
                            'project': proj_name,
                            'amount': amount
                        })

# Get unique projects
unique_projects = []
seen = set()
for proj in projects_with_funding:
    if proj['project'] not in seen:
        unique_projects.append(proj)
        seen.add(proj['project'])

print('__RESULT__:')
print(json.dumps({
    'total_funding': total_funding,
    'projects': unique_projects,
    'count': len(unique_projects)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': 'file_storage/functions.execute_python:5.json', 'var_functions.execute_python:12': {'park_funding_projects_count': 20, 'sample_park_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}]}, 'var_functions.execute_python:18': {'total_park_projects': 20, 'total_funding_all_parks': 1033000, 'sample_projects': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}]}}

exec(code, env_args)
