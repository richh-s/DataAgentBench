code = """import json
import re

with open(locals()['var_function-call-6799515908634330403'], 'r') as f:
    civic_docs = json.load(f)

full_text = "\n".join([d.get('text', '') for d in civic_docs])

# Find all project starts
# Pattern: Line, newline, (cid:190) Updates/Project Description
# We'll use finditer
# Note: (cid:190) might be represented as unicode char or literally.
# In the previous output, it appeared as "(cid:190)".
# We'll regex for `\n(.*?)\n\s*\(cid:190\) (?:Updates|Project Description):`

pattern = re.compile(r'\n(.*?)\n\s*\(cid:190\) (?:Updates|Project Description):', re.MULTILINE)

matches = list(pattern.finditer(full_text))

projects = []
for i, m in enumerate(matches):
    name = m.group(1).strip()
    start_idx = m.end()
    end_idx = matches[i+1].start() if i+1 < len(matches) else len(full_text)
    body = full_text[start_idx:end_idx]
    
    # Determine section by looking backwards from the project name
    # This is a bit expensive, but we can do it efficiently.
    # Actually, we can just scan the text before this match to find the last Section Header.
    # Let's assume section headers are "Capital Improvement Projects" or "Disaster Recovery Projects"
    
    preceding_text = full_text[:m.start()]
    # Find last occurrence of section headers
    cap_idx = preceding_text.rfind("Capital Improvement Projects")
    dis_idx = preceding_text.rfind("Disaster Recovery Projects")
    
    section = "Unknown"
    if dis_idx > cap_idx:
        section = "Disaster"
    elif cap_idx > dis_idx:
        section = "Capital"
        
    projects.append({
        "name": name,
        "section": section,
        "body": body
    })

# Analyze Projects
target_projects = []

for p in projects:
    is_disaster = False
    st_2022 = False
    
    # Check Section
    if p["section"] == "Disaster":
        is_disaster = True
    
    # Check Name/Body for keywords
    if "FEMA" in p["name"] or "CalOES" in p["name"] or "Disaster" in p["name"]:
        is_disaster = True
    if "FEMA" in p["body"] or "CalOES" in p["body"]:
        is_disaster = True
        
    # Check Start Date
    # Look for "Begin Construction: ... 2022" or "Start: ... 2022" in body
    # Regex for dates in body
    # (cid:131) Begin Construction: <date>
    date_pattern = re.compile(r'Begin Construction:(.*?)\n')
    date_matches = date_pattern.findall(p["body"])
    
    for d_str in date_matches:
        if "2022" in d_str:
            st_2022 = True
            break
            
    # Also check "Advertise: ... 2022" if Begin Construction is not found?
    # "started in 2022" -> usually Begin Construction.
    # What if "Begin Construction: Spring 2022"? Yes.
    
    if is_disaster and st_2022:
        target_projects.append(p)

print(f"DEBUG: Found {len(target_projects)} target projects.")
for p in target_projects:
    print(f" - {p['name']}")

# Match with Funding
with open(locals()['var_function-call-16421974567631203467'], 'r') as f:
    funding_data = json.load(f)

total_funding = 0
matched_ids = set()
matched_names = []

for p in target_projects:
    p_name_clean = p["name"].replace("(CalOES Project)", "").replace("(FEMA Project)", "").strip().lower()
    
    for rec in funding_data:
        f_name = rec["Project_Name"]
        f_name_clean = f_name.lower()
        
        # Check match
        # If project name matches
        if p_name_clean in f_name_clean or f_name_clean in p_name_clean:
             if rec["Funding_ID"] not in matched_ids:
                 total_funding += float(rec["Amount"])
                 matched_ids.add(rec["Funding_ID"])
                 matched_names.append(f_name)

print("__RESULT__:")
print(json.dumps({"total_funding": total_funding, "matched_projects": matched_names}))"""

