code = """import json
import re

# Load funding and civic docs data
funding_records = locals()['var_functions.query_db:56']
civic_docs = locals()['var_functions.query_db:58']

# Strategy: Find projects where 2022 appears in civic docs near disaster indicators
disaster_funding_2022 = 0
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions 2022
    if '2022' not in text:
        continue
    
    # Look for disaster keywords in the text
    has_disaster = any(keyword in text for keyword in ['FEMA', 'CalOES', 'CalJPIA', 'disaster'])
    
    if not has_disaster:
        continue
    
    # Find project names in the document
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if line and len(line) > 10:  # Skip very short lines
            # Check if this is a project name (starts with capitals or 2022)
            if re.match(r'^[A-Z0-9]', line):
                # Remove suffixes to get base name
                base_name = line.split(' (')[0].strip()
                
                # Check if this project has funding with disaster suffix
                for funding_record in funding_records:
                    funding_name = funding_record['Project_Name']
                    funding_base = funding_name.split(' (')[0].strip()
                    
                    # Match by base name
                    if (funding_base == base_name or 
                        funding_base in base_name or 
                        base_name in funding_base):
                        
                        # Check if context near this line mentions 2022
                        line_index = lines.index(line)
                        start_context = max(0, line_index-3)
                        end_context = min(len(lines), line_index+5)
                        context = ' '.join(lines[start_context:end_context])
                        
                        if '2022' in context:
                            amount = int(funding_record['Amount'])
                            if base_name not in disaster_projects_2022:
                                disaster_projects_2022.append(base_name)
                            disaster_funding_2022 += amount

# Also check for projects explicitly named with 2022
for record in funding_records:
    project_name = record['Project_Name']
    if '2022' in project_name:
        # Check if it's disaster-related by checking base project
        base_name = project_name.split(' (')[0].strip()
        # Verify it's disaster project by checking if there's a disaster version
        for check_record in funding_records:
            check_name = check_record['Project_Name']
            check_base = check_name.split(' (')[0].strip()
            if (check_base == base_name and 
                any(suffix in check_name for suffix in ['(FEMA', '(CalOES', '(CalJPIA'])):
                disaster_funding_2022 += int(record['Amount'])
                if base_name not in disaster_projects_2022:
                    disaster_projects_2022.append(base_name)

# Remove duplicates and calculate unique funding
disaster_projects_2022 = list(set(disaster_projects_2022))

print('__RESULT__:')
print(json.dumps({
    'total_disaster_funding_2022': disaster_funding_2022,
    'project_count': len(disaster_projects_2022),
    'project_names': disaster_projects_2022
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'status': 'loaded', 'count': 0}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'status': 'checked_types'}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000', 'Funding_Source': 'Research Institution Funding'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000', 'Funding_Source': 'Government Grant'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000', 'Funding_Source': 'Local NGO Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000', 'Funding_Source': 'Taxpayer Contribution'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000', 'Funding_Source': 'Local Business Support'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000', 'Funding_Source': 'Cultural Heritage Grant'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000', 'Funding_Source': 'Educational Sponsorship'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000', 'Funding_Source': 'Private Sponsor'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000', 'Funding_Source': 'Impact Investment Fund'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000', 'Funding_Source': 'Development Bank Loan'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000', 'Funding_Source': 'Federal Assistance'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000', 'Funding_Source': 'National Foundation Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000', 'Funding_Source': 'Municipal Fund'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000', 'Funding_Source': 'Community Fund'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000', 'Funding_Source': 'International Aid'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000', 'Funding_Source': 'Environmental Grant'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000', 'Funding_Source': 'State Development Grant'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000', 'Funding_Source': 'Local Business Support'}], 'var_functions.query_db:44': [{'total_funding': '1410000'}], 'var_functions.query_db:46': [], 'var_functions.query_db:52': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'total_amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'total_amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'total_amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'total_amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'total_amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'total_amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'total_amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'total_amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'total_amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'total_amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'total_amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'total_amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'total_amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'total_amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'total_amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'total_amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'total_amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'total_amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'total_amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'total_amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'total_amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'total_amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'total_amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'total_amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'total_amount': '77000'}], 'var_functions.query_db:56': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.query_db:62': [{'total_funding': 'None'}], 'var_functions.query_db:64': [{'Project_Name': '2022 Annual Street Maintenance', 'Amount': '45000'}, {'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Amount': '38000'}]}

exec(code, env_args)
