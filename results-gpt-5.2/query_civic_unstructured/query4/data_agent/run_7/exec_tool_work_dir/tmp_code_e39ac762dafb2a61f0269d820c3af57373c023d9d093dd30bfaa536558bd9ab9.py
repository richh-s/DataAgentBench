code = """import json, re

path_docs = var_call_OG5mKrxRUa6HzkclVyHwauDM
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

spring_started = set()

# Patterns indicating start in Spring 2022
pats = [
    re.compile(r"\bStart(?:\s+Date)?\s*:\s*Spring\s+2022\b", re.IGNORECASE),
    re.compile(r"\bStarted\s*:\s*Spring\s+2022\b", re.IGNORECASE),
    re.compile(r"\bBegin\s+Construction\s*:\s*Spring\s+2022\b", re.IGNORECASE),
    re.compile(r"\bBegin\s+Design\s*:\s*Spring\s+2022\b", re.IGNORECASE),
]

# Project name line must be a plausible title (letters/digits/&/()- and length)
name_ok = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ,&/\-\(\)\.]{4,120}$")
# Lines to ignore
ignore = re.compile(r"^(page\s+\d+|agenda item|recommended action|discussion|project schedule|estimated schedule|project description|project updates|updates)\b", re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    if not text or ('Spring 2022' not in text and 'spring 2022' not in text):
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not any(p.search(ln) for p in pats):
            continue
        # backtrack to find a plausible project title, stopping if hit a blank line after some distance
        proj = None
        for j in range(i-1, max(-1, i-40), -1):
            cand = lines[j].strip()
            if cand == '' or cand.startswith('(cid'):
                continue
            if ignore.search(cand):
                continue
            if re.search(r":\s*(spring|summer|fall|winter)\s+\d{4}\b", cand, flags=re.IGNORECASE):
                continue
            if not name_ok.match(cand):
                continue
            # Must contain a keyword like Project, Road, Park, Drain, etc OR be in Title Case with spaces
            if not re.search(r"\b(Project|Road|Park|Storm|Drain|Canyon|PCH|Bridge|Culvert|Warning|Signals|Facility|Water|Sidewalk|Walkway|Slope|Guardrail|Skate)\b", cand):
                continue
            proj = cand
            break
        if proj:
            spring_started.add(proj)

print('__RESULT__:')
print(json.dumps(sorted(spring_started)))"""

env_args = {'var_call_OG5mKrxRUa6HzkclVyHwauDM': 'file_storage/call_OG5mKrxRUa6HzkclVyHwauDM.json', 'var_call_GSCrnvURhXDKm8mhIi6Lg1L6': 'file_storage/call_GSCrnvURhXDKm8mhIi6Lg1L6.json', 'var_call_Q0b1hUX4FlHaWWzXcAsupB2o': {'projects_started_spring_2022_count': 14, 'total_funding_usd': 87000, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'projects_missing_funding_match': ['Fire.', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}}

exec(code, env_args)
