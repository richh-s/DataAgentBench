code = """import json, re
from pathlib import Path

path = Path(var_call_ZWoyq0N426C8voVRyLT5IXbs)
rows = json.loads(path.read_text())

# First, build index of publication_number -> assignee from all rows
pub_to_assignee = {}
for r in rows:
    pi = r['Patents_info']
    m = re.search(r'(?:pub\. number|publication number) ([A-Z]{2}-[0-9A-Z]+-[AB][0-9])', pi)
    pubnum = m.group(1) if m else None
    am = re.search(r'assignee_harmonized: ([^,;]+)', pi)
    assignee = am.group(1).strip() if am else None
    if not assignee:
        m2 = re.search(r'owned by ([^,.;]+)', pi)
        if not m2:
            m2 = re.search(r'assigned to ([^,.;]+)', pi)
        assignee = m2.group(1).strip() if m2 else None
    if pubnum and assignee:
        pub_to_assignee[pubnum] = assignee

# Next, find cases where cited_pub belongs to UNIV CALIFORNIA and citing assignee is not UNIV CALIFORNIA
results = {}
for r in rows:
    pi = r['Patents_info']
    am = re.search(r'assignee_harmonized: ([^,;]+)', pi)
    citing_assignee = am.group(1).strip() if am else None
    if not citing_assignee:
        m2 = re.search(r'owned by ([^,.;]+)', pi)
        if not m2:
            m2 = re.search(r'assigned to ([^,.;]+)', pi)
        citing_assignee = m2.group(1).strip() if m2 else None
    if not citing_assignee or 'UNIV CALIFORNIA' in citing_assignee.upper():
        continue
    cpc_list = json.loads(r['cpc']) if r['cpc'] else []
    prim_codes = sorted({e['code'] for e in cpc_list if e.get('first')})
    cites = json.loads(r['citation']) if r['citation'] else []
    for c in cites:
        cpub = c.get('publication_number')
        if not cpub:
            continue
        ass = pub_to_assignee.get(cpub)
        if ass and 'UNIV CALIFORNIA' in ass.upper():
            if citing_assignee not in results:
                results[citing_assignee] = set()
            for code in prim_codes:
                # primary CPC subclass: trim to main group (before last '/')
                mcode = re.match(r'([A-Z]\d+[A-Z]\d+)/\d+', code)
                results[citing_assignee].add(mcode.group(1) if mcode else code)

# Convert sets to sorted lists
final = {k: sorted(v) for k,v in results.items()}

out = json.dumps(final)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_uQANuj8MAsLxyJnznAiafEGt': [], 'var_call_dViraW13HaF6dn3FuimMKgJO': ['cpc_definition'], 'var_call_ZWoyq0N426C8voVRyLT5IXbs': 'file_storage/call_ZWoyq0N426C8voVRyLT5IXbs.json', 'var_call_KwMpoKd5UllBN4ggEflldeee': {'records': [{'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2022074631-A1', 'cited_pub': 'US-4599677-A', 'primary_cpc': ['F25B21/00']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2022074631-A1', 'cited_pub': 'US-2015129765-A1', 'primary_cpc': ['F25B21/00']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2022074631-A1', 'cited_pub': 'FR-3105380-A1', 'primary_cpc': ['F25B21/00']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2022074631-A1', 'cited_pub': 'US-11466906-B2', 'primary_cpc': ['F25B21/00']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2001053519-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-0212892-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2002115120-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-03016910-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2003119064-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2003199000-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2004191783-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2004203083-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2005116268-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2006046259-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2006036220-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2006078882-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2007042425-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2007050146-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2007280917-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2008137465-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2009148933-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2009197774-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2010012834-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2010105046-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2010197518-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2010216115-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2012009547-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2012015904-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2012009567-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2012065087-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2012121978-A2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2012316076-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'WO-2013103781-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2015018234-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-9057109-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-9200322-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-9410204-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2016237501-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2016265059-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2016289765-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-2017029891-A1', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-9803243-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-10047396-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has publication number US-11421276-B2', 'citing_pub': 'US-11421276-B2', 'cited_pub': 'US-10196690-B2', 'primary_cpc': ['C12Q1/6883']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2017281687-A1', 'cited_pub': 'US-2003032003-A1', 'primary_cpc': ['A61K35/28']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2017281687-A1', 'cited_pub': 'US-9439928-B2', 'primary_cpc': ['A61K35/28']}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'citing_pub': 'US-2017281687-A1', 'cited_pub': 'US-9682106-B2', 'primary_cpc': ['A61K35/28']}, {'citing_assignee': None, 'citing_pub': 'US-6237292-B1', 'cited_pub': 'DE-1509371-A1', 'primary_cpc': ['E04H9/021']}, {'citing_assignee': None, 'citing_pub': 'US-6237292-B1', 'cited_pub': 'US-3616113-A', 'primary_cpc': ['E04H9/021']}, {'citing_assignee': None, 'citing_pub': 'US-6237292-B1', 'cited_pub': 'US-4370390-A', 'primary_cpc': ['E04H9/021']}], 'num_rows': 169, 'num_relations': 1308, 'sample_cited_pubs': ['CN-101061570-A', 'CN-101086963-A', 'CN-101631902-A', 'CN-102964610-A', 'CN-103224947-A', 'CN-103233028-A', 'CN-103343120-A', 'CN-104264260-A', 'CN-106880693-A', 'CN-107058224-A', 'CN-1237247-A', 'CN-1346403-A', 'CN-1413250-A', 'CN-85101623-A', 'DE-1509371-A1', 'EP-0111214-A2', 'EP-0399833-A1', 'EP-0474891-A1', 'EP-0474894-A1', 'EP-0476808-A1', 'EP-0497542-A1', 'EP-0513982-A2', 'EP-0524013-A1', 'EP-0640846-B1', 'EP-0922957-A1', 'EP-1122806-A1', 'EP-1699104-A1', 'EP-1939202-A1', 'EP-2162185-B1', 'EP-2341149-A1', 'EP-2355893-B1', 'EP-2440284-B1', 'EP-2489275-A1', 'EP-2515996-A2', 'EP-2544319-B1', 'EP-2667942-A2', 'EP-2674501-A1', 'EP-2694154-A1', 'EP-2707094-B1', 'EP-2736592-B1', 'EP-2741810-A1', 'EP-2755718-B1', 'EP-2764103-A2', 'EP-2784162-B1', 'EP-2928557-A2', 'EP-2962694-A1', 'EP-3285856-A1', 'EP-3294376-A1', 'EP-3338855-A1', 'EP-3403690-A1']}, 'var_call_5lmHW0pYHNrqYky4Ro5xSHOR': [{'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}]}

exec(code, env_args)
