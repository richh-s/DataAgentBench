code = """import json
import re

with open(locals()['var_function-call-6964896026869671245'], 'r') as f:
    civic_docs = json.load(f)

with open(locals()['var_function-call-867828661549977430'], 'r') as f:
    funding_data = json.load(f)

full_text = chr(10).join([doc['text'] for doc in civic_docs])
full_text_lower = full_text.lower()

def clean_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    return name.strip()

funding_by_clean_name = {}
for entry in funding_data:
    raw_name = entry['Project_Name']
    amt = int(entry['Amount'])
    c_name = clean_name(raw_name)
    if c_name not in funding_by_clean_name:
        funding_by_clean_name[c_name] = {'amounts': [], 'raw_names': []}
    funding_by_clean_name[c_name]['amounts'].append(amt)
    funding_by_clean_name[c_name]['raw_names'].append(raw_name)

total_funding = 0
matched_projects = []

for c_name, data in funding_by_clean_name.items():
    if len(c_name) < 5: continue
    if "project_" in c_name.lower(): continue

    # Find the project section in text
    start_search = 0
    while True:
        idx = full_text.find(c_name, start_search)
        if idx == -1:
            break
        
        # Extract a focused context
        # We assume the project description follows the name.
        # We'll take up to 800 chars, but stop if we see what looks like another project header.
        # This is hard to robustly detect, but we can look for "Page" or large gaps.
        raw_context = full_text[idx:idx+800]
        context_lower = raw_context.lower()
        
        # Check Park
        is_park = False
        if 'park' in c_name.lower() and 'parking' not in c_name.lower():
            is_park = True
        elif re.search(r'\bpark\b', context_lower):
            # Verify "park" isn't part of "Parking" or "Spark" etc.
            # \b handles word boundaries.
            is_park = True
            
        # Check Completion
        is_completed_2022 = False
        if is_park:
             # Strict check for construction completion
             # Patterns: "Construction was completed... 2022", "Construction completed... 2022"
             if re.search(r'construction\s+(was\s+)?completed.*2022', context_lower):
                 is_completed_2022 = True
             elif re.search(r'project\s+(was\s+)?completed.*2022', context_lower):
                 is_completed_2022 = True
             # Check for negative "Design completed"
             if "complete design" in context_lower and not is_completed_2022:
                 # If only "complete design" is present, it's not construction completion
                 pass
        
        if is_park and is_completed_2022:
            total = sum(data['amounts'])
            total_funding += total
            matched_projects.append({
                "name": c_name,
                "amount": total,
                "reason": "Found park and construction completed 2022"
            })
            break # Move to next project
        
        start_search = idx + 1

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "projects": matched_projects}))"""

env_args = {'var_function-call-6964896026869671245': 'file_storage/function-call-6964896026869671245.json', 'var_function-call-16721484954554461294': ['Funding'], 'var_function-call-867828661549977430': 'file_storage/function-call-867828661549977430.json', 'var_function-call-7895803557599904901': {'total_funding': 118000, 'projects': [{'name': 'Bluffs Park Shade Structure', 'amount': 21000}, {'name': 'Permanent Skate Park', 'amount': 97000}]}, 'var_function-call-15919782058148255785': {'Permanent Skate Park': 'Permanent Skate Park\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Spring 2023\n(cid:131) Begin Construction: Winter 2024\n\nPCH at Trancas Canyon Road Right Turn Lane\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to Caltrans for review and expecting comments in\n\nthe Spring 2023.\n\n(cid:190) Estimated Schedule:\n\n(cid:131) Complete Design: Fall 2023\n(cid:131) Begin Cons', 'Bluffs Park Shade Structure': 'Bluffs Park Shade Structure\n\n(cid:190) Updates: Construction was completed November 2022. Notice of completion\n\nfiled January 2023\n\nPage 4 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\nMarie Canyon Green Streets\n(cid:190) Updates:\n\n(cid:131) Construction was completed, January 2023\n(cid:131) Scheduled for Council acceptance on April 24, 2023\n\nBroad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoi', 'Point Dume Walkway Repairs': 'Point Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study\nand includes installing new raised medians and improvements. New raised\nmedians are proposed east and west of PCH and Paradise Cove Road. The\nproposed improvemen', 'Broad Beach Road Water Quality Repair': 'Broad Beach Road Water Quality Repair\n\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nPoint Dume Walkway Repairs\n(cid:190) Updates:\n\n(cid:131) Construction was completed, November 2022\n(cid:131) Notice of completion filed January 2023\n\nCapital Improvement Projects (Not Started)\n\nPCH Median Improvements at Paradise Cove and Zuma Beach\n\n(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study'}}

exec(code, env_args)
