code = """import re
import json
import pandas as pd

docs = var_call_Y6KliHUVetrVzq4id2vRDGuk
fund_rows = var_call_GXwgmB9PEiwyXVvvgDY0YcyO

fund_df = pd.DataFrame(fund_rows)
if fund_df.empty:
    fund_df = pd.DataFrame(columns=['Funding_ID','Project_Name','Funding_Source','Amount'])

# helper
month_keywords = ['march','april','may','spring']

extracted = []

for doc in docs:
    text = doc.get('text','')
    if not isinstance(text,str):
        continue
    # Normalize newlines
    t = text
    # Try to find explicit project blocks using 'Project_Name' or 'Project Name' or 'Project:'
    # Split by occurrences of common project headers
    parts = re.split(r'(?:Project[_ ]Name|Project Name|Project:)\s*', t, flags=re.IGNORECASE)
    # The first part is preamble
    for part in parts[1:]:
        # part likely starts with the project name then other fields
        # Extract first line as potential project name
        m_name = re.match(r"\s*[:\-\"]?\s*([A-Za-z0-9\(\)\-\.,'& ]{3,100})", part)
        if m_name:
            pname = m_name.group(1).strip()
        else:
            # fallback: take up to newline
            pname = part.split('\n',1)[0].strip()
        # Search within the next 400 chars for st or start patterns
        nxt = part[:400]
        m_st = re.search(r"\b(?:st|start(?: date)?|start_time|start:)\s*[:\-]?\s*([A-Za-z0-9\-/ ]{3,40})", nxt, flags=re.IGNORECASE)
        st_val = None
        if m_st:
            st_val = m_st.group(1).strip()
        else:
            # try to find season or month mentions near this block
            m_season = re.search(r"(Spring|March|April|May)\s*[,\s]*2022|2022\s*[-/]?\s*(Spring|March|April|May)|2022-(?:Spring|03|04|05)", nxt, flags=re.IGNORECASE)
            if m_season:
                st_val = m_season.group(0).strip()
        extracted.append({'Project_Name': pname, 'st': st_val, 'source_file': doc.get('filename')})

# Also attempt to find date mentions in whole text and link to nearest project-like phrase before them
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r"(2022[-/ ]?(?:Spring|03|04|05)|\b(?:March|April|May)\s*2022|Spring\s*2022)", text, flags=re.IGNORECASE):
        st_val = m.group(0)
        # look back up to 200 chars for a project name marker
        start_idx = max(0, m.start()-200)
        snippet = text[start_idx:m.start()]
        # try to find last occurrence of 'Project' or 'Project Name'
        mm = re.search(r"(?:Project[_ ]Name|Project Name|Project:)\s*([A-Za-z0-9\(\)\-\.,'& ]{3,100})$", snippet, flags=re.IGNORECASE)
        if mm:
            pname = mm.group(1).strip()
        else:
            # fallback: take last line
            lines = snippet.strip().splitlines()
            if lines:
                pname = lines[-1].strip()
            else:
                pname = None
        if pname:
            extracted.append({'Project_Name': pname, 'st': st_val, 'source_file': doc.get('filename')})

# Clean extracted entries
cleaned = []
for e in extracted:
    pname = e.get('Project_Name')
    if not pname:
        continue
    # cleanup punctuation
    pname = re.sub(r"\s+", " ", pname).strip(' :\n\t\r\"')
    st = e.get('st') or ''
    st = st.strip()
    cleaned.append({'Project_Name': pname, 'st': st, 'source_file': e.get('source_file')})

# Deduplicate by Project_Name and st
unique = {}
for e in cleaned:
    key = (e['Project_Name'].lower(), e['st'].lower())
    if key not in unique:
        unique[key] = e

projects = list(unique.values())

# Filter projects that started in Spring 2022
def is_spring_2022(s):
    if not s:
        return False
    s_low = s.lower()
    if '2022' in s_low and 'spring' in s_low:
        return True
    # months
    for mon in ['march','april','may']:
        if mon in s_low and '2022' in s_low:
            return True
    # date patterns like 2022-03, 2022-04, 2022-05 or 2022-03-xx
    if re.search(r"2022[-/]0?3|2022[-/]0?4|2022[-/]0?5|2022-(?:03|04|05)", s_low):
        return True
    return False

spring_projects = [p for p in projects if is_spring_2022(p.get('st',''))]

# If none found using st field, try finding any project blocks mentioning 'Spring 2022' near them
if not spring_projects:
    for e in projects:
        # search in source file text for project name and spring mention
        fname = e.get('source_file')
        doc = next((d for d in docs if d.get('filename')==fname), None)
        if not doc:
            continue
        text = doc.get('text','')
        # find occurrences of project name then see if within 200 chars there's spring 2022
        for m in re.finditer(re.escape(e['Project_Name']), text, flags=re.IGNORECASE):
            window = text[max(0,m.start()-200):m.end()+200]
            if re.search(r"(Spring\s*2022|March\s*2022|April\s*2022|May\s*2022|2022[-/ ]?(?:Spring|03|04|05))", window, flags=re.IGNORECASE):
                spring_projects.append(e)
                break

# Deduplicate project names
seen = {}
final_projects = []
for p in spring_projects:
    name = p['Project_Name'].strip()
    if name.lower() not in seen:
        seen[name.lower()] = True
        final_projects.append(name)

# Join with funding
results = []
for name in final_projects:
    # match funding rows where Project_Name equals (case-insensitive)
    matches = fund_df[fund_df['Project_Name'].astype(str).str.lower()==name.lower()]
    total = int(matches['Amount'].sum()) if not matches.empty else 0
    rows = matches.to_dict(orient='records')
    results.append({'Project_Name': name, 'Funding': total, 'Funding_Records': rows})

count = len(final_projects)
total_funding = sum(r['Funding'] for r in results)

out = {'count': count, 'total_funding': total_funding, 'projects': results}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Y6KliHUVetrVzq4id2vRDGuk': ['civic_docs'], 'var_call_GXwgmB9PEiwyXVvvgDY0YcyO': ['Funding']}

exec(code, env_args)
