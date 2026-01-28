code = """import json
import re

# Load funding data from storage
funding_records = locals()['var_functions.query_db:36']

# Create set of disaster project names for matching
disaster_project_names = set()
for record in funding_records:
    disaster_project_names.add(record['Project_Name'])

# The civic docs file path
import os
civic_docs_path = '/tmp/tmp9q1f0j8y.json'

if not os.path.exists(civic_docs_path):
    print('__RESULT__:')
    print(json.dumps({'error': 'Civic docs file not found', 'path': civic_docs_path}))
else:
    # Load civic docs
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
    
    # Extract projects started in 2022
    projects_2022 = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
                
            # Skip headers and formatting
            if any(line.startswith(x) for x in [
                'Public Works', 'Commission', 'Agenda', 'To:', 'Prepared by',
                'Approved by', 'Date', 'Meeting', 'Subject:', 'RECOMMENDED',
                'DISCUSSION:', 'Capital Improvement', 'Page', '(cid:'
            ]):
                continue
            
            if line.startswith('(') or line.startswith('•'):
                continue
                
            # Check if this line is a project name (has updates or schedule after it)
            has_updates = False
            has_schedule = False
            for j in range(i+1, min(i+6, len(lines))):
                next_line = lines[j].strip()
                if 'Updates:' in next_line:
                    has_updates = True
                if 'Schedule:' in next_line or 'Project Schedule:' in next_line:
                    has_schedule = True
            
            if has_updates or has_schedule:
                # Look for 2022 start date in following lines
                start_date = None
                for j in range(i+1, min(i+20, len(lines))):
                    schedule_line = lines[j].strip()
                    # Look for construction/advertise dates
                    if 'Begin Construction:' in schedule_line or 'Advertise:' in schedule_line:
                        date_match = re.search(r'(\d{4}|Spring \d{4}|Summer \d{4}|Fall \d{4}|Winter \d{4}|\d{4}-\w+)', schedule_line)
                        if date_match:
                            start_date = date_match.group(1)
                            break
                
                if start_date and '2022' in str(start_date):
                    projects_2022.append({
                        'name': line,
                        'start_date': start_date
                    })
    
    # Remove duplicates
    unique_projects_2022 = {}
    for proj in projects_2022:
        unique_projects_2022[proj['name']] = proj['start_date']
    
    # Match with disaster projects and funding
    total_funding_2022 = 0
    matched_projects = []
    
    for project_name, start_date in unique_projects_2022.items():
        # Find matching disaster project in funding records
        for funding_record in funding_records:
            funding_name = funding_record['Project_Name']
            
            # Check if this is the same project (handle variations)
            # Remove suffixes for comparison
            base_name = re.sub(r'\s*\([^)]*\)\s*$', '', project_name).strip()
            funding_base = re.sub(r'\s*\([^)]*\)\s*$', '', funding_name).strip()
            
            if (base_name.lower() == funding_base.lower() or
                base_name.lower() in funding_name.lower() or
                funding_base.lower() in project_name.lower()):
                
                amount = int(funding_record['Amount'])
                total_funding_2022 += amount
                matched_projects.append({
                    'project': project_name,
                    'funding_project': funding_name,
                    'start_date': start_date,
                    'amount': amount
                })
                break
    
    output = {
        'total_funding_for_2022_disaster_projects': total_funding_2022,
        'matched_projects': matched_projects,
        'projects_started_in_2022_count': len(unique_projects_2022)
    }
    
    print('__RESULT__:')
    print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:28': [{'total_funding': '1410000'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:36': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': '85000'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': '14000'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': '81000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Amount': '18000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Amount': '78000'}, {'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Amount': '37000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Amount': '77000'}]}

exec(code, env_args)
