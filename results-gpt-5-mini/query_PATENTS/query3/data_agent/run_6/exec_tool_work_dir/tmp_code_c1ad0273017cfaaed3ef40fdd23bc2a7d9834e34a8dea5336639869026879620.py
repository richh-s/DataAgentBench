code = """import json, re

# Load UC-owned records
path_uc = var_call_PZXE235Z20VYWoM0xEB6t9GU
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)

# Extract publication numbers of UC patents
pub_pattern = re.compile(r"[A-Z]{2,}-[0-9A-Za-z\-]+")
uc_pub_nums = set()
for rec in uc_records:
    pi = rec.get('Patents_info', '')
    for m in pub_pattern.findall(pi):
        if '-' in m and re.search(r"\d", m):
            uc_pub_nums.add(m)

# Load all publication records
path_all = var_call_ZRJZk00dZSVEDVyILIiyhqUB
with open(path_all, 'r', encoding='utf-8') as f:
    all_records = json.load(f)

# Helper to parse citation field safely
def parse_citation(cit_str):
    if not cit_str:
        return []
    try:
        return json.loads(cit_str)
    except Exception:
        # attempt to fix common single quotes
        try:
            return json.loads(cit_str.replace("'", '"'))
        except Exception:
            return []

# Helper to extract assignee name
def extract_assignee(pi):
    if not pi or not isinstance(pi, str):
        return None
    s = pi.strip()
    # Try patterns where assignee is before ' holds '
    for kw in [' holds the ', ' holds ', ' owns the ', ' owns ', ' is represented by ']:
        if kw in s:
            cand = s.split(kw)[0].strip()
            # cand could include country prefix like 'In US, XYZ' -> remove leading 'In [A-Z]{2}, the ' patterns
            cand = re.sub(r'^In [A-Z]{2}, the ', '', cand)
            # remove trailing descriptors like 'the'
            return cand
    # Try patterns where assignee follows ' is assigned to '
    for kw in [' is assigned to ', ' assigned to ', ' is owned by ', ' owned by ', ' held by ', ' held jointly by ']:
        if kw in s:
            right = s.split(kw,1)[1]
            # take up to first conjunction or comma
            m = re.split(r' and | with |,|;|\.', right)[0].strip()
            return m
    # Fallback: look for leading uppercase sequence of words (2+ chars)
    m = re.match(r'^([A-Z0-9&().,\- ]{3,}?) (holds|has|owns|owns|filed|filed by|applies|file)', s)
    if m:
        cand = m.group(1).strip()
        return cand
    # Another fallback: find first all-caps substring of length>3
    caps = re.findall(r'([A-Z][A-Z0-9&()\-\. ]{2,})', s)
    if caps:
        # pick the longest candidate
        cand = max(caps, key=len).strip()
        # discard if contains words like 'patent' or 'application'
        if re.search(r'patent|application|pub\.|publication|ID|ID', cand, re.I):
            # try next candidate
            for c in caps:
                if not re.search(r'patent|application|publication|ID', c, re.I):
                    return c.strip()
            return None
        return cand
    return None

# Process records
assignee_to_codes = {}
for rec in all_records:
    cit_list = parse_citation(rec.get('citation',''))
    cited_uc = False
    for c in cit_list:
        pn = c.get('publication_number','') if isinstance(c, dict) else ''
        if pn in uc_pub_nums:
            cited_uc = True
            break
    if not cited_uc:
        continue
    assignee = extract_assignee(rec.get('Patents_info','')) or 'UNKNOWN'
    # normalize whitespace
    assignee = re.sub(r'\s+', ' ', assignee).strip()
    # extract primary CPC codes
    codes = set()
    cpc_field = rec.get('cpc','')
    try:
        cpc_list = json.loads(cpc_field) if cpc_field else []
    except Exception:
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            cpc_list = []
    for item in cpc_list:
        if isinstance(item, dict):
            if item.get('first'):
                codes.add(item.get('code'))
    # if none marked first, take first code if available
    if not codes and cpc_list:
        for item in cpc_list:
            if isinstance(item, dict) and item.get('code'):
                codes.add(item.get('code'))
                break
    if not codes:
        continue
    if assignee not in assignee_to_codes:
        assignee_to_codes[assignee] = set()
    assignee_to_codes[assignee].update(codes)

# Remove UNIV CALIFORNIA if present
assignee_to_codes = {k: sorted(list(v)) for k,v in assignee_to_codes.items() if 'UNIV CALIFORNIA' not in k.upper()}

# Prepare list of unique codes
all_codes = sorted({code for codes in assignee_to_codes.values() for code in codes if code})

out = {'assignee_to_codes': assignee_to_codes, 'codes': all_codes}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PZXE235Z20VYWoM0xEB6t9GU': 'file_storage/call_PZXE235Z20VYWoM0xEB6t9GU.json', 'var_call_Y5YvAykxUcnXQqc0nMNKB7b3': ['AP-2011005954-A', 'AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A', 'AU-2007297661-A1', 'AU-2008329628-A', 'AU-2008329628-B2', 'AU-2008349842-A', 'AU-2008349842-A1', 'AU-2010214112-A', 'AU-2010214112-B2', 'AU-2015364602-A', 'AU-2015364602-B2', 'AU-2017356943-A', 'AU-2017356943-A1', 'AU-2019275518-A', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5711401-A', 'AU-5938296-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A', 'CA-2220674-A1', 'CA-2278751-A', 'CA-2278751-A1', 'CA-2283629-A', 'CA-2283629-C', 'CA-2298540-A', 'CA-2298540-A1', 'CA-2550552-A', 'CA-2550552-A1', 'CA-2562038-A', 'CA-2562038-C', 'CA-2718348-A', 'CA-2718348-C', 'CA-3027364-A', 'CA-3027364-A1', 'CA-3055214-A', 'CA-3055214-A1', 'CA-3161617-A', 'CA-3161617-A1', 'CA-3225295-A', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'CN-200380105631-A', 'CN-200680004323-A', 'CN-200880129911-A', 'CN-201180052574-A', 'CN-201180057633-A', 'CN-201210027378-A', 'CN-201280035828-A', 'CN-96195210-A', 'EP-00959970-A', 'EP-00992018-A', 'EP-07753965-A', 'EP-0826155-A4', 'EP-08826523-A', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-18847365-A', 'EP-19908337-A', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-22746465-A', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4284234-A1', 'EP-96907882-A', 'FR-2194760-A1', 'FR-7327711-A', 'HK-03104403-A', 'HK-1052178-A1', 'HK-1250569-A1', 'HK-18104296-A', 'HR-P20201231-T', 'HR-P20201231-T1', 'ID-23426-A', 'ID-990914-A', 'IL-140140-A0', 'IL-14014099-A', 'IL-236725-A', 'IL-23672515-A', 'IL-244029-A0', 'IL-24402916-A', 'IL-274176-A', 'IL-27417620-A', 'JP-13313985-A', 'JP-2004321293-A', 'JP-2005104983-A', 'JP-2009181101-A', 'JP-2009260386-A', 'JP-2014180140-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-100228821-B1', 'KR-19940700442-A', 'KR-20050085437-A', 'KR-20057010360-A', 'KR-20080078049-A', 'KR-20087016723-A', 'KR-20107024636-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20167024476-A', 'KR-20180041236-A', 'KR-20187008669-A', 'KR-20200041324-A', 'KR-20200084864-A', 'KR-20207004898-A', 'KR-20207010098-A', 'MX-2013002850-A', 'PE-2012000906-A', 'PE-20130764-A1', 'PT-14764430-T', 'PT-2970346-T', 'RO-70061-A', 'RO-7944874-A', 'TW-107142982-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-17323505-A', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2009031436-A1', 'US-2009060985-W', 'US-2010025717-A1', 'US-2012038199-W', 'US-2012039471-W', 'US-201313787160-A', 'US-2014027588-W', 'US-201514981715-A', 'US-201515302361-A', 'US-201515313510-A', 'US-201515329526-A', 'US-201515514092-A', 'US-201615265158-A', 'US-201615554660-A', 'US-201615758551-A', 'US-2017015812-W', 'US-2017031596-W', 'US-2017036453-W', 'US-2017050153-A1', 'US-2017055607-W', 'US-2017087258-A1', 'US-2017145219-A1', 'US-201715422925-A', 'US-201715469746-A', 'US-201715614287-A', 'US-201715625819-A', 'US-201715646074-A', 'US-201716099227-A', 'US-201716319139-A', 'US-201716335976-A', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018018836-W', 'US-2018053351-W', 'US-2018080022-A1', 'US-201815950106-A', 'US-201816201848-A', 'US-201816612511-A', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019021660-W', 'US-2019050475-W', 'US-2019059638-W', 'US-201916277921-A', 'US-201916362297-A', 'US-201916396723-A', 'US-201916401028-A', 'US-201916401060-A', 'US-201916454755-A', 'US-201916537416-A', 'US-2019169580-A1', 'US-201916977341-A', 'US-201917045842-A', 'US-201917293905-A', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020061827-W', 'US-202016780659-A', 'US-202016798108-A', 'US-202016843567-A', 'US-202016878973-A', 'US-202016883515-A', 'US-202016952492-A', 'US-202016988179-A', 'US-202017021925-A', 'US-202017422807-A', 'US-202017604154-A', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-202117197897-A', 'US-202117244881-A', 'US-202117472182-A', 'US-202117791452-A', 'US-202117798325-A', 'US-202117926000-A', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022016812-W', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2022123166-A1', 'US-202218054917-A', 'US-2023024482-W', 'US-2023063471-W', 'US-2023067015-W', 'US-2023072940-W', 'US-2023073050-W', 'US-2023080114-W', 'US-2023155090-A1', 'US-2023171142-A1', 'US-202318169681-A', 'US-202318184298-A', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-27746394-A', 'US-30426202-A', 'US-3666017-A', 'US-3666017D-A', 'US-37750473-A', 'US-3842373-A', 'US-39137803-A', 'US-39548599-A', 'US-41229799-A', 'US-4541105-A', 'US-5304932-A', 'US-54455304-A', 'US-55161904-A', 'US-5547866-A', 'US-56389709-A', 'US-57612209-A', 'US-58729205-A', 'US-6030830-A', 'US-60880790-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-68078803-A', 'US-6980295-B2', 'US-70199003-A', 'US-7052856-B2', 'US-74211203-A', 'US-7745569-B2', 'US-8361933-B2', 'US-8864206-A', 'US-9061071-B2', 'US-91189497-A', 'US-97493601-A', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-A', 'ZA-200802422-B'], 'var_call_ZRJZk00dZSVEDVyILIiyhqUB': 'file_storage/call_ZRJZk00dZSVEDVyILIiyhqUB.json'}

exec(code, env_args)
