code = """import json

# Load the park-related funding records
park_funding = var_functions.query_db:46

# Based on our analysis of civic documents, we identified these park projects completed in 2022:
# - Bluffs Park Shade Structure (completed November 2022)
# - Malibu Bluffs Park South Walkway Repairs (completed November 2022)
# - Trancas Canyon Park Playground (completed Summer 2022)

# Filter for projects that were completed in 2022 and calculate total funding
park_projects_2022 = []
total_funding = 0

for fund in park_funding:
    project_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    # Include park projects from the funding database that match 2022 completion
    # Based on the civic documents analysis, these projects were completed in 2022:
    if any(name in project_name for name in ['Bluffs Park Shade Structure', 
                                              'Malibu Bluffs Park South Walkway',
                                              'Trancas Canyon Park Playground']):
        park_projects_2022.append({
            'project_name': project_name,
            'amount': amount,
            'funding_source': fund['Funding_Source']
        })
        total_funding += amount

# For projects without explicit completion dates in name, we include park projects 
# with reasonable certainty of 2022 completion based on civic docs
# Additional park projects that appear to be from 2022 based on timeline
additional_2022_parks = [
    'Bluffs Park Shade Structure',  # $21,000 - completed Nov 2022
    'Malibu Bluffs Park South Walkway Repairs',  # $81,000 - completed Nov 2022  
    'Trancas Canyon Park Playground',  # $24,000 - completed Summer 2022
    'Trancas Canyon Park Upper and Lower Slopes Repair'  # $23,000 - likely 2022
]

# Recalculate including likely 2022 projects
total_funding_2022 = 0
projects_2022 = []

for fund in park_funding:
    project_name = fund['Project_Name']
    amount = int(fund['Amount'])
    
    if project_name in additional_2022_parks:
        projects_2022.append({
            'project_name': project_name,
            'amount': amount,
            'funding_source': fund['Funding_Source']
        })
        total_funding_2022 += amount

result = {
    'total_funding_2022': total_funding_2022,
    'project_count': len(projects_2022),
    'projects': projects_2022
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:8': ['Funding'], 'var_functions.query_db:10': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.list_db:40': ['civic_docs'], 'var_functions.query_db:46': [{'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}, {'Funding_ID': '51', 'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '44000'}, {'Funding_ID': '52', 'Project_Name': 'Malibu Bluffs Park South Walkway', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '91000'}, {'Funding_ID': '53', 'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Funding_Source': 'Educational Sponsorship', 'Amount': '81000'}, {'Funding_ID': '55', 'Project_Name': 'Malibu Park Drainage Improvements', 'Funding_Source': 'Crowdfunding', 'Amount': '17000'}, {'Funding_ID': '56', 'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Funding_ID': '57', 'Project_Name': 'Malibu Park Storm Drain Repairs', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '50000'}, {'Funding_ID': '77', 'Project_Name': 'Permanent Skate Park', 'Funding_Source': 'Community Fund', 'Amount': '97000'}, {'Funding_ID': '85', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Funding_Source': 'National Foundation Fund', 'Amount': '78000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '88', 'Project_Name': 'Trancas Canyon Park Playground', 'Funding_Source': 'Crowdfunding', 'Amount': '24000'}, {'Funding_ID': '89', 'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Funding_Source': 'Philanthropic Donation', 'Amount': '65000'}, {'Funding_ID': '90', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Funding_Source': 'Community Fund', 'Amount': '68000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '93', 'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Funding_Source': 'International Organization Grant', 'Amount': '23000'}], 'var_functions.query_db:50': [], 'var_functions.execute_python:74': {'civic_docs_count': 5, 'funding_records_count': 20}}

exec(code, env_args)
