code = """import json, re

def load_var(v):
    if isinstance(v, str):
        with open(v,'r') as f:
            return json.load(f)
    return v

business_records = load_var(var_call_2zESRXQokhF5Lf5iMBJbnpbn)

out = []
for b in business_records[:20]:
    desc = b.get('description') or ''
    tokens = re.findall(r"\b([A-Z]{2})\b", desc)
    out.append({'business_id': b.get('business_id'), 'desc': desc, 'tokens': tokens})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_5WRzRpXAfI3DswmAJC6LyAJg': ['business', 'checkin'], 'var_call_TswX3NFH0hPFBvda8Rluvpwq': ['review', 'tip', 'user'], 'var_call_2YqDNDO27mXYKnAbO6OxgAPy': 'file_storage/call_2YqDNDO27mXYKnAbO6OxgAPy.json', 'var_call_2zESRXQokhF5Lf5iMBJbnpbn': 'file_storage/call_2zESRXQokhF5Lf5iMBJbnpbn.json', 'var_call_iTkaQoBL33XRjP3WrF6keht3': 'file_storage/call_iTkaQoBL33XRjP3WrF6keht3.json', 'var_call_vQpg8ij8b9x9OXwsuP3Q28Oq': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_XWg3IBCtyJa56pviinmx3e1c': {'total_business_records': 100, 'mapped_businesses': 0, 'sample_mapped_items': [], 'sample_no_state': [{'business_id': 'businessid_49', 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a ra'}, {'business_id': 'businessid_47', 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, '}, {'business_id': 'businessid_88', 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Range'}, {'business_id': 'businessid_41', 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Me'}, {'business_id': 'businessid_33', 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Ha'}, {'business_id': 'businessid_74', 'description': 'Located at 735 Dodecanese Blvd in Tarpon Springs, FL, this charming establishment offers a delightful selection of treat'}, {'business_id': 'businessid_92', 'description': 'Located at 690 W Dekalb Pike in King of Prussia, PA, this business offers a diverse range of services and products in th'}, {'business_id': 'businessid_64', 'description': 'Located at 12337 Olive Blvd in Creve Coeur, MO, this establishment offers a range of services in Nail Salons, Beauty & S'}, {'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home'}, {'business_id': 'businessid_29', 'description': 'Located at 41 Haddon Ave in Collingswood, NJ, this versatile establishment offers a range of services including Wedding '}], 'sample_review_refs': ['businessref_34', 'businessref_89', 'businessref_82', 'businessref_66', 'businessref_95', 'businessref_24', 'businessref_40', 'businessref_47', 'businessref_16', 'businessref_96', 'businessref_46', 'businessref_21', 'businessref_9', 'businessref_26', 'businessref_96', 'businessref_43', 'businessref_68', 'businessref_24', 'businessref_22', 'businessref_57']}}

exec(code, env_args)
