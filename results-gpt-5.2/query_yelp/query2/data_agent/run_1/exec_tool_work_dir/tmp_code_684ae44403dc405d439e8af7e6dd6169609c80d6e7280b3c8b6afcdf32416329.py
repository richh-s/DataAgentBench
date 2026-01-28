code = """import json, re, pandas as pd
path=var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ
with open(path,'r',encoding='utf-8') as f:
    biz=json.load(f)
# build business map
states=set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
pat=re.compile(r"\b([A-Z]{2})\b")

def parse_state(desc):
    if not desc:
        return None
    for st in pat.findall(desc):
        if st in states:
            return st
    return None

biz_rows=[]
for r in biz:
    bid=r.get('business_id')
    if not bid: continue
    bn=bid.replace('businessid_','')
    st=parse_state(r.get('description'))
    try:
        rc=int(r.get('review_count'))
    except:
        rc=None
    biz_rows.append({'bid_num':bn,'state':st,'review_count':rc})

dfb=pd.DataFrame(biz_rows).dropna(subset=['state','review_count'])
state_reviews=dfb.groupby('state',as_index=False)['review_count'].sum().sort_values('review_count',ascending=False)
top_state=state_reviews.iloc[0]['state']
# load reviews from duckdb via storage var? query
import duckdb
con=duckdb.connect()
# attach existing user_database? cannot. so instead query_db already provides access; will use var_call for all reviews.
print('__RESULT__:')
print(json.dumps({'top_state':top_state}))"""

env_args = {'var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json', 'var_call_2KcQNtpgWpdSy1Ok7ZD7VufB': [{'ok': '1'}], 'var_call_iDLnvQzRnnHRmtOtfJh3kfSb': {'error': 'no data'}, 'var_call_sEv23LjnqO49MSBvPhfKlGY3': 'file_storage/call_sEv23LjnqO49MSBvPhfKlGY3.json', 'var_call_zXiTEzX91odMa4CJxEAx00gP': {'rows': 100, 'non_null_state': 0, 'states': []}, 'var_call_B6IM8jaF5rX1p5iM8qF2VgoU': [{'_id': '6859a000fe8b31cd7362e2ab', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_AbAwj8kdnlFf2pVw1afmmjoY': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'matches': []}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'matches': []}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'matches': []}, {'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'matches': []}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'matches': []}], 'var_call_lDB9BfCia6z2sYGqX1VCrD3j': {'sample_repr': "'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'", 'len': 244, 'ord_CA': [44, 32, 67, 65]}, 'var_call_nNdsbtVdafT6lrPsMOxP79uD': {'findall': [], 'search': None}, 'var_call_xLgz1iZOmCWMNNrkdmrDHjfN': {'findall': ['CA']}, 'var_call_VYtsVN2b9BHt61QB7O0w7bP0': {'state': 'MO', 'total_reviews': 2243, 'avg_business_rating': None}, 'var_call_LImOiBDjbYMDSfoVmWQmJ952': {'path': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json'}, 'var_call_8fQjkzx4oqlsQUCQZv9rGpie': [{'n': '2000'}]}

exec(code, env_args)
