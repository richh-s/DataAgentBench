code = """import json

# Load the funding data
funding_path = var_functions.query_db_38
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

print('Loaded', len(funding_records), 'funding records')

# Load the civic documents
civic_path = var_functions.query_db_2
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'civic documents')

# Extract project names from funding data
project_names = [record['Project_Name'] for record in funding_records]
print('Project names from funding data:', len(project_names))
print('First 10:', project_names[:10])

# Now extract project information from civic documents
project_info_map = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Look for project names (usually followed by Updates or Project Schedule)
        if (i + 1 < len(lines) and 
            ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1] or 
             'Project Description:' in lines[i+1])):
            
            project_name = line
            status = 'Unknown'
            
            # Look ahead to find status
            for j in range(i+1, min(i+15, len(lines))):
                next_line = lines[j].strip().lower()
                
                if 'under construction' in next_line:
                    status = 'construction'
                    break
                elif 'construction was completed' in next_line:
                    status = 'completed'
                    break
                elif 'complete design:' in next_line or 'design:' in next_line:
                    if 'design' not in next_line or 'complete' not in next_line:
                        status = 'design'
                        break
                elif 'not started' in next_line:
                    status = 'not started'
                    break
            
            project_info_map[project_name] = status

print('Project info extracted from documents:', len(project_info_map))

# Now combine funding data with status information
final_results = []

for funding_record in funding_records:
    project_name = funding_record['Project_Name']
    amount = int(funding_record['Amount'])
    
    # Find matching project in the civic documents
    status = 'Unknown'
    for doc_project_name, doc_status in project_info_map.items():
        # Check for exact match or close match
        if (project_name == doc_project_name or 
            project_name in doc_project_name or 
            doc_project_name in project_name):
            status = doc_status
            break
    
    final_results.append({
        'Project_Name': project_name,
        'Funding_Source': funding_record['Funding_Source'],
        'Amount': amount,
        'Status': status
    })

# Output results
print('\nFEMA/Emergency Projects Summary:')
print('=' * 80)
for result in final_results:
    print(f"Project: {result['Project_Name']}")
    print(f"Funding Source: {result['Funding_Source']}")
    print(f"Amount: ${result['Amount']:,}")
    print(f"Status: {result['Status']}")
    print('-' * 60)

print(f'\nTotal projects found: {len(final_results)}')

# Format output
print('\n__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': [{'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Encinal Canyon Road Repairs', 'Funding_Source': 'State Development Grant', 'Amount': '47000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Malibu Canyon Road Traffic Study', 'Funding_Source': 'State Development Grant', 'Amount': '97000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Funding_Source': 'State Development Grant', 'Amount': '27000'}, {'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Repair Project', 'Funding_Source': 'Federal Assistance', 'Amount': '30000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}, {'Project_Name': 'project_476', 'Funding_Source': 'State Development Grant', 'Amount': '35000'}, {'Project_Name': 'project_418', 'Funding_Source': 'State Development Grant', 'Amount': '32000'}, {'Project_Name': 'project_393', 'Funding_Source': 'State Development Grant', 'Amount': '25000'}, {'Project_Name': 'project_374', 'Funding_Source': 'State Development Grant', 'Amount': '45000'}, {'Project_Name': 'project_366', 'Funding_Source': 'State Development Grant', 'Amount': '44000'}, {'Project_Name': 'project_118', 'Funding_Source': 'Government Grant', 'Amount': '55000'}, {'Project_Name': 'project_343', 'Funding_Source': 'Government Grant', 'Amount': '60000'}, {'Project_Name': 'project_500', 'Funding_Source': 'State Development Grant', 'Amount': '93000'}, {'Project_Name': 'project_463', 'Funding_Source': 'State Development Grant', 'Amount': '35000'}, {'Project_Name': 'project_459', 'Funding_Source': 'State Development Grant', 'Amount': '26000'}, {'Project_Name': 'project_404', 'Funding_Source': 'State Development Grant', 'Amount': '23000'}, {'Project_Name': 'project_227', 'Funding_Source': 'Federal Assistance', 'Amount': '78000'}, {'Project_Name': 'project_396', 'Funding_Source': 'Federal Assistance', 'Amount': '18000'}, {'Project_Name': 'project_425', 'Funding_Source': 'Federal Assistance', 'Amount': '91000'}, {'Project_Name': 'project_147', 'Funding_Source': 'State Development Grant', 'Amount': '69000'}, {'Project_Name': 'project_342', 'Funding_Source': 'State Development Grant', 'Amount': '61000'}, {'Project_Name': 'project_134', 'Funding_Source': 'Federal Assistance', 'Amount': '32000'}, {'Project_Name': 'project_179', 'Funding_Source': 'State Development Grant', 'Amount': '25000'}, {'Project_Name': 'project_146', 'Funding_Source': 'State Development Grant', 'Amount': '76000'}, {'Project_Name': 'project_55', 'Funding_Source': 'State Development Grant', 'Amount': '32000'}, {'Project_Name': 'project_27', 'Funding_Source': 'State Development Grant', 'Amount': '43000'}, {'Project_Name': 'project_379', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'project_274', 'Funding_Source': 'State Development Grant', 'Amount': '96000'}, {'Project_Name': 'project_412', 'Funding_Source': 'Federal Assistance', 'Amount': '62000'}, {'Project_Name': 'project_172', 'Funding_Source': 'Government Grant', 'Amount': '90000'}, {'Project_Name': 'project_482', 'Funding_Source': 'Government Grant', 'Amount': '80000'}, {'Project_Name': 'project_400', 'Funding_Source': 'State Development Grant', 'Amount': '24000'}, {'Project_Name': 'project_149', 'Funding_Source': 'State Development Grant', 'Amount': '62000'}, {'Project_Name': 'project_148', 'Funding_Source': 'Government Grant', 'Amount': '28000'}, {'Project_Name': 'project_460', 'Funding_Source': 'State Development Grant', 'Amount': '21000'}, {'Project_Name': 'project_332', 'Funding_Source': 'Federal Assistance', 'Amount': '65000'}, {'Project_Name': 'project_304', 'Funding_Source': 'State Development Grant', 'Amount': '73000'}, {'Project_Name': 'project_75', 'Funding_Source': 'Government Grant', 'Amount': '69000'}], 'var_functions.query_db:38': [{'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Encinal Canyon Road Repairs', 'Funding_Source': 'State Development Grant', 'Amount': '47000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Malibu Canyon Road Traffic Study', 'Funding_Source': 'State Development Grant', 'Amount': '97000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Funding_Source': 'State Development Grant', 'Amount': '14000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Funding_Source': 'State Development Grant', 'Amount': '27000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Repair Project', 'Funding_Source': 'Federal Assistance', 'Amount': '30000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}, {'Project_Name': 'project_476', 'Funding_Source': 'State Development Grant', 'Amount': '35000'}, {'Project_Name': 'project_418', 'Funding_Source': 'State Development Grant', 'Amount': '32000'}, {'Project_Name': 'project_393', 'Funding_Source': 'State Development Grant', 'Amount': '25000'}, {'Project_Name': 'project_374', 'Funding_Source': 'State Development Grant', 'Amount': '45000'}, {'Project_Name': 'project_366', 'Funding_Source': 'State Development Grant', 'Amount': '44000'}, {'Project_Name': 'project_118', 'Funding_Source': 'Government Grant', 'Amount': '55000'}, {'Project_Name': 'project_343', 'Funding_Source': 'Government Grant', 'Amount': '60000'}, {'Project_Name': 'project_500', 'Funding_Source': 'State Development Grant', 'Amount': '93000'}, {'Project_Name': 'project_463', 'Funding_Source': 'State Development Grant', 'Amount': '35000'}, {'Project_Name': 'project_459', 'Funding_Source': 'State Development Grant', 'Amount': '26000'}, {'Project_Name': 'project_404', 'Funding_Source': 'State Development Grant', 'Amount': '23000'}, {'Project_Name': 'project_227', 'Funding_Source': 'Federal Assistance', 'Amount': '78000'}, {'Project_Name': 'project_396', 'Funding_Source': 'Federal Assistance', 'Amount': '18000'}, {'Project_Name': 'project_425', 'Funding_Source': 'Federal Assistance', 'Amount': '91000'}, {'Project_Name': 'project_147', 'Funding_Source': 'State Development Grant', 'Amount': '69000'}, {'Project_Name': 'project_342', 'Funding_Source': 'State Development Grant', 'Amount': '61000'}, {'Project_Name': 'project_134', 'Funding_Source': 'Federal Assistance', 'Amount': '32000'}, {'Project_Name': 'project_179', 'Funding_Source': 'State Development Grant', 'Amount': '25000'}, {'Project_Name': 'project_146', 'Funding_Source': 'State Development Grant', 'Amount': '76000'}, {'Project_Name': 'project_55', 'Funding_Source': 'State Development Grant', 'Amount': '32000'}, {'Project_Name': 'project_27', 'Funding_Source': 'State Development Grant', 'Amount': '43000'}, {'Project_Name': 'project_379', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Project_Name': 'project_274', 'Funding_Source': 'State Development Grant', 'Amount': '96000'}, {'Project_Name': 'project_412', 'Funding_Source': 'Federal Assistance', 'Amount': '62000'}, {'Project_Name': 'project_172', 'Funding_Source': 'Government Grant', 'Amount': '90000'}, {'Project_Name': 'project_482', 'Funding_Source': 'Government Grant', 'Amount': '80000'}, {'Project_Name': 'project_400', 'Funding_Source': 'State Development Grant', 'Amount': '24000'}, {'Project_Name': 'project_149', 'Funding_Source': 'State Development Grant', 'Amount': '62000'}, {'Project_Name': 'project_148', 'Funding_Source': 'Government Grant', 'Amount': '28000'}, {'Project_Name': 'project_460', 'Funding_Source': 'State Development Grant', 'Amount': '21000'}, {'Project_Name': 'project_332', 'Funding_Source': 'Federal Assistance', 'Amount': '65000'}, {'Project_Name': 'project_304', 'Funding_Source': 'State Development Grant', 'Amount': '73000'}, {'Project_Name': 'project_75', 'Funding_Source': 'Government Grant', 'Amount': '69000'}]}

exec(code, env_args)
