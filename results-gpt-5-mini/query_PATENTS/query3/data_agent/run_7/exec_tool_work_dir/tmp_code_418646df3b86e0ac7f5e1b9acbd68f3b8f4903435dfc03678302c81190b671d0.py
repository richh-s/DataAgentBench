code = """import json, re
path_uc = var_call_AMrDYDRyAiDk5vRxmCAz6wcC
path_all = var_call_W5rgnwjwlnuucJOnL4ymHVEj
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)
with open(path_all, 'r', encoding='utf-8') as f:
    all_records = json.load(f)

# extract UC publication numbers more carefully from Patents_info
pubs = set()
for rec in uc_records:
    pi = rec.get('Patents_info','')
    # look for patterns like 'pub. number XXX' or 'publication number XXX' or 'with pub. number XXX' or 'with publication number XXX' or trailing 'with publication number XXX.'
    m = re.search(r'pub(?:lication)?\.?(?:\s*number|\.|no\.|\s*)\s*([A-Z]{2}-[0-9A-Za-z-]+)', pi, re.IGNORECASE)
    if m:
        pubs.add(m.group(1))
    # fallback: any token like XX-123... in pi
    for m2 in re.finditer(r'\b([A-Z]{2}-[0-9A-Za-z-]+)\b', pi):
        tok = m2.group(1)
        if any(ch.isdigit() for ch in tok):
            pubs.add(tok)
# also include possible variants: remove hyphens
pubs = sorted(pubs)
# prepare variants map
variants = {}
for p in pubs:
    key = p
    v = set()
    v.add(p)
    v.add(p.replace('-', ''))
    # add just digits
    digits = re.sub(r'[^0-9]', '', p)
    if digits:
        v.add(digits)
    # add without country prefix
    no_pref = re.sub(r'^[A-Z]{2}-', '', p)
    v.add(no_pref)
    variants[key] = v

# search citations
citing_rowids = set()
rowid_to_rec = {rec.get('rowid'): rec for rec in all_records}
for rec in all_records:
    cit = rec.get('citation') or ''
    if not cit:
        continue
    cit_lower = cit.lower()
    for p, vs in variants.items():
        for variant in vs:
            if not variant:
                continue
            if variant.lower() in cit_lower:
                # found match
                citing_rowids.add(rec.get('rowid'))
                break
        # continue to next pub

# collect assignees and primary CPC codes from these citing rows
assignee_codes = {}
import collections

def extract_assignee(pi):
    if not pi:
        return None
    pi = pi.strip()
    # common formats: 'XYZ holds the US patent application...' or 'In US, the application ... is owned by XYZ and has pub. number ...'
    # try 'holds the' pattern
    m = re.match(r'^(.*?)\s+(?:holds the|holds|owns|is owned by|is assigned to|assigned to|is held by|is belonging to|belonging to)\b', pi, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(' ,.;')
    # try 'The XYZ holds the' or 'XYZ holds the'
    m = re.search(r'([A-Z0-9 \.&,-]{2,}?)\s+(?:holds the|is owned by|owned by|is assigned to)\b', pi, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(' ,.;')
    # fallback: leading token before 'has' or 'with'
    m = re.match(r'^(.*?)(?:,| has | with |\s+holds )', pi)
    if m:
        return m.group(1).strip().rstrip(' ,.;')
    return pi[:50]

for rid in citing_rowids:
    rec = rowid_to_rec.get(rid)
    if not rec:
        continue
    assg = extract_assignee(rec.get('Patents_info','')) or 'UNKNOWN'
    # exclude UNIV CALIFORNIA
    if re.search(r'UNIV\s+CALIFORNIA', assg, re.IGNORECASE):
        continue
    # parse cpc
    cpc_field = rec.get('cpc') or '[]'
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpcs = []
    primary = []
    for entry in cpcs:
        if isinstance(entry, dict) and entry.get('first'):
            code = entry.get('code')
            if code:
                primary.append(code)
    if not primary and cpcs:
        e = cpcs[0]
        if isinstance(e, dict) and e.get('code'):
            primary.append(e.get('code'))
    if not primary:
        continue
    if assg not in assignee_codes:
        assignee_codes[assg] = set()
    for code in primary:
        assignee_codes[assg].add(code)

# prepare result
assignee_codes = {k: sorted(list(v)) for k, v in assignee_codes.items()}
all_codes = sorted({c for codes in assignee_codes.values() for c in codes})
output = {'assignee_to_codes': assignee_codes, 'codes': all_codes, 'num_citing_records': len(citing_rowids)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_WakKrtRs7x6PBnTcp6hvegg1': ['publicationinfo'], 'var_call_qAMMTH6DzqiVvTFW2mhfJi8Q': ['cpc_definition'], 'var_call_AMrDYDRyAiDk5vRxmCAz6wcC': 'file_storage/call_AMrDYDRyAiDk5vRxmCAz6wcC.json', 'var_call_9qbdQ9cSLtDErtaVc0iyJeV7': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_W5rgnwjwlnuucJOnL4ymHVEj': 'file_storage/call_W5rgnwjwlnuucJOnL4ymHVEj.json', 'var_call_hiEDx97eI0s2OuNCnssd6gsu': {'assignee_to_codes': {}, 'primary_codes': []}, 'var_call_qhqjvnptplNNQHPt4QBm4Khj': {'uc_count': 0, 'cited_count': 1142081, 'direct_intersect': [], 'norm_intersect': []}, 'var_call_3kKxCeXOfCQbm5cex0PRFT52': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_auw8NwGKIzv8QrklGOFSgKuW': 'file_storage/call_auw8NwGKIzv8QrklGOFSgKuW.json'}

exec(code, env_args)
