code = """import json, re
from collections import defaultdict

business_file = var_call_bMlI0wwqqGU76zQ64hXscDNu
with open(business_file, 'r') as f:
    businesses = json.load(f)
reviews = var_call_ZeNfPgJ79XsLq31ozHPuH1PT

biz_to_cats = {}

for b in businesses:
    bid = b.get('business_id')
    if not bid:
        continue
    if bid.startswith('businessid_'):
        suffix = bid.split('_', 1)[1]
        bref = 'businessref_' + suffix
    else:
        bref = bid

    cats = []
    if 'categories' in b and b['categories']:
        c = b['categories']
        if isinstance(c, list):
            cats = [str(x).strip() for x in c if x]
        else:
            cats = [x.strip() for x in str(c).split(',') if x.strip()]
    else:
        desc = b.get('description') or ''
        part = desc
        # try common markers
        for marker in [' in ', ' including ', ' category of ', ' offers ', ' offering ']:
            if marker in desc:
                part = desc.split(marker)[-1]
                break
        part = part.strip().strip('.')
        # take last up to 3 comma-separated segments
        tokens = [t.strip() for t in part.split(',') if t.strip()]
        if tokens:
            cand = ', '.join(tokens[-3:])
        else:
            cand = part
        toks = []
        for piece in cand.split(','):
            for sub in piece.split(' and '):
                sub = sub.strip()
                # remove common leading phrases
                for prefix in ['this establishment offers', 'this facility offers', 'offers a range of services in', 'offers a range of services,', 'offers', 'providing a range of services in', 'provides', 'offering']:
                    if sub.lower().startswith(prefix):
                        sub = sub[len(prefix):].strip()
                if sub:
                    toks.append(sub)
        clean = []
        for t in toks:
            if 'need' in t.lower() or 'offers' in t.lower():
                continue
            t = t.strip(' .')
            if t.lower().startswith('the '):
                t = t[4:]
            if t:
                clean.append(t)
        cats = clean

    # normalize and split further
    norm = []
    for c in cats:
        if not isinstance(c, str):
            c = str(c)
        parts = [p.strip() for p in re.split('[/&]', c)]
        for p in parts:
            for q in p.split(' and '):
                qq = q.strip().strip("'\".")
                if qq:
                    norm.append(qq)
    # dedupe
    norm = list(dict.fromkeys(norm))
    if norm:
        biz_to_cats[bref] = norm

cat_counts = defaultdict(int)
missing = set()
for r in reviews:
    bref = r.get('business_ref')
    if not bref:
        continue
    cats = biz_to_cats.get(bref)
    if not cats:
        missing.add(bref)
        continue
    for c in cats:
        cat_counts[c] += 1

# try recover missing from businessid mapping
if missing:
    id_map = {b.get('business_id'): b for b in businesses if b.get('business_id')}
    for mb in list(missing):
        if mb.startswith('businessref_'):
            suffix = mb.split('_',1)[1]
            bid = 'businessid_' + suffix
            b = id_map.get(bid)
            if not b:
                continue
            # extract categories same as above
            cats = []
            if 'categories' in b and b['categories']:
                c = b['categories']
                if isinstance(c, list):
                    cats = [str(x).strip() for x in c if x]
                else:
                    cats = [x.strip() for x in str(c).split(',') if x.strip()]
            else:
                desc = b.get('description') or ''
                part = desc
                for marker in [' in ', ' including ', ' category of ', ' offers ', ' offering ']:
                    if marker in desc:
                        part = desc.split(marker)[-1]
                        break
                part = part.strip().strip('.')
                tokens = [t.strip() for t in part.split(',') if t.strip()]
                if tokens:
                    cand = ', '.join(tokens[-3:])
                else:
                    cand = part
                toks = []
                for piece in cand.split(','):
                    for sub in piece.split(' and '):
                        sub = sub.strip()
                        for prefix in ['this establishment offers', 'this facility offers', 'offers a range of services in', 'offers a range of services,', 'offers', 'providing a range of services in', 'provides', 'offering']:
                            if sub.lower().startswith(prefix):
                                sub = sub[len(prefix):].strip()
                        if sub:
                            toks.append(sub)
                clean = []
                for t in toks:
                    if 'need' in t.lower() or 'offers' in t.lower():
                        continue
                    t = t.strip(' .')
                    if t.lower().startswith('the '):
                        t = t[4:]
                    if t:
                        clean.append(t)
                cats = clean
            norm = []
            for c in cats:
                if not isinstance(c, str):
                    c = str(c)
                parts = [p.strip() for p in re.split('[/&]', c)]
                for p in parts:
                    for q in p.split(' and '):
                        qq = q.strip().strip("'\".")
                        if qq:
                            norm.append(qq)
            norm = list(dict.fromkeys(norm))
            if norm:
                biz_to_cats[mb] = norm
                missing.discard(mb)
                for r in reviews:
                    if r.get('business_ref') == mb:
                        for c in norm:
                            cat_counts[c] += 1

sorted_cats = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = [{'category': k, 'review_count': v} for k, v in sorted_cats[:5]]

print("__RESULT__:")
print(json.dumps(top5))"""

