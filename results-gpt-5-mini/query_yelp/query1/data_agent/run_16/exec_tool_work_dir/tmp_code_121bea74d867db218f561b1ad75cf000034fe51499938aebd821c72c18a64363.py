code = """import json
# var_call_wm70yztkUrj5ZQLD5nWp0Yx6 is available from previous query_db call
docs = var_call_wm70yztkUrj5ZQLD5nWp0Yx6
refs = []
for d in docs:
    bid = d.get('business_id')
    if bid and bid.startswith('businessid_'):
        refs.append(bid.replace('businessid_', 'businessref_'))
    elif bid:
        refs.append(bid)

# Ensure unique
refs = sorted(list(dict.fromkeys(refs)))

print('__RESULT__:')
print(json.dumps(refs))"""

env_args = {'var_call_wm70yztkUrj5ZQLD5nWp0Yx6': [{'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94', 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90', 'description': 'Located at 2831 E 38th St in Indianapolis, IN, this establishment offers a diverse menu featuring Fast Food, Seafood, Restaurants, catering to a variety of tastes and preferences.'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}]}

exec(code, env_args)
