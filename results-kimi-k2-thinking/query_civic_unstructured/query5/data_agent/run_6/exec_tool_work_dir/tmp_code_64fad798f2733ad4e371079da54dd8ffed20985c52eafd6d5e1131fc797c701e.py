code = """import json

# From the query results, extract the data
funding_data = var_functions.query_db_74  # Disaster projects
print(f"Found {len(funding_data)} disaster projects in funding database")

# Check the civic documents for 2022 disaster projects
civic_docs = var_functions.query_db_76

# Let's manually extract project information from the civic documents
disaster_2022_projects = []

# Look for patterns indicating disaster projects that started in 2022
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for disaster indicators and 2022
        if '2022' in line:
            # Check surrounding context
            context_start = max(0, i-5)
            context_end = min(len(lines), i+6)
            context = ' '.join(lines[context_start:context_end])
            context_upper = context.upper()
            
            # Check if this is disaster-related
            if any(indicator in context_upper for indicator in ['FEMA', 'CALOES', 'CALJPIA']):
                # Look for project name
                for look_pos in range(max(0, i-3), min(len(lines), i+1)):
                    potential_name = lines[look_pos].strip()
                    if (len(potential_name) > 10 and 
                        potential_name == potential_name.title() and 
                        not potential_name.startswith('(') and 
                        not potential_name.isupper()):
                        # Match with funding data
                        doc_project_clean = potential_name.split('(')[0].strip().upper()
                        
                        for fund_record in funding_data:
                            fund_name = fund_record['Project_Name'].upper()
                            fund_clean = fund_name.split('(')[0].strip()
                            
                            if (doc_project_clean == fund_clean or 
                                doc_project_clean in fund_clean or 
                                fund_clean in doc_project_clean):
                                
                                project_data = {
                                    'Project_Name': fund_record['Project_Name'],
                                    'Amount': int(fund_record['Amount'])
                                }
                                if project_data not in disaster_2022_projects:
                                    disaster_2022_projects.append(project_data)
                                    break

# Remove duplicates
unique_projects = []
seen_names = set()
for proj in disaster_2022_projects:
    if proj['Project_Name'] not in seen_names:
        seen_names.add(proj['Project_Name'])
        unique_projects.append(proj)

total_funding = sum(p['Amount'] for p in unique_projects)
num_projects = len(unique_projects)

print(f"\n{'='*70}")
print(f"RESULT: {num_projects} disaster projects started in 2022")
print(f"TOTAL FUNDING: ${total_funding:,}")
print(f"{'='*70}")

print("\nProjects:")
for proj in unique_projects:
    print(f"  - {proj['Project_Name']}: ${proj['Amount']:,}")

result = {
    'total_funding': total_funding,
    'num_projects': num_projects,
    'projects': unique_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.list_db:22': ['civic_docs'], 'var_functions.list_db:32': ['civic_docs'], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:64': {'error': 'Data access failed'}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:68': [], 'var_functions.query_db:74': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:76': 'file_storage/functions.query_db:76.json', 'var_functions.query_db:78': 'file_storage/functions.query_db:78.json'}

exec(code, env_args)
