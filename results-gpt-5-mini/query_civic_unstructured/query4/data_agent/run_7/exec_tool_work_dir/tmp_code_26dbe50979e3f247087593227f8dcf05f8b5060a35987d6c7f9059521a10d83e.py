code = """import json, re
# Load civic docs results
with open(var_call_BM51I30oAu2S3Iytx6gDIzK1, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load funding table results
with open(var_call_t4yJcXht1E12iGFg700a7l0f, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Build funding map
fund_map = {}
for rec in funding:
    name = rec.get('Project_Name')
    try:
        amt = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
    except:
        try:
            amt = int(float(rec.get('Amount')))
        except:
            amt = 0
    fund_map[name] = amt

# Prepare patterns
spring_pattern = re.compile(r"(?i)(spring(?:/summer)?\s*2022|march\s*2022|april\s*2022|may\s*2022)")
begin_keywords = re.compile(r"(?i)\b(begin|beginning|start|starting|advertis|advertise|advertised)\b")

matched_projects = {}

# For each funding project, search in docs
for proj in fund_map.keys():
    pname = proj
    pname_escaped = re.escape(pname)
    # search across all docs
    found_flag = False
    for doc in docs:
        text = doc.get('text','')
        lower = text.lower()
        # attempt to find project name in text
        idx = lower.find(pname.lower())
        if idx != -1:
            # define window
            start = max(0, idx-300)
            end = min(len(text), idx+len(pname)+400)
            window = text[start:end]
            if spring_pattern.search(window) and begin_keywords.search(window):
                matched_projects[pname] = fund_map.get(pname,0)
                found_flag = True
                break
            # if spring pattern appears and window has words like 'begin construction' specifically
            if re.search(r'(?i)spring', window) and re.search(r'(?i)begin (?:construction|design|work)', window):
                matched_projects[pname] = fund_map.get(pname,0)
                found_flag = True
                break
            # also accept patterns like 'Complete Design: March 2022' followed by 'Begin Construction: Spring 2022'
            # check a larger surrounding area: 2000 chars
            start2 = max(0, idx-2000)
            end2 = min(len(text), idx+len(pname)+2000)
            window2 = text[start2:end2]
            if spring_pattern.search(window2) and begin_keywords.search(window2):
                matched_projects[pname] = fund_map.get(pname,0)
                found_flag = True
                break
    # also handle case where project name in docs might be slightly different e.g., removing '(FEMA Project)'
    if not found_flag:
        # remove parenthetical suffix from funding name and try
        pname_no_paren = re.sub(r"\s*\([^)]*\)", "", pname).strip()
        if pname_no_paren.lower() != pname.lower():
            for doc in docs:
                text = doc.get('text','')
                idx = text.lower().find(pname_no_paren.lower())
                if idx != -1:
                    start = max(0, idx-300)
                    end = min(len(text), idx+len(pname_no_paren)+400)
                    window = text[start:end]
                    if spring_pattern.search(window) and begin_keywords.search(window):
                        matched_projects[pname] = fund_map.get(pname,0)
                        found_flag = True
                        break

# Additionally, scan docs for any project-like lines followed by 'Begin Construction: Spring 2022' if not matched via funding names
# extract lines with pattern 'Begin' near 'Spring 2022' and attempt to capture the project title above
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if re.search(r'(?i)begin(?:ning)?(?: construction| design| construction| design)?:?\s*(spring(?:/summer)?\s*2022|march\s*2022|april\s*2022|may\s*2022)', line):
            # look upward for project title within 10 lines
            for k in range(1, 12):
                idx = i - k
                if idx < 0:
                    break
                cand = lines[idx].strip()
                if not cand:
                    continue
                if len(cand) > 3 and len(cand) < 150 and not re.search(r'(?i)^(updates:|project schedule:|project description:|agenda item|page \d+|item|to:|prepared by:|approved by:|date prepared:)', cand):
                    # normalize
                    cand_norm = re.sub(r'\s+', ' ', cand)
                    # try to match this cand to funding map keys
                    for key in fund_map.keys():
                        if cand_norm.lower() in key.lower() or key.lower() in cand_norm.lower():
                            matched_projects[key] = fund_map.get(key,0)

# Build result
projects_list = []
for k,v in matched_projects.items():
    projects_list.append({"Project_Name": k, "Amount": v})

count = len(projects_list)
total = sum(p['Amount'] for p in projects_list)

result = {"count": count, "total_funding": total, "projects": projects_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BM51I30oAu2S3Iytx6gDIzK1': 'file_storage/call_BM51I30oAu2S3Iytx6gDIzK1.json', 'var_call_T3E2Gtr9Skk7kPywXXcfXGbG': [], 'var_call_RsjBgFTxZckD0UpAUEWZa0lb': ['manufacturers for filters that will work in the proposed project area. It is', 'advertised for construction bids shortly after this date.', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'to review', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'is finalizing the bid documents.', 'timber with non-combustible materials.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'A kick-off meeting was held in late December.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'started and is anticipated to be completed by the Spring of 2022.', 'assessment district will be created.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'within the City.', 'construction bids.', 'management services was approved by Council on March 14, 2022.', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'of 2022.'], 'var_call_t4yJcXht1E12iGFg700a7l0f': 'file_storage/call_t4yJcXht1E12iGFg700a7l0f.json'}

exec(code, env_args)
