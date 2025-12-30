code = """import json
import pandas as pd
import re
import datetime

with open(locals()['var_function-call-17289363314070391295'], 'r') as f:
    funding_data = json.load(f)
funding_df = pd.DataFrame(funding_data)

with open(locals()['var_function-call-14887521830663367550'], 'r') as f:
    civic_docs = json.load(f)

def extract_date(filename):
    match = re.search(r'(\d{2})(\d{2})(\d{4})', filename)
    if match:
        return datetime.datetime(int(match.group(3)), int(match.group(1)), int(match.group(2)))
    return datetime.datetime.min

civic_docs.sort(key=lambda x: extract_date(x['filename']), reverse=True)

header_pattern = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)\s*\((Design|Construction|Not Started|Completed)\)', re.IGNORECASE)

relevant_projects = []

def get_status_from_docs(search_name, docs):
    # Returns (status, is_relevant_in_text)
    # Default status 'not started'
    status = 'not started'
    found = False
    is_relevant = False
    
    norm_search = ' '.join(search_name.split())
    
    for doc in docs:
        text = doc['text']
        if norm_search.lower() in ' '.join(text.split()).lower():
            lines = text.splitlines()
            current_section_status = None
            for line in lines:
                h_match = header_pattern.search(line)
                if h_match:
                    s_str = h_match.group(2).lower()
                    if 'design' in s_str: current_section_status = 'design'
                    elif 'construction' in s_str: current_section_status = 'construction'
                    elif 'not started' in s_str: current_section_status = 'not started'
                
                if norm_search.lower() in ' '.join(line.split()).lower():
                    if current_section_status: status = current_section_status
                    found = True
                    
                    # check context
                    start_idx = text.lower().find(search_name.lower())
                    if start_idx == -1: start_idx = text.lower().find(norm_search.lower())
                    
                    if start_idx != -1:
                        context = text[start_idx:start_idx+800]
                        if 'fema' in context.lower() or 'emergency' in context.lower():
                            is_relevant = True
                        if 'construction was completed' in context.lower() or 'project was completed' in context.lower() or 'notice of completion' in context.lower():
                            status = 'completed'
                    break
            if found: break
            
    return status, is_relevant, found

for index, row in funding_df.iterrows():
    project_name = row['Project_Name']
    funding_source = row['Funding_Source']
    amount = row['Amount']
    
    # Check relevance by name
    name_relevant = False
    if 'FEMA' in project_name.upper() or 'EMERGENCY' in project_name.upper():
        name_relevant = True
        
    status, is_relevant_text, found = get_status_from_docs(project_name, civic_docs)
    
    if not found and '(' in project_name:
        # Try finding base name
        # Remove (...) at the end
        base_name = re.sub(r'\s*\(.*?\)$', '', project_name)
        if base_name != project_name:
            status_base, is_relevant_base, found_base = get_status_from_docs(base_name, civic_docs)
            if found_base:
                status = status_base
                # If name was already relevant (has FEMA), we keep it relevant.
                # If name wasn't relevant, we check if base name context is relevant.
                if is_relevant_base:
                    is_relevant_text = True
    
    if name_relevant or is_relevant_text:
        relevant_projects.append({'Project_Name': project_name, 'Funding_Source': funding_source, 'Amount': amount, 'Status': status})

print('__RESULT__:')
print(json.dumps(relevant_projects))"""

env_args = {'var_function-call-14887521830663364851': ['civic_docs'], 'var_function-call-14887521830663367550': 'file_storage/function-call-14887521830663367550.json', 'var_function-call-17289363314070391640': ['Funding'], 'var_function-call-17289363314070391295': 'file_storage/function-call-17289363314070391295.json', 'var_function-call-17873287086282119790': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000', 'Status': 'design'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000', 'Status': 'design'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)
