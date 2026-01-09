code = """import json, pandas as pd

# reviews per business_ref from DuckDB
rev = pd.DataFrame(var_call_IAxKn7y6NUcSQ1eb4KRbR1T4)
if rev.empty:
    out = []
else:
    rev['review_cnt'] = rev['review_cnt'].astype(int)
    # load businesses from mongo dump (file)
    path = var_call_7aD3sDvKS6exOZlTIQZ4Pgrh
    with open(path, 'r') as f:
        biz = pd.DataFrame(json.load(f))
    # map businessid_ -> businessref_
    biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)

    # extract categories from description: text after 'categories of' or 'including'
    def extract_cats(desc):
        if not isinstance(desc, str):
            return []
        s = desc
        cats = None
        if 'categories of' in s:
            cats = s.split('categories of',1)[1]
        elif 'including' in s:
            cats = s.split('including',1)[1]
        elif 'in the category of' in s:
            cats = s.split('in the category of',1)[1]
        else:
            return []
        # trim to sentence end
        for sep in ['.', ' making', ' perfect', ' offering']:
            if sep in cats:
                cats = cats.split(sep,1)[0]
        cats = cats.replace("'", "")
        # split by commas and 'and'
        parts = []
        for p in cats.replace(' and ', ',').split(','):
            p = p.strip()
            if p:
                parts.append(p)
        # de-duplicate preserving order
        seen=set(); out=[]
        for p in parts:
            if p not in seen:
                seen.add(p); out.append(p)
        return out

    biz['categories'] = biz['description'].apply(extract_cats)

    merged = rev.merge(biz[['business_ref','categories']], on='business_ref', how='left')
    merged = merged.explode('categories')
    merged = merged.dropna(subset=['categories'])
    cat_tot = merged.groupby('categories', as_index=False)['review_cnt'].sum()
    cat_tot = cat_tot.sort_values(['review_cnt','categories'], ascending=[False, True]).head(5)
    out = cat_tot.to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_bP3BgILQtC5h9gdmsfBccXAF': [], 'var_call_t08hDTgziaPRQm8zBIBPYfqI': [{'yelping_since': '10 Jun 2013, 17:32', 'n': '2'}, {'yelping_since': '2005-07-18 06:22:37', 'n': '1'}, {'yelping_since': 'May 21, 2011 at 03:22 PM', 'n': '1'}, {'yelping_since': '22 Jul 2007, 21:50', 'n': '1'}, {'yelping_since': '2009-04-30 03:16:12', 'n': '1'}, {'yelping_since': 'August 18, 2008 at 08:13 AM', 'n': '1'}, {'yelping_since': '07 Sep 2009, 22:20', 'n': '1'}, {'yelping_since': '2011-01-22 16:07:48', 'n': '1'}, {'yelping_since': '2010-12-15 02:17:17', 'n': '1'}, {'yelping_since': 'April 23, 2010 at 07:48 PM', 'n': '1'}, {'yelping_since': '09 Dec 2007, 01:03', 'n': '1'}, {'yelping_since': '12 Feb 2011, 01:00', 'n': '1'}, {'yelping_since': '2009-04-17 13:38:22', 'n': '1'}, {'yelping_since': 'May 23, 2009 at 05:44 PM', 'n': '1'}, {'yelping_since': '2010-07-12 16:29:17', 'n': '1'}, {'yelping_since': '2011-04-17 16:27:25', 'n': '1'}, {'yelping_since': '2010-06-26 21:11:26', 'n': '1'}, {'yelping_since': 'January 17, 2011 at 10:14 PM', 'n': '1'}, {'yelping_since': '2010-04-19 19:23:27', 'n': '1'}, {'yelping_since': '29 Feb 2012, 02:51', 'n': '1'}], 'var_call_ebTWVr6VKVdp66V3X1nGc5sy': [{'date': '2019-05-30 11:54:00', 'n': '1'}, {'date': '2017-08-05 01:46:00', 'n': '1'}, {'date': '17 Jul 2020, 20:30', 'n': '1'}, {'date': '2019-12-15 18:28:00', 'n': '1'}, {'date': '2016-06-28 02:18:33', 'n': '1'}, {'date': 'June 22, 2019 at 08:35 PM', 'n': '1'}, {'date': '18 Dec 2020, 20:22', 'n': '1'}, {'date': 'February 08, 2014 at 04:33 AM', 'n': '1'}, {'date': '2021-07-05 17:24:00', 'n': '1'}, {'date': '10 Sep 2021, 13:32', 'n': '1'}, {'date': '09 Jan 2021, 21:20', 'n': '1'}, {'date': '12 Jan 2013, 04:37', 'n': '1'}, {'date': 'July 05, 2016 at 11:43 PM', 'n': '1'}, {'date': 'January 22, 2011 at 12:14 AM', 'n': '1'}, {'date': '2015-11-13 15:51:00', 'n': '1'}, {'date': '2014-07-09 22:09:00', 'n': '1'}, {'date': '2009-01-12 19:40:00', 'n': '1'}, {'date': '2012-03-17 15:49:12', 'n': '1'}, {'date': 'December 31, 2019 at 12:41 AM', 'n': '1'}, {'date': '2012-06-20 09:58:00', 'n': '1'}], 'var_call_IAxKn7y6NUcSQ1eb4KRbR1T4': [{'business_ref': 'businessref_79', 'review_cnt': '8'}, {'business_ref': 'businessref_44', 'review_cnt': '4'}, {'business_ref': 'businessref_13', 'review_cnt': '3'}, {'business_ref': 'businessref_9', 'review_cnt': '3'}, {'business_ref': 'businessref_74', 'review_cnt': '2'}, {'business_ref': 'businessref_25', 'review_cnt': '1'}, {'business_ref': 'businessref_66', 'review_cnt': '2'}, {'business_ref': 'businessref_6', 'review_cnt': '4'}, {'business_ref': 'businessref_71', 'review_cnt': '1'}, {'business_ref': 'businessref_91', 'review_cnt': '2'}, {'business_ref': 'businessref_46', 'review_cnt': '1'}, {'business_ref': 'businessref_1', 'review_cnt': '1'}, {'business_ref': 'businessref_47', 'review_cnt': '1'}, {'business_ref': 'businessref_16', 'review_cnt': '1'}, {'business_ref': 'businessref_55', 'review_cnt': '1'}, {'business_ref': 'businessref_29', 'review_cnt': '1'}, {'business_ref': 'businessref_39', 'review_cnt': '1'}, {'business_ref': 'businessref_67', 'review_cnt': '5'}, {'business_ref': 'businessref_15', 'review_cnt': '3'}, {'business_ref': 'businessref_33', 'review_cnt': '5'}, {'business_ref': 'businessref_81', 'review_cnt': '1'}, {'business_ref': 'businessref_36', 'review_cnt': '3'}, {'business_ref': 'businessref_12', 'review_cnt': '4'}, {'business_ref': 'businessref_60', 'review_cnt': '4'}, {'business_ref': 'businessref_89', 'review_cnt': '3'}, {'business_ref': 'businessref_17', 'review_cnt': '1'}, {'business_ref': 'businessref_43', 'review_cnt': '3'}, {'business_ref': 'businessref_31', 'review_cnt': '1'}, {'business_ref': 'businessref_99', 'review_cnt': '1'}, {'business_ref': 'businessref_53', 'review_cnt': '1'}, {'business_ref': 'businessref_51', 'review_cnt': '3'}, {'business_ref': 'businessref_37', 'review_cnt': '6'}, {'business_ref': 'businessref_57', 'review_cnt': '7'}, {'business_ref': 'businessref_8', 'review_cnt': '4'}, {'business_ref': 'businessref_56', 'review_cnt': '1'}, {'business_ref': 'businessref_62', 'review_cnt': '2'}, {'business_ref': 'businessref_86', 'review_cnt': '4'}, {'business_ref': 'businessref_97', 'review_cnt': '1'}, {'business_ref': 'businessref_72', 'review_cnt': '1'}, {'business_ref': 'businessref_85', 'review_cnt': '1'}, {'business_ref': 'businessref_42', 'review_cnt': '1'}, {'business_ref': 'businessref_40', 'review_cnt': '3'}, {'business_ref': 'businessref_7', 'review_cnt': '2'}, {'business_ref': 'businessref_92', 'review_cnt': '2'}, {'business_ref': 'businessref_61', 'review_cnt': '1'}, {'business_ref': 'businessref_88', 'review_cnt': '4'}, {'business_ref': 'businessref_21', 'review_cnt': '4'}, {'business_ref': 'businessref_26', 'review_cnt': '4'}, {'business_ref': 'businessref_68', 'review_cnt': '1'}, {'business_ref': 'businessref_4', 'review_cnt': '1'}, {'business_ref': 'businessref_23', 'review_cnt': '1'}, {'business_ref': 'businessref_41', 'review_cnt': '1'}, {'business_ref': 'businessref_10', 'review_cnt': '1'}, {'business_ref': 'businessref_45', 'review_cnt': '5'}, {'business_ref': 'businessref_82', 'review_cnt': '2'}, {'business_ref': 'businessref_14', 'review_cnt': '3'}, {'business_ref': 'businessref_3', 'review_cnt': '2'}, {'business_ref': 'businessref_96', 'review_cnt': '4'}, {'business_ref': 'businessref_98', 'review_cnt': '3'}, {'business_ref': 'businessref_22', 'review_cnt': '1'}, {'business_ref': 'businessref_20', 'review_cnt': '1'}, {'business_ref': 'businessref_76', 'review_cnt': '1'}], 'var_call_7aD3sDvKS6exOZlTIQZ4Pgrh': 'file_storage/call_7aD3sDvKS6exOZlTIQZ4Pgrh.json'}

exec(code, env_args)