env_args = {'var_function-call-16421974567631203467': 'file_storage/function-call-16421974567631203467.json', 'var_function-call-16421974567631202340': 'file_storage/function-call-16421974567631202340.json', 'var_function-call-6799515908634330403': 'file_storage/function-call-6799515908634330403.json', 'var_function-call-17193814516790891739': {'total': 0, 'projects': [], 'matched': []}, 'var_function-call-2668714204962722020': 'Done', 'var_function-call-11486011269853492389': [{'name': 'Trancas Canyon Park Playground', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:190) Updates: Construction was completed November 2022. Notice of completion']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:131) Construction was completed, November 2022']}, {'name': 'Point Dume Walkway Repairs', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': ['(cid:131) Construction was completed, November 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['anticipated to have a final design by March 2022. The project will be', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', 'project will have final approval by March 2022. The project will be', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '2022. This project requires Caltrans approval since the work will be on', 'approval by March 2022. The project will be advertised for construction', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'meeting was held on January 20, 2022. Project alternatives will be', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer/Winter 2022', 'of the assessment district to June 30, 2022.', '(cid:131) Advertise for Bidding: February 2022', '(cid:131) Begin Construction: Fall 2022', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', '(cid:131) Complete Design: Spring 2022', 'March 2022', '(cid:131) Begin Design: Spring 2022', 'scheduled to be accepted by the Council at the January 24, 2022 meeting.', 'at the January 24, 2022 meeting.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Completion Date: Spring 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Fall 2022', 'dates_2022': ['January 24, 2022 meeting.', 'anticipated that the final design will be complete by February 2022. The', 'beginning in April 2022.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: April 2022', '(cid:131) The project design will commence during the Spring 2022.', 'started and is anticipated to be completed by the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', 'anticipated that the final design will be complete by July 2022. The', 'beginning in Fall 2022.', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022']}, {'name': 'Citywide Guardrail Replacement', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Malibu Park Storm Drain Repairs', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['(cid:131) Begin Construction: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Spring 2022', 'dates_2022': ['(cid:131) Begin Construction: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Completion Date: Spring 2022']}, {'name': 'Marie Canyon Green Streets', 'section': 'Capital', 'is_disaster': True, 'st': '(cid:131) Begin Construction: Fall 2022', 'dates_2022': ['(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Summer 2022', 'management services was approved by Council on March 14, 2022.', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) This project will be presented to the Planning Commission in May 2022.', 'by March 2022. The project will be advertised for construction bids', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Summer 2022', '(cid:131) Award Contract and Begin Construction: Summer 2022', 'meeting was held on January 20, 2022 and February 23, 2022 and', '2022.', '(cid:131) Complete Design: Summer 2022', '(cid:131) Begin Construction: Fall/Winter 2022', 'of the assessment district to June 30, 2022. A new request for further', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Staff received bids on February 24, 2022. Award of contract is', 'scheduled for the April 11, 2022 Council meeting.', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'Commission will then review the project in Spring 2022 before final', '(cid:131) Complete Design: Spring 2022', 'go to Council in April 2022 after the Funding Agreement is issued by', '(cid:131) Begin Design: Late Spring 2022', 'by the Council at the January 24, 2022 meeting.', '24, 2022 meeting.', '(cid:131) Complete Design: March 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Summer 2022', '(cid:131) Completion Date: Spring 2022', 'Proposals are due in April 14, 2022.', 'anticipated that the final design will be complete by March 2022. The', 'beginning in Spring 2022.', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', 'completed by Spring 2022.', 'of 2022.', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Fall 2022', 'anticipated that the final design will be complete by July 2022. The', 'beginning in Fall 2022.', '(cid:131) Complete Design: July 2022', '(cid:131) Begin Construction: Fall 2022', '2022.']}, {'name': 'Citywide Guardrail Replacement', 'section': 'Capital', 'is_disaster': False, 'st': None, 'dates_2022': []}, {'name': 'Malibu Park Storm Drain Repairs', 'section': 'Capital', 'is_disaster': True, 'st': None, 'dates_2022': ['accepted by the Council on January 24, 2022']}, {'name': 'Birdview Avenue Improvements (CalOES Project)', 'section': 'Capital', 'is_disaster': True, 'st': None, 'dates_2022': ['Improvement. The project was accepted by the Council on January 24, 2022']}]}

exec(code, env_args)
