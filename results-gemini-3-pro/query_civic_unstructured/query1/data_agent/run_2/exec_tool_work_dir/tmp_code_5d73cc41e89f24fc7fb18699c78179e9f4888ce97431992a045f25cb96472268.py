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
        
        # Get non-empty lines
        lines = [line.strip() for line in section_content.splitlines() if line.strip()]
        
        for i in range(len(lines) - 1):
            line = lines[i]
            next_line = lines[i+1]
            
            # Check next line for keywords
            if 'Updates:' in next_line or 'Project Schedule' in next_line or 'cid:190' in next_line:
                # Clean the line (remove leading bullets if any, though likely project name is clean)
                # Sometimes project name has a bullet too? No, usually headers don't.
                extracted_projects.add(line.lower())

# Check intersection
count = 0
matches = []
# Also check for names that are in funding but slightly different
# e.g. ignoring case and punctuation
funding_lookup = {re.sub(r'[^a-z0-9]', '', n): n for n in high_funding_projects}

for p in extracted_projects:
    p_norm = re.sub(r'[^a-z0-9]', '', p)
    
    # Direct lookup
    if p in high_funding_projects:
        count += 1
        matches.append(p)
    elif p_norm in funding_lookup:
        # Match found with normalization
        count += 1
        matches.append(funding_lookup[p_norm]) # Store the funding db version
    else:
        # Check if one contains the other?
        # e.g. "Westward Beach Road Repair Project" vs "Westward Beach Road Repair"
        found = False
        for f_norm in funding_lookup:
            if f_norm in p_norm and len(f_norm) > 10: # avoid short matches
                count += 1
                matches.append(funding_lookup[f_norm])
                found = True
                break
            elif p_norm in f_norm and len(p_norm) > 10:
                count += 1
                matches.append(funding_lookup[f_norm])
                found = True
                break
        
        if not found:
            pass

# Deduplicate matches
unique_matches = sorted(list(set(matches)))

print("__RESULT__:")
print(json.dumps({
    "count": len(unique_matches), 
    "matches": unique_matches, 
    "extracted_sample": list(extracted_projects)[:10]
}))"""

env_args = {'var_function-call-6378966293970192781': ['Funding'], 'var_function-call-6378966293970194138': ['civic_docs'], 'var_function-call-9124692178282648902': 'file_storage/function-call-9124692178282648902.json', 'var_function-call-10183875392572160973': 'file_storage/function-call-10183875392572160973.json', 'var_function-call-5838596585415121062': {'count': 0, 'matches': [], 'extracted_example': ['marie canyon green streets']}, 'var_function-call-16884651973826242969': {'extracted_sample': ['marie canyon green streets', 'marie canyon green streets', 'marie canyon green streets', 'marie canyon green streets'], 'funding_sample': ['project_232', 'project_138', 'project_118', 'project_484', 'project_46', 'project_196', 'project_149', 'project_221', 'project_170', 'project_230'], 'debug_sections': [{'content_start': '\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the Cou', 'ended_by': 'Agenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Be'}, {'content_start': '\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) A hydrology report was prepared and will be used to size the pre-\nmanufactured biofilters. City staff is reviewing multiple biofilter\nmanufac', 'ended_by': 'Agenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nadvertised for'}, {'content_start': '\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) The City has recently received Measure W funds to complete this\nproject. Staff is working on the project plans to prepare for public\nbidding.', 'ended_by': 'Agenda Item # 4.A.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPCH Signal Sync'}]}}

exec(code, env_args)
