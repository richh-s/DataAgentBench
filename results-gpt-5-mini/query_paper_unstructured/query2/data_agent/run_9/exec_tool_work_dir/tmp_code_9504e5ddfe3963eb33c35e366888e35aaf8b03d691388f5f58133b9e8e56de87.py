code = """import json

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
    # detect source using simple substring checks on uppercase text
    txt_upper = text.upper()
    source = None
    if 'ACM' in txt_upper:
        source = 'ACM'
    elif 'IEEE' in txt_upper:
        source = 'IEEE'
    elif 'PUBMED' in txt_upper:
        source = 'PubMed'
    # extract first 4-digit year between 1980 and 2025 by scanning
    year = None
    tlen = len(text)
    for i in range(tlen - 3):
        s = text[i:i+4]
        if s.isdigit():
            y = int(s)
            if 1980 <= y <= 2025:
                year = y
                break
    paper_info[title] = {'source': source, 'year': year}

# Join citations (for 2018 data already) with papers and filter by source == 'ACM'
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
