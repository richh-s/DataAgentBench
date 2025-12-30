code = """import json
import pandas as pd
from datetime import datetime
import re

# Load data
funding_path = locals()['var_function-call-400742028544773800']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)
df_funding = pd.DataFrame(funding_data)

docs_path = locals()['var_function-call-400742028544771257']
with open(docs_path, 'r') as f:
    docs_data = json.load(f)

# Sort docs by date
def extract_date(filename):
    match = re.search(r'(\d{8})', filename)
    if match:
        return datetime.strptime(match.group(1), "%m%d%Y")
    return datetime.min

docs_data.sort(key=lambda x: extract_date(x['filename']))

extracted_projects = {}

for doc in docs_data:
    text = doc['text']
    lines = text.split(chr(10))
    
    current_status = None
    current_project = None
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if 'Capital Improvement Projects' in line or 'Disaster Recovery Projects' in line:
            if '(Design)' in line:
                current_status = 'design'
            elif '(Construction)' in line:
                current_status = 'construction_section'
            elif '(Not Started)' in line:
                current_status = 'not started'
            i += 1
            continue
            
        if line and current_status:
            if 'Agenda Item' in line or ('Page' in line and 'of' in line):
                i += 1
                continue
            
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            
            is_project = False
            if j < len(lines):
                next_line = lines[j].strip()
                if '(cid:190)' in next_line or next_line.startswith('Updates:'):
                    is_project = True
            
            if is_project:
                # Normalization of Name
                p_name = line
                if p_name in extracted_projects:
                    # Update status, append text
                    extracted_projects[p_name]['status'] = current_status
                    extracted_projects[p_name]['text'] += " " + current_project_text if 'current_project_text' in locals() else "" # Logic fix below
                else:
                    extracted_projects[p_name] = {
                        'name': p_name,
                        'status': current_status,
                        'text': ''
                    }
                current_project = extracted_projects[p_name]
                i += 1
                continue

        if current_project:
            current_project['text'] += line + ' '
        
        i += 1

# Process Results
results = []
extracted_map = {k.lower(): v for k, v in extracted_projects.items()}
keywords = ['emergency', 'fema']

for idx, row in df_funding.iterrows():
    f_name = row['Project_Name']
    f_source = row['Funding_Source']
    f_amount = row['Amount']
    
    # Matching
    match = None
    
    # Exact
    match = extracted_map.get(f_name.lower())
    
    # Suffix
    if not match:
        base_name = f_name
        suffixes = ['(FEMA Project)', '(CalOES Project)', '(FEMA/CalOES Project)', '(FEMA)', '(CalJPIA Project)', '(CalJPIA/FEMA Project)']
        for s in suffixes:
            if base_name.endswith(s) or base_name.endswith(s.strip()):
                base_name = base_name.replace(s, '').strip()
        match = extracted_map.get(base_name.lower())
        
        # Fuzzy / Token Overlap
        if not match:
            # Check if base_name tokens are covered by a key
            base_tokens = base_name.lower().split()
            best_match = None
            for k, v in extracted_map.items():
                k_tokens = k.split()
                # Check coverage: all base tokens appear in k (as substrings)
                if all(any(bt in kt for kt in k_tokens) for bt in base_tokens):
                    best_match = v
                    break
                # Also check reverse: all k tokens in base (unlikely for short base)
            match = best_match

    # Status Determination
    status = 'Unknown'
    text_content = ''
    
    if match:
        raw_status = match['status']
        text_content = match['text']
        if raw_status == 'construction_section':
            lower_text = text_content.lower()
            if 'completed' in lower_text and ('construction' in lower_text or 'notice of completion' in lower_text):
                status = 'completed'
            elif 'notice of completion' in lower_text:
                status = 'completed'
            else:
                status = 'design' # Using design as active state per hints
        else:
            status = raw_status
            
    # Relevance
    is_relevant = False
    if any(k in f_name.lower() for k in keywords):
        is_relevant = True
    if text_content and any(k in text_content.lower() for k in keywords):
        is_relevant = True
    
    if is_relevant:
        results.append({
            "Project_Name": f_name,
            "Funding_Source": f_source,
            "Amount": f_amount,
            "Status": status
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11967641288845648595': ['Funding'], 'var_function-call-11967641288845651132': ['civic_docs'], 'var_function-call-400742028544773800': 'file_storage/function-call-400742028544773800.json', 'var_function-call-400742028544771257': 'file_storage/function-call-400742028544771257.json', 'var_function-call-12739522525466525577': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'design'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}], 'var_function-call-14094171746541198642': 'file_storage/function-call-14094171746541198642.json', 'var_function-call-5277286139680866153': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000', 'Status': 'Unknown'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}]}

exec(code, env_args)