env_args = {'var_call_FtQDs9t37b9ajoV5oHsKXbyM': ['business', 'checkin'], 'var_call_NGylznUif9kP3DVOxx6U7Kty': ['review', 'tip', 'user'], 'var_call_bMlI0wwqqGU76zQ64hXscDNu': 'file_storage/call_bMlI0wwqqGU76zQ64hXscDNu.json', 'var_call_bSAzqTmdc7kL5ATaGnt3s2CC': [{'user_id': 'userid_746'}, {'user_id': 'userid_1109'}, {'user_id': 'userid_1950'}, {'user_id': 'userid_1316'}, {'user_id': 'userid_1182'}, {'user_id': 'userid_151'}, {'user_id': 'userid_1158'}, {'user_id': 'userid_508'}, {'user_id': 'userid_435'}, {'user_id': 'userid_958'}, {'user_id': 'userid_1879'}, {'user_id': 'userid_308'}, {'user_id': 'userid_1179'}, {'user_id': 'userid_324'}, {'user_id': 'userid_863'}, {'user_id': 'userid_100'}, {'user_id': 'userid_1333'}, {'user_id': 'userid_1636'}, {'user_id': 'userid_1850'}, {'user_id': 'userid_711'}, {'user_id': 'userid_729'}, {'user_id': 'userid_1505'}, {'user_id': 'userid_1315'}, {'user_id': 'userid_1708'}, {'user_id': 'userid_1661'}, {'user_id': 'userid_850'}, {'user_id': 'userid_1675'}, {'user_id': 'userid_227'}, {'user_id': 'userid_577'}, {'user_id': 'userid_257'}, {'user_id': 'userid_598'}, {'user_id': 'userid_847'}, {'user_id': 'userid_673'}, {'user_id': 'userid_1856'}, {'user_id': 'userid_384'}, {'user_id': 'userid_935'}, {'user_id': 'userid_210'}, {'user_id': 'userid_1101'}, {'user_id': 'userid_945'}, {'user_id': 'userid_842'}, {'user_id': 'userid_1351'}, {'user_id': 'userid_230'}, {'user_id': 'userid_593'}, {'user_id': 'userid_1431'}, {'user_id': 'userid_686'}, {'user_id': 'userid_527'}, {'user_id': 'userid_244'}, {'user_id': 'userid_393'}, {'user_id': 'userid_1178'}, {'user_id': 'userid_526'}, {'user_id': 'userid_90'}, {'user_id': 'userid_238'}, {'user_id': 'userid_1105'}], 'var_call_ZeNfPgJ79XsLq31ozHPuH1PT': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}]}

exec(code, env_args)
