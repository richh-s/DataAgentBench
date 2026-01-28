code = """import json, re
# Access previous tool results from storage variables
allrecs_path = var_call_5I4DtjpcM4Fv7fjmRPlhswNj
with open(allrecs_path, 'r') as f:
    allrecs = json.load(f)
# var_call_icvb... contains result with 'univ_pubnums'
univ_info = var_call_icvbIiMtDvkLH9LESvKq8EtC
univ_pubnums = set(univ_info.get('univ_pubnums', []))

# Build map of cited publication numbers -> citing records
pub_to_citing = {}
for rec in allrecs:
    citations = rec.get('citation') or []
    if isinstance(citations, str):
        try:
            citations = json.loads(citations)
        except:
            citations = []
    if not isinstance(citations, list):
        continue
    for c in citations:
        if isinstance(c, dict):
            p = (c.get('publication_number') or '').upper().strip().rstrip('.').rstrip(',')
            if p:
                pub_to_citing.setdefault(p, []).append(rec)

# Helper to extract assignee
def extract_assignee(pi):
    if not pi:
        return None
    s = pi.strip()
    # common forms: 'X holds the ...', 'In US, the application ... is assigned to X and has publication number Y.'
    # Try pattern '... is assigned to X and has' or 'is owned by X and has'
    m = re.search(r'IS ASSIGNED TO\s+([^,\.]+)', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'OWNED BY\s+([^,\.]+)', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'IS OWNED BY\s+([^,\.]+)', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'HOLDS\s+the\s+[^,\.]+\s+\((?:application|app\.|ID|number)\s+[^)]+\)', s, flags=re.IGNORECASE)
    if m:
        # try to get leading token before 'holds'
        parts = re.split(r'\s+holds\b', s, flags=re.IGNORECASE)
        return parts[0].strip()
    # pattern 'X holds the US patent application (ID ...), with publication number ...'
    m = re.search(r'^(.*?)\s+HOLDS\b', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # pattern 'The US application (number ...) is owned by X and has pub. number ...'
    m = re.search(r'\)\s+IS OWNED BY\s+([^,\.]+)', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # pattern '... is belonging to X and has publication'
    m = re.search(r'BELONGING TO\s+([^,\.]+)', s, flags=re.IGNORECASE)
    if m:
        return m.group(1).strip()
    # fallback: take leading segment before comma or '('
    parts = re.split(r',|\(', s)
    if parts:
        return parts[0].strip()
    return s

assignee_to_codes = {}
all_codes = set()
for up in univ_pubnums:
    citing = pub_to_citing.get(up, [])
    for rec in citing:
        pi = rec.get('Patents_info') or ''
        assignee = extract_assignee(pi)
        if not assignee:
            continue
        an_upper = re.sub(r'\s+', ' ', assignee).strip().upper()
        if 'UNIV' in an_upper and 'CALIFORNIA' in an_upper:
            continue
        # get primary CPC
        primary = None
        cpc_field = rec.get('cpc')
        if cpc_field:
            try:
                cpcs = json.loads(cpc_field)
            except:
                cpcs = []
            if isinstance(cpcs, list) and cpcs:
                for it in cpcs:
                    if isinstance(it, dict) and it.get('first'):
                        primary = it.get('code'); break
                if not primary and isinstance(cpcs[0], dict):
                    primary = cpcs[0].get('code')
        if not primary:
            continue
        norm = re.sub(r'[^A-Z0-9 &\-\.]+',' ', an_upper).strip()
        assignee_to_codes.setdefault(norm, set()).add(primary)
        all_codes.add(primary)

# Prepare output
entries = [{'assignee': a, 'codes': sorted(list(codes))} for a, codes in assignee_to_codes.items()]
out = {'entries': entries, 'codes': sorted(list(all_codes)), 'univ_pubnum_count': len(univ_pubnums)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5I4DtjpcM4Fv7fjmRPlhswNj': 'file_storage/call_5I4DtjpcM4Fv7fjmRPlhswNj.json', 'var_call_3VyetCwrZExI2Xpet9Um2Z3I': 'file_storage/call_3VyetCwrZExI2Xpet9Um2Z3I.json', 'var_call_aQiaaKewuvuNUgNV4DvyEt09': {'pairs': [], 'codes': []}, 'var_call_dEoQDTzU3g8MBJxJTTtcYTmC': 'file_storage/call_dEoQDTzU3g8MBJxJTTtcYTmC.json', 'var_call_nxN5eBvJXYwbAZgZ0FnUqKrV': [], 'var_call_Lb2aFYNCzIUGMiHjFYMERzCW': 'file_storage/call_Lb2aFYNCzIUGMiHjFYMERzCW.json', 'var_call_ejIAYQLOHqeJ95QlU8d5FeRT': {'univ_pubnums': [], 'assignees': {}, 'codes': []}, 'var_call_t4S4NSfolHw3HxJaXMVQ6zn0': ['In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.', 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.', 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.', 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.', 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.', 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.', 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.', 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.', 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.', 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.', 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.', 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.', 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.', 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.', 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.', 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.', 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.', 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.', 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.', 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'], 'var_call_Igfcem8S67QyNMRoogvuC7Hx': ['US-11081687-B2', 'US-10794458-B2', 'US-11124615-B2', 'US-10610606-B2', 'US-10957507-B2', 'US-10933114-B2', 'US-11169125-B2', 'US-10695419-B2', 'US-10950222-B2', 'US-11168653-B2', 'US-10853219-B2', 'US-11136369-B2', 'US-11076136-B2', 'US-10898606-B2', 'US-11182846-B2', 'US-11130385-B2', 'US-10720793-B2', 'US-11141094-B2', 'US-10918785-B2', 'US-11601114-B2', 'US-10924243-B2', 'US-11018783-B2', 'US-11072514-B2', 'US-10859440-B2', 'US-10875306-B2', 'US-10692314-B2', 'US-10904976-B2', 'US-10704655-B2', 'US-10897184-B2', 'US-10826200-B2', 'US-11128943-B2', 'US-10809655-B2', 'US-11273226-B2', 'US-11024606-B2', 'US-11231876-B2', 'US-11126940-B2', 'US-11911287-B2', 'US-10868205-B2', 'US-11082077-B2', 'US-11202094-B2', 'US-11025166-B2', 'US-10974840-B2', 'US-11032098-B2', 'US-11713774-B2', 'US-11307152-B2', 'US-11371080-B2', 'US-11478419-B2', 'US-11137932-B2', 'US-11813423-B2', 'US-10868012-B2'], 'var_call_zKZnqCokJgv0xKzGi1atG7xH': {'univ_pubnums': ['US-201916400501-A', 'US-201917255566-A', 'US-202017075052-A', 'US-202117198827-A'], 'assignees': {}, 'codes': []}, 'var_call_e2fEOEju9owEpr8d19Prk6Nj': 'file_storage/call_e2fEOEju9owEpr8d19Prk6Nj.json', 'var_call_R7wHNTeats3Jq8IUN9URcP36': {'univ_pubnums_count': 0, 'univ_pubnums_sample': [], 'assignees': {}, 'codes': []}, 'var_call_2AYs5vG1e9GMqwRPrOEZJfYX': 'file_storage/call_2AYs5vG1e9GMqwRPrOEZJfYX.json', 'var_call_dLVGDnQitturZmwAgxZRBHDg': {'univ_pub_count': 0, 'univ_pub_sample': [], 'assignee_to_codes': {}, 'codes': []}, 'var_call_Gdeak1GPadEOCEiU4f5Odv3S': [], 'var_call_bxjjFNUUaQim1772RZFO1gUL': [{'idx': 0, 'rowid': '1173', 'Patents_info': 'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.'}, {'idx': 1, 'rowid': '6244', 'Patents_info': 'UNIV CALIFORNIA holds the TW patent filing (app. number TW-107142982-A), with pub. number TW-201925402-A.'}, {'idx': 2, 'rowid': '6967', 'Patents_info': 'In US, the patent application (no. US-201916454755-A) is assigned to UNIV CALIFORNIA and has publication number US-11421276-B2.'}, {'idx': 3, 'rowid': '10358', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent application (no. AU-2019275518-A), with pub. number AU-2019275518-B2.'}, {'idx': 4, 'rowid': '14719', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (no. US-201515313510-A), with publication no. US-2017194630-A1.'}, {'idx': 5, 'rowid': '17880', 'Patents_info': 'The JP patent filing (application no. JP-13313985-A) is assigned to UNIV CALIFORNIA and has pub. number JP-S6163700-A.'}, {'idx': 6, 'rowid': '20566', 'Patents_info': 'The US patent application (number US-201715625819-A) is assigned to UNIV CALIFORNIA and has pub. number US-2017281687-A1.'}, {'idx': 7, 'rowid': '21654', 'Patents_info': 'UNIV CALIFORNIA holds the EP patent application (ID EP-00992018-A), with publication no. EP-1224461-B1.'}, {'idx': 8, 'rowid': '23096', 'Patents_info': 'The AU application (number AU-2003247814-A) is belonging to UNIV CALIFORNIA and has publication number AU-2003247814-A1.'}, {'idx': 9, 'rowid': '26944', 'Patents_info': 'Patent filing (application no. AU-2017356943-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2017356943-A1.'}, {'idx': 10, 'rowid': '28157', 'Patents_info': 'The EP patent filing (app. number EP-21763795-A) is owned by THE REGENTS OF UNIV OF CALIFORNIA and has publication number EP-4114888-A1.'}, {'idx': 11, 'rowid': '29441', 'Patents_info': 'The US patent filing (app. number US-39548599-A) is held by UNIV CALIFORNIA AT SAN DIEGO and has publication number US-6237292-B1.'}, {'idx': 12, 'rowid': '31022', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-55161904-A), with publication number US-7745569-B2.'}, {'idx': 13, 'rowid': '31321', 'Patents_info': 'The US patent filing (application no. US-201515329526-A) is owned by UNIV CALIFORNIA and has publication number US-11072681-B2.'}, {'idx': 14, 'rowid': '31849', 'Patents_info': 'UNIV CALIFORNIA holds the AU application (ID AU-2002254753-A), with publication no. AU-2002254753-B2.'}, {'idx': 15, 'rowid': '32410', 'Patents_info': 'In US, the application (no. US-201313787160-A) is belonging to UNIV CALIFORNIA and has pub. number US-9061071-B2.'}, {'idx': 16, 'rowid': '38103', 'Patents_info': 'In KR, the patent application (ID KR-20057010360-A) is held by UNIV CALIFORNIA and has publication number KR-20050085437-A.'}, {'idx': 17, 'rowid': '38489', 'Patents_info': 'Patent application (number KR-20167024476-A) from KR, owned by UNIV CALIFORNIA, with publication number KR-20160119166-A.'}, {'idx': 18, 'rowid': '44126', 'Patents_info': 'The EP application (no. EP-96907882-A) is belonging to UNIV CALIFORNIA BUSINESS AND P and has pub. number EP-0826155-A4.'}, {'idx': 19, 'rowid': '45431', 'Patents_info': 'In US, the application (no. US-201916277921-A) is assigned to UNIV CALIFORNIA and has publication number US-2019169580-A1.'}, {'idx': 20, 'rowid': '45586', 'Patents_info': 'In US, the patent application (ID US-202016878973-A) is belonging to UNIV CALIFORNIA and has publication number US-2020283856-A1.'}, {'idx': 21, 'rowid': '46983', 'Patents_info': 'Patent filing (app. number AU-2898989-A) from AU, held by UNIV CALIFORNIA, with publication number AU-2898989-A.'}, {'idx': 22, 'rowid': '47560', 'Patents_info': 'UNIV CALIFORNIA holds the RO patent filing (application no. RO-7944874-A), with pub. number RO-70061-A.'}, {'idx': 23, 'rowid': '49516', 'Patents_info': 'UNIV CALIFORNIA holds the WO patent filing (application number US-2017015812-W), with publication number WO-2017136335-A1.'}, {'idx': 24, 'rowid': '49554', 'Patents_info': 'In WO, the patent application (no. US-2019059638-W) is held by UNIV CALIFORNIA and has publication no. WO-2020096950-A1.'}, {'idx': 25, 'rowid': '51458', 'Patents_info': 'The WO patent filing (application no. US-2020061827-W) is assigned to UNIV CALIFORNIA and has pub. number WO-2021102420-A1.'}, {'idx': 26, 'rowid': '51676', 'Patents_info': 'In WO, the patent filing (app. number US-2012039471-W) is belonging to UNIV CALIFORNIA and has pub. number WO-2012162563-A2.'}, {'idx': 27, 'rowid': '52250', 'Patents_info': 'The US application (ID US-201916537416-A) is owned by UNIV CALIFORNIA and has publication no. US-10900049-B2.'}, {'idx': 28, 'rowid': '52261', 'Patents_info': 'The US patent filing (application no. US-201816612511-A) is assigned to UNIV CALIFORNIA and has pub. number US-11376346-B2.'}, {'idx': 29, 'rowid': '53005', 'Patents_info': 'UNIV CALIFORNIA holds the US patent application (number US-201715646074-A), with publication no. US-2017369950-A1.'}, {'idx': 30, 'rowid': '54178', 'Patents_info': 'UNIV CALIFORNIA holds the KR patent filing (app. number KR-20187008669-A), with publication no. KR-20180041236-A.'}, {'idx': 31, 'rowid': '58433', 'Patents_info': 'The CN patent filing (application no. CN-200380105631-A) is owned by UNIV CALIFORNIA and has pub. number CN-100339724-C.'}, {'idx': 32, 'rowid': '59263', 'Patents_info': 'UNIV SOUTHERN CALIFORNIA holds the IL patent filing (application no. IL-25502617-A), with publication no. IL-255026-A0.'}, {'idx': 33, 'rowid': '59811', 'Patents_info': 'UNIV CALIFORNIA holds the US application (no. US-8864206-A), with publication number US-2009031436-A1.'}, {'idx': 34, 'rowid': '60661', 'Patents_info': 'UNIV CALIFORNIA holds the AU patent filing (application number AU-2005269556-A), with publication number AU-2005269556-A1.'}, {'idx': 35, 'rowid': '60775', 'Patents_info': 'The US patent filing (application no. US-201916362297-A) is assigned to UNIV CALIFORNIA and has publication no. US-11248107-B2.'}, {'idx': 36, 'rowid': '61782', 'Patents_info': 'Patent filing (application no. US-2019021660-W) from WO, assigned to UNIV CALIFORNIA, with publication number WO-2019173834-A1.'}, {'idx': 37, 'rowid': '62158', 'Patents_info': 'UNIV CALIFORNIA holds the US patent filing (app. number US-201715422925-A), with pub. number US-2017145219-A1.'}, {'idx': 38, 'rowid': '62241', 'Patents_info': 'The US patent filing (application no. US-201815950106-A) is held by UNIV CALIFORNIA and has publication no. US-2018304537-A1.'}, {'idx': 39, 'rowid': '62863', 'Patents_info': 'In US, the application (ID US-202016883515-A) is owned by UNIV CALIFORNIA and has publication number US-2021002329-A1.'}, {'idx': 40, 'rowid': '67033', 'Patents_info': 'The KR application (number KR-20207004898-A) is belonging to UNIV CALIFORNIA and has pub. number KR-20200041324-A.'}, {'idx': 41, 'rowid': '67292', 'Patents_info': 'In CN, the application (no. CN-201180052574-A) is belonging to UNIV CALIFORNIA and has pub. number CN-103189548-A.'}, {'idx': 42, 'rowid': '72225', 'Patents_info': 'The CA application (no. CA-2298540-A) is held by UNIV CALIFORNIA and has pub. number CA-2298540-A1.'}, {'idx': 43, 'rowid': '72905', 'Patents_info': 'UNIV CALIFORNIA holds the AU application (number AU-2001296493-A), with publication no. AU-2001296493-B2.'}, {'idx': 44, 'rowid': '72928', 'Patents_info': 'In AU, the application (ID AU-2008329628-A) is belonging to UNIV CALIFORNIA and has publication no. AU-2008329628-B2.'}, {'idx': 45, 'rowid': '73746', 'Patents_info': 'Application (no. US-201916401060-A) from US, assigned to UNIV CALIFORNIA, with publication no. US-10765865-B2.'}, {'idx': 46, 'rowid': '76840', 'Patents_info': 'In JP, the application (ID JP-2004321293-A) is belonging to UNIV CALIFORNIA and has publication number JP-2005104983-A.'}, {'idx': 47, 'rowid': '83278', 'Patents_info': 'The IL patent application (no. IL-14014099-A) is assigned to UNIV CALIFORNIA and has publication no. IL-140140-A0.'}, {'idx': 48, 'rowid': '83857', 'Patents_info': 'The US application (number US-202017021925-A) is assigned to UNIV CALIFORNIA and has pub. number US-2021000566-A1.'}, {'idx': 49, 'rowid': '85989', 'Patents_info': 'In US, the patent application (ID US-17323505-A) is held by UNIV CALIFORNIA and has pub. number US-2006051790-A1.'}], 'var_call_5u6G3Nq3mLlcwZ7JaJJei0te': [], 'var_call_Q1Yn0gzDdJlywK8GztIWlqtg': 'file_storage/call_Q1Yn0gzDdJlywK8GztIWlqtg.json', 'var_call_vzuoC75vu0K7pjeVzCZhS8ja': {'univ_pub_count': 0, 'univ_pubnums_sample': [], 'assignee_to_codes': {}, 'codes': []}, 'var_call_YteJss3LihNXniHaRMamhchJ': {'univ_pub_count': 0, 'univ_pub_sample': [], 'assignee_to_codes': {}, 'codes': []}, 'var_call_hAg448T5YM1Lp1FEDNzVKj18': [], 'var_call_icvbIiMtDvkLH9LESvKq8EtC': {'univ_pub_count': 167, 'univ_pubnums': ['AP-3334-A', 'AU-2001257114-A1', 'AU-2001296493-B2', 'AU-2002254753-B2', 'AU-2003247814-A1', 'AU-2003294429-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2008329628-B2', 'AU-2017356943-A1', 'AU-2409401-A', 'AU-2898989-A', 'AU-3353000-A', 'AU-5366398-A', 'AU-5621298-A', 'AU-564791-B2', 'AU-5938296-A', 'AU-6533598-A', 'AU-767912-B2', 'AU-7724398-A', 'BR-112018069510-A2', 'BR-112021021092-A8', 'BR-9610580-A', 'CA-2220674-A1', 'CA-2278751-A1', 'CA-2283629-C', 'CA-2494262-A1', 'CA-2718348-C', 'CA-3027364-A1', 'CA-3055214-A1', 'CA-3154773-A1', 'CA-3161617-A1', 'CA-3225295-A1', 'CN-101584047-A', 'CN-102348779-A', 'CN-103237558-A', 'CN-103687626-A', 'CN-108603219-A', 'CN-1120376-C', 'DE-1089906-B', 'DK-132341-B', 'EP-1224461-B1', 'EP-2029921-A4', 'EP-2210307-A4', 'EP-2903996-B1', 'EP-3668487-A4', 'EP-3866867-A1', 'EP-4039824-A1', 'EP-4114888-A1', 'EP-4123294-A1', 'FR-2194760-A1', 'HK-1052178-A1', 'IL-140140-A0', 'IL-236725-A', 'IL-255026-A0', 'IL-91330-A0', 'JP-2005104983-A', 'JP-2009260386-A', 'JP-2011101408-A', 'KR-100228821-B1', 'KR-20050043737-A', 'KR-20050085437-A', 'KR-20080078049-A', 'KR-20110004413-A', 'KR-20160119166-A', 'KR-20180041236-A', 'KR-20200084864-A', 'PE-20130764-A1', 'PT-2970346-T', 'US-10337029-B2', 'US-10359432-B2', 'US-10744347-B2', 'US-10746600-B2', 'US-10765865-B2', 'US-10900049-B2', 'US-11014955-B2', 'US-11072681-B2', 'US-11226538-B2', 'US-11248107-B2', 'US-11313722-B2', 'US-11421276-B2', 'US-11445941-B2', 'US-11607427-B2', 'US-11960018-B2', 'US-12025581-B2', 'US-1744990-A', 'US-1858758-A', 'US-2003112494-A1', 'US-2004115131-A1', 'US-2005136639-A1', 'US-2005165588-A1', 'US-2005234013-A1', 'US-2005241084-A1', 'US-2006002432-A1', 'US-2008047008-A1', 'US-2008139409-A1', 'US-2009031436-A1', 'US-2010025717-A1', 'US-2016122192-A1', 'US-2017050153-A1', 'US-2017087258-A1', 'US-2017194630-A1', 'US-2017294981-A1', 'US-2017342455-A1', 'US-2017369950-A1', 'US-2018080022-A1', 'US-2018177786-A1', 'US-2018277766-A1', 'US-2018304537-A1', 'US-2018348310-A1', 'US-2019169580-A1', 'US-2019209590-A1', 'US-2019271597-A1', 'US-2020283856-A1', 'US-2021002329-A1', 'US-2021039104-A1', 'US-2021181673-A1', 'US-2021210965-A1', 'US-2021278215-A1', 'US-2021282642-A1', 'US-2022123166-A1', 'US-2022170091-A1', 'US-2022364168-A1', 'US-2023150660-A1', 'US-2023314781-A1', 'US-2023340506-A1', 'US-2072963-A', 'US-2086055-A', 'US-2381912-A', 'US-2386828-A', 'US-2791757-A', 'US-2850810-A', 'US-2900339-A', 'US-2915879-A', 'US-2975132-A', 'US-3054838-A', 'US-3062706-A', 'US-3073853-A', 'US-3666017-A', 'US-3842373-A', 'US-5023808-A', 'US-5073907-A', 'US-5891398-A', 'US-6030830-A', 'US-6237292-B1', 'US-6559125-B1', 'US-6625368-B1', 'US-6980295-B2', 'US-7052856-B2', 'US-7745569-B2', 'US-8361933-B2', 'US-8764681-B2', 'WO-2010027391-A2', 'WO-2012158833-A3', 'WO-2014152660-A1', 'WO-2017136335-A1', 'WO-2018067976-A1', 'WO-2018152537-A1', 'WO-2019067860-A1', 'WO-2019173834-A1', 'WO-2020096950-A1', 'WO-2022178138-A1', 'WO-2022245977-A2', 'WO-2023212447-A2', 'WO-2023239670-A1', 'WO-2024050335-A2', 'ZA-200802422-B'], 'assignee_to_codes': {}, 'codes': []}, 'var_call_Ham1qVP9ngVDfIlZRVj1kn2d': {'entries': [], 'codes': []}}

exec(code, env_args)
