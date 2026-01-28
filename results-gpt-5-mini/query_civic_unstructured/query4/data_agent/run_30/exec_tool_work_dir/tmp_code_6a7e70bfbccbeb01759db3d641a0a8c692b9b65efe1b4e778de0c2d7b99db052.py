code = """import json, re

with open(var_call_VRJfQzwEvGj1nReSJtvXQEzi, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_RVk0cVgnA6ObHRufRtLeY0mk, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Build normalized funding map: normalized_name -> list of (original_name, amount)
import unicodedata

def normalize(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFKD', s)
    s = s.lower()
    # remove parenthetical content
    s = re.sub(r"\(.*?\)", "", s)
    # remove punctuation
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

funding_map = {}
for r in funding_rows:
    orig = r.get('Project_Name','').strip()
    amt = r.get('Total_Amount', 0)
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    norm = normalize(orig)
    if norm in funding_map:
        funding_map[norm].append((orig, amt_int))
    else:
        funding_map[norm] = [(orig, amt_int)]

# find lines indicating Spring 2022
pattern = re.compile(r"spring(?:\s+of)?\s*,?\s*2022|spring\s*2022|spring\s*'22", re.IGNORECASE)
exclude_phrases = ['updates', 'project schedule', 'project description', 'agenda', 'item', 'page', 'meeting', 'subject', 'recommended action', 'discussion', 'estimated schedule', 'project updates', 'project schedule:', 'project schedule']

candidates = []

for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if pattern.search(line):
            # search backwards up to 10 lines for a likely title
            title = None
            for j in range(idx-1, max(-1, idx-12), -1):
                if j < 0:
                    break
                cand = lines[j].strip()
                if not cand:
                    continue
                low = cand.lower()
                if any(p in low for p in exclude_phrases):
                    continue
                if cand.endswith(':'):
                    continue
                if cand.startswith('(') or cand.startswith('cid'):
                    continue
                # avoid short words
                if len(cand) < 5:
                    continue
                # avoid lines that are mostly sentences
                # prefer lines with Title Case or containing keywords
                keywords = ['park','road','drain','storm','improv','repair','project','median','playground','water','skate','trail','slope','retaining','signal','walkway','culvert','bridge','drainage','maintenance']
                if any(k in low for k in keywords) or cand.istitle() or 'Project' in cand or 'project' in cand:
                    title = cand
                    break
            if title:
                candidates.append(title)

# unique preserving order
seen = set()
uniq = []
for t in candidates:
    if t not in seen:
        seen.add(t)
        uniq.append(t)

# Match to funding using normalized substring matching
matched = []
unmatched = []
for t in uniq:
    norm_t = normalize(t)
    found = False
    # exact norm match
    if norm_t in funding_map:
        entries = funding_map[norm_t]
        # sum amounts for entries
        amt = sum(a for (_,a) in entries)
        matched.append({'doc_title': t, 'funding_name': funding_map[norm_t][0][0], 'amount': amt})
        found = True
    else:
        # search for funding keys that contain norm_t or vice versa
        for fk, entries in funding_map.items():
            if norm_t and (norm_t in fk or fk in norm_t):
                amt = sum(a for (_,a) in entries)
                matched.append({'doc_title': t, 'funding_name': entries[0][0], 'amount': amt})
                found = True
                break
    if not found:
        unmatched.append({'doc_title': t, 'amount': 0})

# compute totals
num_projects = len(uniq)
total_funding = sum(m['amount'] for m in matched)

result = {
    'num_projects_started_spring_2022': num_projects,
    'total_funding': total_funding,
    'matched': matched,
    'unmatched': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_SWdYhnNcnfGhyqygrmZo9Hum': ['civic_docs'], 'var_call_jMjslhGHl4uH9yM8CMklZCNe': ['Funding'], 'var_call_VRJfQzwEvGj1nReSJtvXQEzi': 'file_storage/call_VRJfQzwEvGj1nReSJtvXQEzi.json', 'var_call_RVk0cVgnA6ObHRufRtLeY0mk': 'file_storage/call_RVk0cVgnA6ObHRufRtLeY0mk.json', 'var_call_HxmEgKLx08PnRvZXNslqiuuR': {'num_projects_found_in_docs': 39, 'total_funding_for_those_projects': 87000, 'projects': {'matched': [{'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000}], 'unmatched': [{'Project_Name': 'advertised for construction bids shortly after this date.', 'Amount': 0}, {'Project_Name': 'agreement will be sent to City Council in March.', 'Amount': 0}, {'Project_Name': 'project will begin in conjunction with the PCH Median Improvement', 'Amount': 0}, {'Project_Name': 'to review', 'Amount': 0}, {'Project_Name': 'sending this project out to bid during the Spring of 2022.', 'Amount': 0}, {'Project_Name': 'Commission will then review the project in Spring 2022 before final', 'Amount': 0}, {'Project_Name': 'review by the Council.', 'Amount': 0}, {'Project_Name': 'March 2022', 'Amount': 0}, {'Project_Name': 'is finalizing the bid documents.', 'Amount': 0}, {'Project_Name': 'within the City.', 'Amount': 0}, {'Project_Name': 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'Amount': 0}, {'Project_Name': 'started and is anticipated to be completed by the Spring of 2022.', 'Amount': 0}, {'Project_Name': 'drain towards the end of Clover Heights will help eliminate this issue.', 'Amount': 0}, {'Project_Name': 'that was damaged by the Woolsey Fire.', 'Amount': 0}, {'Project_Name': 'Fire.', 'Amount': 0}, {'Project_Name': 'management services was approved by Council on March 14, 2022.', 'Amount': 0}, {'Project_Name': 'will begin in conjunction with the PCH Median Improvement', 'Amount': 0}, {'Project_Name': 'shade structures at Malibu Bluffs Park.', 'Amount': 0}, {'Project_Name': 'Metro.', 'Amount': 0}, {'Project_Name': 'timber with non-combustible materials.', 'Amount': 0}, {'Project_Name': 'City.', 'Amount': 0}, {'Project_Name': 'beginning in Spring 2022.', 'Amount': 0}, {'Project_Name': 'completed by Spring 2022.', 'Amount': 0}, {'Project_Name': 'of 2022.', 'Amount': 0}, {'Project_Name': 'damaged by the Woolsey Fire.', 'Amount': 0}, {'Project_Name': 'Median Improvement.', 'Amount': 0}, {'Project_Name': 'draft plans are expected to be completed in Spring 2022. The Planning', 'Amount': 0}, {'Project_Name': 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'Amount': 0}, {'Project_Name': 'August.', 'Amount': 0}, {'Project_Name': 'consultants to develop the master plan.', 'Amount': 0}, {'Project_Name': 'to develop the master plan. Proposals are due in September 2021.', 'Amount': 0}, {'Project_Name': 'under review. Staff anticipates completing the selection process next month', 'Amount': 0}, {'Project_Name': 'Caltrans. The project is currently out to bids with bids due December', 'Amount': 0}, {'Project_Name': 'is working on the project plans to prepare for public bidding.', 'Amount': 0}, {'Project_Name': 'the Public Works Commission to revise the project scope.', 'Amount': 0}, {'Project_Name': 'Westward Beach Road.', 'Amount': 0}, {'Project_Name': 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'Amount': 0}]}}}

exec(code, env_args)
