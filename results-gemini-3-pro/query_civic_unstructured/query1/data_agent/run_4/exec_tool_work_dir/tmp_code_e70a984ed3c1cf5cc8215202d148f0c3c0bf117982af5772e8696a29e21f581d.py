code = """import json
import difflib

# Get paths
funding_path = locals()['var_function-call-1424370091685766711']
docs_path = locals()['var_function-call-10286396622452696184']

# Load data
with open(funding_path, 'r') as f:
    funding_records = json.load(f)
funding_names = [r['Project_Name'].strip() for r in funding_records]
funding_map = {r['Project_Name'].strip(): r['Amount'] for r in funding_records}

with open(docs_path, 'r') as f:
    docs = json.load(f)

# Extract candidates again
candidates = set()
for doc in docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    in_design = False
    for line in lines:
        line = line.strip()
        if not line: continue
        if 'Capital Improvement Projects (Design)' in line:
            in_design = True
            continue
        if 'Capital Improvement Projects' in line and 'Design' not in line:
            in_design = False
        if 'Disaster Recovery Projects' in line:
            in_design = False
        if in_design:
            if line.startswith('(cid:') or line.startswith('Page ') or line.startswith('Agenda Item'): continue
            if any(x in line.lower() for x in ['prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:', 'recommended action:', 'discussion:']): continue
            if 'Updates:' in line or 'Schedule:' in line: continue
            if line.startswith('Item') or line.startswith('To:') or line.startswith('From:'): continue
            if len(line) > 100 or line.endswith('.'): continue
            name = line.strip()
            if len(name) < 5: continue
            candidates.add(name)

# Check specific candidates
targets = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "Westward Beach Road Repair Project",
    "Trancas Canyon Park Upper and Lower Slopes Repair",
    "Civic Center Water Treatment Facility Phase 2"
]

results = {}
for t in candidates:
    # Find best match in funding_names
    # difflib.get_close_matches(word, possibilities, n=1, cutoff=0.6)
    matches = difflib.get_close_matches(t, funding_names, n=1, cutoff=0.5)
    best_match = matches[0] if matches else None
    
    amount = 0
    if best_match:
        try:
            amount = float(funding_map[best_match])
        except:
            amount = 0
            
    results[t] = {"best_match": best_match, "amount": amount}

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-1424370091685766711': 'file_storage/function-call-1424370091685766711.json', 'var_function-call-10286396622452696184': 'file_storage/function-call-10286396622452696184.json', 'var_function-call-834927334582506323': {'matches': ['Outdoor Warning Signs', 'Permanent Skate Park', 'Malibu Bluffs Park South Walkway Repairs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Canyon Road Traffic Study', 'Westward Beach Road Drainage Improvements Project', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Storm Drain Master Plan'], 'extracted_candidates': ['comments mid-April. This project required their review since the project', 'final design is complete and the project will be advertised for', 'schedule will be developed upon the completion of the Cultural', 'assessment district will be created.', 'Metro.', 'In May 2021, the Council approved funding for additional engineering', 'to perform construction', "Council's direction.", 'modification of the schedule has been requested.', 'draft plans are expected to be completed in early 2022. The Planning', 'Outdoor Warning Signs', 'reviewed multiple biofilter', 'the agreement.', 'manufacturers for filters that will work in the proposed project area. The', 'meeting was held on January 20, 2022 and February 23, 2022 and', 'final approval. It is anticipated that the project will have final approval', 'Westward Beach Road Repair Project', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', '2022 Morning View Resurfacing & Storm Drain Improvements', 'Civic Center Water Treatment Facility Phase 2', 'bicycles pavement markings, delineated parallel parking spaces and', 'preliminary estimated assessments in July 2021. Staff has been', '2022.', 'speed humps. There is room to add a pathway within the R/W per', 'Permanent Skate Park', 'Coastal Development Permit and directed the Public Works and Public', 'Malibu Bluffs Park South Walkway Repairs', 'consultant. It is anticipated that this agreement will go to Council in', 'Clover Heights Storm Drainage Improvements', 'manufactured biofilters. City staff is reviewing multiple biofilter', 'routed through Caltrans for final approval. It is anticipated that the', 'PCH at Trancas Canyon Road Right Turn Lane', 'with the property owners regarding their proposed assessments.', 'PCH Signal Synchronization System Improvements Project', 'Resources review.', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'project will begin in conjunction with the PCH Median Improvement', 'on Pacific Coast Highway. The project reports and plans are being', 'advertised for construction bids after this date. A construction manager', 'scheduled for the April 11, 2022 Council meeting.', 'evaluating the project costs.', 'to develop project', 'of the assessment district to June 30, 2022. A new request for further', 'meeting was held on January 20, 2022. Project alternatives will be', '2022. This project requires Caltrans approval since the work will be on', 'Council directed staff to withdraw the proposed project and associated', 'March 2022', 'Marie Canyon Green Streets', 'management services was approved by Council on March 14, 2022.', 'construction bids after approval. An agreement for construction', 'management.', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'project and will submit to the County for review.', 'program.', 'project alternatives were presented to the commissions. City staff will', 'the County and will be finalizing the design.', 'will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.', 'to review', 'the process of', 'manufactured biofilters. City staff', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'Latigo Canyon Road Retaining Wall Repair Project', 'for final approval. It is anticipated that the project will have final', 'agreement will be sent to City Council in March.', 'presented to the commissions at a future date.', 'seeking proposals', 'Safety Commissions', 'Commission will then review the project in Spring 2022 before final', 'Malibu Canyon Road Traffic Study', 'shortly after final approval. If possible, the construction of this project', 'Individual letters were mailed to all properties within Phase 2 with their', 'routed through Caltrans for final approval. The project will have final', 'selected a qualified consultant. It is anticipated that the agreement will', 'approval by the end of the March. The project will be advertised for', 'review by the Council.', 'to finalize plans and specifications', 'The project reports and plans are being routed through Caltrans for', 'bids shortly after final approval. If possible, the construction of this', 'bidding.', 'Malibu Park Drainage Improvements', 'City will be issuing a RFQ/P for design services in the summer of 2023', 'advertised for construction bids shortly after this date.', 'sending this project out to bid during the Spring of 2022.', 'of the assessment district to June 30, 2022.', 'or phasing out the project', 'from consultants', 'feasible traffic safety improvements can be constructed at this location.', 'required for this project. Staff is waiting for the County’s approval of', 'Commission meeting for project direction due to concerns regarding', 'Westward Beach Road Drainage Improvements Project', 'preliminary estimated assessments. Staff has been communicating', 'and Harbor. Staff is working out the final details of the project with', 'overall project costs.', 'the County.', 'project. Staff is working on the project plans to prepare for public', 'cleared the project.', 'present the recommended design alternatives to Council on March 28,', 'project', 'anticipated to have a final design by March 2022. The project will be', 'project will have final approval by March 2022. The project will be', 'alternatives. A joint Public Works and Public Safety Commission', 'This project requires Caltrans approval since the work will be on PCH.', '8, 2021. This project requires Caltrans approval since the work will be', 'amenities such as trash cans, benches, tables, and restrooms.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'to Malibu Bluffs Park. The project would include parking and additional site', 'construction bids.', 'PCH. The project reports and plans are being routed through Caltrans', 'September 20, 2021. At the December 13, 2021, City Council meeting,', 'work related to the project. Staff has worked with the consultant over', 'been finalized and incorporated into GIS.', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Bluffs Park Shade Structure', 'Westward Beach Road Improvements Project', 'Storm Drain Master Plan', 'Resources review for the SRF funding application', 'Commission in February.', 'go to Council in April 2022 after the Funding Agreement is issued by', 'the past several months to complete the engineering work, and the final', 'Trancas Canyon Park Playground', 'execution in July and has followed up with an additional letter to those', 'the Spring 2023.', 'and rejected all bids due to a budget shortfall', 'the project', 'sirens height and feedback from residents and the community.', 'property owners.', 'communicating with the property owners regarding their proposed', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'approval by March 2022. The project will be advertised for construction', 'assessments.', 'Fund program.', 'by March 2022. The project will be advertised for construction bids', 'February 1, 2021.', 'manufacturers for filters that will work in the proposed project area. It is']}, 'var_function-call-14033121997091606812': {'count': 12, 'matches': ['Malibu Canyon Road Traffic Study', 'Malibu Bluffs Park South Walkway Repairs', 'Outdoor Warning Signs', 'Civic Center Stormwater Diversion Structure', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'PCH at Trancas Canyon Road Right Turn Lane', 'PCH Median Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Trancas Canyon Park Playground', 'Westward Beach Road Drainage Improvements Project', 'Permanent Skate Park'], 'debug': ['Started Design Section', 'Stopped Design Section at: Capital Improvement Projects (Construction)', 'Started Design Section', 'Stopped Design Section at: Capital Improvement Projects (Construction)', 'Started Design Section']}}

exec(code, env_args)
