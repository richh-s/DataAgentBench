code = """import json, re
# Load full publicationinfo query result
path = var_call_0h1lVBuDoAWrvSOcNhImBEul
with open(path, 'r', encoding='utf-8') as f:
    all_rows = json.load(f)

# Identify UNIV CALIFORNIA publication numbers
uc_pub_nums = set()
for rec in all_rows:
    pi = rec.get('Patents_info','')
    if re.search(r'univ(ersity)?\.?\s+california', pi, re.IGNORECASE):
        # attempt to extract publication number from text
        m = re.search(r'pub(?:lication)?(?:\. )?number\s+([A-Z0-9\-]+)', pi, re.IGNORECASE)
        if m:
            uc_pub_nums.add(m.group(1))
        else:
            # fallback: find tokens like XX-123... pattern
            m2 = re.search(r'([A-Z]{2}-[0-9A-Z\-]+)', pi)
            if m2:
                uc_pub_nums.add(m2.group(1))
# Also include publication numbers from rows where Patents_info explicitly contains UNIV CALIFORNIA from previous filtered results (var_call_5Gv...)
try:
    path2 = var_call_5GvTT0NlNMDl9lKfwXv71Uct
    with open(path2, 'r', encoding='utf-8') as f2:
        filtered = json.load(f2)
    for rec in filtered:
        cit = rec.get('citation','')
        # some filtered rows had publication numbers in Patents_info; also parse Patents_info for pub numbers
        pi = rec.get('Patents_info','')
        m = re.search(r'\b([A-Z]{2}-[0-9A-Z\-]+)\b', pi)
        if m:
            uc_pub_nums.add(m.group(1))
except Exception:
    pass

# Also collect any publication numbers that appear within publicationinfo rows that are assigned to UC via various patterns
for rec in all_rows:
    pi = rec.get('Patents_info','')
    if re.search(r'univ(ersity)?\.?\s+california', pi, re.IGNORECASE):
        # try to find any US/WO/EP/... patterns
        for m in re.findall(r'\b([A-Z]{2}-[0-9A-Z\-]+)\b', pi):
            uc_pub_nums.add(m)

# Now iterate over all rows to find citations including any UC pub numbers
assignee_cpc = {}  # assignee -> set of primary cpc codes
for rec in all_rows:
    # parse citation field which may be JSON string
    cit_field = rec.get('citation','')
    try:
        citations = json.loads(cit_field) if cit_field and cit_field.strip().startswith('[') else []
    except Exception:
        citations = []
    cited_pub_nums = set()
    for c in citations:
        pn = c.get('publication_number') if isinstance(c, dict) else None
        if pn:
            cited_pub_nums.add(pn)
    # check intersection
    if not uc_pub_nums.intersection(cited_pub_nums):
        continue
    # extract assignee from Patents_info
    pi = rec.get('Patents_info','')
    assignee = None
    # try patterns
    patterns = [r'^(.*?) holds', r'^(.*?) holds the', r'^(.*?) is assigned to', r'^(.*?) is owned by', r'^(.*?) owns', r'^(.*?) has the', r'^(.*?) holders? of', r'^(.*?)\s+filed', r'^(.*?)\s+holds the US', r'is assigned to\s+([^,\.]+)', r'is owned by\s+([^,\.]+)']
    for p in patterns:
        m = re.search(p, pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip() if p.startswith('^') else m.group(1).strip()
            break
    if not assignee:
        # try to find uppercase group before 'the US' or before 'patent'
        m2 = re.search(r'([A-Z0-9 &,\.\'"\-]{3,}?) holds the', pi)
        if m2:
            assignee = m2.group(1).strip()
    if not assignee:
        # final fallback: take first 40 chars
        assignee = pi.split(' ')[0:4]
        assignee = ' '.join(assignee)
    # normalize
    assignee_norm = re.sub(r'\s+', ' ', assignee).strip()
    # skip if assignee is Univ California
    if re.search(r'univ(ersity)?\.?\s+california', assignee_norm, re.IGNORECASE):
        continue
    # parse cpc field
    cpc_field = rec.get('cpc','')
    primary_codes = []
    try:
        cpcs = json.loads(cpc_field) if cpc_field and cpc_field.strip().startswith('[') else []
        for entry in cpcs:
            if isinstance(entry, dict) and entry.get('first'):
                code = entry.get('code')
                if code:
                    primary_codes.append(code)
        if not primary_codes and cpcs:
            # fallback: take first code entries
            for entry in cpcs[:1]:
                if isinstance(entry, dict) and entry.get('code'):
                    primary_codes.append(entry.get('code'))
    except Exception:
        primary_codes = []
    if not primary_codes:
        continue
    assignee_cpc.setdefault(assignee_norm, set()).update(primary_codes)

# prepare output
assignee_list = []
unique_cpcs = set()
for a, codes in assignee_cpc.items():
    assignee_list.append({'assignee': a, 'cpcs': sorted(list(codes))})
    unique_cpcs.update(codes)

output = {'assignee_primary_cpcs': assignee_list, 'unique_cpcs': sorted(list(unique_cpcs)), 'uc_pub_count': len(uc_pub_nums)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_fY2ydqqc8zfZUbusfxXecokG': ['publicationinfo'], 'var_call_s4PAVSm8xBo3FtsrFV63F6Zt': ['cpc_definition'], 'var_call_5GvTT0NlNMDl9lKfwXv71Uct': 'file_storage/call_5GvTT0NlNMDl9lKfwXv71Uct.json', 'var_call_s6YH0Dz4vUJdlzAfY4r8cQkC': {'publication_numbers': ['AP-2011005954-A', 'AU-2001257114-A1', 'AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A', 'AU-2003297741-A1', 'AU-2004253879-A', 'AU-2004253879-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2007297661-A', 'AU-2007297661-A1', 'AU-2008329628-A', 'AU-2008329628-B2', 'AU-2008349842-A', 'AU-2008349842-A1', 'AU-2009234210-A', 'AU-2009234210-A1', 'AU-2010214112-A', 'AU-2010214112-B2', 'AU-2015364602-A', 'AU-2015364602-B2', 'AU-2017356943-A', 'AU-2017356943-A1', 'AU-2019275518-A', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5711401-A', 'AU-5938296-A', 'AU-6492396-A', 'AU-6535890-A', 'AU-7724398-A', 'BR-112021021092-A', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A', 'CA-2220674-A1', 'CA-2278751-A', 'CA-2278751-A1', 'CA-2283629-A', 'CA-2283629-C', 'CA-2298540-A', 'CA-2298540-A1', 'CA-2494262-A', 'CA-2494262-A1', 'CA-2550552-A', 'CA-2550552-A1', 'CA-2562038-A', 'CA-2562038-C', 'CA-2718348-A', 'CA-2718348-C', 'CA-3027364-A', 'CA-3027364-A1', 'CA-3055214-A', 'CA-3055214-A1', 'CA-3161617-A', 'CA-3161617-A1', 'CA-3225295-A', 'CA-3225295-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-1120376-C', 'CN-200380105631-A', 'CN-200680004323-A', 'CN-200880129911-A', 'CN-201180052574-A', 'CN-201180057633-A', 'CN-201210027378-A', 'CN-201280035828-A', 'CN-96195210-A', 'EP-00959970-A', 'EP-00992018-A', 'EP-07753965-A', 'EP-0826155-A4', 'EP-08826523-A', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-18847365-A', 'EP-19908337-A', 'EP-2029921-A4', 'EP-21763795-A', 'EP-2210307-A4', 'EP-22746465-A', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4114888-A1', 'EP-4284234-A1', 'EP-96907882-A', 'FR-2194760-A1', 'FR-7327711-A', 'HK-03104403-A', 'HK-1052178-A1', 'HK-1250569-A1', 'HK-18104296-A', 'ID-23426-A', 'ID-990914-A', 'IL-140140-A0', 'IL-14014099-A', 'IL-236725-A', 'IL-23672515-A', 'IL-244029-A0', 'IL-24402916-A', 'IL-255026-A0', 'IL-25502617-A', 'IL-274176-A', 'IL-27417620-A', 'JP-13313985-A', 'JP-2004321293-A', 'JP-2005104983-A', 'JP-2009181101-A', 'JP-2009260386-A', 'JP-2014180140-A', 'JP-2014224156-A', 'KR-100228821-B1', 'KR-19940700442-A', 'KR-20050085437-A', 'KR-20057010360-A', 'KR-20080078049-A', 'KR-20087016723-A', 'KR-20107024636-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20167024476-A', 'KR-20180041236-A', 'KR-20187008669-A', 'KR-20200041324-A', 'KR-20200084864-A', 'KR-20207004898-A', 'KR-20207010098-A', 'MX-2013002850-A', 'PE-2012000906-A', 'PE-20130764-A1', 'PT-14764430-T', 'PT-2970346-T', 'RO-70061-A', 'RO-7944874-A', 'TW-107142982-A', 'TW-201925402-A', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11546022-B2', 'US-11607427-B2', 'US-11667770-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-17323505-A', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2008047008-A1', 'US-2008139409-A1', 'US-2009031436-A1', 'US-2009060985-W', 'US-2010025717-A1', 'US-2012038199-W', 'US-2012039471-W', 'US-201313787160-A', 'US-2014027588-W', 'US-201514791007-A', 'US-201514981715-A', 'US-201515302361-A', 'US-201515313510-A', 'US-201515329526-A', 'US-201515514092-A', 'US-201615265158-A', 'US-201615554660-A', 'US-201615758551-A', 'US-2017015812-W', 'US-2017031596-W', 'US-2017036453-W', 'US-2017050153-A1', 'US-2017055607-W', 'US-2017087258-A1', 'US-2017145219-A1', 'US-201715422925-A', 'US-201715469746-A', 'US-201715614287-A', 'US-201715625819-A', 'US-201715646074-A', 'US-201716099227-A', 'US-201716319139-A', 'US-201716335976-A', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017294981-A1', 'US-2017369950-A1', 'US-2018018836-W', 'US-2018053351-W', 'US-2018080022-A1', 'US-201815904103-A', 'US-201815950106-A', 'US-201816201848-A', 'US-201816612511-A', 'US-2018177786-A1', 'US-2018243924-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019021660-W', 'US-2019034067-W', 'US-2019050475-W', 'US-2019059638-W', 'US-201916277921-A', 'US-201916362297-A', 'US-201916396723-A', 'US-201916401028-A', 'US-201916401060-A', 'US-201916454755-A', 'US-201916537416-A', 'US-2019169580-A1', 'US-201916977341-A', 'US-201917045842-A', 'US-201917293905-A', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020061827-W', 'US-202016743881-A', 'US-202016780659-A', 'US-202016798108-A', 'US-202016843567-A', 'US-202016878973-A', 'US-202016883515-A', 'US-202016952492-A', 'US-202016988179-A', 'US-202017021925-A', 'US-202017422807-A', 'US-202017604154-A', 'US-2020222513-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-202117197897-A', 'US-202117244881-A', 'US-202117472182-A', 'US-202117791452-A', 'US-202117798325-A', 'US-202117926000-A', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022016812-W', 'US-2022018060-A1', 'US-2022029878-W', 'US-2022074631-A1', 'US-2022123166-A1', 'US-202218054917-A', 'US-2023024482-W', 'US-2023063471-W', 'US-2023067015-W', 'US-2023072940-W', 'US-2023073050-W', 'US-2023080114-W', 'US-2023155090-A1', 'US-2023171142-A1', 'US-202318169681-A', 'US-202318184298-A', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-2023340506-A1', 'US-27746394-A', 'US-30426202-A', 'US-3384508-A', 'US-3666017-A', 'US-37750473-A', 'US-3842373-A', 'US-39137803-A', 'US-39548599-A', 'US-41229799-A', 'US-4541105-A', 'US-5304932-A', 'US-54455304-A', 'US-55161904-A', 'US-5547866-A', 'US-56389709-A', 'US-57612209-A', 'US-58729205-A', 'US-6030830-A', 'US-60880790-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-68078803-A', 'US-6980295-B2', 'US-70199003-A', 'US-7052856-B2', 'US-74211203-A', 'US-7745569-B2', 'US-8361933-B2', 'US-8864206-A', 'US-9061071-B2', 'US-91189497-A', 'US-9274095-B2', 'US-97493601-A', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020068183-A3', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2022245977-A2', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024050335-A2', 'WO-2024112568-A1', 'ZA-200802422-A', 'ZA-200802422-B'], 'count': 345}, 'var_call_0h1lVBuDoAWrvSOcNhImBEul': 'file_storage/call_0h1lVBuDoAWrvSOcNhImBEul.json'}

exec(code, env_args)
