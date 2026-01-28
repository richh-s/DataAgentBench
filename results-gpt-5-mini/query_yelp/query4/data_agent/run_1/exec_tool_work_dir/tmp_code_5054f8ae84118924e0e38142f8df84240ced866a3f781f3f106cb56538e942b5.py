code = """import json

# load previous python result mapping
mapping = var_call_A9n99iJc9tv6dc2hp1y41ZmQ
# load reviews query result
reviews_file = var_call_Qy3bbpiEPqRZv3GwSpflEel5
with open(reviews_file, 'r') as f:
    reviews = json.load(f)

# convert ratings to int and aggregate by category
from collections import defaultdict

cat_ratings = defaultdict(list)

for r in reviews:
    bref = r.get('business_ref')
    rating = r.get('rating')
    try:
        rating = int(rating)
    except:
        continue
    cat = mapping['ref_to_category'].get(bref, 'Unknown')
    cat_ratings[cat].append(rating)

# compute counts of businesses per category (unique business refs) among credit-card-accepting businesses
cat_businesses = defaultdict(set)
for bref, cat in mapping['ref_to_category'].items():
    cat_businesses[cat].add(bref)

# Find category with largest number of businesses
cat_counts = {cat: len(s) for cat, s in cat_businesses.items()}
max_cat = max(cat_counts.items(), key=lambda x: x[1])[0]
max_count = cat_counts[max_cat]

# Compute average rating for that category (average over all reviews of businesses in that category)
ratings = cat_ratings.get(max_cat, [])
avg_rating = None
if ratings:
    avg_rating = sum(ratings)/len(ratings)

result = {
    'category_with_most_credit_card_businesses': max_cat,
    'business_count': max_count,
    'average_rating': avg_rating
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ON7DXNzg44RXYnmlF5NVxm84': ['business', 'checkin'], 'var_call_Pgxm7eIExSxzxvdTgnJfg3u5': ['review', 'tip', 'user'], 'var_call_FjUnubLN1jtXQpNIovHafnH2': 'file_storage/call_FjUnubLN1jtXQpNIovHafnH2.json', 'var_call_A9n99iJc9tv6dc2hp1y41ZmQ': {'business_refs': ['businessref_49', 'businessref_47', 'businessref_88', 'businessref_33', 'businessref_92', 'businessref_64', 'businessref_52', 'businessref_29', 'businessref_10', 'businessref_61', 'businessref_54', 'businessref_8', 'businessref_91', 'businessref_83', 'businessref_93', 'businessref_24', 'businessref_95', 'businessref_26', 'businessref_84', 'businessref_89', 'businessref_32', 'businessref_71', 'businessref_97', 'businessref_14', 'businessref_3', 'businessref_27', 'businessref_75', 'businessref_2', 'businessref_48', 'businessref_67', 'businessref_76', 'businessref_100', 'businessref_63', 'businessref_45', 'businessref_68', 'businessref_6', 'businessref_87', 'businessref_66', 'businessref_55', 'businessref_30', 'businessref_15', 'businessref_96', 'businessref_11', 'businessref_73', 'businessref_4', 'businessref_77', 'businessref_18', 'businessref_65', 'businessref_86', 'businessref_53', 'businessref_40', 'businessref_44', 'businessref_43', 'businessref_9', 'businessref_20', 'businessref_37', 'businessref_62', 'businessref_94', 'businessref_90', 'businessref_31', 'businessref_85', 'businessref_25', 'businessref_82', 'businessref_58', 'businessref_60', 'businessref_21', 'businessref_98', 'businessref_16', 'businessref_46', 'businessref_22', 'businessref_36', 'businessref_38', 'businessref_81', 'businessref_13', 'businessref_17'], 'ref_to_category': {'businessref_49': 'Education', 'businessref_47': 'St', 'businessref_88': 'enthusiasts a premier destination for Gun/Rifle Ranges', 'businessref_33': 'including Nail Salons', 'businessref_92': 'the fields of Cosmetics & Beauty Supply', 'businessref_64': 'Nail Salons', 'businessref_52': 'a diverse selection of Antiques', 'businessref_29': 'including Wedding Planning', 'businessref_10': "the category of 'Restaurants", 'businessref_61': 'the categories of Medical Centers', 'businessref_54': 'a variety of services including Service Stations', 'businessref_8': 'Unknown', 'businessref_91': 'a delightful array of options ranging from Food', 'businessref_83': 'Optometrists', 'businessref_93': 'a diverse menu featuring American (New) cuisine', 'businessref_24': 'the categories of Food', 'businessref_95': 'a diverse menu featuring Restaurants', 'businessref_26': 'a variety of offerings', 'businessref_84': 'categories such as Books', 'businessref_89': 'including Dry Cleaning & Laundry', 'businessref_32': 'a great atmosphere for enjoying Bars', 'businessref_71': 'Automotive', 'businessref_97': 'Body Shops', 'businessref_14': 'a diverse selection of products across various categories', 'businessref_3': 'including Contractors', 'businessref_27': 'the category of Restaurants', 'businessref_75': 'the categories of Home & Garden', 'businessref_2': 'an exquisite selection of Shopping', 'businessref_48': 'a delightful selection of Pizza', 'businessref_67': 'Vietnamese', 'businessref_76': 'a diverse range of products across various categories', 'businessref_100': 'a range of solutions including Home Services', 'businessref_63': 'Home Services', 'businessref_45': 'the categories of Food', 'businessref_68': 'the categories of Beauty & Spas', 'businessref_6': 'a delightful mix of Restaurants', 'businessref_87': 'a delightful menu featuring Restaurants', 'businessref_66': 'the categories of Fast Food', 'businessref_55': 'St', 'businessref_30': 'a wide range of services and products', 'businessref_15': 'Automotive', 'businessref_96': 'a vibrant atmosphere perfect for enjoying a diverse selection of experiences', 'businessref_11': 'Cosmetic Dentists', 'businessref_73': 'Home Services', 'businessref_4': 'Health & Medical', 'businessref_77': 'Hotels & Travel', 'businessref_18': 'categories such as Home Decor', 'businessref_65': 'a vibrant atmosphere perfect for enjoying Irish', 'businessref_86': 'a diverse menu featuring American (New)', 'businessref_53': 'a diverse menu featuring Salad', 'businessref_40': 'Venues & Event Spaces', 'businessref_44': 'a delightful array of options', 'businessref_43': 'a delightful menu featuring Tex-Mex', 'businessref_9': 'a delightful menu featuring Restaurants', 'businessref_20': 'a diverse array of options', 'businessref_37': 'Fitness & Instruction', 'businessref_62': 'a diverse range of products and services', 'businessref_94': 'a diverse menu that showcases a delightful fusion of flavors across categories such as Food', 'businessref_90': 'a diverse menu featuring Fast Food', 'businessref_31': 'Automotive services', 'businessref_85': 'a tempting selection of treats', 'businessref_25': 'the categories of Food', 'businessref_82': 'a delightful array of options', 'businessref_58': 'a wide range of services and products', 'businessref_60': 'one convenient location', 'businessref_21': 'a comprehensive range of services and products', 'businessref_98': 'Real Estate', 'businessref_16': 'a fantastic experience for those seeking American (New)', 'businessref_46': 'a diverse experience with options for Restaurants', 'businessref_22': 'the field of Doctors', 'businessref_36': "the categories of 'Restaurants", 'businessref_38': 'Hair Salons', 'businessref_81': 'a wide range of services including Barbers', 'businessref_13': 'a delightful experience encompassing Food', 'businessref_17': 'the categories of Shopping'}, 'count_credit_card_businesses': 75}, 'var_call_Qy3bbpiEPqRZv3GwSpflEel5': 'file_storage/call_Qy3bbpiEPqRZv3GwSpflEel5.json'}

exec(code, env_args)
