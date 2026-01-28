code = """import json, re, os
from pathlib import Path

# Load tool results from storage variables
with open(var_call_oDWHmWe0M0DmfgCA82RsPJIG, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_3DDaxrLDAz4I4zXgAIqWcxmL, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Normalize funding entries to list of dicts
funding_records = funding

# Prepare helper functions
def find_status_in_text(text, idx):
    # Search backward for known section headers within a reasonable window
    headers = [
        (re.compile(r'Capital Improvement Projects \(Design\)', re.I), 'design'),
        (re.compile(r'Capital Improvement Projects \(Construction\)', re.I), 'completed'),
        (re.compile(r'Capital Improvement Projects \(Not Started\)', re.I), 'not started'),
        (re.compile(r'Capital Improvement Projects \(Design\)', re.I), 'design'),
        (re.compile(r'Disaster Recovery Projects', re.I), 'design'),
        (re.compile(r'Capital Improvement Projects', re.I), 'design')
    ]
    search_area_start = max(0, idx-2000)
    prefix = text[search_area_start:idx]
    # find the last header occurrence and return mapped status
    last_pos = -1
    last_status = None
    for pat, status in headers:
        m = list(pat.finditer(prefix))
        if m:
            if m[-1].start() > last_pos:
                last_pos = m[-1].start()
                last_status = status
    if last_status:
        return last_status
    # fallback heuristics nearby
    window = text[max(0, idx-500): idx+500].lower()
    if 'complete design' in window or 'preliminary design' in window or 'in the design' in window or 'design phase' in window:
        return 'design'
    if 'construction was completed' in window or 'complete construction' in window or 'begin construction' in window or 'under construction' in window or 'begin construction' in window:
        return 'completed'
    if 'not started' in window or 'not begun' in window:
        return 'not started'
    return 'unknown'

# Identify funding records related to FEMA or emergency
related = []
for rec in funding_records:
    pname = rec.get('Project_Name','')
    pname_low = pname.lower()
    related_flag = False
    reason = ''
    # If project name itself contains 'fema' or 'emergency'
    if 'fema' in pname_low or 'emergency' in pname_low:
        related_flag = True
        reason = 'name_contains'
    # Or project name contains 'outdoor warning' (emergency warning)
    if not related_flag and 'outdoor warning' in pname_low:
        related_flag = True
        reason = 'name_contains'
    # Otherwise, search in civic docs for mentions of project name near 'fema' or 'emergency'
    if not related_flag:
        for d in docs:
            text = d.get('text','')
            # find occurrences of project name (use a simplified key: remove parentheticals and extra whitespace)
            base = re.sub(r"\(.*?\)", "", pname)
            base = re.sub(r"[^a-zA-Z0-9\s\-&]", "", base).strip()
            if not base:
                continue
            # search case-insensitive
            for m in re.finditer(re.escape(base), text, flags=re.I):
                idx = m.start()
                window = text[max(0, idx-200): idx+200].lower()
                if 'fema' in window or 'caloes' in window or 'cal o es' in window or 'emergency' in window or 'outdoor warning' in window:
                    related_flag = True
                    reason = 'context_match'
                    break
            if related_flag:
                break
    if related_flag:
        # determine status by locating the project occurrence in docs
        status = 'unknown'
        found = False
        for d in docs:
            text = d.get('text','')
            base = re.sub(r"\(.*?\)", "", pname)
            base = re.sub(r"[^a-zA-Z0-9\s\-&]", "", base).strip()
            if not base:
                continue
            m = re.search(re.escape(base), text, flags=re.I)
            if m:
                idx = m.start()
                status = find_status_in_text(text, idx)
                found = True
                break
        # If not found by exact base, try searching by shorter key tokens (first 4 words)
        if not found:
            tokens = pname.split()
            key = ' '.join(tokens[:4]) if len(tokens)>=4 else pname
            key = re.sub(r"[^a-zA-Z0-9\s]", "", key).strip()
            for d in docs:
                text = d.get('text','')
                m = re.search(re.escape(key), text, flags=re.I)
                if m:
                    idx = m.start()
                    status = find_status_in_text(text, idx)
                    found = True
                    break
        out = {
            'Project_Name': rec.get('Project_Name'),
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': int(rec.get('Amount')) if rec.get('Amount') not in (None, '') else None,
            'Status': status,
            'Match_Reason': reason
        }
        related.append(out)

# Remove duplicates (same project_name + funding source + amount)
uniq = []
seen = set()
for r in related:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'])
    if key not in seen:
        seen.add(key)
        uniq.append(r)

import json
result_json = json.dumps(uniq)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_3DDaxrLDAz4I4zXgAIqWcxmL': 'file_storage/call_3DDaxrLDAz4I4zXgAIqWcxmL.json', 'var_call_vq2b2a25Jc8iJUtp8pZJzMKb': ['Funding'], 'var_call_oDWHmWe0M0DmfgCA82RsPJIG': 'file_storage/call_oDWHmWe0M0DmfgCA82RsPJIG.json'}

exec(code, env_args)
