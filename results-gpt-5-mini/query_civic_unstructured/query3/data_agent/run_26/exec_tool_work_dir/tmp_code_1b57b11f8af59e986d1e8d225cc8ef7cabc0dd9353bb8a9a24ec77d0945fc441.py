code = """import json, re

# Load the civic_docs query result from the provided storage file
with open(var_call_YgTnLjoJw69LVcdnv0lyQzQZ, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
seen = set()

# Headers to detect status by section
header_status_map = {
    'capital improvement projects (design)': 'design',
    'capital improvement projects (construction)': 'completed',
    'capital improvement projects (not started)': 'not started',
    'disaster recovery projects': 'design'
}

# Regex to find candidate project titles
title_regex = re.compile(r"^([A-Z][A-Za-z0-9 &'\-/,:.]{4,200}?\b(?:Project|Projects|Repair|Repairs|Improvements|Improvement|Facility|Park|Study|Playground|Walkway|Master Plan|Treatment|Project Description))", re.M)

for doc in docs:
    text = doc.get('text','')
    lower_text = text.lower()
    # find header positions
    header_positions = []
    for h in header_status_map:
        idx = lower_text.find(h)
        if idx!=-1:
            header_positions.append((idx,h))
    header_positions.sort()

    for m in title_regex.finditer(text):
        title = m.group(1).strip()
        start = m.start(1)
        # define block of nearby text to search for keywords
        end = min(len(text), start+800)
        block = text[start:end].lower()
        # check if 'fema' or 'emergency' appears in a window around the title (before or after)
        window_start = max(0, start-400)
        window_end = min(len(text), start+800)
        window = text[window_start:window_end].lower()
        if ('fema' in window) or ('emergency' in window):
            # determine status by looking for nearest header before the title
            status = None
            prior_headers = [hp for hp in header_positions if hp[0] < start]
            if prior_headers:
                # take the last prior header
                status = header_status_map[prior_headers[-1][1]]
            # fallback: infer from nearby block words
            if not status:
                if re.search(r'complete design|final design|preliminary design|design phase|working with the consultant to finalize the design', block):
                    status = 'design'
                elif re.search(r'construction was completed|complete construction|notice of completion|completed|complete construction', block):
                    status = 'completed'
                elif re.search(r'not started|identified|will be identified|will be issuing', block):
                    status = 'not started'
            if not status:
                # default to design if unsure
                status = 'design'

            # deduplicate
            if title not in seen:
                seen.add(title)
                projects.append({'Project_Name': title, 'Status': status})

# As additional check, also search for common suffixes like '(FEMA Project)' directly
extra_regex = re.compile(r"([A-Z][A-Za-z0-9 &'\-/,:.]{4,200}?\(FEMA Project\))")
for doc in docs:
    text = doc.get('text','')
    for m in extra_regex.finditer(text):
        title = m.group(1).strip()
        if title not in seen:
            # try to infer status by searching nearby
            start = m.start(1)
            block = text[start:start+800].lower()
            status = None
            if re.search(r'design', block):
                status = 'design'
            elif re.search(r'complete|completed', block):
                status = 'completed'
            else:
                status = 'design'
            seen.add(title)
            projects.append({'Project_Name': title, 'Status': status})

# Output result as JSON string
print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_YgTnLjoJw69LVcdnv0lyQzQZ': 'file_storage/call_YgTnLjoJw69LVcdnv0lyQzQZ.json'}

exec(code, env_args)
