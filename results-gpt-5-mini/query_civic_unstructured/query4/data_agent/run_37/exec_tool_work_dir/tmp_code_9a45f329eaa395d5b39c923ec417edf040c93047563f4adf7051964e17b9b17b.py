code = """import json
path = var_call_5J0jB65f4W1d5CqKhYLb27ML
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# We need to find projects that started in Spring 2022.
# From earlier, we extracted candidate project title lines from civic docs
civic_candidates = var_call_r73JOKvmqWfLMBOlmgqb4Hd2

# Normalize project names from funding table and look for matches where civic candidate mentions project name
funding_by_name = {item['Project_Name']: int(item['total_amount']) for item in funding}

# Determine which funding projects correspond to civic candidates: check if the funding Project_Name appears (case-insensitive) in any civic candidate line OR vice versa
spring_projects = set()
for fname in funding_by_name:
    low_fname = fname.lower()
    for cand in civic_candidates:
        low_cand = cand.lower()
        if low_fname in low_cand or low_cand in low_fname:
            # check if the civic candidate line contains indication of Spring 2022
            if 'spring' in low_cand and '2022' in low_cand:
                spring_projects.add(fname)
            # or phrases like 'beginning in spring 2022' or 'spring of 2022'
            if 'spring of 2022' in low_cand or 'spring 2022' in low_cand or 'beginning in spring 2022' in low_cand or 'spring 2022' in low_cand:
                spring_projects.add(fname)
        # Also check if cand mentions the month word March/April/May with 2022
        if any(m in low_cand for m in ['march 2022','april 2022','may 2022','march 2022','beginning in april 2022','beginning in march 2022']):
            if low_fname in low_cand or low_cand in low_fname:
                spring_projects.add(fname)

# Additionally, some civic candidate lines are full project names already. We'll also check funding names for words present in candidates
for cand in civic_candidates:
    for fname in funding_by_name:
        if cand.lower() in fname.lower() or fname.lower() in cand.lower():
            if '2022' in cand or 'spring' in cand.lower() or 'march' in cand.lower() or 'april' in cand.lower() or 'may' in cand.lower():
                spring_projects.add(fname)

# Manual matches based on common appearance in civic doc preview earlier: From the civic doc we saw lines like
# "PCH Median Improvements Project", "PCH Signal Synchronization System Improvements Project", "Westward Beach Road Repair Project", "Clover Heights Storm Drainage Improvements", "Bluffs Park Shade Structure", "Marie Canyon Green Streets", "Latigo Canyon Road Retaining Wall Repair Project", "Trancas Canyon Park..."
# Use heuristics: if funding project name contains one of these keywords and the civic candidates mention spring 2022 near them.
keywords = ['pch median','pch signal','westward beach','clover heights','bluffs park shade','marie canyon','latigo canyon','trancas canyon','permanent skate','pch at trancas']
for fname in funding_by_name:
    lf = fname.lower()
    for k in keywords:
        if k in lf:
            # check if corresponding candidate mentions spring/2022
            for cand in civic_candidates:
                if k.split()[0] in cand.lower() and ('spring' in cand.lower() or '2022' in cand.lower() or 'march' in cand.lower() or 'april' in cand.lower() or 'may' in cand.lower()):
                    spring_projects.add(fname)

# Now summarize
spring_projects = sorted(list(spring_projects))
total_amount = sum(funding_by_name[p] for p in spring_projects)

output = {'spring_projects': spring_projects, 'count': len(spring_projects), 'total_amount': total_amount}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_BT53iOXDUlKYiILn447GjfpJ': [], 'var_call_dqgmrJKK5TBMw3nz65PRF9uh': ['civic_docs'], 'var_call_CXyxXVPH2gGXd2Rsb1S2p8Td': 'file_storage/call_CXyxXVPH2gGXd2Rsb1S2p8Td.json', 'var_call_r73JOKvmqWfLMBOlmgqb4Hd2': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'to review', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'is finalizing the bid documents.', 'timber with non-combustible materials.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'within the City.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'started and is anticipated to be completed by the Spring of 2022.', 'assessment district will be created.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'construction bids.', 'construction bids after approval. An agreement for construction', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'City.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'of 2022.', 'the project costs.', 'Marie Canyon Green Streets', 'Median Improvement.', 'the past several months to complete the engineering work, and the final', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'guardrails within the project limits.', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'assessment.', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'under review. Staff anticipates completing the selection process next month', 'than the available budget for the project.', '8, 2022.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.'], 'var_call_pD0AVrMmyZH3jnhSvgs0MZuL': ['Funding'], 'var_call_5J0jB65f4W1d5CqKhYLb27ML': 'file_storage/call_5J0jB65f4W1d5CqKhYLb27ML.json'}

exec(code, env_args)
