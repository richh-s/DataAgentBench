code = """import json

# Re-run the extraction logic to get the sets
funding_file = locals()['var_function-call-4872762091954436572']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

high_funding_projects = set()
all_funding_projects = set()
for item in funding_data:
    all_funding_projects.add(item['Project_Name'].strip())
    try:
        if float(item['Amount']) > 50000:
            high_funding_projects.add(item['Project_Name'].strip())
    except:
        pass

docs_file = locals()['var_function-call-4872762091954434845']
with open(docs_file, 'r') as f:
    civic_docs = json.load(f)

capital_design_projects = set()
target_header = "Capital Improvement Projects (Design)"
next_headers = [
    "Capital Improvement Projects (Construction)",
    "Capital Improvement Projects (Not Started)",
    "Disaster Recovery Projects"
]

for doc in civic_docs:
    text = doc.get('text', '')
    start_idx = text.find(target_header)
    if start_idx == -1:
        continue
    start_idx += len(target_header)
    
    end_idx = len(text)
    for nh in next_headers:
        idx = text.find(nh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx:end_idx]
    lines = [l.strip() for l in section_text.split(chr(10)) if l.strip()]
    
    for i in range(len(lines) - 1):
        line = lines[i]
        next_line = lines[i+1]
        
        is_start_of_block = False
        if "(cid:190)" in next_line:
            is_start_of_block = True
        elif "Updates:" in next_line or "Project Description:" in next_line or "Project Schedule:" in next_line or "Estimated Schedule:" in next_line:
            is_start_of_block = True
            
        if is_start_of_block:
            if "Page" in line and "of" in line:
                continue
            if "Agenda Item" in line:
                continue
            
            capital_design_projects.add(line)

result = capital_design_projects.intersection(high_funding_projects)
missed = capital_design_projects - high_funding_projects

# Check if missed projects exist in all_funding_projects (meaning they were filtered out by amount)
# or if they are not in funding table at all (meaning name mismatch or not funded)
missed_but_in_db = missed.intersection(all_funding_projects)
missed_not_in_db = missed - all_funding_projects

print("__RESULT__:")
print(json.dumps({
    "matched_count": len(result),
    "matched_projects": list(result),
    "missed_but_in_db (low funding)": list(missed_but_in_db),
    "missed_not_in_db (name mismatch or no funding record)": list(missed_not_in_db)
}))"""

env_args = {'var_function-call-4872762091954436572': 'file_storage/function-call-4872762091954436572.json', 'var_function-call-4872762091954434845': 'file_storage/function-call-4872762091954434845.json', 'var_function-call-14207660122880327924': {'count': 0, 'projects': []}, 'var_function-call-14847519188014513356': {'count': 10, 'projects': ['PCH at Trancas Canyon Road Right Turn Lane', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Civic Center Stormwater Diversion Structure', 'Malibu Canyon Road Traffic Study', 'Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Permanent Skate Park'], 'extracted_sample': ['March 2022', '(cid:131) Staff is currently working on the final design plans', 'PCH at Trancas Canyon Road Right Turn Lane', '(cid:131) Funding agreement is schedule for city council on March 27, 2023', 'Storm Drain Master Plan', '(cid:131) City to request proposal from consultant for design services', 'Latigo Canyon Road Retaining Wall Repair Project', 'the County and will be finalizing the design.', 'Trancas Canyon Park Playground', 'Metro.'], 'funding_sample': ['project_166', 'project_41', 'PCH at Trancas Canyon Road Right Turn Lane', 'Recommended Action', 'Storm Drain Master Plan', 'project_2', 'project_35', 'Harbor Vista Curb Return', 'project_216', 'Latigo Canyon Road Retaining Wall Repair Project'], 'debug_lines': ['2022 Morning View Resurfacing & Storm Drain Improvements', '(cid:190) Updates:', '(cid:131) Staff is working with the consultant to finalize the design plans for this', 'project and will submit to the County for review.', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', '(cid:131) Begin Construction: Fall 2023', 'PCH Median Improvements Project', '(cid:190) Updates:', '(cid:131) On September 22, 2022, the City received four (4) construction bids', 'and rejected all bids due to a budget shortfall', '(cid:131) City will work with the design consultant to review design alternatives', 'or phasing out the project', '(cid:190) Project Schedule:', '(cid:131) Complete Design: Summer 2023', '(cid:131) Advertise: Fall 2023', 'Page 1 of 6', 'Agenda Item # 4.B.', '(cid:131) Begin Construction: Fall 2023']}}

exec(code, env_args)
