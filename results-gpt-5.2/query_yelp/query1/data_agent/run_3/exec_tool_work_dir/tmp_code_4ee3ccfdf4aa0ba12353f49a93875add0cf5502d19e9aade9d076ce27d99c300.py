code = """import json, pandas as pd

# businesses in Indianapolis, IN
biz = pd.DataFrame(var_call_r4hrmmk4KifSZLH1XJa6MhUQ)
if biz.empty:
    out = {"average_rating": None, "business_count": 0, "review_count": 0}
else:
    biz["business_ref"] = biz["business_id"].str.replace('businessid_', 'businessref_', regex=False)

    # load reviews (large) from file
    path = var_call_xMC10xSzCH3H9Kw7uRhS59Ls
    with open(path, 'r') as f:
        reviews = json.load(f)
    rev = pd.DataFrame(reviews)
    rev["rating"] = pd.to_numeric(rev["rating"], errors='coerce')

    merged = rev.merge(biz[["business_ref"]], on="business_ref", how="inner")
    avg_rating = float(merged["rating"].mean()) if not merged.empty else None
    out = {
        "average_rating": avg_rating,
        "business_count": int(biz.shape[0]),
        "review_count": int(merged.shape[0])
    }

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LNMawGAqps43lW2xN1T12i5P': [], 'var_call_xMC10xSzCH3H9Kw7uRhS59Ls': 'file_storage/call_xMC10xSzCH3H9Kw7uRhS59Ls.json', 'var_call_mGmcArRonvgefmJxyGvkBcL6': [{'business_id': 'businessid_52', 'description': 'Located at 5000 W 96th St in Indianapolis, IN, this establishment offers a diverse selection of Antiques, Shopping, Home Services, and Lighting Fixtures & Equipment for all your home and decorative needs.'}, {'business_id': 'businessid_84', 'description': 'Located at 5816 Crawfordsville Rd in Indianapolis, IN, this store offers a diverse selection of products in categories such as Books, Mags, Music & Video, Video Game Stores, Videos & Video Game Rental, Electronics, Shopping, and Hobby Shops.'}, {'business_id': 'businessid_76', 'description': 'Located at 8401 Michigan Rd in Indianapolis, IN, this shopping destination offers a diverse range of products across various categories, including Fashion, Department Stores, Furniture Stores, Shopping, Home Decor, Home & Garden, and Discount Store.'}, {'business_id': 'businessid_87', 'description': 'Located at 6416 W Washington St in Indianapolis, IN, this establishment offers a delightful menu featuring Restaurants, Chicken Wings, Fish & Chips, and American (Traditional) cuisine.'}, {'business_id': 'businessid_65', 'description': 'Located at 5198 Allisonville Rd in Indianapolis, IN, this venue offers a vibrant atmosphere perfect for enjoying Irish, Bars, Restaurants, Pubs, Nightlife.'}, {'business_id': 'businessid_94', 'description': 'Located at 4320 W 96th St in Indianapolis, IN, this inviting establishment offers a diverse menu that showcases a delightful fusion of flavors across categories such as Food, Specialty Food, Ethnic Food, Modern European, Restaurants.'}, {'business_id': 'businessid_90', 'description': 'Located at 2831 E 38th St in Indianapolis, IN, this establishment offers a diverse menu featuring Fast Food, Seafood, Restaurants, catering to a variety of tastes and preferences.'}, {'business_id': 'businessid_16', 'description': 'Located at 4901 E 82nd St, Ste 900 in Indianapolis, IN, this vibrant establishment offers a fantastic experience for those seeking American (New), Nightlife, Bars, Restaurants, Pubs.'}], 'var_call_r4hrmmk4KifSZLH1XJa6MhUQ': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
