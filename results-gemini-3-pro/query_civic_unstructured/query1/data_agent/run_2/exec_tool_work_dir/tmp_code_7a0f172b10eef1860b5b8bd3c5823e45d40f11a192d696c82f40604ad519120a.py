code = """import json
import re

path_fund = locals()['var_function-call-9124692178282648902']
path_docs = locals()['var_function-call-10183875392572160973']

with open(path_fund, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
for record in funding_data:
    high_funding_projects.add(record['Project_Name'].strip().lower())

with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

extracted_projects = set()
section_start_regex = r"Capital Improvement Projects\s*\(Design\)"
section_end_regex = r"(?:Capital Improvement Projects|Disaster Recovery Projects|Agenda Item)"

for doc in civic_docs:
    text = doc['text']
    parts = re.split(section_start_regex, text, flags=re.IGNORECASE)
    
    for part in parts[1:]:
        end_match = re.search(section_end_regex, part, flags=re.IGNORECASE)
        if end_match:
            section_content = part[:end_match.start()]
        else:
            section_content = part
        
        lines = [line.strip() for line in section_content.splitlines() if line.strip()]
        
        for i in range(len(lines) - 1):
            line = lines[i]
            next_line = lines[i+1]
            
            # Heuristic: Project name line should likely start with Uppercase or Digit
            if not (line[0].isupper() or line[0].isdigit()):
                continue

            # Heuristic: Line shouldn't be too long (paragraph)
            if len(line) > 100:
                continue
            
            # Check next line for keywords
            if 'Updates:' in next_line or 'Project Schedule' in next_line or 'cid:190' in next_line:
                extracted_projects.add(line.lower())

# Matching
matches = []
funding_lookup = {re.sub(r'[^a-z0-9]', '', n): n for n in high_funding_projects}

for p in extracted_projects:
    p_norm = re.sub(r'[^a-z0-9]', '', p)
    
    if p in high_funding_projects:
        matches.append(p)
    elif p_norm in funding_lookup:
        matches.append(funding_lookup[p_norm])
    else:
         # Fuzzy check
        found = False
        for f_norm in funding_lookup:
            if f_norm in p_norm and len(f_norm) > 10:
                matches.append(funding_lookup[f_norm])
                found = True
                break
            elif p_norm in f_norm and len(p_norm) > 10:
                matches.append(funding_lookup[f_norm])
                found = True
                break

unique_matches = sorted(list(set(matches)))

print("__RESULT__:")
print(json.dumps({
    "count": len(unique_matches), 
    "matches": unique_matches, 
    "extracted_all": list(extracted_projects)
}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json', 'var_function-call-5838596585415121062': {'count': 0, 'matches': [], 'extracted_example': ['marie canyon green streets']}, 'var_function-call-16884651973826242969': {'extracted_sample': ['marie canyon green streets', 'marie canyon green streets', 'marie canyon green streets', 'marie canyon green streets'], 'funding_sample': ['project_232', 'project_138', 'project_118', 'project_484', 'project_46', 'project_196', 'project_149', 'project_221', 'project_170', 'project_230'], 'debug_sections': [{'content_start': '\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the Cou', 'ended_by': 'Agenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Be'}, {'content_start': '\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufac', 'ended_by': 'Agenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nadvertised for'}, {'content_start': '\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) The City has recently received Measure W funds to complete this\nproject. Staff is working on the project plans to prepare for public\nbidding.', 'ended_by': 'Agenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPCH Signal Sync'}]}, 'var_function-call-1150047470152958143': {'count': 1, 'matches': ['pch median improvements project'], 'extracted_sample': ['management.', '2022 morning view resurfacing & storm drain improvements', 'marie canyon green streets', 'or phasing out the project', 'bidding.', 'project and will submit to the county for review.', 'advertised for construction bids shortly after this date.', 'pch median improvements project', 'construction bids.']}, 'var_function-call-6262475700830654450': [{'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '61', 'Project_Name': 'Marie Canyon Green Streets', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '50000'}, {'Funding_ID': '71', 'Project_Name': 'PCH Median Improvements Project', 'Funding_Source': 'Development Bank Loan', 'Amount': '56000'}, {'Funding_ID': '72', 'Project_Name': 'PCH Median Improvements at Paradise Cove and Zuma Beach', 'Funding_Source': 'State Development Grant', 'Amount': '27000'}, {'Funding_ID': '96', 'Project_Name': 'Westward Beach Road Drainage Improvements Project', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '97', 'Project_Name': 'Westward Beach Road Improvements Project', 'Funding_Source': 'University Research Fund', 'Amount': '29000'}, {'Funding_ID': '98', 'Project_Name': 'Westward Beach Road Repair Project', 'Funding_Source': 'Federal Assistance', 'Amount': '30000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}]}

exec(code, env_args)
