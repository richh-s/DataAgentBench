code = """import json, re
# load UC-assigned records
path_uc = var_call_AMrDYDRyAiDk5vRxmCAz6wcC
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)
# build set of UC publication numbers by parsing Patents_info and also maybe extracting publication numbers from records? But uc_records likely include citation and cpc; we want publication numbers of these UC patents. Try to extract any token like XX-... as before
pub_pat = re.compile(r'\b([A-Z]{2}-[0-9A-Za-z-]+)\b')
uc_pubnums = set()
for rec in uc_records:
    pi = rec.get('Patents_info','')
    for m in pub_pat.finditer(pi):
        tok = m.group(1)
        # heuristics: include if has digits
        if any(c.isdigit() for c in tok):
            uc_pubnums.add(tok)
# Also check if publication numbers appear elsewhere such as citation list of same records? but uc_pubnums should suffice

# load all records with citations
path_allcit = var_call_W5rgnwjwlnuucJOnL4ymHVEj
with open(path_allcit, 'r', encoding='utf-8') as f:
    all_cit_records = json.load(f)

# helper to extract cited publication numbers from citation field

def parse_citation_field(cit_str):
    if not cit_str:
        return []
    try:
        arr = json.loads(cit_str)
    except Exception:
        # try to fix single quotes
        try:
            arr = json.loads(cit_str.replace("'", '"'))
        except Exception:
            return []
    pubs = []
    for item in arr:
        if isinstance(item, dict):
            pn = item.get('publication_number') or item.get('publicationNumber') or ''
            if pn:
                pubs.append(pn)
    return pubs

# helper to extract assignee from Patents_info
assignee_patterns = [r'^(.*?)\s+(?:holds the|holds|owns|is owned by|is assigned to|assigned to|has been assigned to|is held by)\b',
                     r'^(?:In\s+[A-Z]{2},\s+)?the\s+(?:patent|application)\s+(?:no\.|number)?\s*[A-Z0-9-]+\s+is\s+(?:owned|assigned)\s+to\s+(.*?)\b',
                     r'^(.*?)\s+has the',
                     r'^(.*?)\s+files?\s+the']

def extract_assignee(pi):
    if not pi:
        return None
    pi = pi.strip()
    for pat in assignee_patterns:
        m = re.search(pat, pi, re.IGNORECASE)
        if m:
            name = m.group(1).strip()
            # clean trailing punctuation
            name = re.sub(r'\s+\(', ' (', name)
            name = name.rstrip(' ,.;')
            # uppercase normalization
            return name
    # fallback: take leading token up to 'holds' or ', ' or ' has '
    m = re.match(r'^(.*?)(?:,| has | holds | owns )', pi, re.IGNORECASE)
    if m:
        return m.group(1).strip().rstrip(' ,.;')
    # if can't extract, return None
    return None

# iterate to find citing records
from collections import defaultdict
assignee_to_codes = defaultdict(set)
for rec in all_cit_records:
    cit_field = rec.get('citation')
    cited = parse_citation_field(cit_field)
    if not cited:
        continue
    # check intersection
    if any(c in uc_pubnums for c in cited):
        # this record cites a UC patent
        pi = rec.get('Patents_info','')
        assignee = extract_assignee(pi)
        if not assignee:
            assignee = 'UNKNOWN'
        # exclude UNIV CALIFORNIA itself
        if re.search(r'UNIV\s+CALIFORNIA', assignee, re.IGNORECASE):
            continue
        # parse cpc field to get primary codes
        cpc_field = rec.get('cpc') or '[]'
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            try:
                cpcs = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                cpcs = []
        primary_codes = []
        for entry in cpcs:
            if isinstance(entry, dict) and entry.get('first'):
                code = entry.get('code')
                if code:
                    primary_codes.append(code)
        if not primary_codes and cpcs:
            # fallback: take first code
            entry = cpcs[0]
            if isinstance(entry, dict):
                code = entry.get('code')
                if code:
                    primary_codes.append(code)
        for code in primary_codes:
            assignee_to_codes[assignee].add(code)

# prepare outputs
assignee_to_codes = {k: sorted(list(v)) for k, v in assignee_to_codes.items()}
all_primary_codes = sorted({code for codes in assignee_to_codes.values() for code in codes})
output = {'assignee_to_codes': assignee_to_codes, 'primary_codes': all_primary_codes}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_WakKrtRs7x6PBnTcp6hvegg1': ['publicationinfo'], 'var_call_qAMMTH6DzqiVvTFW2mhfJi8Q': ['cpc_definition'], 'var_call_AMrDYDRyAiDk5vRxmCAz6wcC': 'file_storage/call_AMrDYDRyAiDk5vRxmCAz6wcC.json', 'var_call_9qbdQ9cSLtDErtaVc0iyJeV7': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_W5rgnwjwlnuucJOnL4ymHVEj': 'file_storage/call_W5rgnwjwlnuucJOnL4ymHVEj.json'}

exec(code, env_args)
