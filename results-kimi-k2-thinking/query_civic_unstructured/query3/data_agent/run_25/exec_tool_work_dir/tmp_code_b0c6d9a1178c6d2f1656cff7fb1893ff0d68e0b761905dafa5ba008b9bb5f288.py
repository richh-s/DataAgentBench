code = """import json, re

# Load civic documents from file
civic_file = 'var_functions.query_db:32'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract emergency/FEMA projects
project_list = []
seen_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) > 200:
            continue
        
        # Look for project indicators
        has_fema = '(FEMA' in line or 'FEMA' in line
        has_emergency = 'Emergency' in line or 'emergency' in line
        is_project_line = (
            line.isupper() or
            'Project' in line or
            'Improvements' in line or
            'Repairs' in line or
            has_fema or
            has_emergency
        )
        
        if is_project_line and (has_fema or has_emergency or re.search(r'emergency|fema', text, re.IGNORECASE)):
            # Avoid duplicates
            if line in seen_projects:
                continue
            seen_projects.add(line)
            
            # Determine status from context
            status = 'Unknown'
            context_start = max(0, i-10)
            context_end = min(len(lines), i+20)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            if 'design' in context:
                status = 'design'
            elif 'construction' in context and 'completed' not in context:
                status = 'construction'
            elif 'complete' in context:
                status = 'completed'
            elif 'not started' in context:
                status = 'not started'
            
            # Get dates
            dates = re.findall(r'(\d{4}-(?:Spring|Summer|Fall|Winter|\d{1,2}))', context, re.IGNORECASE)
            st = dates[0] if dates else ''
            et = dates[-1] if len(dates) > 1 else ''
            
            # Determine topic
            if 'fema' in text.lower() and 'emergency' in text.lower():
                topic = 'emergency, FEMA'
            elif 'fema' in text.lower():
                topic = 'FEMA'
            else:
                topic = 'emergency'
            
            project_list.append({
                'Project_Name': line,
                'topic': topic,
                'type': 'disaster',
                'status': status,
                'st': st,
                'et': et
            })

# Load funding records
funding_file = 'var_functions.query_db:14'
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Map project names to civic data
civic_map = {p['Project_Name']: p for p in project_list}

# Merge with funding data
final_results = []
for funding in funding_records:
    proj_name = funding['Project_Name']
    civic_match = civic_map.get(proj_name)
    
    if civic_match:
        status = civic_match['status']
        topic = civic_match['topic']
    else:
        # Try fuzzy matching
        for civic_name, civic_data in civic_map.items():
            if (proj_name in civic_name) or (civic_name in proj_name):
                status = civic_data['status']
                topic = civic_data['topic']
                break
        else:
            status = 'Unknown'
            topic = 'FEMA' if 'FEMA' in proj_name else 'emergency'
    
    final_results.append({
        'Project_Name': proj_name,
        'Funding_Source': funding['Funding_Source'],
        'Amount': int(funding['Amount']),
        'Status': status,
        'Topic': topic
    })

# Sort by amount descending
final_results.sort(key=lambda x: x['Amount'], reverse=True)

# Format output
output = []
output.append("PROJECTS RELATED TO EMERGENCY OR FEMA")
output.append("=" * 80)
output.append("")

for result in final_results:
    output.append("Project: " + result['Project_Name'])
    output.append("Funding Source: " + result['Funding_Source'])
    output.append("Amount: " + str(result['Amount']))
    output.append("Status: " + result['Status'])
    output.append("Topic: " + result['Topic'])
    output.append("-" * 80)
    output.append("")

final_answer = "\n".join(output)
print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
