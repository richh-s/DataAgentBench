code = """import json
import re

# Load funding data
with open(locals()['var_function-call-8365727956601891924'], 'r') as f:
    funding_records = json.load(f)

high_funding_projects = set()
for rec in funding_records:
    try:
        amt = int(rec['Amount'])
        if amt > 50000:
            high_funding_projects.add(rec['Project_Name'].strip())
    except:
        pass

# Load civic docs
with open(locals()['var_function-call-8365727956601890549'], 'r') as f:
    civic_docs = json.load(f)

extracted_design_projects = set()

start_header = "Capital Improvement Projects (Design)"
end_headers = [
    "Capital Improvement Projects (Construction)", 
    "Capital Improvement Projects (Not Started)", 
    "Disaster Recovery Projects"
]

# Regex for footers: Page X of Y, Agenda Item #...
# We use \\d because this string is inside a JSON payload
footer_re = re.compile(r"Page \d+ of \d+|Agenda Item #.*", re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    
    start_idx = text.find(start_header)
    if start_idx == -1:
        continue
    
    end_idx = len(text)
    for eh in end_headers:
        idx = text.find(eh, start_idx)
        if idx != -1 and idx < end_idx:
            end_idx = idx
            
    section_text = text[start_idx + len(start_header):end_idx]
    
    parts = section_text.split("(cid:190) Updates:")
    
    for i in range(len(parts) - 1):
        chunk = parts[i]
        lines = chunk.split('\n')
        # Filter lines
        clean_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if footer_re.search(line):
                continue
            clean_lines.append(line)
        
        if clean_lines:
            project_name = clean_lines[-1]
            extracted_design_projects.add(project_name)

matching_projects = extracted_design_projects.intersection(high_funding_projects)

print("__RESULT__:")
print(json.dumps({
    "extracted_design_projects": list(extracted_design_projects),
    "high_funding_projects_count": len(high_funding_projects),
    "matching_projects": list(matching_projects),
    "count": len(matching_projects)
}))"""

env_args = {'var_function-call-8365727956601891924': 'file_storage/function-call-8365727956601891924.json', 'var_function-call-8365727956601890549': 'file_storage/function-call-8365727956601890549.json', 'var_function-call-12646988407192400613': 'Capital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n(cid:131) Begin Construction: Fall 2023\n\nPCH Median Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) On September 22, 2022, the City received four (4) construction bids\n\nand rejected all bids due to a budget shortfall\n\n(cid:131) City will work with the design consultant to review design alternatives\n\nor phasing out the project\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Fall 2023\n\nPage 1 of 6\n\nAgenda Item # 4.B.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Repair Project\n\n(cid:190) Updates:\n\n(cid:131) City working with consultant on the design of the shoulder repairs\n\n(cid:190) Project Schedule:\n\n(cid:131) Complete Design: Summer 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nWestward Beach Road Drainage Improvements Project\n\n(cid:190) Updates:\n\n(cid:131) Plans are under review by Fish and Wildlife and City is expecting\ncomments mid-April. This project required their review since the project\nscope falls within Zuma Canyon Creek. Army Corp. of Engineers has\ncleared the project.\n\n(cid:190) Project Schedule:\n\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nClover Heights Storm Drainage Improvements\n\n(cid:190) Updates:\n\n(cid:131) City submitted plans to CalOES for review and working with consultant\n\nto finalize plans and specifications\n\n(cid:190) Project Schedule:\n\n(cid:131) Final Design: Summer, 2023\n(cid:131) Advertise: Summer 2023\n(cid:131) Begin Construction: Fall 2023\n\nLatigo Canyon Road Retaining Wall Repair Project\n\n(cid:190) Updates:\n\n(cid:131) Plans and specifications have be'}

exec(code, env_args)
