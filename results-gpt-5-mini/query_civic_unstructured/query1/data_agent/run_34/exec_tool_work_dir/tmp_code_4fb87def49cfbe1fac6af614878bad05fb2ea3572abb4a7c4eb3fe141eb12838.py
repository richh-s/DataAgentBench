code = """import json
path = var_call_W500uzW6DllqM8siszxSgy14
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# convert Amount to int
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        r['Amount'] = None

# load the extracted project names from civic docs
proj_path = var_call_LsU45WUOsl2pWLbqd1zx6AJH
proj_list = json.loads(open(proj_path, 'r', encoding='utf-8').read())

# Normalize names for matching: lowercase, remove extra spaces
def norm(s):
    return ' '.join(s.lower().strip().split())

proj_norm = {norm(p): p for p in proj_list}

# find funding records for projects that appear in proj_norm and have Amount > 50000
matching = []
for r in funding:
    pn = r.get('Project_Name','')
    key = norm(pn)
    if key in proj_norm and r.get('Amount') is not None and r['Amount'] > 50000:
        matching.append({'Project_Name': pn, 'Amount': r['Amount'], 'Matched_Project_Name_in_docs': proj_norm[key]})

# Also include cases where project name in docs is slightly different: try substring match
for pkey, orig in list(proj_norm.items()):
    for r in funding:
        pn = r.get('Project_Name','')
        if r.get('Amount') is None or r['Amount'] <= 50000:
            continue
        if pkey in norm(pn) or norm(pn) in pkey:
            # check not already included
            if not any(m['Project_Name']==pn and m['Amount']==r['Amount'] for m in matching):
                matching.append({'Project_Name': pn, 'Amount': r['Amount'], 'Matched_Project_Name_in_docs': orig})

# deduplicate matching
seen = set()
unique_matching = []
for m in matching:
    key = (m['Project_Name'], m['Amount'], m['Matched_Project_Name_in_docs'])
    if key not in seen:
        seen.add(key)
        unique_matching.append(m)

# Count how many of these are 'capital' projects with status 'design'.
# From the civic docs extraction we didn't extract types/status per project explicitly; but the projects we extracted came from the 'Capital Improvement Projects (Design)' section, so they are capital + design.
# So count unique project names matched where Matched_Project_Name_in_docs is in proj_list
count = len(unique_matching)

import json
print('__RESULT__:')
print(json.dumps({'count': count, 'matched_projects': unique_matching}))"""

env_args = {'var_call_xWBqhZjvVzRFPrcyF1m6w9tD': ['civic_docs'], 'var_call_SitqQeQgm0QXhLVXJ5E5S5bL': 'file_storage/call_SitqQeQgm0QXhLVXJ5E5S5bL.json', 'var_call_LsU45WUOsl2pWLbqd1zx6AJH': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'project and will submit to the County for review.', 'PCH Median Improvements Project', 'and rejected all bids due to a budget shortfall', 'or phasing out the project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'cleared the project.', 'Clover Heights Storm Drainage Improvements', 'to finalize plans and specifications', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'been finalized and incorporated into GIS.', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Resources review for the SRF funding application', 'Permanent Skate Park', 'project', 'PCH at Trancas Canyon Road Right Turn Lane', 'the Spring 2023.', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.', 'Marie Canyon Green Streets', 'advertised for construction bids shortly after this date.', 'agreement will be sent to City Council in March.', 'PCH Signal Synchronization System Improvements Project', 'project will begin in conjunction with the PCH Median Improvement', 'Westward Beach Road Improvements Project', 'to review', 'with the property owners regarding their proposed assessments.', 'of the assessment district to June 30, 2022.', 'Bluffs Park Shade Structure', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'amenities such as trash cans, benches, tables, and restrooms.', 'review by the Council.', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'March 2022', 'bidding.', 'management.', 'Civic Center Stormwater Diversion Structure', 'the agreement.', 'the County.', 'the County and will be finalizing the design.', 'Commission in February.', 'program.', 'assessment district will be created.', 'Malibu Park Drainage Improvements', 'February 1, 2021.', 'Fund program.', 'evaluating the project costs.', 'overall project costs.', 'construction bids.', 'management services was approved by Council on March 14, 2022.', 'will begin in conjunction with the PCH Median Improvement', "Council's direction.", 'assessments.', 'modification of the schedule has been requested.', 'property owners.', 'scheduled for the April 11, 2022 Council meeting.', 'Metro.', 'proposals from consultants to perform construction management.', 'we are still awaiting comments to those plans.', 'from the County.', 'County and will be finalizing the design.', 'the project costs.', 'Annual Street Maintenance', 'maintenance of City streets.', 'we received comments to those plans.', 'on the comments received.', 'agreement.', 'be signed and executed.', 'schedule to begin the construction.', '2021 Annual Street Maintenance', 'scheduled for the July 11, 2022 Council meeting.', 'Median Improvement.', 'project will be redesigned and constructed early fall.', 'investigation. This work is required with the SRF financing.', 'update regarding the proposed time extension to the MOU deadlines.', 'meeting was held on May 16, 2022 and the design is underway.', 'Michael Landon Center Roof Replacement Project', 'Michael Landon Center at Malibu Bluffs Park.', '2022 Annual Street Maintenance', 'at the July 11, 2022 Council meeting.', 'next week.', 'The project is currently out to bid with proposals due August 4, 2022.', '2022-2023 budget.', 'August.', 'received some comments to those plans.', 'assessment.', 'for proposals', 'September.', 'is working on the project plans to prepare for public bidding.', 'approvals.', 'hearing, but the request has been made.', 'a construction contract to City Council at the October 11, 2021 meeting.', '2022.', 'and execution', 'month and staff is in the final stages of selecting a firm.', 'Commission hearing on November 15, 2021.', 'mobilize for this project.', 'appealed and staff is preparing to respond to the appeal.', 'October 7, 2021 with proposals due November 10th.', 'was approved at the July 11, 2022 Council meeting.', 'than the available budget for the project.', '8, 2022.', 'regarding the proposed time extension to the MOU deadlines.', 'final review by the Council.', 'selecting a firm.', 'the Public Works Commission to revise the project scope.', 'MOU.', 'October 7, 2021 with proposals received November 18.'], 'var_call_XqqmL9a5qKWy4j0uhbJCzGhq': ['Funding'], 'var_call_W500uzW6DllqM8siszxSgy14': 'file_storage/call_W500uzW6DllqM8siszxSgy14.json'}

exec(code, env_args)
