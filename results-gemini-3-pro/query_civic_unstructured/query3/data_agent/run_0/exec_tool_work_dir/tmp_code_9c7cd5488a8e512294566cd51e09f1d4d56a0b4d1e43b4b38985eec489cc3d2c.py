code = """import json
import re

with open(locals()['var_function-call-4694039731328856667'], 'r') as f:
    funding_data = json.load(f)

with open(locals()['var_function-call-11052254391267769107'], 'r') as f:
    civic_docs = json.load(f)

funding_map = {item['Project_Name']: item for item in funding_data}
funding_names = set(funding_map.keys())

# Store all findings: name -> list of {status, text}
project_findings = {}

section_regex = re.compile(r'(Capital Improvement Projects|Disaster Recovery Projects)[ ]*\\((Design|Construction|Not Started)\\)', re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    lines = text.splitlines()
    
    current_status_section = 'unknown'
    current_project_name = None
    current_project_text = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
            
        sec_match = section_regex.search(stripped)
        if sec_match:
            if current_project_name:
                if current_project_name not in project_findings:
                    project_findings[current_project_name] = []
                project_findings[current_project_name].append({
                    'section_status': current_status_section,
                    'text': " ".join(current_project_text)
                })
                current_project_name = None
                current_project_text = []
            
            header_type = sec_match.group(2).lower()
            if 'design' in header_type:
                current_status_section = 'design'
            elif 'not started' in header_type:
                current_status_section = 'not started'
            elif 'construction' in header_type:
                current_status_section = 'construction'
            else:
                current_status_section = 'unknown'
            continue
        
        if stripped in funding_names:
            if current_project_name:
                if current_project_name not in project_findings:
                    project_findings[current_project_name] = []
                project_findings[current_project_name].append({
                    'section_status': current_status_section,
                    'text': " ".join(current_project_text)
                })
            current_project_name = stripped
            current_project_text = []
        else:
            if current_project_name:
                current_project_text.append(stripped)

    if current_project_name:
        if current_project_name not in project_findings:
            project_findings[current_project_name] = []
        project_findings[current_project_name].append({
            'section_status': current_status_section,
            'text': " ".join(current_project_text)
        })

final_results = []

for p_name, findings in project_findings.items():
    # Determine Status and Relevance
    # Status priority: Completed > Design (Construction) > Not Started > Unknown
    
    final_status = 'not started'
    is_related = False
    
    # Check name for relevance
    if 'fema' in p_name.lower() or 'emergency' in p_name.lower() or 'caloes' in p_name.lower():
        is_related = True
        
    found_statuses = set()
    
    for f in findings:
        txt = f['text'].lower()
        sec = f['section_status']
        
        # Check text for relevance
        if 'fema' in txt or 'emergency' in txt or 'caloes' in txt:
            is_related = True
            
        # Refine status
        stat = sec
        if 'completed' in txt and ('construction was completed' in txt or 'notice of completion' in txt):
            stat = 'completed'
        elif stat == 'construction':
            stat = 'design' # Map to active
            
        found_statuses.add(stat)
        
    if 'completed' in found_statuses:
        final_status = 'completed'
    elif 'design' in found_statuses: # includes construction mapped to design
        final_status = 'design'
    elif 'not started' in found_statuses:
        final_status = 'not started'
    else:
        final_status = 'unknown'
        
    if is_related and final_status != 'unknown':
        f_info = funding_map.get(p_name, {})
        final_results.append({
            "Project_Name": p_name,
            "Funding_Source": f_info.get("Funding_Source"),
            "Amount": f_info.get("Amount"),
            "Status": final_status
        })

print("__RESULT__:")
print(json.dumps(final_results))"""

env_args = {'var_function-call-4694039731328856667': 'file_storage/function-call-4694039731328856667.json', 'var_function-call-11052254391267769107': 'file_storage/function-call-11052254391267769107.json', 'var_function-call-5645558577841199670': [{'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000', 'Status': 'design'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000', 'Status': 'not started'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000', 'Status': 'not started'}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000', 'Status': 'not started'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000', 'Status': 'not started'}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000', 'Status': 'not started'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000', 'Status': 'not started'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000', 'Status': 'not started'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000', 'Status': 'not started'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000', 'Status': 'not started'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000', 'Status': 'not started'}]}

exec(code, env_args)
