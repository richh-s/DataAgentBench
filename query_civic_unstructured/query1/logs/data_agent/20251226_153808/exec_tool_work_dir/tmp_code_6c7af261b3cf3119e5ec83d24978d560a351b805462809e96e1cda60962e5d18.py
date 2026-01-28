code = """import json, os, re

# Load funding records (> 50000)
funding_path = var_call_qavtXlmiGoW9QnOA78pUlytE
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funded_names = set()
for rec in funding_records:
    name = rec.get('Project_Name')
    if name:
        funded_names.add(name.strip())

# Load civic documents
civic_path = var_call_RZF88M1S8GL1Z6q8kFep6vBb
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Parser to extract Capital Improvement Projects (Design) project names
stop_markers = [
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'disaster recovery projects',
]

header_marker = 'capital improvement projects (design)'

capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text') or ''
    lines = text.split('\n')
    low_lines = [ln.lower() for ln in lines]

    # Find all indices where the design header appears
    start_indices = [i for i, ln in enumerate(low_lines) if header_marker in ln]
    for start_idx in start_indices:
        # Determine end index
        end_idx = len(lines)
        for j in range(start_idx + 1, len(lines)):
            lnj = low_lines[j]
            if header_marker in lnj:
                end_idx = j
                break
            if any(marker in lnj for marker in stop_markers):
                end_idx = j
                break
        # Extract section lines
        section_lines = lines[start_idx+1:end_idx]
        section_low = [ln.lower() for ln in section_lines]

        # Iterate through lines, detect project names based on preceding line to an Updates/Schedule/Description block
        for idx, ln in enumerate(section_lines):
            ln_stripped = ln.strip()
            ln_low = section_low[idx].strip()
            # triggers indicating we've entered a project's detail block
            trigger = ln_low.endswith('updates:') or ln_low == 'updates:' or ln_low == 'project updates:' or ln_low == 'project schedule:' or ln_low == 'estimated schedule:' or 'project schedule' in ln_low
            if trigger:
                # look backwards for the project name line (skip empty and descriptor lines)
                k = idx - 1
                while k >= 0 and (section_lines[k].strip() == '' or section_low[k].strip().startswith('agenda item') or section_low[k].strip().startswith('page ')):
                    k -= 1
                # if the immediate previous is a description line, step back further
                if k >= 0 and (section_low[k].strip().endswith('description:') or 'description:' in section_low[k]):
                    k -= 1
                    while k >= 0 and (section_lines[k].strip() == '' or section_low[k].strip().startswith('agenda item') or section_low[k].strip().startswith('page ')):
                        k -= 1
                if k >= 0:
                    candidate = section_lines[k].strip()
                    # filter out non-name lines
                    if candidate and not candidate.lower().endswith(':') and len(candidate) > 2 and not candidate.lower().startswith(('agenda item', 'page ')):
                        # clean artifacts
                        cand = candidate
                        # remove weird bullet markers like (cid:190) or (cid:131)
                        cand = re.sub(r"\(cid:[^\)]*\)", "", cand).strip()
                        # collapse multiple spaces
                        cand = re.sub(r"\s+", " ", cand)
                        capital_design_projects.add(cand)
        
        # Additionally, capture standalone project titles: lines that are title-like and followed by an Updates/Description within a few lines
        for idx, ln in enumerate(section_lines):
            cand = ln.strip()
            low = cand.lower()
            if not cand:
                continue
            if low.startswith(('agenda item', 'page ')):
                continue
            if low.endswith(':'):
                continue
            # skip typical descriptor starts
            if any(kw in low for kw in ['updates', 'schedule', 'description', 'prepared by', 'approved by', 'subject', 'discussion']):
                continue
            # look ahead a few lines for an updates/description to validate as a project header
            lookahead_window = 5
            found_detail = False
            for kk in range(1, lookahead_window+1):
                if idx+kk >= len(section_lines):
                    break
                ahead = section_lines[idx+kk].strip().lower()
                if ahead.endswith('updates:') or ahead == 'updates:' or ahead == 'project updates:' or ahead.endswith('description:') or 'project schedule' in ahead or 'estimated schedule' in ahead:
                    found_detail = True
                    break
            if found_detail:
                # clean artifacts
                clean = re.sub(r"\(cid:[^\)]*\)", "", cand).strip()
                clean = re.sub(r"\s+", " ", clean)
                capital_design_projects.add(clean)

# Intersect with funded project names
matches = sorted(n for n in capital_design_projects if n in funded_names)
count_matches = len(matches)

# Prepare result
result = {"count": count_matches, "matched_projects": matches}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_emkmzpvum2bkhY3KeP5UYxCb': ['civic_docs'], 'var_call_o7fqj1i1czAOdbOZBSxsmZnL': ['Funding'], 'var_call_qavtXlmiGoW9QnOA78pUlytE': 'file_storage/call_qavtXlmiGoW9QnOA78pUlytE.json', 'var_call_RZF88M1S8GL1Z6q8kFep6vBb': 'file_storage/call_RZF88M1S8GL1Z6q8kFep6vBb.json'}

exec(code, env_args)
