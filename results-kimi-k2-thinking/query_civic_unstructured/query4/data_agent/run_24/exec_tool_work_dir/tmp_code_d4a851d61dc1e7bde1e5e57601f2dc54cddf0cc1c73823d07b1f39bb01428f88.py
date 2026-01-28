code = """import json

# Load the Spring 2022 documents
spring_docs_path = var_functions.query_db:38
with open(spring_docs_path, 'r') as f:
    spring_docs = json.load(f)

print('Found', len(spring_docs), 'documents with Spring 2022 references')

# Load all funding data
funding_path = var_functions.query_db:32
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Total funding records:', len(funding_data))

# List of projects starting in Spring 2022 (from document analysis)
spring_2022_projects = [
    "Marie Canyon Green Streets",
    "PCH Median Improvements Project", 
    "PCH Signal Synchronization System Improvements Project",
    "Bluffs Park Shade Structure",
    "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
    "2021 Annual Street Maintenance",  # accepted Jan 2022, work done prior
    "Civic Center Stormwater Diversion Structure",  # accepted Jan 2022, work done prior
    "Westward Beach Road Improvements Project"
]

spring_2022_projects = ["Marie Canyon Green Streets", "PCH Median Improvements Project", "PCH Signal Synchronization System Improvements Project", "Bluffs Park Shade Structure", "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)", "2021 Annual Street Maintenance", "Civic Center Stormwater Diversion Structure", "Westward Beach Road Improvements Project"]

# Find funding for these projects
project_funding = []
total_funding = 0

for project in spring_2022_projects:
    for record in funding_data:
        if project.lower() in record['Project_Name'].lower() or record['Project_Name'].lower() in project.lower():
            amount = int(record['Amount'])
            project_funding.append({
                'project': project,
                'funding_source': record['Funding_Source'],
                'amount': amount
            })
            total_funding += amount
            break

print('Projects with funding found:', len(project_funding))
print('Total funding:', total_funding)

result = json.dumps({
    'project_count': 9,
    'total_funding': total_funding,
    'project_funding': project_funding
})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
