code = """import json, re
reviews = var_call_huS02AjbshVXxq9dqXTecfbd
businesses_path = var_call_ZzdVoaucnJIPcpQ2neAbPUYW
with open(businesses_path, 'r') as f:
    businesses = json.load(f)

biz_map = {b.get('business_id'): b.get('description','') for b in businesses}

def extract_categories(desc):
    if not desc:
        return []
    s = desc.strip()
    s_low = s.lower()
    # try to find 'offers' then look for 'in' or 'including' after it
    idx_off = s_low.find('offers')
    tail = ''
    if idx_off != -1:
        after = s[idx_off+6:]
        # look for 'including' or 'in'
        m_incl = re.search(r'\bincluding\b', after, flags=re.IGNORECASE)
        m_in = re.search(r'\bin\b', after, flags=re.IGNORECASE)
        pos = None
        if m_incl:
            pos = m_incl.start()
            tail = after[pos+len('including'):]
        elif m_in:
            pos = m_in.start()
            tail = after[pos+len('in'):]
        else:
            tail = after
    else:
        # fallback: take substring after last ' in '
        idx = s_low.rfind(' in ')
        if idx != -1:
            tail = s[idx+4:]
        else:
            tail = s
    # stop at first period or end
    tail = re.split(r'[\.\n]', tail)[0]
    # replace ampersand and ' and ' with commas
    tail = tail.replace('&', ',')
    tail = tail.replace(' and ', ', ')
    tail = tail.replace(';', ',')
    parts = [p.strip() for p in tail.split(',') if p.strip()]
    cleaned = []
    for p in parts:
        p = re.sub(r"^(the category of|the fields of|products in|services in|a range of services in|a diverse range of services in)\s+", '', p, flags=re.IGNORECASE)
        p = p.strip(' .')
        if p:
            cleaned.append(p)
    return cleaned

from collections import defaultdict
cat_counts = defaultdict(int)
for r in reviews:
    business_ref = r.get('business_ref')
    try:
        cnt = int(r.get('cnt',0))
    except:
        cnt = 0
    if business_ref and business_ref.startswith('businessref_'):
        suffix = business_ref.split('_',1)[1]
        business_id = 'businessid_' + suffix
    else:
        business_id = business_ref
    desc = biz_map.get(business_id, '')
    cats = extract_categories(desc)
    if not cats:
        continue
    for c in cats:
        cat_counts[c] += cnt

items = sorted(cat_counts.items(), key=lambda x: x[1], reverse=True)
top5 = items[:5]
result = [{"category": k, "review_count": v} for k,v in top5]
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Fw2tyGmX4GlIrQhbfl0vO0yL': ['business', 'checkin'], 'var_call_IUWrQiofbxx8rpNOXG0WBB5M': ['review', 'tip', 'user'], 'var_call_9LOh7LCZGRIQeKEQpdNEBj00': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar', 'review_count': '81', 'is_open': '0', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}, 'hours': {'Monday': '7:0-18:0', 'Tuesday': '7:0-18:0', 'Wednesday': '7:0-18:0', 'Thursday': '7:0-18:0', 'Friday': '7:0-19:0', 'Saturday': '8:0-19:0', 'Sunday': '10:0-17:0'}, 'description': 'Located at 9916 Clayton Rd in St. Louis, MO, this establishment offers a wide range of services, including Hair Salons, Beauty & Spas, Hair Stylists, Skin Care, Blow Dry/Out Services, and Makeup Artists.'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns', 'review_count': '39', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}, 'hours': {'Monday': '10:0-19:0', 'Tuesday': '10:0-19:0', 'Wednesday': '10:0-19:0', 'Thursday': '10:0-19:0', 'Friday': '10:0-19:0', 'Saturday': '10:0-19:0'}, 'description': 'Located at 11655 W Executive Dr in Boise, ID, this facility offers enthusiasts a premier destination for Gun/Rifle Ranges, Active Life.'}, {'_id': '6859a000fe8b31cd7362e2ae', 'business_id': 'businessid_41', 'name': 'Palms Primary Care', 'review_count': '5', 'is_open': '1', 'attributes': 'None', 'hours': {'Monday': '8:30-17:0', 'Tuesday': '8:30-17:0', 'Wednesday': '8:30-17:0', 'Thursday': '8:30-17:0', 'Friday': '8:30-17:0'}, 'description': 'Located at 1615 Pasadena Ave S, Ste 430 in Saint Petersburg, FL, this facility offers a range of services in Internal Medicine, Doctors, Health & Medical.'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails', 'review_count': '28', 'is_open': '1', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}, 'hours': {'Monday': '9:30-19:0', 'Tuesday': '9:30-19:0', 'Wednesday': '9:30-19:0', 'Thursday': '9:30-19:0', 'Friday': '9:30-19:0', 'Saturday': '9:30-17:30'}, 'description': 'Located at 9655 E US Hwy 36, Unit H in Avon, IN, this establishment offers a range of services including Nail Salons, Hair Removal, Beauty & Spas, and Waxing.'}], 'var_call_huS02AjbshVXxq9dqXTecfbd': [{'business_ref': 'businessref_45', 'cnt': '3'}, {'business_ref': 'businessref_74', 'cnt': '2'}, {'business_ref': 'businessref_66', 'cnt': '2'}, {'business_ref': 'businessref_33', 'cnt': '2'}, {'business_ref': 'businessref_36', 'cnt': '2'}, {'business_ref': 'businessref_60', 'cnt': '2'}, {'business_ref': 'businessref_57', 'cnt': '2'}, {'business_ref': 'businessref_92', 'cnt': '2'}, {'business_ref': 'businessref_96', 'cnt': '2'}, {'business_ref': 'businessref_13', 'cnt': '1'}, {'business_ref': 'businessref_79', 'cnt': '1'}, {'business_ref': 'businessref_15', 'cnt': '1'}, {'business_ref': 'businessref_12', 'cnt': '1'}, {'business_ref': 'businessref_31', 'cnt': '1'}, {'business_ref': 'businessref_53', 'cnt': '1'}, {'business_ref': 'businessref_86', 'cnt': '1'}, {'business_ref': 'businessref_62', 'cnt': '1'}, {'business_ref': 'businessref_37', 'cnt': '1'}, {'business_ref': 'businessref_26', 'cnt': '1'}, {'business_ref': 'businessref_68', 'cnt': '1'}, {'business_ref': 'businessref_41', 'cnt': '1'}, {'business_ref': 'businessref_10', 'cnt': '1'}, {'business_ref': 'businessref_98', 'cnt': '1'}, {'business_ref': 'businessref_14', 'cnt': '1'}, {'business_ref': 'businessref_20', 'cnt': '1'}, {'business_ref': 'businessref_6', 'cnt': '1'}], 'var_call_i8dTZy5WL693EWHezgSTpSWM': [], 'var_call_Lz3umEbjO9nHwq38p0sguIZl': [], 'var_call_ZzdVoaucnJIPcpQ2neAbPUYW': 'file_storage/call_ZzdVoaucnJIPcpQ2neAbPUYW.json'}

exec(code, env_args)
