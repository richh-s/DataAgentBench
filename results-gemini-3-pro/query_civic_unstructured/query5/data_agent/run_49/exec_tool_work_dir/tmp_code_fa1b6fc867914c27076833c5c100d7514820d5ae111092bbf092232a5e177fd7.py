code = """import json

with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

lines = []
for d in civic_docs:
    lines.extend(d.get('text', '').splitlines())

projects = []
current_project = None
current_section = "Unknown"

for i in range(len(lines)):
    line = lines[i].strip()
    if not line: continue
    
    # Check Section
    if "Capital Improvement Projects" in line:
        current_section = "Capital"
    elif "Disaster Recovery Projects" in line:
        current_section = "Disaster"
        
    is_project = False
    if i + 1 < len(lines):
        next_line = lines[i+1].strip()
        if "(cid:190)" in next_line and ("Updates:" in next_line or "Project Description:" in next_line):
            if "Agenda" not in line and "Page" not in line:
                is_project = True
                
    if is_project:
        if current_project:
            projects.append(current_project)
        current_project = {"name": line, "body": "", "section": current_section}
    elif current_project:
        current_project["body"] += line + " "

if current_project:
    projects.append(current_project)

# Find Marie Canyon
target = None
for p in projects:
    if "Marie Canyon Green Streets" in p["name"]:
        target = p
        break

print("__RESULT__:")
if target:
    print(json.dumps({"name": target["name"], "section": target["section"], "body_snippet": target["body"][:1000]}))
else:
    print(json.dumps("Not Found"))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json', 'var_function-call-17193814516790891739': {'total': 0, 'projects': [], 'matched': []}, 'var_function-call-2668714204962722020': 'Done', 'var_function-call-11486011269853492389': [{'name': 'Trancas Canyon Park Playground', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:190) Updates: Construction was completed November 2022. Notice of completion']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:131) Construction was completed, November 2022']}, {'name': 'Point Dume Walkway Repairs', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:131) Construction was completed, November 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['anticipated to have a final design by March 2022. The project will be', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', 'project will have final approval by March 2022. The project will be', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '2022. This project requires Caltrans approval since the work will be on', 'approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'meeting was held on January 20, 2022. Project alternatives will be', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer/Winter 2022', 'of the assessment district to June 30, 2022.', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Begin Construction: Fall 2022', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', '(cid:131) Complete Design: Spring 2022', 'March 2022', '(cid:131) Begin Design: Spring 2022', 'scheduled to be accepted by the Council at the January 24, 2022 meeting.', 'at the January 24, 2022 meeting.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Completion Date: Spring 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Fall 2022', 'dates_2022': ['January 24, 2022 meeting.', 'anticipated that the final design will be complete by February 2022. The', 'beginning in April 2022.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) The project design will commence during the Spring 2022.', 'started and is anticipated to be completed by the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', 'anticipated that the final design will be complete by July 2022. The', 'beginning in Fall 2022.', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022']}, {'name': 'Citywide Guardrail Replacement', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Malibu Park Storm Drain Repairs', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['(cid:131) Begin Construction: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['(cid:131) Begin Construction: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Completion Date: Spring 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Fall 2022', 'dates_2022': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Summer 2022', 'management services was approved by Council on March 14, 2022.', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Summer 2022', '(cid:131) Award Contract and Begin Construction: Summer 2022', 'meeting was held on January 20, 2022 and February 23, 2022 and', '2022.', '(cid:131) Complete Design: Summer 2022', '(cid:131) Begin Construction: Fall/Winter 2022', 'of the assessment district to June 30, 2022. A new request for further', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Staff received bids on February 24, 2022. Award of contract is', 'scheduled for the April 11, 2022 Council meeting.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', '(cid:131) Complete Design: Spring 2022', 'go to Council in April 2022 after the Funding Agreement is issued by', '(cid:131) Begin Design: Late Spring 2022', 'by the Council at the January 24, 2022 meeting.', '24, 2022 meeting.', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Completion Date: Spring 2022', 'Proposals are due in April 14, 2022.', 'anticipated that the final design will be complete by March 2022. The', 'beginning in Spring 2022.', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', 'completed by Spring 2022.', 'of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', 'anticipated that the final design will be complete by July 2022. The', 'beginning in Fall 2022.', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022', '2022.']}, {'name': 'Citywide Guardrail Replacement', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Malibu Park Storm Drain Repairs', 'section': 'Capital', 'is_disaster': True, 'st': None, 'dates_2022': ['accepted by the Council on January 24, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'section': 'Capital', 'is_disaster': True, 'st': None, 'dates_2022': ['Improvement. The project was accepted by the Council on January 24, 2022']}], 'var_function-call-6807658236164967810': {'total_funding': 214000.0, 'matched_projects': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)'], 'debug_targets': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements (CalOES Project)', 'Marie Canyon Green Streets']}, 'var_function-call-3961940813441405265': {'total': 228000.0, 'matched': ['Marie Canyon Green Streets', 'Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)'], 'targets': [{'name': 'Marie Canyon Green Streets', 'reason': ['Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword CalOES', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'reason': ['Name Keyword', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword CalOES', 'Body Keyword CalOES', 'Body Keyword CalOES', 'Body Keyword FEMA', 'Body Keyword FEMA']}, {'name': 'Marie Canyon Green Streets', 'reason': ['Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword CalOES', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword CalOES', 'Body Keyword CalOES', 'Body Keyword CalOES', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA', 'Body Keyword FEMA']}]}}

exec(code, env_args)
