code = """import json, re, pandas as pd
with open(var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ,'r',encoding='utf-8') as f:
    biz=json.load(f)
with open(var_call_SiWdtb51ESa1pBbYcxn7LZib,'r',encoding='utf-8') as f:
    rev=json.load(f)

states=set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY','DC'])
pat=re.compile(r"(?<![A-Za-z])([A-Z]{2})(?![A-Za-z])")

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
    bn=int(bid.replace('businessid_',''))
    st=parse_state(r.get('description'))
    try:
        rc=int(r.get('review_count'))
    except:
        rc=None
    biz_rows.append({'bid_num':bn,'state':st,'review_count':rc})
dfb=pd.DataFrame(biz_rows).dropna(subset=['state','review_count'])
state_reviews=dfb.groupby('state',as_index=False)['review_count'].sum().sort_values('review_count',ascending=False)
top_state=state_reviews.iloc[0]['state']
# map bid->state for all businesses
state_map=dfb.set_index('bid_num')['state'].to_dict()
ratings=[]
for r in rev:
    br=r.get('business_ref')
    if not br: continue
    bn=int(br.replace('businessref_',''))
    if state_map.get(bn)!=top_state:
        continue
    try:
        ratings.append(int(r.get('rating')))
    except:
        pass
avg_rating = sum(ratings)/len(ratings) if ratings else None
out={'state':top_state,'total_reviews':int(state_reviews.iloc[0]['review_count']), 'avg_rating':avg_rating}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Pr7tc0HKLfl3LZJKrJI2qkwZ': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json', 'var_call_2KcQNtpgWpdSy1Ok7ZD7VufB': [{'ok': '1'}], 'var_call_iDLnvQzRnnHRmtOtfJh3kfSb': {'error': 'no data'}, 'var_call_sEv23LjnqO49MSBvPhfKlGY3': 'file_storage/call_sEv23LjnqO49MSBvPhfKlGY3.json', 'var_call_zXiTEzX91odMa4CJxEAx00gP': {'rows': 100, 'non_null_state': 0, 'states': []}, 'var_call_B6IM8jaF5rX1p5iM8qF2VgoU': [{'_id': '6859a000fe8b31cd7362e2ab', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_AbAwj8kdnlFf2pVw1afmmjoY': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.', 'matches': []}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.', 'matches': []}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.', 'matches': []}, {'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.', 'matches': []}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.', 'matches': []}], 'var_call_lDB9BfCia6z2sYGqX1VCrD3j': {'sample_repr': "'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'", 'len': 244, 'ord_CA': [44, 32, 67, 65]}, 'var_call_nNdsbtVdafT6lrPsMOxP79uD': {'findall': [], 'search': None}, 'var_call_xLgz1iZOmCWMNNrkdmrDHjfN': {'findall': ['CA']}, 'var_call_VYtsVN2b9BHt61QB7O0w7bP0': {'state': 'MO', 'total_reviews': 2243, 'avg_business_rating': None}, 'var_call_LImOiBDjbYMDSfoVmWQmJ952': {'path': 'file_storage/call_Pr7tc0HKLfl3LZJKrJI2qkwZ.json'}, 'var_call_8fQjkzx4oqlsQUCQZv9rGpie': [{'n': '2000'}], 'var_call_1JQx3RgSnXolofjoeUEdJGSR': {'n': 100, 'n_state': 0, 'n_valid': 0}, 'var_call_LLvqGEqw0ZuzZTiAmbyJsv1S': [{'business_ref': 'businessref_79', 'avg_rating': '4.627906976744186', 'n_reviews': '43'}, {'business_ref': 'businessref_44', 'avg_rating': '2.9285714285714284', 'n_reviews': '42'}, {'business_ref': 'businessref_13', 'avg_rating': '3.9166666666666665', 'n_reviews': '12'}, {'business_ref': 'businessref_87', 'avg_rating': '3.3333333333333335', 'n_reviews': '6'}, {'business_ref': 'businessref_59', 'avg_rating': '4.6', 'n_reviews': '30'}], 'var_call_SiWdtb51ESa1pBbYcxn7LZib': 'file_storage/call_SiWdtb51ESa1pBbYcxn7LZib.json', 'var_call_YeM9vIIT6B8Prhwq04s2jAmy': {'sample': [{'desc': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offer', 'state': None}, {'desc': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishm', 'state': None}, {'desc': 'Located at 11655 W Executive Dr in Boise, ID, this facility ', 'state': None}, {'desc': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg,', 'state': None}, {'desc': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establ', 'state': None}, {'desc': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this c', 'state': None}, {'desc': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this bu', 'state': None}, {'desc': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establi', 'state': None}, {'desc': 'Located at 5000 W 96th St in Indianapolis, IN, this establis', 'state': None}, {'desc': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile', 'state': None}], 'n': 100, 'n_state': 0}, 'var_call_9PodT0ZJMZAIwfOeNc24S0qx': {'matches': []}, 'var_call_qVAgx4GEzSxbjeDtni6oxeSR': {'matches': ['CA']}}

exec(code, env_args)
