code = """import json
p = var_call_C9qcVttwHc7nHk3C6JaXP5aS
records = json.loads(open(p).read())

markers = [
 'offers a range of services in',
 'offers a diverse range of services in',
 'in the category of',
 'offers a delightful array of options ranging from',
 'offers a delightful array of dishes in the category of',
 'this establishment offers a range of services including',
 'this establishment offers a variety of services including'
]

from collections import Counter
cat_counter = Counter()
cat_refs = {}

for r in records:
    attrs = r.get('attributes') or {}
    accepts = attrs.get('BusinessAcceptsCreditCards')
    if not accepts:
        continue
    if str(accepts).lower() != 'true':
        continue
    desc = (r.get('description') or '').lower()
    seg = None
    for m in markers:
        if m in desc:
            seg = desc.split(m,1)[1]
            break
    if not seg:
        continue
    seg = seg.split('.',1)[0]
    parts = []
    for part in seg.split(','):
        for sub in part.split(' and '):
            s = sub.strip()
            if s:
                parts.append(s)
    if not parts:
        continue
    biz_id = r.get('business_id')
    biz_ref = 'businessref_' + biz_id.split('_',1)[1] if biz_id and '_' in biz_id else biz_id
    for c in parts:
        cat_counter[c] += 1
        cat_refs.setdefault(c, set()).add(biz_ref)

if cat_counter:
    top_cat, top_count = cat_counter.most_common(1)[0]
    top_refs = sorted(list(cat_refs[top_cat]))
else:
    top_cat = None
    top_count = 0
    top_refs = []

res = {'top_category': top_cat, 'count': top_count, 'business_refs': top_refs}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_pmHQOWf5XZpZBfTwoeAsLrn5': ['business', 'checkin'], 'var_call_AyQe6THSNrZu3vGFHFiFVdxz': ['review', 'tip', 'user'], 'var_call_AMs1LTGeLtTG44p5m35fTNCl': 'file_storage/call_AMs1LTGeLtTG44p5m35fTNCl.json', 'var_call_QI9mfKBsxhT8moCr2ZwCitqP': [{'business_id': 'businessid_49', 'business_ref': 'businessref_49', 'name': 'Steps to Learning Montessori Preschool', 'categories': None}, {'business_id': 'businessid_47', 'business_ref': 'businessref_47', 'name': 'Breeze Blow Dry Bar', 'categories': None}, {'business_id': 'businessid_88', 'business_ref': 'businessref_88', 'name': 'Impact Guns', 'categories': None}, {'business_id': 'businessid_33', 'business_ref': 'businessref_33', 'name': 'J&Q Nails', 'categories': None}, {'business_id': 'businessid_92', 'business_ref': 'businessref_92', 'name': 'Luminosity', 'categories': None}, {'business_id': 'businessid_64', 'business_ref': 'businessref_64', 'name': 'Nail Care Salon', 'categories': None}, {'business_id': 'businessid_52', 'business_ref': 'businessref_52', 'name': 'Architectural Antiques of Indianapolis', 'categories': None}, {'business_id': 'businessid_29', 'business_ref': 'businessref_29', 'name': "Aster's Floral Shop", 'categories': None}, {'business_id': 'businessid_10', 'business_ref': 'businessref_10', 'name': 'China Wok', 'categories': None}, {'business_id': 'businessid_61', 'business_ref': 'businessref_61', 'name': 'Brandon Family Medical Care', 'categories': None}, {'business_id': 'businessid_54', 'business_ref': 'businessref_54', 'name': '7-Eleven', 'categories': None}, {'business_id': 'businessid_8', 'business_ref': 'businessref_8', 'name': 'Uber', 'categories': None}, {'business_id': 'businessid_91', 'business_ref': 'businessref_91', 'name': 'Cafe Porche and snowbar', 'categories': None}, {'business_id': 'businessid_83', 'business_ref': 'businessref_83', 'name': 'Eyeglass World', 'categories': None}, {'business_id': 'businessid_93', 'business_ref': 'businessref_93', 'name': "Callahan's Corner", 'categories': None}, {'business_id': 'businessid_24', 'business_ref': 'businessref_24', 'name': 'FroYo Frozen Yogurt', 'categories': None}, {'business_id': 'businessid_95', 'business_ref': 'businessref_95', 'name': 'Subway', 'categories': None}, {'business_id': 'businessid_26', 'business_ref': 'businessref_26', 'name': "McDonald's", 'categories': None}, {'business_id': 'businessid_84', 'business_ref': 'businessref_84', 'name': 'Gamestop', 'categories': None}, {'business_id': 'businessid_89', 'business_ref': 'businessref_89', 'name': 'King of Prussia Laundromat', 'categories': None}, {'business_id': 'businessid_32', 'business_ref': 'businessref_32', 'name': 'The Recovery Room Bar & Grill', 'categories': None}, {'business_id': 'businessid_71', 'business_ref': 'businessref_71', 'name': 'Lithia Ford Lincoln of Boise', 'categories': None}, {'business_id': 'businessid_97', 'business_ref': 'businessref_97', 'name': 'Executive Auto Body', 'categories': None}, {'business_id': 'businessid_14', 'business_ref': 'businessref_14', 'name': 'Ross Dress for Less', 'categories': None}, {'business_id': 'businessid_3', 'business_ref': 'businessref_3', 'name': 'Mr. Dry Out', 'categories': None}, {'business_id': 'businessid_27', 'business_ref': 'businessref_27', 'name': 'Egg Roll King Two', 'categories': None}, {'business_id': 'businessid_75', 'business_ref': 'businessref_75', 'name': 'Light World', 'categories': None}, {'business_id': 'businessid_2', 'business_ref': 'businessref_2', 'name': 'Bloom', 'categories': None}, {'business_id': 'businessid_48', 'business_ref': 'businessref_48', 'name': 'The Loop Taste of Chicago', 'categories': None}, {'business_id': 'businessid_67', 'business_ref': 'businessref_67', 'name': "Hanoi's Pho", 'categories': None}, {'business_id': 'businessid_76', 'business_ref': 'businessref_76', 'name': 'Big Lots', 'categories': None}, {'business_id': 'businessid_100', 'business_ref': 'businessref_100', 'name': 'Service First Heating & Air Conditioning', 'categories': None}, {'business_id': 'businessid_63', 'business_ref': 'businessref_63', 'name': 'The Iron Shop', 'categories': None}, {'business_id': 'businessid_45', 'business_ref': 'businessref_45', 'name': 'The Fresh Market', 'categories': None}, {'business_id': 'businessid_68', 'business_ref': 'businessref_68', 'name': 'Brow Art', 'categories': None}, {'business_id': 'businessid_6', 'business_ref': 'businessref_6', 'name': 'The Jungle', 'categories': None}, {'business_id': 'businessid_87', 'business_ref': 'businessref_87', 'name': 'Jordans Fish and Chicken', 'categories': None}, {'business_id': 'businessid_66', 'business_ref': 'businessref_66', 'name': 'Panda Express', 'categories': None}, {'business_id': 'businessid_55', 'business_ref': 'businessref_55', 'name': 'Uptown Snoballs and Ice Cream', 'categories': None}, {'business_id': 'businessid_30', 'business_ref': 'businessref_30', 'name': 'Dalco Home Remodeling', 'categories': None}, {'business_id': 'businessid_15', 'business_ref': 'businessref_15', 'name': 'Take 5 Oil Change', 'categories': None}, {'business_id': 'businessid_96', 'business_ref': 'businessref_96', 'name': 'Farmhaus Restaurant', 'categories': None}, {'business_id': 'businessid_11', 'business_ref': 'businessref_11', 'name': 'Allan Link,DMD - The DentaLink', 'categories': None}, {'business_id': 'businessid_73', 'business_ref': 'businessref_73', 'name': 'Biggest Little Pools', 'categories': None}, {'business_id': 'businessid_4', 'business_ref': 'businessref_4', 'name': 'Dentistry for Children and Adolescents - St. Charles', 'categories': None}, {'business_id': 'businessid_77', 'business_ref': 'businessref_77', 'name': 'Holiday Inn Philadelphia Stadium', 'categories': None}, {'business_id': 'businessid_18', 'business_ref': 'businessref_18', 'name': 'Sleep Number', 'categories': None}, {'business_id': 'businessid_65', 'business_ref': 'businessref_65', 'name': "Pat Flynn's Public House", 'categories': None}, {'business_id': 'businessid_86', 'business_ref': 'businessref_86', 'name': "Humpty's Dumplings", 'categories': None}, {'business_id': 'businessid_53', 'business_ref': 'businessref_53', 'name': 'Samwich', 'categories': None}, {'business_id': 'businessid_40', 'business_ref': 'businessref_40', 'name': 'Artesano Gallery & Iron Works', 'categories': None}, {'business_id': 'businessid_44', 'business_ref': 'businessref_44', 'name': 'Fishtown Diner', 'categories': None}, {'business_id': 'businessid_43', 'business_ref': 'businessref_43', 'name': 'Taco Bell', 'categories': None}, {'business_id': 'businessid_9', 'business_ref': 'businessref_9', 'name': 'Coffee House Too Cafe', 'categories': None}, {'business_id': 'businessid_20', 'business_ref': 'businessref_20', 'name': 'Chick-fil-A', 'categories': None}, {'business_id': 'businessid_37', 'business_ref': 'businessref_37', 'name': 'Orangetheory Fitness Carrollwood', 'categories': None}, {'business_id': 'businessid_62', 'business_ref': 'businessref_62', 'name': 'Winn Dixie', 'categories': None}, {'business_id': 'businessid_94', 'business_ref': 'businessref_94', 'name': 'Taste of Europe', 'categories': None}, {'business_id': 'businessid_90', 'business_ref': 'businessref_90', 'name': "Long John Silver's", 'categories': None}, {'business_id': 'businessid_31', 'business_ref': 'businessref_31', 'name': 'Island Way Car Wash', 'categories': None}, {'business_id': 'businessid_85', 'business_ref': 'businessref_85', 'name': 'Insomnia Cookies', 'categories': None}, {'business_id': 'businessid_25', 'business_ref': 'businessref_25', 'name': 'Great Harvest Bread Co', 'categories': None}, {'business_id': 'businessid_82', 'business_ref': 'businessref_82', 'name': 'Miles Table', 'categories': None}, {'business_id': 'businessid_58', 'business_ref': 'businessref_58', 'name': 'GOLFTEC Westshore', 'categories': None}, {'business_id': 'businessid_60', 'business_ref': 'businessref_60', 'name': 'Walmart', 'categories': None}, {'business_id': 'businessid_21', 'business_ref': 'businessref_21', 'name': 'Ford of Port Richey', 'categories': None}, {'business_id': 'businessid_98', 'business_ref': 'businessref_98', 'name': 'Brookmont Apartment Homes', 'categories': None}, {'business_id': 'businessid_16', 'business_ref': 'businessref_16', 'name': 'Fox and Hound English Pub and Grille', 'categories': None}, {'business_id': 'businessid_46', 'business_ref': 'businessref_46', 'name': 'Salt + Smoke', 'categories': None}, {'business_id': 'businessid_22', 'business_ref': 'businessref_22', 'name': 'Main Line Spine', 'categories': None}, {'business_id': 'businessid_36', 'business_ref': 'businessref_36', 'name': 'Pho & Beyond', 'categories': None}, {'business_id': 'businessid_38', 'business_ref': 'businessref_38', 'name': 'Philadelphia Hair Studio', 'categories': None}, {'business_id': 'businessid_81', 'business_ref': 'businessref_81', 'name': 'Fantastic Sams Cut & Color', 'categories': None}, {'business_id': 'businessid_13', 'business_ref': 'businessref_13', 'name': 'Avian Glen Winery', 'categories': None}, {'business_id': 'businessid_17', 'business_ref': 'businessref_17', 'name': 'Whitemarsh Jewelers', 'categories': None}], 'var_call_3k1hsRIYHCr2DW040Jlo0mlW': {'top_category': None, 'count': 0, 'business_refs': []}, 'var_call_OTLsOGoAw4e2uyzfJTssqFU9': [], 'var_call_lCvMWnQGFzwOMqcItymbiMoG': [], 'var_call_Eci27b05XMNsJftbOfuTxZ1L': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_call_C9qcVttwHc7nHk3C6JaXP5aS': 'file_storage/call_C9qcVttwHc7nHk3C6JaXP5aS.json', 'var_call_5PlcWz42zkM0lsOY4gEgyynZ': 77}

exec(code, env_args)
