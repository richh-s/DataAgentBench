code = """import json

# Load Spring 2022 documents
spring_docs_path = var_functions.query_db:38
with open(spring_docs_path, 'r') as f:
    spring_docs = json.load(f)

print('Loaded', len(spring_docs), 'documents mentioning Spring 2022')

# Load funding data
funding_path = var_functions.query_db:50
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('Loaded', len(funding_data), 'funding records')

# Identify projects that started in Spring 2022 based on document analysis
# These are projects explicitly mentioned in the documents with Spring 2022 start dates
spring_2022_project_names = [
    "Marie Canyon Green Streets",
    "PCH Median Improvements Project", 
    "PCH Signal Synchronization System Improvements Project",
    "Bluffs Park Shade Structure",
    "Broad Beach Road Water Quality Infrastructure Repairs",
    "Latigo Canyon Road Roadway/Retaining Wall Improvements",
    "2021 Annual Street Maintenance",
    "Civic Center Stormwater Diversion Structure"
]

# Map normalized names to actual funding records
funding_map = {}

for project_base_name in spring_2022_project_names:
    # Find matching funding records
    matching_records = []
    
    for record in funding_data:
        record_name = record['Project_Name']
        
        # Check for direct match or containment
        if (project_base_name.lower() in record_name.lower() or 
            record_name.lower() in project_base_name.lower()):
            matching_records.append(record)
    
    if matching_records:
        # Use the base project name as key
        key = project_base_name
        if key not in funding_map:
            funding_map[key] = []
        funding_map[key].extend(matching_records)

# Calculate total funding (avoiding double-counting by using record IDs)
processed_ids = set()
total_funding = 0
project_details = []

for project_name, records in funding_map.items():
    project_funding = 0
    funding_sources = []
    
    for record in records:
        record_id = record['Funding_ID']
        if record_id not in processed_ids:
            amount = int(record['Amount'])
            project_funding += amount
            total_funding += amount
            funding_sources.append({
                'source': record['Funding_Source'],
                'amount': amount,
                'exact_name': record['Project_Name']
            })
            processed_ids.add(record_id)
    
    if project_funding > 0:
        project_details.append({
            'project_name': project_name,
            'total_funding': project_funding,
            'funding_records': funding_sources
        })

# Sort projects by funding amount
project_details.sort(key=lambda x: x['total_funding'], reverse=True)

# Prepare result
result = {
    'project_count': len(project_details),
    'total_funding': total_funding,
    'projects': project_details
}

print('\n=== SUMMARY ===')
print('Projects starting in Spring 2022:', len(project_details))
print('Total funding: $' + str(total_funding))
print('\nProjects breakdown:')
for p in project_details:
    print(f"- {p['project_name']}: ${p['total_funding']:,}")

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:16': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:50': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '46', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '61', 'Project_Name': 'Marie Canyon Green Streets', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '50000'}, {'Funding_ID': '71', 'Project_Name': 'PCH Median Improvements Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '56000'}, {'Funding_ID': '72', 'Project_Name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Funding_Source': 'State Development Grant', 'Amount': '27000'}, {'Funding_ID': '74', 'Project_Name': 'PCH Signal Synchronization System Improvements Project', 'Funding_Source': 'International Aid', 'Amount': '16000'}]}

exec(code, env_args)
