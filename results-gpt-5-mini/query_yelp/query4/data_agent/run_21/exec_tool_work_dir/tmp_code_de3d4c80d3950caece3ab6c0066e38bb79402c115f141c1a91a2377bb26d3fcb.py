code = """import json
import pandas as pd

# Load full business collection
with open(var_call_qfWASP1jDANvWkjEHQI1Aunt, 'r') as f:
    businesses = json.load(f)

# Load reviews
with open(var_call_5NMb4LqhLRjQjxmxk1VqC7DE, 'r') as f:
    reviews = json.load(f)

# DataFrames
df_b = pd.DataFrame(businesses)
if 'attributes' not in df_b.columns:
    df_b['attributes'] = None
if 'categories' not in df_b.columns:
    df_b['categories'] = None

# Determine accepts credit cards by simple string checks
def accepts_cc(attr):
    try:
        s = str(attr)
        if 'BusinessAcceptsCreditCards' not in s:
            return False
        # check for True presence after key
        return 'True' in s
    except Exception:
        return False

df_b['accepts_cc'] = df_b['attributes'].apply(accepts_cc)

# Filter businesses that accept credit cards
df_cc = df_b[df_b['accepts_cc']].copy()

# Parse categories
def parse_categories(cat, desc=None):
    if cat is None:
        return []
    # if it's a list
    if isinstance(cat, list):
        return [c for c in cat if c]
    s = str(cat)
    if s in ['None', 'NoneType']:
        return []
    parts = [p.strip() for p in s.split(',') if p.strip()]
    return parts

# Apply
if not df_cc.empty:
    df_cc['category_list'] = df_cc['categories'].apply(lambda c: parse_categories(c))
    # try to infer from description if category_list empty and description exists
    if 'description' in df_cc.columns:
        def infer(row):
            if row['category_list']:
                return row['category_list']
            desc = row.get('description')
            if not desc or desc == 'None':
                return []
            s = str(desc)
            seg = s.split('-')[0].split('|')[0].split(':')[0]
            parts = [p.strip() for p in seg.split(',') if p.strip()]
            return parts
        df_cc['category_list'] = df_cc.apply(infer, axis=1)
else:
    df_cc['category_list'] = []

# Explode categories
if not df_cc.empty:
    df_exploded = df_cc[['business_id', 'category_list']].explode('category_list')
    df_exploded = df_exploded[df_exploded['category_list'].notnull() & (df_exploded['category_list'] != '')]
else:
    df_exploded = pd.DataFrame(columns=['business_id', 'category_list'])

# Determine top category
if df_exploded.empty:
    top_category = 'Unknown'
    business_ids_in_top = df_cc['business_id'].tolist()
    business_count = len(business_ids_in_top)
else:
    counts = df_exploded.groupby('category_list')['business_id'].nunique().reset_index(name='business_count')
    counts = counts.sort_values(['business_count', 'category_list'], ascending=[False, True]).reset_index(drop=True)
    top_category = counts.loc[0, 'category_list']
    business_count = int(counts.loc[0, 'business_count'])
    business_ids_in_top = df_exploded[df_exploded['category_list'] == top_category]['business_id'].unique().tolist()

# Map business IDs to business_ref
business_refs = [bid.replace('businessid_', 'businessref_') for bid in business_ids_in_top]

# Reviews DataFrame
df_r = pd.DataFrame(reviews)
if 'rating' in df_r.columns:
    df_r['rating'] = pd.to_numeric(df_r['rating'], errors='coerce')
else:
    df_r['rating'] = None

# Filter reviews for business_refs
if business_refs:
    df_top_reviews = df_r[df_r['business_ref'].isin(business_refs)].copy()
else:
    df_top_reviews = pd.DataFrame(columns=df_r.columns)

if not df_top_reviews.empty:
    avg_rating = round(float(df_top_reviews['rating'].mean()), 2)
else:
    avg_rating = None

result = {
    'category': top_category,
    'business_count': business_count,
    'average_rating': avg_rating
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rvHRCEMFNVO1KVxPBGjUb6qf': ['business', 'checkin'], 'var_call_Yw2wnhmJIcG2RMsGwwxCEmln': ['review', 'tip', 'user'], 'var_call_qfWASP1jDANvWkjEHQI1Aunt': 'file_storage/call_qfWASP1jDANvWkjEHQI1Aunt.json', 'var_call_E4IHpk0FisD4sHL1SMAjMwL5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool'}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'name': 'Breeze Blow Dry Bar'}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'name': 'Impact Guns'}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'name': 'J&Q Nails'}, {'_id': '6859a000fe8b31cd7362e2b1', 'business_id': 'businessid_92', 'name': 'Luminosity'}, {'_id': '6859a000fe8b31cd7362e2b2', 'business_id': 'businessid_64', 'name': 'Nail Care Salon'}, {'_id': '6859a000fe8b31cd7362e2b3', 'business_id': 'businessid_52', 'name': 'Architectural Antiques of Indianapolis'}, {'_id': '6859a000fe8b31cd7362e2b4', 'business_id': 'businessid_29', 'name': "Aster's Floral Shop"}, {'_id': '6859a000fe8b31cd7362e2b5', 'business_id': 'businessid_10', 'name': 'China Wok'}, {'_id': '6859a000fe8b31cd7362e2b6', 'business_id': 'businessid_61', 'name': 'Brandon Family Medical Care'}, {'_id': '6859a000fe8b31cd7362e2b7', 'business_id': 'businessid_54', 'name': '7-Eleven'}, {'_id': '6859a000fe8b31cd7362e2b8', 'business_id': 'businessid_8', 'name': 'Uber'}, {'_id': '6859a000fe8b31cd7362e2ba', 'business_id': 'businessid_91', 'name': 'Cafe Porche and snowbar'}, {'_id': '6859a000fe8b31cd7362e2bb', 'business_id': 'businessid_83', 'name': 'Eyeglass World'}, {'_id': '6859a000fe8b31cd7362e2bc', 'business_id': 'businessid_93', 'name': "Callahan's Corner"}, {'_id': '6859a000fe8b31cd7362e2be', 'business_id': 'businessid_24', 'name': 'FroYo Frozen Yogurt'}, {'_id': '6859a000fe8b31cd7362e2bf', 'business_id': 'businessid_95', 'name': 'Subway'}, {'_id': '6859a000fe8b31cd7362e2c1', 'business_id': 'businessid_26', 'name': "McDonald's"}, {'_id': '6859a000fe8b31cd7362e2c2', 'business_id': 'businessid_84', 'name': 'Gamestop'}, {'_id': '6859a000fe8b31cd7362e2c3', 'business_id': 'businessid_89', 'name': 'King of Prussia Laundromat'}, {'_id': '6859a000fe8b31cd7362e2c4', 'business_id': 'businessid_32', 'name': 'The Recovery Room Bar & Grill'}, {'_id': '6859a000fe8b31cd7362e2c7', 'business_id': 'businessid_71', 'name': 'Lithia Ford Lincoln of Boise'}, {'_id': '6859a000fe8b31cd7362e2c8', 'business_id': 'businessid_97', 'name': 'Executive Auto Body'}, {'_id': '6859a000fe8b31cd7362e2c9', 'business_id': 'businessid_14', 'name': 'Ross Dress for Less'}, {'_id': '6859a000fe8b31cd7362e2ca', 'business_id': 'businessid_3', 'name': 'Mr. Dry Out'}, {'_id': '6859a000fe8b31cd7362e2ce', 'business_id': 'businessid_27', 'name': 'Egg Roll King Two'}, {'_id': '6859a000fe8b31cd7362e2cf', 'business_id': 'businessid_75', 'name': 'Light World'}, {'_id': '6859a000fe8b31cd7362e2d1', 'business_id': 'businessid_2', 'name': 'Bloom'}, {'_id': '6859a000fe8b31cd7362e2d3', 'business_id': 'businessid_48', 'name': 'The Loop Taste of Chicago'}, {'_id': '6859a000fe8b31cd7362e2d4', 'business_id': 'businessid_67', 'name': "Hanoi's Pho"}, {'_id': '6859a000fe8b31cd7362e2d7', 'business_id': 'businessid_76', 'name': 'Big Lots'}, {'_id': '6859a000fe8b31cd7362e2d8', 'business_id': 'businessid_100', 'name': 'Service First Heating & Air Conditioning'}, {'_id': '6859a000fe8b31cd7362e2da', 'business_id': 'businessid_63', 'name': 'The Iron Shop'}, {'_id': '6859a000fe8b31cd7362e2db', 'business_id': 'businessid_45', 'name': 'The Fresh Market'}, {'_id': '6859a000fe8b31cd7362e2dc', 'business_id': 'businessid_68', 'name': 'Brow Art'}, {'_id': '6859a000fe8b31cd7362e2dd', 'business_id': 'businessid_6', 'name': 'The Jungle'}, {'_id': '6859a000fe8b31cd7362e2de', 'business_id': 'businessid_87', 'name': 'Jordans Fish and Chicken'}, {'_id': '6859a000fe8b31cd7362e2e1', 'business_id': 'businessid_66', 'name': 'Panda Express'}, {'_id': '6859a000fe8b31cd7362e2e2', 'business_id': 'businessid_55', 'name': 'Uptown Snoballs and Ice Cream'}, {'_id': '6859a000fe8b31cd7362e2e3', 'business_id': 'businessid_30', 'name': 'Dalco Home Remodeling'}, {'_id': '6859a000fe8b31cd7362e2e5', 'business_id': 'businessid_15', 'name': 'Take 5 Oil Change'}, {'_id': '6859a000fe8b31cd7362e2e6', 'business_id': 'businessid_96', 'name': 'Farmhaus Restaurant'}, {'_id': '6859a000fe8b31cd7362e2e7', 'business_id': 'businessid_11', 'name': 'Allan Link,DMD - The DentaLink'}, {'_id': '6859a000fe8b31cd7362e2e8', 'business_id': 'businessid_73', 'name': 'Biggest Little Pools'}, {'_id': '6859a000fe8b31cd7362e2e9', 'business_id': 'businessid_4', 'name': 'Dentistry for Children and Adolescents - St. Charles'}, {'_id': '6859a000fe8b31cd7362e2ea', 'business_id': 'businessid_77', 'name': 'Holiday Inn Philadelphia Stadium'}, {'_id': '6859a000fe8b31cd7362e2eb', 'business_id': 'businessid_18', 'name': 'Sleep Number'}, {'_id': '6859a000fe8b31cd7362e2ec', 'business_id': 'businessid_65', 'name': "Pat Flynn's Public House"}, {'_id': '6859a000fe8b31cd7362e2ed', 'business_id': 'businessid_86', 'name': "Humpty's Dumplings"}, {'_id': '6859a000fe8b31cd7362e2ee', 'business_id': 'businessid_53', 'name': 'Samwich'}, {'_id': '6859a000fe8b31cd7362e2ef', 'business_id': 'businessid_40', 'name': 'Artesano Gallery & Iron Works'}, {'_id': '6859a000fe8b31cd7362e2f0', 'business_id': 'businessid_44', 'name': 'Fishtown Diner'}, {'_id': '6859a000fe8b31cd7362e2f1', 'business_id': 'businessid_43', 'name': 'Taco Bell'}, {'_id': '6859a000fe8b31cd7362e2f3', 'business_id': 'businessid_9', 'name': 'Coffee House Too Cafe'}, {'_id': '6859a000fe8b31cd7362e2f4', 'business_id': 'businessid_20', 'name': 'Chick-fil-A'}, {'_id': '6859a000fe8b31cd7362e2f5', 'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood'}, {'_id': '6859a000fe8b31cd7362e2f7', 'business_id': 'businessid_62', 'name': 'Winn Dixie'}, {'_id': '6859a000fe8b31cd7362e2f8', 'business_id': 'businessid_94', 'name': 'Taste of Europe'}, {'_id': '6859a000fe8b31cd7362e2fa', 'business_id': 'businessid_90', 'name': "Long John Silver's"}, {'_id': '6859a000fe8b31cd7362e2fb', 'business_id': 'businessid_31', 'name': 'Island Way Car Wash'}, {'_id': '6859a000fe8b31cd7362e2fc', 'business_id': 'businessid_85', 'name': 'Insomnia Cookies'}, {'_id': '6859a000fe8b31cd7362e2fd', 'business_id': 'businessid_25', 'name': 'Great Harvest Bread Co'}, {'_id': '6859a000fe8b31cd7362e2fe', 'business_id': 'businessid_82', 'name': 'Miles Table'}, {'_id': '6859a000fe8b31cd7362e2ff', 'business_id': 'businessid_58', 'name': 'GOLFTEC Westshore'}, {'_id': '6859a000fe8b31cd7362e302', 'business_id': 'businessid_60', 'name': 'Walmart'}, {'_id': '6859a000fe8b31cd7362e303', 'business_id': 'businessid_21', 'name': 'Ford of Port Richey'}, {'_id': '6859a000fe8b31cd7362e304', 'business_id': 'businessid_98', 'name': 'Brookmont Apartment Homes'}, {'_id': '6859a000fe8b31cd7362e305', 'business_id': 'businessid_16', 'name': 'Fox and Hound English Pub and Grille'}, {'_id': '6859a000fe8b31cd7362e306', 'business_id': 'businessid_46', 'name': 'Salt + Smoke'}, {'_id': '6859a000fe8b31cd7362e307', 'business_id': 'businessid_22', 'name': 'Main Line Spine'}, {'_id': '6859a000fe8b31cd7362e308', 'business_id': 'businessid_36', 'name': 'Pho & Beyond'}, {'_id': '6859a000fe8b31cd7362e30b', 'business_id': 'businessid_38', 'name': 'Philadelphia Hair Studio'}, {'_id': '6859a000fe8b31cd7362e30c', 'business_id': 'businessid_81', 'name': 'Fantastic Sams Cut & Color'}, {'_id': '6859a000fe8b31cd7362e30d', 'business_id': 'businessid_13', 'name': 'Avian Glen Winery'}, {'_id': '6859a000fe8b31cd7362e30e', 'business_id': 'businessid_17', 'name': 'Whitemarsh Jewelers'}], 'var_call_5NMb4LqhLRjQjxmxk1VqC7DE': 'file_storage/call_5NMb4LqhLRjQjxmxk1VqC7DE.json'}

exec(code, env_args)
