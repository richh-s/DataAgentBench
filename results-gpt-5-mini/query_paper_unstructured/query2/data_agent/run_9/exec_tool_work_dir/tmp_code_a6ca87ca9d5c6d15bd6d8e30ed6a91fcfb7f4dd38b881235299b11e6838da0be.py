code = """import json
import re
import statistics

# Load data from storage-provided file paths
with open(var_call_xc8RpNs4m3VfqJoxH5PSzOPB, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_AvYEiHdcIMMpxDys6ZfKr3LG, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Convert citations to dict keyed by title, ensure citation_count is int
cit_map = {}
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count'))
    except Exception:
        # handle non-int gracefully
        try:
            count = int(float(rec.get('citation_count')))
        except Exception:
            continue
    cit_map[title] = count

# Process papers: extract title (filename without .txt), source detection, year
paper_info = {}
for rec in papers:
    filename = rec.get('filename','')
    text = rec.get('text','') or ''
    if not filename:
        continue
    # derive title matching Citations table: filename without .txt
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # detect source: look for 'ACM' as a standalone or © ACM
    source = None
    if re.search(r'\bACM\b', text, re.IGNORECASE) or re.search(r'\u00a9\s*ACM', text, re.IGNORECASE):
        source = 'ACM'
    elif re.search(r'\bIEEE\b', text, re.IGNORECASE):
        source = 'IEEE'
    elif re.search(r'PubMed', text, re.IGNORECASE):
        source = 'PubMed'
    else:
        # fallback: try to find Copyright line
        m = re.search(r'Copyright\s+\d{4}\s+by\s+([^\n]+)', text, re.IGNORECASE)
        if m:
            src = m.group(1).strip()
            if 'ACM' in src.upper():
                source = 'ACM'
            elif 'IEEE' in src.upper():
                source = 'IEEE'
            else:
                source = src
    # extract first 4-digit year between 1980 and 2025 from the beginning of text
    year = None
    m_all = re.findall(r'\b(19|20)\d{2}\b', text)
    # The above returns only the first two digits due to grouping; better find all full
    m_full = re.findall(r'\b(19\d{2}|20\d{2})\b', text)
    if m_full:
        # choose first within reasonable range
        for ystr in m_full:
            y = int(ystr)
            if 1980 <= y <= 2025:
                year = y
                break
    paper_info[title] = {'source': source, 'year': year}

# Join citations (for 2018) with papers and filter by source == 'ACM'
counts = []
for title, count in cit_map.items():
    info = paper_info.get(title)
    if info and info.get('source') == 'ACM':
        counts.append(count)

if counts:
    avg = sum(counts)/len(counts)
else:
    avg = None

# Print result in required format as JSON-serializable
print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_call_xc8RpNs4m3VfqJoxH5PSzOPB': 'file_storage/call_xc8RpNs4m3VfqJoxH5PSzOPB.json', 'var_call_AvYEiHdcIMMpxDys6ZfKr3LG': 'file_storage/call_AvYEiHdcIMMpxDys6ZfKr3LG.json'}

exec(code, env_args)
