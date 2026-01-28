code = """import json
import re
from collections import Counter

# Load data from previous tool calls
reviews = var_call_vunatd67HdPvDqcvMKa4Hlk7

# Load full businesses JSON from file path
with open(var_call_g2U3xDmTwFulr4TehhB3PpzP, 'r') as f:
    businesses = json.load(f)

biz_map = {b.get('business_id'): b.get('description', '') for b in businesses}

patterns = [
    'in the category of (.*)$',
    'offers a range of services in (.*)$',
    'offers a diverse selection.* in (.*)$',
    'offers .* in (.*)$',
    'specializes in (.*)$'
]

def extract_categories(desc):
    if not desc or not isinstance(desc, str):
        return []
    desc = desc.strip()
    cat_text = None
    for pat in patterns:
        m = re.search(pat, desc, flags=re.IGNORECASE)
        if m:
            cat_text = m.group(1)
            break
    if not cat_text:
        idx = desc.lower().rfind(' in ')
        if idx != -1:
            cat_text = desc[idx+4:]
        else:
            cat_text = desc
    cat_text = cat_text.strip().strip('.')
    # Split into candidate categories using common separators and the word ' and '
    parts = re.split(',|;|/| and | & | or ', cat_text)
    cats = []
    for p in parts:
        p = p.strip()
        # remove surrounding quotes
        p = p.strip('\"\'')
        if not p:
            continue
        p = re.sub('^(the )?(categories?|fields?|category) of ', '', p, flags=re.IGNORECASE)
        p = p.strip()
        if p:
            cats.append(p)
    cats = [re.sub('\s+', ' ', c).strip() for c in cats]
    return cats

cnt = Counter()
missing = 0
for r in reviews:
    bref = r.get('business_ref')
    if not bref:
        continue
    bid = bref.replace('businessref_', 'businessid_')
    desc = biz_map.get(bid)
    if not desc:
        missing += 1
        continue
    cats = extract_categories(desc)
    for c in cats:
        cnt[c] += 1

top5 = cnt.most_common(5)
result = [{'category': k, 'review_count': v} for k, v in top5]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FO5COTDed15BouxvA7m79yeV': ['checkin', 'business'], 'var_call_Xxu9cV1liPI4Hh7Y6vyHn9Wz': ['review', 'tip', 'user'], 'var_call_rWH0w2w6NH9QL5VSFjRC6v8J': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_g2U3xDmTwFulr4TehhB3PpzP': 'file_storage/call_g2U3xDmTwFulr4TehhB3PpzP.json', 'var_call_vunatd67HdPvDqcvMKa4Hlk7': [{'review_id': 'reviewid_318', 'user_id': 'userid_1101', 'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'review_id': 'reviewid_1049', 'user_id': 'userid_1105', 'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'review_id': 'reviewid_454', 'user_id': 'userid_863', 'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'review_id': 'reviewid_1065', 'user_id': 'userid_308', 'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'review_id': 'reviewid_704', 'user_id': 'userid_729', 'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'review_id': 'reviewid_84', 'user_id': 'userid_935', 'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'review_id': 'reviewid_1110', 'user_id': 'userid_1856', 'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'review_id': 'reviewid_655', 'user_id': 'userid_435', 'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'review_id': 'reviewid_1239', 'user_id': 'userid_1178', 'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'review_id': 'reviewid_515', 'user_id': 'userid_1109', 'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'review_id': 'reviewid_44', 'user_id': 'userid_593', 'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'review_id': 'reviewid_65', 'user_id': 'userid_1182', 'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'review_id': 'reviewid_1216', 'user_id': 'userid_230', 'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'review_id': 'reviewid_781', 'user_id': 'userid_244', 'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'review_id': 'reviewid_334', 'user_id': 'userid_1316', 'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'review_id': 'reviewid_124', 'user_id': 'userid_324', 'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'review_id': 'reviewid_957', 'user_id': 'userid_1850', 'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'review_id': 'reviewid_1174', 'user_id': 'userid_686', 'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'review_id': 'reviewid_1502', 'user_id': 'userid_1950', 'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'review_id': 'reviewid_919', 'user_id': 'userid_945', 'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'review_id': 'reviewid_926', 'user_id': 'userid_1179', 'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'review_id': 'reviewid_1457', 'user_id': 'userid_1879', 'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'review_id': 'reviewid_1576', 'user_id': 'userid_850', 'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'review_id': 'reviewid_1677', 'user_id': 'userid_958', 'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'review_id': 'reviewid_160', 'user_id': 'userid_1661', 'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'review_id': 'reviewid_1207', 'user_id': 'userid_210', 'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'review_id': 'reviewid_1635', 'user_id': 'userid_151', 'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'review_id': 'reviewid_1966', 'user_id': 'userid_100', 'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'review_id': 'reviewid_1791', 'user_id': 'userid_598', 'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'review_id': 'reviewid_1986', 'user_id': 'userid_746', 'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'review_id': 'reviewid_1137', 'user_id': 'userid_1675', 'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'review_id': 'reviewid_1555', 'user_id': 'userid_1505', 'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'review_id': 'reviewid_1408', 'user_id': 'userid_842', 'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'review_id': 'reviewid_1388', 'user_id': 'userid_257', 'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'review_id': 'reviewid_62', 'user_id': 'userid_1333', 'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'review_id': 'reviewid_280', 'user_id': 'userid_711', 'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
