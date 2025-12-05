code = """import json, pandas as pd, re, os

# load citing records that mention UNIV CALIFORNIA in citation field
path = var_call_asLEDEVZB27JXVJDCCIaMVU9
with open(path, 'r') as f:
    citing_data = json.load(f)

citing_df = pd.DataFrame(citing_data)

# extract citing assignee from Patents_info

def extract_assignee(text):
    m = re.search(r'is (?:owned by|belonging to|assigned to|held by) (.+?) and has', text)
    if m:
        return m.group(1).strip()
    m = re.search(r'is assigned to (.+?),', text)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by (.+?),', text)
    if m:
        return m.group(1).strip()
    return None

citing_df['assignee'] = citing_df['Patents_info'].apply(extract_assignee)

# filter out UNIV CALIFORNIA itself
citing_df = citing_df[citing_df['assignee'].notna()]
citing_df = citing_df[~citing_df['assignee'].str.contains('UNIV CALIFORNIA', case=False, na=False)]

# parse CPC JSON and get primary (first=true) codes

def get_primary_cpc(cpc_text):
    try:
        lst = json.loads(cpc_text)
    except Exception:
        return []
    return [entry['code'] for entry in lst if entry.get('first')]

citing_df['primary_cpc'] = citing_df['cpc'].apply(get_primary_cpc)

# explode to one row per assignee-primary_cpc
rows = []
for _, r in citing_df.iterrows():
    for code in r['primary_cpc']:
        rows.append({'assignee': r['assignee'], 'symbol': code})

res_df = pd.DataFrame(rows).drop_duplicates()

result = json.dumps(res_df.to_dict(orient='records'))
print("__RESULT__:")
print(result)"""

env_args = {'var_call_TgiczeIG8IbC3AHgD6egu7ty': [], 'var_call_n4V8UNccRkuupBzCXO9gjH41': 'file_storage/call_n4V8UNccRkuupBzCXO9gjH41.json', 'var_call_rZutMZg3p1Cn4vhQp30nuQzR': {'uc_publication_numbers': ['US-2022074631-A1', 'TW-201925402-A', 'US-11421276-B2', 'AU-2019275518-B2', 'JP-S6163700-A', 'US-2017281687-A1', 'AU-2003247814-A1', 'AU-2017356943-A1', 'US-6237292-B1', 'US-7745569-B2', 'US-11072681-B2', 'US-9061071-B2', 'KR-20050085437-A', 'KR-20160119166-A', 'EP-0826155-A4', 'US-2019169580-A1', 'US-2020283856-A1', 'AU-2898989-A', 'RO-70061-A', 'WO-2017136335-A1', 'WO-2021102420-A1', 'WO-2012162563-A2', 'US-11376346-B2', 'CN-100339724-C', 'US-2009031436-A1', 'AU-2005269556-A1', 'WO-2019173834-A1', 'US-2017145219-A1', 'US-2021002329-A1', 'KR-20200041324-A', 'CN-103189548-A', 'CA-2298540-A1', 'JP-2005104983-A', 'US-2021000566-A1', 'US-2006051790-A1', 'PT-2970346-T', 'US-2023171142-A1', 'WO-2018026404-A3', 'US-2006292670-A1', 'US-2021101879-A1', 'US-2023321419-A1', 'AU-2003297741-A1', 'WO-2017214343-A1', 'US-2021282642-A1', 'US-2019209590-A1', 'US-10359432-B2', 'US-11667770-B2', 'CA-3161617-A1', 'JP-2009260386-A', 'CA-2562038-C', 'US-7052856-B2', 'US-6750960-B2', 'EP-2210307-A4', 'US-2020025859-A1', 'US-2021039104-A1', 'EP-1212462-A1', 'WO-2014152660-A1', 'US-5547866-A', 'US-2023279470-A1', 'AU-2008349842-A1', 'EP-4284234-A1', 'WO-2018067976-A1', 'WO-2020055916-A9', 'US-6767662-B2', 'US-2021181673-A1', 'WO-2023212447-A2', 'US-6980295-B2', 'AU-2015364602-B2', 'US-2003112494-A1', 'IL-274176-A', 'JP-2014224156-A', 'IL-244029-A0', 'US-2004115131-A1', 'US-2005234013-A1', 'CN-101584047-A', 'AU-2010214112-B2', 'MX-2013002850-A', 'US-2019328740-A1', 'US-2022018060-A1', 'WO-2023225482-A3', 'WO-2024044766-A3', 'AU-2007297661-A1', 'WO-2019067860-A1', 'WO-2024112568-A1', 'CA-2550552-A1', 'PE-20130764-A1', 'US-11014955-B2', 'KR-20110004413-A', 'CN-102584712-A', 'CN-103687626-A', 'CN-102067370-B', 'CA-2718348-C', 'US-11546022-B2', 'HK-1052178-A1', 'US-12025581-B2', 'US-2023155090-A1', 'WO-2010045542-A3', 'EP-3668487-A4', 'CA-2283629-C', 'HK-1250569-A1', 'AU-2004253879-A1', 'WO-2023239670-A1', 'WO-2012158833-A3', 'US-10744347-B2', 'HR-P20201231-T1', 'AU-2409401-A', 'ID-23426-A', 'US-5304932-A', 'AU-3353000-A', 'AU-5938296-A', 'US-2010025717-A1', 'US-2017087258-A1', 'US-2018243924-A1', 'AU-6535890-A']}, 'var_call_asLEDEVZB27JXVJDCCIaMVU9': 'file_storage/call_asLEDEVZB27JXVJDCCIaMVU9.json'}

exec(code, env_args)
