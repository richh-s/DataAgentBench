code = """import json
import pandas as pd
import re
from datetime import datetime

path = var_call_6s1Hx5RlvxTCOOHk3gPsx0tp
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

def clean_date(s):
    if not s or not isinstance(s, str):
        return None
    s2 = s
    s2 = s2.replace('on ', ' ')
    s2 = s2.replace('dated ', ' ')
    s2 = s2.replace('the ', ' ')
    s2 = re.sub(r"(\d+)(st|nd|rd|th)", r"\1", s2)
    s2 = s2.replace(',', ' ')
    s2 = s2.strip()
    return pd.to_datetime(s2, dayfirst=True, errors='coerce')


def is_germany(pi):
    if not pi: return False
    s = pi.upper()
    if 'GERMANY' in s: return True
    if re.search(r'\bDE\b', s): return True
    if re.search(r'DE[-_]\d', s): return True
    if re.search(r'IN DE,', s): return True
    return False

filtered = []
for r in records:
    gd = clean_date(r.get('grant_date'))
    if gd is None:
        continue
    if not (pd.Timestamp('2019-07-01') <= gd <= pd.Timestamp('2019-12-31')):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    cpc_field = r.get('cpc')
    try:
        cpc_list = json.loads(cpc_field)
    except Exception:
        cpc_list = []
    fd = clean_date(r.get('filing_date'))
    if fd is None:
        continue
    filing_year = int(fd.year)
    for item in cpc_list:
        if isinstance(item, dict):
            code = item.get('code')
        else:
            code = None
        if not code:
            continue
        code = str(code).strip()
        # remove leading non-alnum
        m = re.match(r'([A-Z]\d{2}[A-Z])', code)
        if m:
            group = m.group(1)
        else:
            # fallback take first 4 chars
            group = code[:4]
        filtered.append({'group': group, 'filing_year': filing_year})

if not filtered:
    out = {'groups': []}
    print('__RESULT__:')
    print(json.dumps(out))
else:
    df = pd.DataFrame(filtered)
    counts = df.groupby(['group','filing_year']).size().reset_index(name='count')
    results = []
    for group, grp_df in counts.groupby('group'):
        grp_sorted = grp_df.sort_values('filing_year')
        years = list(grp_sorted['filing_year'])
        vals = list(grp_sorted['count'])
        s = pd.Series(vals, index=years)
        ema = s.ewm(alpha=0.1, adjust=False).mean()
        best_year = int(ema.idxmax())
        best_ema = float(ema.max())
        results.append({'symbol': group, 'best_year': best_year, 'best_ema': best_ema})
    results = sorted(results, key=lambda x: x['best_ema'], reverse=True)
    symbols = [r['symbol'] for r in results]
    out = {'symbols': symbols, 'groups': results}
    print('__RESULT__:')
    print(json.dumps(out))"""

env_args = {'var_call_DOJ8NTBO8k3pUFTiKas6Zehx': 'file_storage/call_DOJ8NTBO8k3pUFTiKas6Zehx.json', 'var_call_3x0kyDCCcHjS363jdKiOeLf0': {'groups': []}, 'var_call_6s1Hx5RlvxTCOOHk3gPsx0tp': 'file_storage/call_6s1Hx5RlvxTCOOHk3gPsx0tp.json', 'var_call_B7VsHRM5f0Jdk9w0iMgkWsUb': {'symbols': [], 'groups': []}, 'var_call_0HrkzCcWSYJ9t2FzyfChU10r': {'count': 69, 'examples': [{'id': '199', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.', 'grant_date': '14th Mar 2019'}, {'id': '9322', 'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'grant_date': 'dated 21st November 2019'}, {'id': '9333', 'Patents_info': 'The DE application (number DE-102009046500-A) is owned by LEAR CORP and has publication number DE-102009046500-B4.', 'grant_date': 'Mar 21st, 2019'}, {'id': '9335', 'Patents_info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'grant_date': '5th of December, 2019'}, {'id': '9348', 'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'grant_date': '22nd of August, 2019'}, {'id': '9350', 'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'grant_date': 'September the 19th, 2019'}, {'id': '9352', 'Patents_info': 'DIEFFENBACHER GMBH MASCHINEN holds the DE patent application (number DE-102016119956-A), with publication number DE-102016119956-B4.', 'grant_date': 'on March 14th, 2019'}, {'id': '10786', 'Patents_info': 'The DE patent filing (application number DE-102018102700-A) is assigned to DIOGO CARLOS ALBERTO RAMOS and has pub. number DE-102018102700-B3.', 'grant_date': '28th Feb 2019'}, {'id': '10828', 'Patents_info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'grant_date': '17th of October, 2019'}, {'id': '10829', 'Patents_info': 'In DE, the patent application (no. DE-102014209298-A) is held by DENSO CORP and has publication number DE-102014209298-B4.', 'grant_date': 'on March 21st, 2019'}, {'id': '12407', 'Patents_info': 'SCHNEIDER KUNSTSTOFFWERKE GMBH holds the DE patent application (no. DE-102014112758-A), with publication number DE-102014112758-B4.', 'grant_date': '7th March 2019'}, {'id': '12410', 'Patents_info': 'BRUKER BIOSPIN GMBH holds the DE application (number DE-102015218019-A), with publication no. DE-102015218019-B4.', 'grant_date': 'February 28th, 2019'}, {'id': '12411', 'Patents_info': 'Application (no. DE-112015005888-T) from DE, belonging to APPLE INC, with publication number DE-112015005888-B4.', 'grant_date': 'August the 29th, 2019'}, {'id': '12412', 'Patents_info': 'The DE application (ID DE-102016102746-A) is belonging to HAWE Altenstadt Holding GmbH and has pub. number DE-102016102746-B4.', 'grant_date': 'dated 4th July 2019'}, {'id': '35820', 'Patents_info': 'FORD GLOBAL TECH LLC holds the DE application (number DE-102014217501-A), with publication no. DE-102014217501-B4.', 'grant_date': '28th March 2019'}, {'id': '35825', 'Patents_info': 'Patent application (number DE-102017201883-A) from DE, belonging to SIEMENS HEALTHCARE GMBH, with publication no. DE-102017201883-B4.', 'grant_date': '2019 on Mar 28th'}, {'id': '60947', 'Patents_info': 'The DE patent filing (application no. DE-102018213557-A) is assigned to BAYERISCHE MOTOREN WERKE AG and has publication number DE-102018213557-B3.', 'grant_date': '26th September 2019'}, {'id': '60978', 'Patents_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'grant_date': '2019, December 24th'}, {'id': '60982', 'Patents_info': 'The DE patent filing (application no. DE-102014012543-A) is held by IFA TECH GMBH and has pub. number DE-102014012543-B4.', 'grant_date': '21st of February, 2019'}, {'id': '60983', 'Patents_info': 'The DE application (number DE-102015121777-A) is held by BOHNERTH OTTO and has publication no. DE-102015121777-B4.', 'grant_date': '2nd Oct 2019'}]}}

exec(code, env_args)
