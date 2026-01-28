code = """import json, re
path_uc = var_call_AMrDYDRyAiDk5vRxmCAz6wcC
path_allcit = var_call_W5rgnwjwlnuucJOnL4ymHVEj
with open(path_uc, 'r', encoding='utf-8') as f:
    uc_records = json.load(f)
with open(path_allcit, 'r', encoding='utf-8') as f:
    all_cit_records = json.load(f)

# extract UC pubnums as before
pat = re.compile(r'\b([A-Z]{2}-[0-9A-Za-z-]+)\b')
uc_pubnums = set()
for rec in uc_records:
    pi = rec.get('Patents_info','')
    for m in pat.finditer(pi):
        tok = m.group(1)
        if any(c.isdigit() for c in tok):
            uc_pubnums.add(tok)

# extract all cited publication numbers
cited_nums = set()
def parse_citation_field(cit_str):
    if not cit_str:
        return []
    try:
        arr = json.loads(cit_str)
    except Exception:
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

for rec in all_cit_records:
    cited = parse_citation_field(rec.get('citation'))
    for c in cited:
        cited_nums.add(c)

intersect = sorted(list(uc_pubnums & cited_nums))
# Also check normalized forms: remove country prefix from uc_pubnums and cited
def norm(p):
    return re.sub(r'[^0-9A-Za-z]', '', p).upper()
uc_norm = {norm(p):p for p in uc_pubnums}
cited_norm = {norm(p):p for p in cited_nums}
intersect_norm_keys = set(uc_norm.keys()) & set(cited_norm.keys())
intersect_norm = sorted([ (uc_norm[k], cited_norm[k]) for k in intersect_norm_keys ])

output = {'uc_count': len(uc_pubnums), 'cited_count': len(cited_nums), 'direct_intersect': intersect, 'norm_intersect': intersect_norm[:50]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_WakKrtRs7x6PBnTcp6hvegg1': ['publicationinfo'], 'var_call_qAMMTH6DzqiVvTFW2mhfJi8Q': ['cpc_definition'], 'var_call_AMrDYDRyAiDk5vRxmCAz6wcC': 'file_storage/call_AMrDYDRyAiDk5vRxmCAz6wcC.json', 'var_call_9qbdQ9cSLtDErtaVc0iyJeV7': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5938296-A', 'AU-6535890-A', 'CA-2283629-C', 'CA-2298540-A1', 'CA-2550552-A1', 'CA-2562038-C', 'CA-2718348-C', 'CA-3161617-A1', 'CN-100339724-C', 'CN-101584047-A', 'CN-102067370-B', 'CN-102584712-A', 'CN-103189548-A', 'CN-103687626-A', 'EP-0826155-A4', 'EP-1212462-A1', 'EP-2210307-A4', 'EP-3668487-A4', 'EP-4284234-A1', 'HK-1052178-A1', 'HK-1250569-A1', 'HR-P20201231-T1', 'ID-23426-A', 'IL-244029-A0', 'IL-274176-A', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2014224156-A', 'JP-S6163700-A', 'KR-20050085437-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20200041324-A', 'MX-2013002850-A', 'PE-20130764-A1', 'PT-2970346-T', 'RO-70061-A', 'TW-201925402-A', 'US-10359432-B2', 'US-10744347-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11376346-B2', 'US-11421276-B2', 'US-11546022-B2', 'US-11667770-B2', 'US-12025581-B2', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005234013-A1', 'US-2006051790-A1', 'US-2006292670-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2017145219-A1', 'US-2017281687-A1', 'US-2018243924-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019328740-A1', 'US-2020025859-A1', 'US-2020283856-A1', 'US-2021000566-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021101879-A1', 'US-2021181673-A1', 'US-2021282642-A1', 'US-2022018060-A1', 'US-2022074631-A1', 'US-2023155090-A1', 'US-2023171142-A1', 'US-2023279470-A1', 'US-2023321419-A1', 'US-5304932-A', 'US-5547866-A', 'US-6237292-B1', 'US-6750960-B2', 'US-6767662-B2', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-9061071-B2', 'WO-2010045542-A3', 'WO-2012158833-A3', 'WO-2012162563-A2', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2017214343-A1', 'WO-2018026404-A3', 'WO-2018067976-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020055916-A9', 'WO-2021102420-A1', 'WO-2023212447-A2', 'WO-2023225482-A3', 'WO-2023239670-A1', 'WO-2024044766-A3', 'WO-2024112568-A1'], 'var_call_W5rgnwjwlnuucJOnL4ymHVEj': 'file_storage/call_W5rgnwjwlnuucJOnL4ymHVEj.json', 'var_call_hiEDx97eI0s2OuNCnssd6gsu': {'assignee_to_codes': {}, 'primary_codes': []}}

exec(code, env_args)
