code = """import json, re
# Load the Mongo query result from the provided storage file path
with open(var_call_6R96YFFd222Rz7kGsLojDnBk, 'r', encoding='utf-8') as f:
    docs = json.load(f)

found_projects = []

section_headers_patterns = [r"Capital Improvement Projects \(Design\)",
                            r"Capital Improvement Projects \(Construction\)",
                            r"Capital Improvement Projects \(Not Started\)",
                            r"Disaster Recovery Projects", r"Disaster Recovery Projects Status"]

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    # identify indices where a line contains 'Updates:' which often follows a project heading
    headings = []
    for i, line in enumerate(lines):
        if 'Updates:' in line or 'Project Description:' in line or 'Project Description' in line or 'Project Schedule:' in line:
            # find previous non-empty line as heading
            j = i-1
            while j >= 0 and (not lines[j].strip() or lines[j].strip().lower().startswith('(cid:')):
                j -= 1
            if j >= 0:
                heading = lines[j].strip()
                # clean heading
                heading = re.sub(r"\s+", " ", heading)
                headings.append((j, heading))
    # also find explicit 'Project' title lines
    for i, line in enumerate(lines):
        if line.strip().endswith('Project') or 'Project' in line and len(line.strip())<120 and line.strip()[0].isupper():
            heading = line.strip()
            headings.append((i, heading))
    # deduplicate headings by position
    headings = sorted({(pos, h) for pos,h in headings}, key=lambda x: x[0])

    # for each occurrence of 'fema' or 'emergency' find nearest heading above
    lowers = text.lower()
    matches = []
    for m in re.finditer(r'fema|emergency', lowers):
        pos = m.start()
        # find heading with largest position < pos
        chosen = None
        for hp, hh in headings:
            # convert heading line index to char position approx by joining lines up to hp
            charpos = sum(len(l)+1 for l in lines[:hp])
            if charpos <= pos:
                chosen = (charpos, hh)
            else:
                break
        if chosen:
            matches.append(chosen[1])
    # also check windows around each heading for keywords
    for hp, hh in headings:
        charpos = sum(len(l)+1 for l in lines[:hp])
        window_start = max(0, charpos-300)
        window_end = min(len(text), charpos+500)
        window = text[window_start:window_end].lower()
        if 'fema' in window or 'emergency' in window:
            matches.append(hh)
    # also include any heading lines that themselves contain those keywords
    for hp, hh in headings:
        if 'fema' in hh.lower() or 'emergency' in hh.lower():
            matches.append(hh)

    # normalize and collect unique project names
    for name in set(matches):
        clean = name.strip(':').strip()
        # attempt to extract a simple project name (remove leading numbers or bullets)
        clean = re.sub(r'^[0-9\.\-\)\s]+', '', clean)
        found_projects.append({'Project_Name': clean, 'filename': doc.get('filename')})

# deduplicate across docs by Project_Name
unique = {}
for p in found_projects:
    name = p['Project_Name']
    if name not in unique:
        unique[name] = p

# Determine status for each unique project by searching the doc text near the heading
results = []
for name, info in unique.items():
    # find the text snippet that contains the project name
    status = None
    for doc in docs:
        text = doc.get('text','')
        idx = text.lower().find(name.lower())
        if idx!=-1:
            # look for section headers above
            lines = text.splitlines()
            # find line index of occurrence
            char_count = 0
            line_idx = 0
            for li, l in enumerate(lines):
                char_count += len(l)+1
                if char_count > idx:
                    line_idx = li
                    break
            # search up to 20 lines above for section header
            section = None
            for k in range(max(0,line_idx-20), line_idx+1):
                for pat in section_headers_patterns:
                    if re.search(pat, lines[k], re.IGNORECASE):
                        section = lines[k]
                        break
                if section:
                    break
            # search nearby text for explicit status phrases
            window = text[max(0, idx-400): idx+400].lower()
            if any(x in window for x in ['complete design','final design','estimated schedule','preliminary design','design will']):
                status = 'design'
            if any(x in window for x in ['construction was completed','complete construction','notice of completion','completed,']):
                status = 'completed'
            if any(x in window for x in ['project is in the preliminary design phase','project is in the preliminary design','project is in the preliminary']):
                status = 'design'
            if any(x in window for x in ['begin construction','begin construction:','on the project start','currently under construction']):
                # prefer 'design' if not completed; map 'currently under construction' to 'design' is not ideal but use 'design'
                if status is None:
                    status = 'design'
            if section:
                if 'design' in section.lower():
                    status = 'design'
                elif 'construction' in section.lower():
                    # map construction section to 'completed' if not otherwise set
                    if status is None:
                        status = 'completed'
                elif 'not started' in section.lower():
                    status = 'not started'
            if status is None:
                # fallback: look for keywords emergency/fema context maybe indicates disaster -> not started or design
                if 'fema' in window or 'emergency' in window:
                    status = 'design'
            results.append({'Project_Name': name, 'Status': status})
            break

# final unique results
final = []
for r in results:
    final.append({'Project_Name': r['Project_Name'], 'Status': r['Status']})

import json
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_6R96YFFd222Rz7kGsLojDnBk': 'file_storage/call_6R96YFFd222Rz7kGsLojDnBk.json'}

exec(code, env_args)
