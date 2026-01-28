code = """import json, re

# Load full civic docs
civic_path = var_call_CXyxXVPH2gGXd2Rsb1S2p8Td
with open(civic_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding aggregated amounts
funding_path = var_call_5J0jB65f4W1d5CqKhYLb27ML
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

funding_by_name = {item['Project_Name']: int(item['total_amount']) for item in funding}

# Patterns indicating Spring 2022
spring_regex = re.compile(r"(spring\s*(of)?\s*2022|2022\s*-?\s*spring|march\s*2022|april\s*2022|may\s*2022|\b03\b|\b04\b|\b05\b)", re.IGNORECASE)

matched_projects = set()

for proj in funding_by_name:
    pname = proj
    p_low = re.escape(pname.lower())
    # create simple search: remove parentheses content for matching variants
    pname_simple = re.sub(r"\([^)]*\)", "", pname).strip().lower()
    if not pname_simple:
        pname_simple = pname.lower()
    # build token of first few words
    for doc in docs:
        text = doc.get('text','')
        low_text = text.lower()
        # search for exact project name or simplified name in text
        if pname.lower() in low_text or pname_simple in low_text:
            # find all occurrences of the simplified name
            for match in re.finditer(re.escape(pname_simple), low_text):
                start, end = match.start(), match.end()
                window = low_text[max(0, start-200): min(len(low_text), end+200)]
                if spring_regex.search(window):
                    matched_projects.add(proj)
                    break
            if proj in matched_projects:
                break
        else:
            # also check for significant token overlap: if at least two tokens from project name appear near 'spring 2022'
            tokens = [t for t in re.split(r"\W+", pname_simple) if t]
            if len(tokens) >= 2:
                # find occurrences of spring indicators in doc
                for m in spring_regex.finditer(low_text):
                    s = max(0, m.start()-300)
                    e = min(len(low_text), m.end()+300)
                    context = low_text[s:e]
                    # count token matches in context
                    count = sum(1 for t in tokens if t in context)
                    if count >= max(1, int(len(tokens)*0.4)):
                        # consider this a match
                        matched_projects.add(proj)
                        break
                if proj in matched_projects:
                    break

matched_projects = sorted(list(matched_projects))
total_amount = sum(funding_by_name[p] for p in matched_projects)

output = {'spring_projects': matched_projects, 'count': len(matched_projects), 'total_amount': total_amount}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_BT53iOXDUlKYiILn447GjfpJ': [], 'var_call_dqgmrJKK5TBMw3nz65PRF9uh': ['civic_docs'], 'var_call_CXyxXVPH2gGXd2Rsb1S2p8Td': 'file_storage/call_CXyxXVPH2gGXd2Rsb1S2p8Td.json', 'var_call_r73JOKvmqWfLMBOlmgqb4Hd2': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'to review', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'is finalizing the bid documents.', 'timber with non-combustible materials.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'within the City.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'started and is anticipated to be completed by the Spring of 2022.', 'assessment district will be created.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'construction bids.', 'construction bids after approval. An agreement for construction', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'City.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'of 2022.', 'the project costs.', 'Marie Canyon Green Streets', 'Median Improvement.', 'the past several months to complete the engineering work, and the final', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'guardrails within the project limits.', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'assessment.', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'under review. Staff anticipates completing the selection process next month', 'than the available budget for the project.', '8, 2022.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.'], 'var_call_pD0AVrMmyZH3jnhSvgs0MZuL': ['Funding'], 'var_call_5J0jB65f4W1d5CqKhYLb27ML': 'file_storage/call_5J0jB65f4W1d5CqKhYLb27ML.json', 'var_call_lWjyWzNHWASdmdA3QTeJQggg': {'spring_projects': [], 'count': 0, 'total_amount': 0}}

exec(code, env_args)
