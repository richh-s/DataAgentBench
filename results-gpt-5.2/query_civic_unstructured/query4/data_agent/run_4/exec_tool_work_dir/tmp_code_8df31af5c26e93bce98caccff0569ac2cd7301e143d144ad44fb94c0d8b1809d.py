code = """import json, re

# projects extracted
proj_info = var_call_bluGKCpuETCZ89D9xWt4f0fe
projects = proj_info['projects']

# load funding totals
raw = var_call_oGPhOfyzB0R5CdhggwQ2EjBu
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = raw
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding}

# filter project names to those that look like real project names and exist in funding table
bad = set([
    'Discussion','Recommended Action','Fire.','August.','March 2022','Metro.','Median Improvement.','Westward Beach Road.'
])

clean = []
for p in projects:
    p2 = p.strip().strip('.')
    if len(p2) < 6: 
        continue
    if p in bad or p2 in bad:
        continue
    # must match funding names exactly
    if p in fund_map:
        clean.append(p)

clean = sorted(set(clean))

total_funding = sum(fund_map[p] for p in clean)

print('__RESULT__:')
print(json.dumps({'count': len(clean), 'total_funding': total_funding, 'projects': clean}))"""

env_args = {'var_call_TlI74jLg2bFHKmzFuVk7AJqM': ['Funding'], 'var_call_5wzrwfkZwg9a9BZl1um4J4FU': ['civic_docs'], 'var_call_fXcE8gcML1dtHYH4pToQFkoT': 'file_storage/call_fXcE8gcML1dtHYH4pToQFkoT.json', 'var_call_bluGKCpuETCZ89D9xWt4f0fe': {'projects': ['8, 2022.', 'A kick-off meeting was held in late December.', 'August.', 'Commission hearing on November 15, 2021.', 'Commission will then review the project in', 'Fire.', 'March 2022', 'Median Improvement.', 'Metro.', 'PCH Signal Synchronization System Improvements Project', 'The project is currently out to bid with proposals due August 4, 2022.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Westward Beach Road.', 'advertised for construction bids shortly after this date.', 'agreement will be sent to City Council in March.', 'and schedule a kick-off meeting in early December 2021.', 'anticipated that the final design will be complete by', 'anticipated to have a final design by', 'approval by', 'assessment district will be created.', 'assessment.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'beginning in', 'beginning in April 2022.', 'beginning in Spring 2022.', 'by', 'completed by', 'construction bids.', 'consultant. It is anticipated that this agreement will go to Council in', 'consultants to develop the master plan.', 'damaged by the Woolsey Fire.', 'draft plans are expected to be completed in', 'drain towards the end of Clover Heights will help eliminate this issue.', 'evaluating the project costs.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'finalized.', 'go to Council in', 'guardrails within the project limits.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'management services was approved by Council on March 14, 2022.', 'meeting was held on May 16, 2022 and the design is underway.', 'of 2022.', 'project will begin in conjunction with the PCH Median Improvement', 'project will have final approval by', 'review by the Council.', 'scheduled for the April 11, 2022 Council meeting.', 'scheduled for the July 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'started and is anticipated to be completed by the Spring of 2022.', 'than the available budget for the project.', 'that was damaged by the Woolsey Fire.', 'the Public Works Commission to revise the project scope.', 'the project costs.', 'timber with non-combustible materials.', 'to develop the master plan. Proposals are due in September 2021.', 'to review', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'will begin in conjunction with the PCH Median Improvement', 'within the City.'], 'count': 62}, 'var_call_oGPhOfyzB0R5CdhggwQ2EjBu': 'file_storage/call_oGPhOfyzB0R5CdhggwQ2EjBu.json'}

exec(code, env_args)
