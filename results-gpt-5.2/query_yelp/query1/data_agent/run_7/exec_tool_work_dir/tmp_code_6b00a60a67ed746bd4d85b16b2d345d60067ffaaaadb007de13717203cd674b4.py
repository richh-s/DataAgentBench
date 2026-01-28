code = """import json, pandas as pd

biz = pd.DataFrame(var_call_jVptH3BaxfXwIUkobi0qClkL)
# map businessid_X -> businessref_X
biz['business_ref'] = biz['business_id'].str.replace('businessid_', 'businessref_', regex=False)
refs = biz['business_ref'].tolist()
# create SQL IN list
in_list = ','.join(["'"+r.replace("'","''")+"'" for r in refs])
query = f"SELECT AVG(rating) AS avg_rating FROM review WHERE business_ref IN ({in_list});"
result = {'query': query}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_g8RWcOZbpIQ0tyDdVAE6AOWO': [], 'var_call_oPWZKzequ4lrTuYoKdWcZNYg': [{'avg_rating_all_reviews': '3.515'}], 'var_call_kNiuExG0C4DrN5m9KoX9ESS0': [{'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}], 'var_call_jVptH3BaxfXwIUkobi0qClkL': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
