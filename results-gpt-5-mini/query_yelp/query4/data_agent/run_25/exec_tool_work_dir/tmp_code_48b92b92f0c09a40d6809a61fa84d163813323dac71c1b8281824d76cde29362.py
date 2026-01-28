code = """import json
from pathlib import Path
# load businesses that accept credit cards
p = Path(var_call_B6wib2tXTY7mz2CRmWcwGLin)
biz_accept = json.loads(p.read_text())
# load reviews mapped
p2 = Path(var_call_YYUsjNNOgsRq05W9Xyzy2OVr)
rev_meta = json.loads(p2.read_text())
# We don't have the full mapped reviews here; instead read original reviews file
p3 = Path(var_call_dgNX2JtQN6c1wyGbWHMecPQu)
reviews = json.loads(p3.read_text())
# create mapping business_id -> list of ratings
ratings_by_business = {}
for r in reviews:
    br = r.get('business_ref')
    if br and isinstance(br, str) and br.startswith('businessref_'):
        bid = 'businessid_' + br.split('_',1)[1]
    else:
        bid = br
    try:
        rating = float(r.get('rating'))
    except:
        continue
    ratings_by_business.setdefault(bid, []).append(rating)

# Parse categories from biz_accept descriptions similar to previous
import re
biz_cats = {}
for r in biz_accept:
    bid = r.get('business_id')
    desc = r.get('description') or ''
    cats = r.get('categories')
    cat_list = []
    if cats and isinstance(cats, list):
        cat_list = cats
    elif cats and isinstance(cats, str):
        cat_list = [c.strip() for c in cats.split(',') if c.strip()]
    else:
        m = re.search(r'offers (?:a|an|the)?(?: range of services)?(?: in| including| such as)? (.*)', desc, flags=re.IGNORECASE)
        if m:
            tail = m.group(1).strip().rstrip('.')
            tail = tail.replace(' and ', ', ')
            parts = [p.strip() for p in re.split(r',|;|\band\b', tail) if p.strip()]
            parts2 = []
            for part in parts:
                for sub in re.split(r'/| & |\band\b', part):
                    s = sub.strip()
                    if s:
                        parts2.append(s)
            cat_list = parts2[:6]
    # normalize categories to first token and title case
    norm = []
    for c in cat_list:
        # remove trailing words like 'to meet all your travel'
        c2 = re.split(r' to | to meet| to cater| for ', c)[0]
        c2 = c2.strip(" '\"")
        # if contains parentheses, remove
        c2 = re.sub(r"\(.*\)", "", c2).strip()
        if c2:
            # keep lower-case consistent
            norm.append(c2.title())
    if not norm:
        # fallback: mark Unknown
        norm = ['Unknown']
    biz_cats[bid] = norm

# Now aggregate counts per category for businesses that accept credit cards
cat_counts = {}
cat_ratings = {}
for bid, cats in biz_cats.items():
    # consider primary category as first
    primary = cats[0]
    cat_counts[primary] = cat_counts.get(primary, 0) + 1
    # compute average rating for this business from reviews if exists
    rlist = ratings_by_business.get(bid, [])
    if rlist:
        avg_biz = sum(rlist)/len(rlist)
        cat_ratings.setdefault(primary, []).append(avg_biz)

# compute average rating per category (average of business averages)
cat_avg = {}
for c, lst in cat_ratings.items():
    cat_avg[c] = sum(lst)/len(lst)

# find category with max count
if cat_counts:
    max_cat = max(cat_counts.items(), key=lambda x: x[1])[0]
    max_count = cat_counts[max_cat]
    avg_rating = cat_avg.get(max_cat, None)
else:
    max_cat = None
    max_count = 0
    avg_rating = None

res = {'top_category': max_cat, 'business_count': max_count, 'average_rating': None}
if avg_rating is not None:
    res['average_rating'] = round(avg_rating,3)

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_lgZkHgp6xdF60q6wisDlHU78': ['checkin', 'business'], 'var_call_8NYYAvcvcbbNpZ4xP3tTyvjV': ['review', 'tip', 'user'], 'var_call_PtZeupfw8rOKXsTtykxJxjAb': 'file_storage/call_PtZeupfw8rOKXsTtykxJxjAb.json', 'var_call_B6wib2tXTY7mz2CRmWcwGLin': 'file_storage/call_B6wib2tXTY7mz2CRmWcwGLin.json', 'var_call_YP4FE6GOpmppMtagA9lUh1Xz': 'file_storage/call_YP4FE6GOpmppMtagA9lUh1Xz.json', 'var_call_dgNX2JtQN6c1wyGbWHMecPQu': 'file_storage/call_dgNX2JtQN6c1wyGbWHMecPQu.json', 'var_call_YYUsjNNOgsRq05W9Xyzy2OVr': {'count': 2000, 'sample': [{'business_id': 'businessid_34', 'rating': 2.0}, {'business_id': 'businessid_89', 'rating': 5.0}, {'business_id': 'businessid_82', 'rating': 4.0}, {'business_id': 'businessid_66', 'rating': 2.0}, {'business_id': 'businessid_95', 'rating': 1.0}, {'business_id': 'businessid_24', 'rating': 4.0}, {'business_id': 'businessid_40', 'rating': 4.0}, {'business_id': 'businessid_47', 'rating': 5.0}, {'business_id': 'businessid_16', 'rating': 3.0}, {'business_id': 'businessid_96', 'rating': 5.0}]}}

exec(code, env_args)
