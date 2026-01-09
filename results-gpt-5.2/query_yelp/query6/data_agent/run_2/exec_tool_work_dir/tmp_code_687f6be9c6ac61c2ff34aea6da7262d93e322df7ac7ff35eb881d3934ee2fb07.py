code = """import json, re
rec = var_call_iNCbgcfkunFrCEYMgpwHE3t5[0]
desc = rec.get('description') or ''
# extract categories after 'featuring'
cat = None
m = re.search(r'featuring\s+(.+?),\s*perfect', desc, flags=re.IGNORECASE)
if m:
    cat = m.group(1).strip()
else:
    # fallback: take after 'menu featuring'
    m = re.search(r'menu\s+featuring\s+(.+?)\.', desc, flags=re.IGNORECASE)
    if m:
        cat = m.group(1).strip()
res = {
  'business_id': rec.get('business_id'),
  'name': rec.get('name'),
  'category': cat
}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_v7S5IzbEKXwemw18QJghL7WF': [], 'var_call_Ubsl0G4VE6rqbOBgRUKJ7f3E': [{'date': '2019-05-30 11:54:00', 'cnt': '1'}, {'date': '2017-08-05 01:46:00', 'cnt': '1'}, {'date': '17 Jul 2020, 20:30', 'cnt': '1'}, {'date': '2019-12-15 18:28:00', 'cnt': '1'}, {'date': '2016-06-28 02:18:33', 'cnt': '1'}, {'date': 'June 22, 2019 at 08:35 PM', 'cnt': '1'}, {'date': '18 Dec 2020, 20:22', 'cnt': '1'}, {'date': 'February 08, 2014 at 04:33 AM', 'cnt': '1'}, {'date': '2021-07-05 17:24:00', 'cnt': '1'}, {'date': '10 Sep 2021, 13:32', 'cnt': '1'}, {'date': '09 Jan 2021, 21:20', 'cnt': '1'}, {'date': '12 Jan 2013, 04:37', 'cnt': '1'}, {'date': 'July 05, 2016 at 11:43 PM', 'cnt': '1'}, {'date': 'January 22, 2011 at 12:14 AM', 'cnt': '1'}, {'date': '2015-11-13 15:51:00', 'cnt': '1'}, {'date': '2014-07-09 22:09:00', 'cnt': '1'}, {'date': '2009-01-12 19:40:00', 'cnt': '1'}, {'date': '2012-03-17 15:49:12', 'cnt': '1'}, {'date': 'December 31, 2019 at 12:41 AM', 'cnt': '1'}, {'date': '2012-06-20 09:58:00', 'cnt': '1'}], 'var_call_y7RiAm3gRPbD28EzM5RtjJhO': [{'business_ref': 'businessref_9', 'avg_rating': '4.375', 'review_cnt': '16'}], 'var_call_iNCbgcfkunFrCEYMgpwHE3t5': [{'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe', 'description': 'Located at 501 Fairmount Ave in Philadelphia, PA, this inviting establishment offers a delightful menu featuring Restaurants, Breakfast & Brunch, American (New), Cafes, perfect for a cozy meal any time of the day.'}]}

exec(code, env_args)
