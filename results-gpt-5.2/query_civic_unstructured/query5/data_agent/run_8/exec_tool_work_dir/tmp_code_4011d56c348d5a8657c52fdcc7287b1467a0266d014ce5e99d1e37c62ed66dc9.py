code = """import json, re
import pandas as pd

def load_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

funding = load_result(var_call_bOOz23WYBvTWRqo0YznHKIHe)
docs = load_result(var_call_lErE1gjrVmu0A0NLFQ7uSw3P)

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype('int64')

# Heuristic extraction: parse agenda-style "Project Schedule" blocks and keep those under Disaster Recovery Projects
# We'll scan each doc for a section labeled "Disaster" and then look for project-name lines followed by schedule lines.

def extract_disaster_projects_started_2022(text):
    results = []
    if not text:
        return results
    # Normalize
    t = text
    # Find disaster sections
    # Capture from "Disaster" header to next major header (e.g., "Capital" or end)
    for m in re.finditer(r"Disaster\s+Recovery\s+Projects(?:\s*\([^\)]*\))?\s*(?:\n|\r\n)+(?P<body>.*?)(?=\n\s*Capital\s+Improvement\s+Projects|\Z)", t, flags=re.IGNORECASE|re.DOTALL):
        body = m.group('body')
        # Split into blocks by double newlines where project name often appears alone
        # We'll detect project name lines: title case, not bullet, length<120
        lines = [ln.strip() for ln in body.splitlines()]
        # Build blocks by detecting likely project name lines
        current_name = None
        current_block = []
        def flush():
            nonlocal current_name, current_block
            if current_name is None:
                return
            block_text = "\n".join(current_block)
            # start criteria: look for "Begin" or "Start" line containing 2022
            started_2022 = False
            # Common patterns: "Begin Construction: Fall 2023"; disaster projects may have "Begin Construction" too
            for ln in current_block:
                if re.search(r"\b(Begin|Start)\b.*\b2022\b", ln, flags=re.IGNORECASE):
                    started_2022 = True
                    break
            if not started_2022:
                # Sometimes schedule is inline "Begin construction: 2022" without Begin/Start keyword; also st may be "2022-".
                if re.search(r"Begin\s+Construction\s*:\s*[^\n]*2022|Start\s*:\s*[^\n]*2022", block_text, flags=re.IGNORECASE):
                    started_2022 = True
                elif re.search(r"\b2022\b-(Spring|Summer|Fall|Winter|\d{2})", block_text, flags=re.IGNORECASE):
                    # if any 2022-season/month appears near word 'Begin' within 80 chars
                    if re.search(r"Begin.{0,80}2022|Start.{0,80}2022", block_text, flags=re.IGNORECASE|re.DOTALL):
                        started_2022 = True
            if started_2022:
                results.append(current_name)
            current_name = None
            current_block = []
        
        for ln in lines:
            if not ln:
                continue
            # identify major subheaders and skip
            if re.match(r"(Design|Construction|Not Started)\b", ln, flags=re.IGNORECASE):
                continue
            # Likely project name: not starting with bullet chars, contains letters, few punctuation
            if (not re.match(r"^[\(\[\u2022\*\-\u2013\u2014]|^\(cid", ln) and
                re.search(r"[A-Za-z]", ln) and
                len(ln) <= 120 and
                not re.search(r"^(Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION)\b", ln, flags=re.IGNORECASE) and
                # names in these reports often don't end with ':'
                not ln.endswith(':') and
                # avoid page/footer
                not re.search(r"^Page\s+\d+\s+of\s+\d+", ln, flags=re.IGNORECASE) and
                # avoid agenda item markers
                not re.search(r"Agenda Item", ln, flags=re.IGNORECASE)
               ):
                # treat as new project name if we already have one and next lines contain updates/schedule
                # But avoid ordinary sentences.
                if ln[0].isupper() and (current_name is None or len(current_block)>0):
                    # flush previous
                    flush()
                    current_name = ln
                    current_block = []
                    continue
            if current_name is not None:
                current_block.append(ln)
        flush()
    return results

started_2022_projects = set()
for d in docs:
    started_2022_projects.update(extract_disaster_projects_started_2022(d.get('text','')))

# Additional heuristic: project names that include FEMA/CalOES/CalJPIA and have start in 2022 somewhere in doc
# We'll look for lines like "Begin Construction: 2022" within 5 lines of a line containing (FEMA|CalOES|CalJPIA)
for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r"\((?:FEMA|CalOES|CalJPIA)[^\)]*\)", ln):
            window = "\n".join(lines[i:i+8])
            if re.search(r"\b(Begin|Start)\b.*\b2022\b", window, flags=re.IGNORECASE):
                started_2022_projects.add(ln)

# Join funding
started_list = sorted(started_2022_projects)
sel = fund_df[fund_df['Project_Name'].isin(started_list)]

total = int(sel['total_amount'].sum())

out = {
    "total_funding_usd": total,
    "matched_projects_count": int(sel['Project_Name'].nunique()),
    "matched_projects": sel.sort_values('total_amount', ascending=False)[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bOOz23WYBvTWRqo0YznHKIHe': 'file_storage/call_bOOz23WYBvTWRqo0YznHKIHe.json', 'var_call_lErE1gjrVmu0A0NLFQ7uSw3P': 'file_storage/call_lErE1gjrVmu0A0NLFQ7uSw3P.json'}

exec(code, env_args)
