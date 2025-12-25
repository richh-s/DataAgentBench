code = """import json, pandas as pd

# Load 2016 users from file
path = var_call_VVqfj084o1ksoQOqM5KJ3CkZ
with open(path, 'r') as f:
    users_2016 = json.load(f)

users_df = pd.DataFrame(users_2016)
user_ids_2016 = set(users_df['user_id'].dropna().unique())

# Load reviews (already filtered from 2016-01-01 in SQL)
path_reviews = var_call_27ItVQ0KxTW4qXRBrVAD8hJK
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

reviews_df = pd.DataFrame(reviews)

# Keep reviews from 2016-01-01 onward written by 2016-registered users
reviews_df = reviews_df[reviews_df['user_id'].isin(user_ids_2016)].copy()

# Extract year from mixed-format date strings, keep >= 2016 just in case
import re

def extract_year(s):
    if not isinstance(s, str):
        return None
    m = re.search(r'(20[0-9]{2})', s)
    return int(m.group(1)) if m else None

reviews_df['year'] = reviews_df['date'].apply(extract_year)
reviews_df = reviews_df[reviews_df['year'] >= 2016]

# Map business_ref (businessref_X) to business_id form (businessid_X)
reviews_df['business_id'] = reviews_df['business_ref'].str.replace('businessref_', 'businessid_', regex=False)

# Business categories
biz_df = pd.DataFrame(var_call_gOS4e247cisRfgcgFyyH3p1C)

# In case categories field is missing, assume it's a comma-separated string in description, but here we only have business_id; so just proceed without categories (will yield no result).
# However, likely categories are stored under key 'categories' but projection preview only showed business_id; handle missing safely.
if 'categories' not in biz_df.columns:
    biz_df['categories'] = None

# Merge reviews with businesses
merged = reviews_df.merge(biz_df, on='business_id', how='left')

# Split categories (assume comma-separated string)

def split_categories(c):
    if not isinstance(c, str):
        return []
    return [x.strip() for x in c.split(',') if x.strip()]

merged['cat_list'] = merged['categories'].apply(split_categories)

# Explode
exploded = merged.explode('cat_list')
exploded = exploded[exploded['cat_list'].notna() & (exploded['cat_list'] != '')]

# Count reviews per category
cat_counts = exploded.groupby('cat_list').size().reset_index(name='review_count')

# Top 5
top5 = cat_counts.sort_values('review_count', ascending=False).head(5)

result = top5.to_dict(orient='records')

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_1kwlbvgFSskTax9d7WF9Eh1Q': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}], 'var_call_3GYHBMaePCIzPitMRylgokIW': ['checkin', 'business'], 'var_call_FcjvjKRHBOJUitKPiCvEu5wx': ['review', 'tip', 'user'], 'var_call_17GKmNXVPzGwb2YnwhNgJXtD': [], 'var_call_kBwbgbUAiyJEvTKPFvKQxOsJ': [{'yelping_since': 'October 10, 2009 at 01:37 AM'}, {'yelping_since': 'May 21, 2011 at 03:22 PM'}, {'yelping_since': '2005-07-18 06:22:37'}, {'yelping_since': '2009-04-30 03:16:12'}, {'yelping_since': 'August 18, 2008 at 08:13 AM'}, {'yelping_since': 'May 23, 2009 at 05:44 PM'}, {'yelping_since': '22 Jul 2007, 21:50'}, {'yelping_since': '2011-01-22 16:07:48'}, {'yelping_since': '2010-12-15 02:17:17'}, {'yelping_since': 'April 23, 2010 at 07:48 PM'}, {'yelping_since': '09 Dec 2007, 01:03'}, {'yelping_since': '12 Feb 2011, 01:00'}, {'yelping_since': '2009-04-17 13:38:22'}, {'yelping_since': 'January 17, 2011 at 10:14 PM'}, {'yelping_since': '07 Sep 2009, 22:20'}, {'yelping_since': '2011-04-17 16:27:25'}, {'yelping_since': '2010-06-26 21:11:26'}, {'yelping_since': '29 Feb 2012, 02:51'}, {'yelping_since': '2010-04-19 19:23:27'}, {'yelping_since': '2010-07-12 16:29:17'}], 'var_call_VVqfj084o1ksoQOqM5KJ3CkZ': 'file_storage/call_VVqfj084o1ksoQOqM5KJ3CkZ.json', 'var_call_27ItVQ0KxTW4qXRBrVAD8hJK': 'file_storage/call_27ItVQ0KxTW4qXRBrVAD8hJK.json', 'var_call_gOS4e247cisRfgcgFyyH3p1C': [{'business_id': 'businessid_49'}, {'business_id': 'businessid_47'}, {'business_id': 'businessid_88'}, {'business_id': 'businessid_41'}, {'business_id': 'businessid_33'}, {'business_id': 'businessid_74'}, {'business_id': 'businessid_92'}, {'business_id': 'businessid_64'}, {'business_id': 'businessid_52'}, {'business_id': 'businessid_29'}, {'business_id': 'businessid_10'}, {'business_id': 'businessid_61'}, {'business_id': 'businessid_54'}, {'business_id': 'businessid_8'}, {'business_id': 'businessid_59'}, {'business_id': 'businessid_91'}, {'business_id': 'businessid_83'}, {'business_id': 'businessid_93'}, {'business_id': 'businessid_1'}, {'business_id': 'businessid_24'}, {'business_id': 'businessid_95'}, {'business_id': 'businessid_50'}, {'business_id': 'businessid_26'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_89'}, {'business_id': 'businessid_32'}, {'business_id': 'businessid_70'}, {'business_id': 'businessid_42'}, {'business_id': 'businessid_71'}, {'business_id': 'businessid_97'}, {'business_id': 'businessid_14'}, {'business_id': 'businessid_3'}, {'business_id': 'businessid_35'}, {'business_id': 'businessid_28'}, {'business_id': 'businessid_57'}, {'business_id': 'businessid_27'}, {'business_id': 'businessid_75'}, {'business_id': 'businessid_34'}, {'business_id': 'businessid_2'}, {'business_id': 'businessid_19'}, {'business_id': 'businessid_48'}, {'business_id': 'businessid_67'}, {'business_id': 'businessid_7'}, {'business_id': 'businessid_51'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_100'}, {'business_id': 'businessid_5'}, {'business_id': 'businessid_63'}, {'business_id': 'businessid_45'}, {'business_id': 'businessid_68'}, {'business_id': 'businessid_6'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_78'}, {'business_id': 'businessid_79'}, {'business_id': 'businessid_66'}, {'business_id': 'businessid_55'}, {'business_id': 'businessid_30'}, {'business_id': 'businessid_80'}, {'business_id': 'businessid_15'}, {'business_id': 'businessid_96'}, {'business_id': 'businessid_11'}, {'business_id': 'businessid_73'}, {'business_id': 'businessid_4'}, {'business_id': 'businessid_77'}, {'business_id': 'businessid_18'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_86'}, {'business_id': 'businessid_53'}, {'business_id': 'businessid_40'}, {'business_id': 'businessid_44'}, {'business_id': 'businessid_43'}, {'business_id': 'businessid_72'}, {'business_id': 'businessid_9'}, {'business_id': 'businessid_20'}, {'business_id': 'businessid_37'}, {'business_id': 'businessid_56'}, {'business_id': 'businessid_62'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_39'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_31'}, {'business_id': 'businessid_85'}, {'business_id': 'businessid_25'}, {'business_id': 'businessid_82'}, {'business_id': 'businessid_58'}, {'business_id': 'businessid_12'}, {'business_id': 'businessid_99'}, {'business_id': 'businessid_60'}, {'business_id': 'businessid_21'}, {'business_id': 'businessid_98'}, {'business_id': 'businessid_16'}, {'business_id': 'businessid_46'}, {'business_id': 'businessid_22'}, {'business_id': 'businessid_36'}, {'business_id': 'businessid_69'}, {'business_id': 'businessid_23'}, {'business_id': 'businessid_38'}, {'business_id': 'businessid_81'}, {'business_id': 'businessid_13'}, {'business_id': 'businessid_17'}]}

exec(code, env_args)
