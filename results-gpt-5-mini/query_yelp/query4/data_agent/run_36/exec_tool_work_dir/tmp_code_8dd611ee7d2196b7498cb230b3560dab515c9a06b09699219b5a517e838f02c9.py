code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_SAZGzLxLXbN199MGBjTmNm1v, 'r') as f:
    businesses = json.load(f)
with open(var_call_y40HEuxeyQN0L9Kcca7Zn9Up, 'r') as f:
    reviews = json.load(f)

df_biz = pd.DataFrame(businesses)
# Ensure necessary columns exist
if 'business_id' not in df_biz.columns:
    df_biz['business_id'] = df_biz.get('_id')

# Normalize attributes and categories
def accepts_cc(attr):
    if not attr or attr == 'None':
        return False
    if isinstance(attr, dict):
        val = attr.get('BusinessAcceptsCreditCards')
    else:
        # sometimes attributes are strings that look like dicts or 'None'
        try:
            # try to eval-ish by looking for substring
            s = str(attr)
            if "BusinessAcceptsCreditCards" in s:
                # crude parse: look for BusinessAcceptsCreditCards': 'True'
                if 'True' in s:
                    return True
                else:
                    return False
            else:
                return False
        except Exception:
            return False
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    s = str(val)
    return 'True' in s


def parse_categories(cat):
    if not cat or cat == 'None':
        return []
    if isinstance(cat, list):
        return [c.strip() for c in cat if c]
    if isinstance(cat, str):
        # split by comma
        parts = [c.strip() for c in cat.split(',') if c.strip()]
        return parts
    return []

# Apply
df_biz['accepts_cc'] = df_biz['attributes'].apply(accepts_cc)
# categories might not exist in some docs
if 'categories' not in df_biz.columns:
    df_biz['categories'] = None

df_biz['categories_parsed'] = df_biz['categories'].apply(parse_categories)

# Filter businesses that accept credit cards and have categories
df_biz_cc = df_biz[df_biz['accepts_cc']].copy()
# Explode categories
df_biz_cc = df_biz_cc[['business_id','categories_parsed']].explode('categories_parsed')
df_biz_cc = df_biz_cc.dropna(subset=['categories_parsed'])
df_biz_cc = df_biz_cc[df_biz_cc['categories_parsed'] != '']

# Count unique businesses per category
cat_counts = df_biz_cc.groupby('categories_parsed')['business_id'].nunique().reset_index(name='business_count')
if cat_counts.empty:
    result = {"category": None, "business_count": 0, "average_rating": None}
else:
    cat_counts = cat_counts.sort_values(['business_count','categories_parsed'], ascending=[False, True])
    top_row = cat_counts.iloc[0]
    top_category = top_row['categories_parsed']
    top_count = int(top_row['business_count'])

    # Prepare reviews
    df_rev = pd.DataFrame(reviews)
    if df_rev.empty:
        avg_rating = None
    else:
        # convert rating to numeric
        if 'rating' in df_rev.columns:
            df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')
        else:
            df_rev['rating'] = None
        # map business_ref to business_id
        if 'business_ref' in df_rev.columns:
            df_rev['business_id'] = df_rev['business_ref'].astype(str).str.replace('businessref_','businessid_')
        else:
            df_rev['business_id'] = None

        # get business_ids for top category
        biz_ids_top = df_biz_cc[df_biz_cc['categories_parsed'] == top_category]['business_id'].unique().tolist()
        # filter reviews
        df_rev_top = df_rev[df_rev['business_id'].isin(biz_ids_top)]
        if df_rev_top.empty:
            avg_rating = None
        else:
            avg_rating = float(df_rev_top['rating'].mean())

    result = {"category": top_category, "business_count": top_count, "average_rating": (None if avg_rating is None else round(avg_rating, 2))}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PfBFEnOqSxBmE3yZz4jDYeYE': ['business', 'checkin'], 'var_call_NjmNYE8FrhRYoKqDZPZ3zDE6': ['review', 'tip', 'user'], 'var_call_SAZGzLxLXbN199MGBjTmNm1v': 'file_storage/call_SAZGzLxLXbN199MGBjTmNm1v.json', 'var_call_y40HEuxeyQN0L9Kcca7Zn9Up': 'file_storage/call_y40HEuxeyQN0L9Kcca7Zn9Up.json'}

exec(code, env_args)
