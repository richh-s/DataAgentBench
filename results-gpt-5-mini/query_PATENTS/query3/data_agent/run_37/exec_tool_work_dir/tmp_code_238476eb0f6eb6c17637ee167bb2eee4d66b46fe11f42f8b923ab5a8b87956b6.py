code = """import json, re
# load stored results
p_univ = var_call_SpSHlWc9Wvw6XBIPzo9P5Jzs
p_citing = var_call_xp9eB5BsCwHtYqksfoAOoevu
with open(p_univ, 'r', encoding='utf-8') as f:
    univ_recs = json.load(f)
with open(p_citing, 'r', encoding='utf-8') as f:
    citing_recs = json.load(f)
# list of UNIV CAL publication numbers extracted earlier available in var_call_CEEYJNOxc1MAwzkxfjmdkF0C
univ_pubs = var_call_CEEYJNOxc1MAwzkxfjmdkF0C
univ_set = set([s.upper() for s in univ_pubs])

# helper to parse citation JSON string into list
def parse_json_field(s):
    if not s:
        return []
    try:
        return json.loads(s)
    except Exception:
        # try to fix single quotes
        try:
            return json.loads(s.replace("'", '"'))
        except Exception:
            return []

# helper to extract assignee from Patents_info
assignee_patterns = [
    re.compile(r"^(?P<assignee>.*?) holds", re.IGNORECASE),
    re.compile(r"^(?P<assignee>.*?) holds the", re.IGNORECASE),
    re.compile(r"is owned by (?P<assignee>.*?)(?: and| with| who|,|\.|$)", re.IGNORECASE),
    re.compile(r"is assigned to (?P<assignee>.*?)(?: and| with| who|,|\.|$)", re.IGNORECASE),
    re.compile(r"(?P<assignee>.*?) holds the .* patent", re.IGNORECASE),
    re.compile(r"(?P<assignee>.*?) owns the .* patent", re.IGNORECASE),
    re.compile(r"(?P<assignee>.*?) is the assignee", re.IGNORECASE),
]

def extract_assignee(text):
    if not text:
        return None
    for pat in assignee_patterns:
        m = pat.search(text)
        if m:
            a = m.group('assignee').strip()
            # clean trailing phrases
            a = re.sub(r"\s+holds$", "", a, flags=re.IGNORECASE).strip()
            return a
    # fallback: look for uppercase sequences at start
    m2 = re.match(r"^([A-Z0-9\-\.,& ]{4,}?) (?:has|holds|owns|is)", text)
    if m2:
        return m2.group(1).strip()
    # another fallback: take first token group before 'the US' etc
    m3 = re.match(r"^(?P<assignee>[^,\.]+),", text)
    if m3:
        return m3.group('assignee').strip()
    return None

# iterate citing records and find those that cite any univ pub
assignee_to_codes = {}
for rec in citing_recs:
    citation_field = rec.get('citation')
    cite_list = parse_json_field(citation_field)
    cites_univ = False
    for c in cite_list:
        pubnum = c.get('publication_number','') if isinstance(c, dict) else ''
        if pubnum and pubnum.upper() in univ_set:
            cites_univ = True
            break
    if not cites_univ:
        continue
    # extract assignee
    pi = rec.get('Patents_info','')
    assignee = extract_assignee(pi)
    if not assignee:
        # try to find pattern 'the application (ID US-...) is owned by UNIV CALIFORNIA' style at end
        m = re.search(r"owned by ([A-Z0-9 \t\.,&'-]+)", pi, re.IGNORECASE)
        if m:
            assignee = m.group(1).strip()
    if not assignee:
        assignee = "UNKNOWN"
    assignee_up = assignee.upper()
    if 'UNIV CALIFORNIA' in assignee_up or 'UNIVERSITY OF CALIFORNIA' in assignee_up:
        continue
    # parse cpc field
    cpc_field = rec.get('cpc')
    codes = []
    try:
        cpc_list = json.loads(cpc_field) if cpc_field else []
    except Exception:
        try:
            cpc_list = json.loads(cpc_field.replace("'", '"')) if cpc_field else []
        except Exception:
            cpc_list = []
    # find codes where first==true
    for entry in cpc_list:
        if isinstance(entry, dict):
            if entry.get('first'):
                codes.append(entry.get('code'))
    if not codes:
        # fallback: take first code in list
        for entry in cpc_list:
            if isinstance(entry, dict) and entry.get('code'):
                codes.append(entry.get('code'))
                break
    if not codes:
        continue
    # normalize
    codes = [c for c in codes if c]
    if not codes:
        continue
    assignee_to_codes.setdefault(assignee.strip(), set()).update(codes)

# produce unique codes list
unique_codes = sorted({code for codes in assignee_to_codes.values() for code in codes})
# prepare output
out = {
    'assignee_to_codes': {k: sorted(list(v)) for k,v in assignee_to_codes.items()},
    'unique_codes': unique_codes
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ut7WdDsWTHeaPTY0l7N78YWW': ['publicationinfo'], 'var_call_42eJZpAO2w2mYOtquWKcommi': ['cpc_definition'], 'var_call_SpSHlWc9Wvw6XBIPzo9P5Jzs': 'file_storage/call_SpSHlWc9Wvw6XBIPzo9P5Jzs.json', 'var_call_CEEYJNOxc1MAwzkxfjmdkF0C': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A1', 'WO-2019173834-A1', 'US-2017145219-A1', 'US-2021002329-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'JP-2005104983-A', 'US-2021000566-A1', 'US-2006051790-A1', 'PT-2970346-T', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-2021282642-A1', 'US-2019209590-A1', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'JP-2009260386-A', 'CA-2562038-C', 'US-7052856-B2', 'US-6750960-B2', 'EP-2210307-A4', 'US-2020025859-A1', 'US-2021039104-A1', 'EP-1212462-A1', 'WO-2014152660-A1', 'US-5547866-A', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-2003112494-A1', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'US-2004115131-A1', 'US-2005234013-A1', 'CN-101584047-A', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2019067860-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'PE-20130764-A1', 'US-11014955-B2', 'KR-20110004413-A', 'CN-102584712-A', 'CN-103687626-A', 'CN-102067370-B', 'CA-2718348-C', 'US-11546022-B2', 'HK-1052178-A1', 'US-12025581-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'EP-3668487-A4', 'CA-2283629-C', 'HK-1250569-A1', 'AU-2004253879-A1', 'WO-2023239670-A1', 'WO-2012158833-A3', 'US-10744347-B2', 'AU-2409401-A', 'ID-23426-A', 'US-5304932-A', 'AU-3353000-A', 'AU-5938296-A', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2018243924-A1', 'AU-6535890-A', 'US-202117472182-A', 'US-201715625819-A', 'AU-2003247814-A', 'US-55161904-A', 'KR-20167024476-A', 'US-201715646074-A', 'KR-20207004898-A', 'AU-2001296493-A', 'US-202017021925-A', 'PT-14764430-T', 'AU-7724398-A', 'US-201715614287-A', 'US-202117197897-A', 'KR-20087016723-A', 'CA-2562038-A', 'US-41229799-A', 'US-201716335976-A', 'EP-00959970-A', 'US-2014027588-W', 'US-2023073050-W', 'EP-22746465-A', 'CN-96195210-A', 'IL-27417620-A', 'IL-24402916-A', 'US-4541105-A', 'AU-2010214112-A', 'US-2023067015-W', 'EP-19908337-A', 'US-2023080114-W', 'CA-2550552-A', 'US-201515514092-A', 'US-202016843567-A', 'ZA-200802422-A', 'CN-200880129911-A', 'US-201816201848-A', 'EP-18847365-A', 'CA-2283629-A', 'US-202218054917-A', 'ID-990914-A', 'US-201615758551-A', 'TW-107142982-A', 'US-39548599-A', 'US-2012039471-W', 'KR-20187008669-A', 'US-201715422925-A', 'KR-20207010098-A', 'US-54455304-A', 'FR-7327711-A', 'EP-08826523-A', 'KR-19940700442-A', 'US-30426202-A', 'JP-2014180140-A', 'US-58729205-A', 'US-201916396723-A', 'HK-18104296-A', 'AU-2004253879-A', 'BR-9610580-A', 'AU-5366398-A'], 'var_call_xp9eB5BsCwHtYqksfoAOoevu': 'file_storage/call_xp9eB5BsCwHtYqksfoAOoevu.json'}

exec(code, env_args)
