code = """import json
import re

# Read funding data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Create funding dictionary
funding_dict = {}
for record in funding_data:
    project_name = record.get('Project_Name', '')
    if project_name:
        funding_dict[project_name] = {
            'Funding_Source': record.get('Funding_Source', ''),
            'Amount': int(record.get('Amount', 0))
        }

# Read civic documents
civic_file = locals()['var_functions.query_db:18']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract emergency/FEMA projects from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    current_type = None
    current_status = None
    
    for line in lines:
        line_clean = line.strip()
        
        # Check section headers
        if 'Capital Improvement Projects (Design)' in line_clean:
            current_type = 'capital'
            current_status = 'design'
        elif 'Capital Improvement Projects (Construction)' in line_clean:
            current_type = 'capital'
            current_status = 'completed'
        elif 'Capital Improvement Projects (Not Started)' in line_clean:
            current_type = 'capital'
            current_status = 'not started'
        elif 'Disaster Recovery' in line_clean:
            current_type = 'disaster'
            current_status = 'design' if 'Design' in line_clean else 'completed' if 'Construction' in line_clean else 'not started'
        
        # Look for project names
        elif current_type and line_clean and len(line_clean) > 15:
            lower_clean = line_clean.lower()
            if any(term in lower_clean for term in ['fema', 'emergency', 'warning', 'siren', 'disaster']):
                # Skip unwanted lines
                skip_words = ['Project Description:', 'Project Updates:', 'Project Schedule:', 'RECOMMENDED', 'DISCUSSION:']
                if not any(skip in line_clean for skip in skip_words):
                    projects.append({
                        'Project_Name': line_clean,
                        'Status': current_status
                    })

# Merge with funding data
result = []
seen_projects = set()

for proj in projects:
    proj_name = proj['Project_Name']
    
    # Direct match
    if proj_name in funding_dict:
        fund_data = funding_dict[proj_name]
        if proj_name not in seen_projects:
            result.append({
                'Project_Name': proj_name,
                'Funding_Source': fund_data['Funding_Source'],
                'Amount': fund_data['Amount'],
                'Status': proj['Status']
            })
            seen_projects.add(proj_name)
    else:
        # Partial match
        for fund_name, fund_data in funding_dict.items():
            if fund_name in proj_name or proj_name in fund_name:
                if fund_name not in seen_projects:
                    result.append({
                        'Project_Name': fund_name,
                        'Funding_Source': fund_data['Funding_Source'],
                        'Amount': fund_data['Amount'],
                        'Status': proj['Status']
                    })
                    seen_projects.add(fund_name)
                break

# Also include projects from funding data that don't appear in civic docs
if not result:
    for proj_name, fund_data in funding_dict.items():
        if any(term in proj_name.lower() for term in ['fema', 'emergency', 'warning', 'siren']):
            result.append({
                'Project_Name': proj_name,
                'Funding_Source': fund_data['Funding_Source'],
                'Amount': fund_data['Amount'],
                'Status': 'Unknown'
            })

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '73', 'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '98', 'Project_Name': 'Westward Beach Road Repair Project', 'Funding_Source': 'Federal Assistance', 'Amount': '30000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}, {'Funding_ID': '222', 'Project_Name': 'project_227', 'Funding_Source': 'Federal Assistance', 'Amount': '78000'}, {'Funding_ID': '224', 'Project_Name': 'project_396', 'Funding_Source': 'Federal Assistance', 'Amount': '18000'}, {'Funding_ID': '230', 'Project_Name': 'project_425', 'Funding_Source': 'Federal Assistance', 'Amount': '91000'}, {'Funding_ID': '287', 'Project_Name': 'project_134', 'Funding_Source': 'Federal Assistance', 'Amount': '32000'}, {'Funding_ID': '373', 'Project_Name': 'project_412', 'Funding_Source': 'Federal Assistance', 'Amount': '62000'}, {'Funding_ID': '474', 'Project_Name': 'project_332', 'Funding_Source': 'Federal Assistance', 'Amount': '65000'}], 'var_functions.execute_python:10': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs', 'Corral Canyon Culvert Repairs (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Guardrail Replacement Citywide (FEMA Project)', 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Malibu Road Slope Repairs (CalOES Project)', 'Outdoor Warning Signs', 'Outdoor Warning Sirens', 'Outdoor Warning Sirens (FEMA Project)', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warning Sirens - Design (FEMA Project)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'PCH Overhead Warning Signs', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Westward Beach Road Repair Project', 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'project_227', 'project_396', 'project_425', 'project_134', 'project_412', 'project_332'], 'var_functions.execute_python:14': {'funding_records': 500, 'civic_docs': 5, 'emergency_project_count': 38}, 'var_functions.execute_python:16': ['2021 Annual Street Maintenance', '2022 Annual Street Maintenance', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Annual Street Maintenance', 'Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Bluffs Park Shade Structure', 'Bluffs Park Workout Station', 'Broad Beach Road Water Quality Infrastructure Repairs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
