code = """import json
# load full business docs from var_call_jbqZfJnuwdV5EaBTAyM0QEbc (it's a file path)
path = var_call_jbqZfJnuwdV5EaBTAyM0QEbc
with open(path, 'r') as f:
    businesses = json.load(f)
# create mapping from business_id to categories by parsing description field
import re
from collections import defaultdict
biz_cats = {}
for b in businesses:
    bid = b.get('business_id')
    desc = b.get('description') or ''
    # try to extract categories list by taking text after 'offers' or 'offers a range of' or 'offers a range of services in'
    # simpler: split by commas and take last 6 tokens — but better: look for known pattern: categories often appear after 'in the category of' or 'in the categories of' or 'including'
    # We'll heuristically extract text after keywords like 'including', 'offers a range of services in', 'in the category of', 'offers a range of', 'offers a range of options in the fields of', 'offers a diverse range of services'
    cats_text = None
    keywords = ['in the category of', 'in the categories of', 'including', 'offers a range of services in', 'offers a range of', 'offers a diverse range of services', 'offers a range of services and products in the fields of', 'offers a range of services and dining options, including']
    low = desc.lower()
    for kw in keywords:
        if kw in low:
            idx = low.find(kw)
            cats_text = desc[idx+len(kw):]
            break
    if cats_text is None:
        # fallback: if 'offers' present, take substring after 'offers'
        if 'offers' in low:
            idx = low.find('offers')
            cats_text = desc[idx+6:]
        else:
            cats_text = desc
    # remove location/address prefix if present like 'Located at ...,'
    # if there is a comma followed by a space and then a capital letter starting the categories, we try to find the last comma
    # split by '.' then take first sentence's tail
    # Now split by commas and ampersand 'and'
    # Clean punctuation
    cats_text = cats_text.replace(' and ', ', ')
    # remove leading non-letter characters
    cats_text = cats_text.strip(' .:,')
    parts = [p.strip() for p in re.split('[,;/]', cats_text) if p.strip()]
    # take up to first 8 parts and further split by ' & '
    cats = []
    for p in parts[:8]:
        # remove phrases like 'this establishment', 'making it a must-visit for anyone seeking', 'perfect for any occasion', 'to meet all your' etc
        if any(phr in p.lower() for phr in ['located at','this establishment','this facility','this business','making it','perfect for','offers a range','offers a diverse','offers a delightful','offers a wide range']):
            continue
        # remove leading words like 'services', 'products', 'a range of'
        p = re.sub('^the category of\s*','', p, flags=re.I)
        p = re.sub('^categories of\s*','', p, flags=re.I)
        p = re.sub('^services in\s*','', p, flags=re.I)
        p = re.sub("^in\s*","", p, flags=re.I)
        # split by ' & ' and ' and '
        subparts = [s.strip() for s in re.split('&| and ', p) if s.strip()]
        for s in subparts:
            # discard generic words
            s = s.strip(" '")
            if len(s)>2:
                cats.append(s)
    # dedupe preserving order
    seen=set(); final=[]
    for c in cats:
        cl = c.strip().rstrip('.')
        if cl.lower() not in seen:
            seen.add(cl.lower())
            final.append(cl)
    if not final:
        final = ['Unknown']
    biz_cats[bid]=final
# Now load business_ids of interest from var_call_5JoXQQh8MQ7MuvtrjexrnNbz
selected = var_call_5JoXQQh8MQ7MuvtrjexrnNbz
# For each selected business, get its categories
out = []
for b in selected:
    out.append({'business_id': b, 'categories': biz_cats.get(b, ['Unknown'])})
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_C9gA9czJgE1kmFaMnAjscayn': ['business', 'checkin'], 'var_call_V0LGPGxIBep3CChi8UbohmAA': ['review', 'tip', 'user'], 'var_call_0N3RlRFVtiXSjGGaRWdPea0E': 'file_storage/call_0N3RlRFVtiXSjGGaRWdPea0E.json', 'var_call_EDh0gbiart0jlgrNHLeTcg8Z': [{'user_id': 'userid_746', 'yelping_since': '2016-06-23 01:59:28'}, {'user_id': 'userid_1109', 'yelping_since': '2016-10-16 18:32:25'}, {'user_id': 'userid_1950', 'yelping_since': '2016-04-16 03:42:28'}, {'user_id': 'userid_1316', 'yelping_since': '2016-12-29 21:32:44'}, {'user_id': 'userid_1182', 'yelping_since': '2016-03-20 18:41:14'}, {'user_id': 'userid_151', 'yelping_since': '2016-11-07 18:40:10'}, {'user_id': 'userid_1158', 'yelping_since': '2016-01-31 16:25:04'}, {'user_id': 'userid_508', 'yelping_since': '2016-07-08 22:37:42'}, {'user_id': 'userid_435', 'yelping_since': '2016-10-31 09:46:54'}, {'user_id': 'userid_958', 'yelping_since': '2016-03-23 20:55:45'}, {'user_id': 'userid_1879', 'yelping_since': '2016-07-08 17:56:11'}, {'user_id': 'userid_308', 'yelping_since': '2016-07-02 23:48:36'}, {'user_id': 'userid_1179', 'yelping_since': '2016-12-18 17:31:52'}, {'user_id': 'userid_324', 'yelping_since': '2016-10-10 22:09:08'}, {'user_id': 'userid_863', 'yelping_since': '2016-01-16 00:45:41'}, {'user_id': 'userid_100', 'yelping_since': '2016-08-18 11:39:42'}, {'user_id': 'userid_1333', 'yelping_since': '2016-12-07 14:57:41'}, {'user_id': 'userid_1636', 'yelping_since': '2016-02-14 23:51:28'}, {'user_id': 'userid_1850', 'yelping_since': '2016-07-22 19:26:01'}, {'user_id': 'userid_711', 'yelping_since': '2016-07-07 22:59:48'}, {'user_id': 'userid_729', 'yelping_since': '2016-02-06 00:41:18'}, {'user_id': 'userid_1505', 'yelping_since': '2016-07-14 00:26:46'}, {'user_id': 'userid_1315', 'yelping_since': '2016-03-07 02:47:32'}, {'user_id': 'userid_1708', 'yelping_since': '2016-03-06 20:06:53'}, {'user_id': 'userid_1661', 'yelping_since': '2016-06-13 00:48:17'}, {'user_id': 'userid_850', 'yelping_since': '2016-04-05 22:20:15'}, {'user_id': 'userid_1675', 'yelping_since': '2016-02-13 20:18:19'}, {'user_id': 'userid_227', 'yelping_since': '2016-01-16 01:12:00'}, {'user_id': 'userid_577', 'yelping_since': '2016-08-05 21:32:23'}, {'user_id': 'userid_257', 'yelping_since': '2016-10-19 21:58:32'}, {'user_id': 'userid_598', 'yelping_since': '2016-07-24 20:27:40'}, {'user_id': 'userid_847', 'yelping_since': '2016-08-04 20:28:55'}, {'user_id': 'userid_673', 'yelping_since': '2016-09-29 14:11:39'}, {'user_id': 'userid_1856', 'yelping_since': '2016-11-19 23:19:11'}, {'user_id': 'userid_384', 'yelping_since': '2016-04-21 20:00:19'}, {'user_id': 'userid_935', 'yelping_since': '2016-03-04 03:53:07'}, {'user_id': 'userid_210', 'yelping_since': '2016-06-24 03:16:47'}, {'user_id': 'userid_1101', 'yelping_since': '2016-06-13 19:58:37'}, {'user_id': 'userid_945', 'yelping_since': '2016-05-08 04:31:48'}, {'user_id': 'userid_842', 'yelping_since': '2016-02-21 19:02:44'}, {'user_id': 'userid_1351', 'yelping_since': '2016-03-30 02:56:55'}, {'user_id': 'userid_230', 'yelping_since': '2016-09-28 21:47:27'}, {'user_id': 'userid_593', 'yelping_since': '2016-11-18 05:33:16'}, {'user_id': 'userid_1431', 'yelping_since': '2016-01-06 23:48:07'}, {'user_id': 'userid_686', 'yelping_since': '2016-02-20 02:24:38'}, {'user_id': 'userid_527', 'yelping_since': '2016-06-26 04:19:08'}, {'user_id': 'userid_244', 'yelping_since': '2016-02-06 05:06:29'}, {'user_id': 'userid_393', 'yelping_since': '2016-08-16 18:42:51'}, {'user_id': 'userid_1178', 'yelping_since': '2016-05-05 18:04:24'}, {'user_id': 'userid_526', 'yelping_since': '2016-12-16 00:17:31'}, {'user_id': 'userid_90', 'yelping_since': '2016-07-14 00:52:49'}, {'user_id': 'userid_238', 'yelping_since': '2016-12-29 01:41:33'}, {'user_id': 'userid_1105', 'yelping_since': '2016-03-15 21:53:34'}], 'var_call_0SPLx64PFDHEIjiJLbNcXPII': [{'business_ref': 'businessref_74', 'date': '2021-07-16 17:24:00'}, {'business_ref': 'businessref_57', 'date': 'September 04, 2017 at 08:57 PM'}, {'business_ref': 'businessref_96', 'date': 'August 06, 2016 at 02:19 AM'}, {'business_ref': 'businessref_45', 'date': 'August 10, 2016 at 04:36 AM'}, {'business_ref': 'businessref_74', 'date': 'April 17, 2016 at 12:00 AM'}, {'business_ref': 'businessref_53', 'date': '25 Nov 2016, 20:04'}, {'business_ref': 'businessref_41', 'date': 'December 12, 2017 at 02:27 AM'}, {'business_ref': 'businessref_96', 'date': '2017-01-06 11:15:06'}, {'business_ref': 'businessref_10', 'date': '2021-11-28 23:56:00'}, {'business_ref': 'businessref_66', 'date': 'November 10, 2021 at 06:40 AM'}, {'business_ref': 'businessref_31', 'date': '24 Jan 2017, 19:28'}, {'business_ref': 'businessref_92', 'date': '2019-11-14 17:06:00'}, {'business_ref': 'businessref_26', 'date': '2018-07-23 06:45:43'}, {'business_ref': 'businessref_98', 'date': '2017-11-17 16:06:00'}, {'business_ref': 'businessref_45', 'date': 'February 06, 2018 at 07:29 PM'}, {'business_ref': 'businessref_45', 'date': 'October 28, 2016 at 03:54 PM'}, {'business_ref': 'businessref_36', 'date': '2018-05-21 17:51:00'}, {'business_ref': 'businessref_14', 'date': 'May 04, 2017 at 11:25 PM'}, {'business_ref': 'businessref_86', 'date': '2019-04-14 23:08:41'}, {'business_ref': 'businessref_57', 'date': 'October 30, 2018 at 01:06 PM'}, {'business_ref': 'businessref_13', 'date': 'August 22, 2021 at 12:11 AM'}, {'business_ref': 'businessref_68', 'date': 'October 14, 2018 at 04:06 PM'}, {'business_ref': 'businessref_36', 'date': '2016-12-02 00:06:00'}, {'business_ref': 'businessref_60', 'date': '2017-03-24 23:59:00'}, {'business_ref': 'businessref_20', 'date': '27 May 2017, 00:50'}, {'business_ref': 'businessref_15', 'date': 'June 20, 2018 at 02:12 PM'}, {'business_ref': 'businessref_62', 'date': '2018-04-01 10:52:37'}, {'business_ref': 'businessref_33', 'date': 'August 18, 2016 at 11:57 AM'}, {'business_ref': 'businessref_37', 'date': '2016-07-24 20:27:00'}, {'business_ref': 'businessref_92', 'date': '30 Dec 2018, 18:49'}, {'business_ref': 'businessref_66', 'date': 'June 21, 2020 at 07:59 PM'}, {'business_ref': 'businessref_33', 'date': 'August 30, 2019 at 06:15 PM'}, {'business_ref': 'businessref_6', 'date': '30 Jun 2017, 04:44'}, {'business_ref': 'businessref_12', 'date': 'October 26, 2017 at 11:10 PM'}, {'business_ref': 'businessref_79', 'date': '30 Oct 2017, 01:27'}, {'business_ref': 'businessref_60', 'date': '2019-05-29 19:46:00'}], 'var_call_5JoXQQh8MQ7MuvtrjexrnNbz': ['businessid_10', 'businessid_12', 'businessid_13', 'businessid_14', 'businessid_15', 'businessid_20', 'businessid_26', 'businessid_31', 'businessid_33', 'businessid_36', 'businessid_37', 'businessid_41', 'businessid_45', 'businessid_53', 'businessid_57', 'businessid_6', 'businessid_60', 'businessid_62', 'businessid_66', 'businessid_68', 'businessid_74', 'businessid_79', 'businessid_86', 'businessid_92', 'businessid_96', 'businessid_98'], 'var_call_jbqZfJnuwdV5EaBTAyM0QEbc': 'file_storage/call_jbqZfJnuwdV5EaBTAyM0QEbc.json'}

exec(code, env_args)
