code = """import json, re
import pandas as pd

# Load extracted design projects from previous python result
extracted = var_call_bhFeqVdjpqygq2r3KDuADfIX
if isinstance(extracted, str):
    extracted = json.loads(extracted)
design_projects = set(extracted.get('design_projects_extracted', []))

# Basic cleanup: drop obvious non-project lines (contain spaces but have verbs/too long)
clean = set()
for p in design_projects:
    if not p or len(p) < 5 or len(p) > 80:
        continue
    if re.search(r'\b(this|the|and|will|was|were|is|are|project)\b', p, flags=re.I):
        # allow if ends with 'Project' or common naming patterns
        if not re.search(r'\b(Project|Plan|Facility|Signs|Skate Park|Playground|Lane|Improvements|Repair|Repairs|Master Plan|Treatment)\b', p, flags=re.I):
            continue
    if re.match(r'^(\d{4}\.?|March \d{4}|Commission|Discussion|Recommended Action)$', p, flags=re.I):
        continue
    clean.add(p)

# Load funding totals > 50k
fund_src = var_call_zEVy8spMa1a7YrzXoEnQivxx
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = fund_src
fund_projects = {r['Project_Name'] for r in fund}

# Intersection count
intersection = sorted(clean.intersection(fund_projects))

print('__RESULT__:')
print(json.dumps({"count": len(intersection), "projects": intersection}))"""

env_args = {'var_call_NeEllH8kVvzbzjVCAPjBs0bE': [{'cnt': '276'}], 'var_call_TkVPrZucnCTe4WspWeWiKRFr': 'file_storage/call_TkVPrZucnCTe4WspWeWiKRFr.json', 'var_call_bhFeqVdjpqygq2r3KDuADfIX': {'design_projects_extracted': ['2022 Morning View Resurfacing & Storm Drain Improvements', '2022.', '2022. This project requires Caltrans approval since the work will be on', '8, 2021. This project requires Caltrans approval since the work will be', 'Bluffs Park Shade Structure', 'Canyon Road near Harbor Vista Drive and Potter Lane to determine if any', 'Civic Center Stormwater Diversion Structure', 'Civic Center Water Treatment Facility Phase 2', 'Clover Heights Storm Drainage Improvements', 'Coastal Development Permit and directed the Public Works and Public', 'Commission in February.', 'Commission meeting for project direction due to concerns regarding', 'Commission will then review the project in Spring 2022 before final', "Council's direction.", 'February 1, 2021.', 'Fund program.', 'In May 2021, the Council approved funding for additional engineering', 'Individual letters were mailed to all properties within Phase 2 with their', 'Latigo Canyon Road Retaining Wall Repair Project', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Malibu Park Drainage Improvements', 'March 2022', 'Marie Canyon Green Streets', 'Metro.', 'Outdoor Warning Signs', 'PCH Median Improvements Project', 'PCH Signal Synchronization System Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'PCH. The project reports and plans are being routed through Caltrans', 'Permanent Skate Park', 'Resources review for the SRF funding application', 'Resources review.', 'Safety Commissions', 'Storm Drain Master Plan', 'The project reports and plans are being routed through Caltrans for', 'This project requires Caltrans approval since the work will be on PCH.', 'Trancas Canyon Park Playground', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Improvements Project', 'Westward Beach Road Repair Project', 'alternatives. A joint Public Works and Public Safety Commission', 'amenities such as trash cans, benches, tables, and restrooms.', 'and rejected all bids due to a budget shortfall', 'anticipated to have a final design by March 2022. The project will be', 'assessment district will be created.', 'assessments.', 'been finalized and incorporated into GIS.', 'bicycles pavement markings, delineated parallel parking spaces and', 'bidding.', 'bids shortly after final approval. If possible, the construction of this', 'cleared the project.', 'comments mid-April. This project required their review since the project', 'communicating with the property owners regarding their proposed', 'construction bids after approval. An agreement for construction', 'construction bids.', 'draft plans are expected to be completed in early 2022. The Planning', 'evaluating the project costs.', 'execution in July and has followed up with an additional letter to those', 'feasible traffic safety improvements can be constructed at this location.', 'final approval. It is anticipated that the project will have final approval', 'for final approval. It is anticipated that the project will have final', 'go to Council in April 2022 after the Funding Agreement is issued by', 'management services was approved by Council on March 14, 2022.', 'management.', 'manufacturers for filters that will work in the proposed project area. It is', 'manufacturers for filters that will work in the proposed project area. The', 'meeting was held on January 20, 2022 and February 23, 2022 and', 'meeting was held on January 20, 2022. Project alternatives will be', 'modification of the schedule has been requested.', 'of the assessment district to June 30, 2022.', 'of the assessment district to June 30, 2022. A new request for further', 'on Pacific Coast Highway. The project reports and plans are being', 'or phasing out the project', 'overall project costs.', 'permanent skate park located on the Crummer/Case Court parcel adjacent', 'present the recommended design alternatives to Council on March 28,', 'presented to the commissions at a future date.', 'program.', 'project', 'project and will submit to the County for review.', 'project will begin in conjunction with the PCH Median Improvement', 'project will have final approval by March 2022. The project will be', 'property owners.', "rehabilitation of the roadway to max 8' from R/W, add share road with", 'review by the Council.', 'reviewed multiple biofilter', 'routed through Caltrans for final approval. It is anticipated that the', 'routed through Caltrans for final approval. The project will have final', 'schedule will be developed upon the completion of the Cultural', 'scheduled for the April 11, 2022 Council meeting.', 'scope falls within Zuma Canyon Creek. Army Corp. of Engineers has', 'seeking proposals', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'shortly after final approval. If possible, the construction of this project', 'sirens height and feedback from residents and the community.', 'speed humps. There is room to add a pathway within the R/W per', 'the County and will be finalizing the design.', 'the County.', 'the Spring 2023.', 'the agreement.', 'the past several months to complete the engineering work, and the final', 'the process of', 'the project', 'to Malibu Bluffs Park. The project would include parking and additional site', 'to develop project', 'to finalize plans and specifications', 'to perform construction', 'to review', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'will begin in conjunction with the PCH Median Improvement', 'with the property owners regarding their proposed assessments.'], 'design_project_count_extracted': 114}, 'var_call_zEVy8spMa1a7YrzXoEnQivxx': 'file_storage/call_zEVy8spMa1a7YrzXoEnQivxx.json'}

exec(code, env_args)
