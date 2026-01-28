code = """import json
import re

# Load civic docs and funding data from storage files
with open(var_call_cfHyLt4fnl8FkJTA47kfy1vu, 'r') as f:
    docs = json.load(f)
with open(var_call_A5Ab7Zc92qkc90fjfFsdsGTt, 'r') as f:
    funding = json.load(f)

# normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount', 0)))
        except:
            r['Amount'] = 0
    r['Project_Name_clean'] = re.sub(r"\s+", " ", r.get('Project_Name','')).strip().lower()

# Helper to clean project names
def clean_name(s):
    if not s:
        return ''
    s = re.sub(r"\(.*?\)", "", s)  # remove parentheses content
    s = re.sub(r"[^a-z0-9 ]+", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s

spring_months = ['march', 'april', 'may']
season_keywords = ['spring']
start_verbs = ['begin', 'beginning', 'begin construction', 'begin construction:', 'starting', 'start', 'started', 'commence', 'commencing', 'commenced', 'advertise']

found_projects = []

for doc in docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, line in enumerate(lines):
        l = line.lower()
        # check if line indicates a start in spring 2022
        is_spring2022 = False
        if '2022' in l:
            if any(k in l for k in season_keywords):
                is_spring2022 = True
            if any(m + ' 2022' in l or m + ' of 2022' in l or m + ',' in l and '2022' in l for m in spring_months):
                # crude check: look for month names near 2022
                if any(m in l for m in spring_months):
                    is_spring2022 = True
            # also patterns like 'beginning in April 2022' or 'beginning in Spring 2022'
            if any(verb in l for verb in start_verbs) and '2022' in l and (any(m in l for m in spring_months) or 'spring' in l):
                is_spring2022 = True
            # also lines like 'beginning in April 2022.' captured above
        # also some lines might say 'beginning in Spring 2022' without 2022? but hint says use substring matching; require 2022
        if is_spring2022:
            # search upward for a project title within previous 12 lines
            proj_name = None
            for j in range(i-1, max(i-13, -1), -1):
                candidate = lines[j]
                if not candidate:
                    continue
                low = candidate.lower()
                # skip metadata or labels
                skip_tokens = ['updates', 'project schedule', 'project description', 'agenda', 'page', 'item', 'recommend', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action']
                if any(tok in low for tok in skip_tokens):
                    continue
                if ':' in candidate and len(candidate) < 60:
                    # likely a label like 'Project Schedule:'
                    continue
                if candidate.startswith('(cid') or candidate.startswith('('):
                    continue
                # candidate should have words and not be a sentence fragment
                if 3 < len(candidate) < 200:
                    proj_name = candidate
                    break
            if proj_name:
                name = re.sub(r'\s+', ' ', proj_name).strip()
                if name not in found_projects:
                    found_projects.append(name)

# Also search for phrases like 'beginning in April 2022' within the whole text and get preceding non-empty line
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r"(beginning in|beginning|begin construction|begin construction:|begin|starting|started).{0,40}2022", text, flags=re.IGNORECASE):
        start = m.start()
        prev_text = text[:start]
        prev_lines = [ln.strip() for ln in prev_text.splitlines() if ln.strip()]
        if prev_lines:
            candidate = prev_lines[-1]
            if 3 < len(candidate) < 200 and candidate not in found_projects:
                found_projects.append(candidate)

# Deduplicate and clean project names
projects = []
seen = set()
for p in found_projects:
    p_clean = re.sub(r"\s+", " ", p).strip()
    if p_clean.lower() in seen:
        continue
    seen.add(p_clean.lower())
    projects.append(p_clean)

# Now match funding records
matched_projects = []
total_funding = 0
for p in projects:
    p_norm = clean_name(p)
    p_funding = 0
    matched_rows = []
    for r in funding:
        fn = r.get('Project_Name','')
        fn_norm = clean_name(fn)
        # exact or normalized containment matching
        if p_norm and (p_norm == fn_norm or p_norm in fn_norm or fn_norm in p_norm):
            p_funding += r.get('Amount',0)
            matched_rows.append(r.get('Project_Name'))
    matched_projects.append({'project': p, 'funding': p_funding, 'matched_funding_rows': matched_rows})
    total_funding += p_funding

result = {
    'num_projects_started_spring_2022': len(projects),
    'total_funding_for_these_projects': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_cfHyLt4fnl8FkJTA47kfy1vu': 'file_storage/call_cfHyLt4fnl8FkJTA47kfy1vu.json', 'var_call_UX8eNp3US3YqDrI26pcf8swk': {'projects': ['manufacturers for filters that will work in the proposed project area. It is', 'advertised for construction bids shortly after this date.', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'to review', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'is finalizing the bid documents.', 'timber with non-combustible materials.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'A kick-off meeting was held in late December.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'started and is anticipated to be completed by the Spring of 2022.', 'assessment district will be created.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'within the City.', 'Rob DuBoux, Public Works Director/City Engineer', 'construction bids.', 'construction bids after approval. An agreement for construction', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'of 2022.', 'the project costs.', 'scheduled for the July 11, 2022 Council meeting.', 'Median Improvement.', 'Westward Beach Road Repair Project', 'the past several months to complete the engineering work, and the final', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'meeting was held on May 16, 2022 and the design is underway.', 'need of replacing at Malibu Bluffs Park', 'guardrails within the project limits.', 'The project consultant prepared the specifications for the project. The City', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'surrounding areas.', 'assessment.', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'and schedule a kick-off meeting in early December 2021.', 'PCH Median Improvements Project', 'than the available budget for the project.', '8, 2022.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.', '(cid:131)', '(cid:131) Award Contract and']}, 'var_call_A5Ab7Zc92qkc90fjfFsdsGTt': 'file_storage/call_A5Ab7Zc92qkc90fjfFsdsGTt.json', 'var_call_zn6W9L5upgFw4HxEJtSmymmJ': {'funding_count': 500}}

exec(code, env_args)
