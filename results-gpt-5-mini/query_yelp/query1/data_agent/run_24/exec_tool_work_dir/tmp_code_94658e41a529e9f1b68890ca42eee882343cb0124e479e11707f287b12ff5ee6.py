code = """import json
# var_call_NGnvx0GbB969qUUuKWA5CbdX is available from previous query
data = var_call_NGnvx0GbB969qUUuKWA5CbdX
avg_str = None
if isinstance(data, list) and len(data) > 0:
    avg_str = data[0].get('avg_rating')
avg = None
if avg_str is not None:
    try:
        avg = float(avg_str)
    except:
        avg = None
result = {"average_rating": avg}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_QgRUhOJjDvzp3RNrNJ6EVEjy': ['business', 'checkin'], 'var_call_tbRL8DL9aSb0xWr3fMxWoSVT': ['review', 'tip', 'user'], 'var_call_MU7iF5kPLdOzbwfWb9tUzL8x': [{'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}, {'business_id': 'businessid_94', 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'business_id': 'businessid_90', 'description': 'Located at 2831 E 38th St in Indianapolis, IN, this establishment offers a diverse menu featuring Fast Food, Seafood, Restaurants, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_16', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}], 'var_call_NGnvx0GbB969qUUuKWA5CbdX': [{'avg_rating': '3.547008547008547'}]}

exec(code, env_args)
