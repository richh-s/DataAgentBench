code = """import json

# Load the filtered funding data (already contains FEMA/emergency projects)
funding_path = locals()['var_functions.query_db:18']
with open(funding_path, 'r') as f:
    funding_projects = json.load(f)

# Load the filtered civic documents (contain emergency/FEMA keywords)
docs_path = locals()['var_functions.query_db:16']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

# Create funding lookup dictionary
funding_dict = {}
for item in funding_projects:
    pname = item.get('Project_Name', '')
    funding_dict[pname] = {
        'Funding_Source': item.get('Funding_Source', 'Not specified'),
        'Amount': item.get('Amount', 0)
    }

# Function to extract status from document text
def extract_status(text, project_name):
    text_lower = text.lower()
    
    # Check for construction status
    if 'currently under construction' in text_lower and project_name.lower() in text_lower:
        return 'in progress'
    
    if 'complete construction' in text_lower and project_name.lower() in text_lower:
        return 'completed'
    
    if 'not started' in text_lower and project_name.lower() in text_lower:
        return 'not started'
    
    if 'design' in text_lower and project_name.lower() in text_lower:
        return 'design'
    
    return 'Unknown'

# Projects found in funding data
result_projects = []

for fund in funding_projects:
    pname = fund.get('Project_Name', '')
    status = 'Unknown'
    
    # Try to find status from documents
    for doc in civic_docs:
        if pname in doc['text']:
            status = extract_status(doc['text'], pname)
            if status != 'Unknown':
                break
    
    result_projects.append({
        'Project_Name': pname,
        'Funding_Source': fund.get('Funding_Source', 'Not specified'),
        'Amount': fund.get('Amount', 0),
        'Status': status
    })

# Also check documents for projects not in funding data but with emergency/FEMA context
for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 5:
            continue
        
        # Skip headers
        skip_words = ['Public Works', 'Commission', 'Meeting', 'Agenda', 'Page', 'Item']
        if any(word in line for word in skip_words):
            continue
        
        # Check if line is a project name (followed by Updates or Project Schedule)
        if i + 1 < len(lines):
            next_text = ' '.join(lines[i+1:i+3])
            if 'Updates:' in next_text or 'Project Schedule:' in next_text:
                combined = (line + ' ' + text).lower()
                if 'emergency' in combined or 'fema' in combined or 'siren' in combined or 'warning' in combined:
                    funding_info = funding_dict.get(line, {'Funding_Source': 'Not specified', 'Amount': 0})
                    
                    # Only add if not already in results
                    exists = any(p['Project_Name'] == line for p in result_projects)
                    if not exists:
                        status = extract_status(text, line)
                        result_projects.append({
                            'Project_Name': line,
                            'Funding_Source': funding_info['Funding_Source'],
                            'Amount': funding_info['Amount'],
                            'Status': status
                        })

# Format the final result
print('__RESULT__:')
print(json.dumps(result_projects, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '73', 'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
