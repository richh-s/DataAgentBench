code = """import json
import re

# Load data from storage file paths
with open(var_call_io7DH7V8PV9mBNOh0zSErnEA, 'r') as f:
    funding = json.load(f)
with open(var_call_vRSdBNV8cMFik2orVNK6f1Na, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding entries
for r in funding:
    # Ensure consistent keys and types
    r['Project_Name'] = r.get('Project_Name','').strip()
    r['Funding_Source'] = r.get('Funding_Source','').strip()
    # Amount may be string, convert to int if possible
    try:
        r['Amount'] = int(r.get('Amount'))
    except:
        try:
            r['Amount'] = int(float(r.get('Amount')))
        except:
            r['Amount'] = None

# Extract civic project names and nearby status for FEMA/emergency-related sections
keywords = ['fema', 'caloes', 'emergency', 'warning', 'sirens']
proj_info = {}  # name -> {'status_text':..., 'status_mapped':...}

for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # Iterate lines and look for keyword occurrences
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in keywords):
            # Backtrack to find a project title (up to 8 lines up)
            title = None
            for j in range(max(0, i-8), i+1)[::-1]:
                cand = lines[j].strip()
                # Skip empty, page headers, and lines starting with '(' or 'Item' or 'Agenda'
                if not cand:
                    continue
                if cand.lower().startswith(('cid:', 'page', 'agenda', 'item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'discussion', 'recommended action')):
                    continue
                # Heuristic: project titles often contain words like 'Project' or 'Repairs' or 'Improvements' or 'Road' or 'Park' or 'Sirens' or 'Storm'
                if re.search(r'project|repairs|improvements|road|park|sirens|storm|drain|retaining|culvert|bridge|walkway|warning|center|facility|repairs|resurfacing', cand, re.I):
                    title = cand
                    break
            if not title:
                # As fallback, take the nearest non-empty previous line
                for j in range(max(0, i-6), i)[::-1]:
                    cand = lines[j].strip()
                    if cand and not cand.startswith('(cid:'):
                        title = cand
                        break
            if not title:
                continue
            # Now extract status by looking forward from title line
            # find the index of title
            try:
                tindex = lines.index(title)
            except ValueError:
                tindex = i
            status_text = ''
            # Look for 'Updates:' token after title
            for k in range(tindex, min(len(lines), tindex+12)):
                if 'updates:' in lines[k].lower():
                    # collect subsequent lines until blank or 'project schedule' or next title-like line
                    collected = []
                    for m in range(k+1, min(len(lines), k+8)):
                        l = lines[m].strip()
                        if not l:
                            break
                        if re.search(r'project schedule|page \d+|agenda item', l, re.I):
                            break
                        collected.append(l)
                    status_text = ' '.join(collected).strip()
                    break
            if not status_text:
                # fallback: take the line containing keyword and a couple neighbors
                context = [lines[i-1].strip() if i-1>=0 else '', lines[i].strip(), lines[i+1].strip() if i+1<len(lines) else '']
                status_text = ' '.join([c for c in context if c])

            # Map to simple status label
            st = status_text.lower()
            status_mapped = 'not started'
            if any(w in st for w in ['complete', 'completed', 'notice of completion', 'complete construction', 'construction was completed']):
                status_mapped = 'completed'
            elif any(w in st for w in ['design', 'plans are', 'final design', 'preliminary design', 'working with the consultant', 'submitted plans', 'awaiting final']):
                # 'awaiting final' could be not started but often relates to approvals in design
                status_mapped = 'design'
            elif any(w in st for w in ['under construction', 'begin construction', 'begin construction:', 'begin construction']):
                status_mapped = 'completed'
            else:
                # default to not started
                status_mapped = 'not started'

            key = title
            # store if new or prefer more detailed status_text
            if key in proj_info:
                # prefer a non-empty status_text and prefer 'design' or 'completed' over 'not started'
                prev = proj_info[key]
                priority = {'completed':3, 'design':2, 'not started':1}
                if status_mapped != prev['status_mapped'] and priority.get(status_mapped,0) > priority.get(prev['status_mapped'],0):
                    proj_info[key] = {'status_text': status_text, 'status_mapped': status_mapped}
            else:
                proj_info[key] = {'status_text': status_text, 'status_mapped': status_mapped}

# Now match funding records to these projects or directly by keywords in funding name
results = []
for r in funding:
    pname = r['Project_Name']
    lowp = pname.lower()
    include = False
    status = 'unknown'
    # If funding project name contains direct keywords
    if any(k in lowp for k in keywords):
        include = True
    # Or if funding name matches any extracted civic project name by substring
    match_found = None
    for civ_name, info in proj_info.items():
        lowc = civ_name.lower()
        if lowc in lowp or lowp in lowc:
            include = True
            match_found = civ_name
            status = info['status_mapped']
            break
    # Also include cases where funding name shares primary words with civic names (loose match)
    if not include:
        for civ_name, info in proj_info.items():
            civ_words = re.sub(r'[^a-z0-9 ]',' ', civ_name.lower()).split()
            if not civ_words:
                continue
            # check if at least two significant words overlap
            overlap = sum(1 for w in civ_words if w in lowp and len(w)>3)
            if overlap >= 2:
                include = True
                match_found = civ_name
                status = info['status_mapped']
                break
    if include:
        if status == 'unknown' and match_found is None:
            # try to infer status from civic docs by searching for a likely project title within documents
            # For example, Outdoor Warning Sirens should match Outdoor Warning Signs
            for civ_name, info in proj_info.items():
                if civ_name.lower().split()[0] in lowp:
                    status = info['status_mapped']
                    match_found = civ_name
                    break
        results.append({
            'Project_Name': pname,
            'Funding_Source': r.get('Funding_Source'),
            'Amount': r.get('Amount'),
            'Status': status
        })

# Deduplicate by Project_Name (keep first)
seen = set()
uniq_results = []
for rec in results:
    if rec['Project_Name'] not in seen:
        uniq_results.append(rec)
        seen.add(rec['Project_Name'])

# Sort by Project_Name
uniq_results = sorted(uniq_results, key=lambda x: x['Project_Name'].lower())

output = uniq_results

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_io7DH7V8PV9mBNOh0zSErnEA': 'file_storage/call_io7DH7V8PV9mBNOh0zSErnEA.json', 'var_call_vRSdBNV8cMFik2orVNK6f1Na': 'file_storage/call_vRSdBNV8cMFik2orVNK6f1Na.json'}

exec(code, env_args)
