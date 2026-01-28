code = """import json, re
with open(var_call_Ow9DeaE9wDuFRl2s0DGnZKEU, 'r') as f:
    uc_records = json.load(f)
with open(var_call_extKKtbNjMJuiqaFvagK1ONA, 'r') as f:
    cited_records = json.load(f)

# Build UC core digit set
def core_digits(s):
    if not s: return ''
    nums = re.findall(r"\d+", s)
    return ''.join(nums)

uc_cores = set()
for rec in uc_records:
    pi = rec.get('Patents_info','')
    # try to find publication numbers in pi
    pnums = re.findall(r'[A-Z]{2}-[0-9]{4,}[A-Z0-9\-]*|[A-Z]{2}\s*[0-9]{4,}[A-Z0-9\-]*|[A-Z]{2}-[0-9]{1,}', pi)
    # also find bare numbers
    pnums += re.findall(r'\bUS-?\d{4,}[A-Z0-9\-]*\b', pi)
    # fallback: any sequences like digits of length>=4
    if not pnums:
        pnums += re.findall(r'\d{4,,}', pi)
    for p in pnums:
        cd = core_digits(p)
        if cd:
            uc_cores.add(cd)
# Also scan citation fields in uc_records themselves
for rec in uc_records:
    citation = rec.get('citation','')
    try:
        cited_list = json.loads(citation) if citation else []
    except Exception:
        try:
            cited_list = json.loads(citation.replace("'", '"'))
        except Exception:
            cited_list = []
    for c in cited_list:
        pn = c.get('publication_number','')
        if pn:
            uc_cores.add(core_digits(pn))

# Now scan cited_records to find those that cite any UC core
matches = []
for rec in cited_records:
    citation = rec.get('citation','')
    if not citation or citation.strip()=='[]':
        continue
    try:
        cited_list = json.loads(citation)
    except Exception:
        try:
            cited_list = json.loads(citation.replace("'", '"'))
        except Exception:
            cited_list = []
    cited_pn = [c.get('publication_number','') for c in cited_list if c.get('publication_number')]
    cited_cores = [core_digits(p) for p in cited_pn]
    if any(core in uc_cores and core for core in cited_cores):
        # extract assignee
        pi = rec.get('Patents_info','')
        assignee = None
        # patterns
        m = re.search(r'^(.*?)\s+(?:holds|owns|has)\b', pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'is assigned to\s+([^,\.]+)', pi, re.IGNORECASE)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'is owned by\s+([^,\.]+)', pi, re.IGNORECASE)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            m = re.search(r'^(.*?)\s*\(', pi)
            if m:
                assignee = m.group(1).strip()
        if not assignee:
            # fallback to whole
            assignee = pi.strip()
        # normalize assignee: remove leading 'In US, ' or country prefixes
        assignee = re.sub(r'^In\s+\w+,\s*', '', assignee)
        assignee = assignee.strip()
        # parse cpc primary
        cpc_field = rec.get('cpc','')
        codes = []
        try:
            cpc_list = json.loads(cpc_field) if cpc_field else []
        except Exception:
            try:
                cpc_list = json.loads(cpc_field.replace("'", '"'))
            except Exception:
                cpc_list = []
        for c in cpc_list:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    codes.append(code.strip())
        if not codes and cpc_list:
            for c in cpc_list:
                if isinstance(c, dict) and c.get('code'):
                    codes.append(c.get('code').strip())
                    break
        matches.append({'rowid': rec.get('rowid'), 'assignee': assignee, 'codes': codes, 'cited_pn': cited_pn})

# Aggregate by assignee: map assignee -> set of codes
agg = {}
for m in matches:
    a = m['assignee']
    if 'UNIV CALIFORNIA' in a.upper():
        continue
    if a not in agg:
        agg[a] = set()
    for code in m['codes']:
        if code:
            agg[a].add(code)

# prepare results
results = [{'assignee': a, 'codes': sorted(list(codes))} for a,codes in agg.items()]
unique_codes = sorted({c for _,codes in [(r['assignee'], r['codes']) for r in results] for c in codes})

out = {'results': results, 'unique_codes': unique_codes, 'num_matches': len(matches)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ow9DeaE9wDuFRl2s0DGnZKEU': 'file_storage/call_Ow9DeaE9wDuFRl2s0DGnZKEU.json', 'var_call_extKKtbNjMJuiqaFvagK1ONA': 'file_storage/call_extKKtbNjMJuiqaFvagK1ONA.json', 'var_call_jbmF9WDxe6NXpmwtmwGomAs1': {'uc_pubnums': ['AU-2001296493-A', 'AU-2001296493-B2', 'AU-2002254753-A', 'AU-2002254753-B2', 'AU-2003247814-A', 'AU-2003247814-A1', 'AU-2003297741-A', 'AU-2003297741-A1', 'AU-2005269556-A', 'AU-2005269556-A1', 'AU-2008329628-A', 'AU-2008329628-B2', 'AU-2008349842-A', 'AU-2008349842-A1', 'AU-2015364602-A', 'AU-2015364602-B2', 'AU-2017356943-A', 'AU-2017356943-A1', 'AU-2019275518-A', 'AU-2019275518-B2', 'AU-2898989-A', 'AU-7724398-A', 'BR-112021021092-A', 'BR-112021021092-A8', 'CA-2220674-A', 'CA-2220674-A1', 'CA-2298540-A', 'CA-2298540-A1', 'CA-2562038-A', 'CA-2562038-C', 'CA-3161617-A', 'CA-3161617-A1', 'CA-3225295-A', 'CA-3225295-A1', 'CN-100339724-C', 'CN-103189548-A', 'CN-1120376-C', 'CN-200380105631-A', 'CN-201180052574-A', 'CN-96195210-A', 'EP-00959970-A', 'EP-00992018-A', 'EP-0826155-A4', 'EP-08826523-A', 'EP-1212462-A1', 'EP-1224461-B1', 'EP-2210307-A4', 'EP-22746465-A', 'EP-4284234-A1', 'EP-96907882-A', 'FR-2194760-A1', 'FR-7327711-A', 'IL-140140-A0', 'IL-14014099-A', 'IL-274176-A', 'IL-27417620-A', 'JP-13313985-A', 'JP-2004321293-A', 'JP-2005104983-A', 'JP-2009181101-A', 'JP-2009260386-A', 'KR-100228821-B1', 'KR-19940700442-A', 'KR-20050085437-A', 'KR-20057010360-A', 'KR-20080078049-A', 'KR-20087016723-A', 'KR-20160119166-A', 'KR-20167024476-A', 'KR-20180041236-A', 'KR-20187008669-A', 'KR-20200041324-A', 'KR-20200084864-A', 'KR-20207004898-A', 'KR-20207010098-A', 'PT-14764430-T', 'PT-2970346-T', 'RO-70061-A', 'RO-7944874-A', 'TW-107142982-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11072681-B2', 'US-11248107-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11667770-B2', 'US-17323505-A', 'US-2003112494-A1', 'US-2005136639-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2012039471-W', 'US-201313787160-A', 'US-2014027588-W', 'US-201514981715-A', 'US-201515302361-A', 'US-201515313510-A', 'US-201515329526-A', 'US-2017015812-W', 'US-2017031596-W', 'US-2017036453-W', 'US-2017050153-A1', 'US-2017055607-W', 'US-2017145219-A1', 'US-201715422925-A', 'US-201715614287-A', 'US-201715625819-A', 'US-201715646074-A', 'US-201716099227-A', 'US-201716319139-A', 'US-201716335976-A', 'US-2017194630-A1', 'US-2017281687-A1', 'US-2017369950-A1', 'US-2018018836-W', 'US-201815950106-A', 'US-201816612511-A', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019021660-W', 'US-2019050475-W', 'US-2019059638-W', 'US-201916277921-A', 'US-201916362297-A', 'US-201916401060-A', 'US-201916454755-A', 'US-201916537416-A', 'US-2019169580-A1', 'US-201916977341-A', 'US-2019209590-A1', 'US-2020025859-A1', 'US-2020061827-W', 'US-202016878973-A', 'US-202016883515-A', 'US-202016952492-A', 'US-202016988179-A', 'US-202017021925-A', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-202117197897-A', 'US-202117472182-A', 'US-202117791452-A', 'US-202117926000-A', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022016812-W', 'US-2022074631-A1', 'US-2023063471-W', 'US-2023073050-W', 'US-2023171142-A1', 'US-202318169681-A', 'US-202318184298-A', 'US-2023279470-A1', 'US-2023314781-A1', 'US-2023321419-A1', 'US-27746394-A', 'US-30426202-A', 'US-37750473-A', 'US-3842373-A', 'US-39137803-A', 'US-39548599-A', 'US-41229799-A', 'US-54455304-A', 'US-55161904-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-68078803-A', 'US-6980295-B2', 'US-7052856-B2', 'US-74211203-A', 'US-7745569-B2', 'US-8864206-A', 'US-9061071-B2', 'US-97493601-A', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2020096950-A1', 'WO-2021102420-A1', 'WO-2022178138-A1', 'WO-2023212447-A2', 'WO-2024050335-A2'], 'unique_codes': [], 'citing_matches': []}, 'var_call_IDhCGfoBT8OnY6kyI7WyGLdd': []}

exec(code, env_args)
