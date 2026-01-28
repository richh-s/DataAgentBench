code = """import json
from pathlib import Path
# load file paths from storage variables
biz_path = Path(var_call_B6wib2tXTY7mz2CRmWcwGLin)
rev_path = Path(var_call_dgNX2JtQN6c1wyGbWHMecPQu)
# read data
with biz_path.open() as f:
    biz_accept = json.load(f)
with rev_path.open() as f:
    reviews = json.load(f)

# build ratings_by_business mapping
ratings_by_business = {}
for r in reviews:
    br = r.get('business_ref')
    if isinstance(br, str) and br.startswith('businessref_'):
        bid = 'businessid_' + br.split('_',1)[1]
    else:
        bid = br
    try:
        rating = float(r.get('rating'))
    except Exception:
        continue
    ratings_by_business.setdefault(bid, []).append(rating)

# helper to extract categories
def extract_categories(rec):
    cats = rec.get('categories')
    if cats:
        if isinstance(cats, list):
            return [c.strip().title() for c in cats if c and isinstance(c,str)]
        if isinstance(cats, str):
            return [c.strip().title() for c in cats.split(',') if c.strip()]
    desc = (rec.get('description') or '').strip()
    if not desc:
        return ['Unknown']
    # find 'offers' and take substring after it
    low = desc.lower()
    idx = low.find('offers')
    if idx == -1:
        # try 'this' or return Unknown
        return ['Unknown']
    tail = desc[idx+len('offers'):].strip()
    # remove leading 'a', 'a range of services', etc
    prefixes = ['a range of services in', 'a range of services', 'a range of services, including', 'in', 'including', 'a', 'an', 'the']
    for p in prefixes:
        if tail.lower().startswith(p):
            tail = tail[len(p):].strip()
            break
    # cut at first period
    if '.' in tail:
        tail = tail.split('.',1)[0]
    # replace ' and ' with ', '
    tail = tail.replace(' and ', ', ')
    parts = [p.strip().title() for p in tail.split(',') if p.strip()]
    if not parts:
        return ['Unknown']
    # further split elements that contain '/' or '&'
    final = []
    for p in parts:
        for sep in ['/',' & '] :
            if sep in p:
                for sub in p.split(sep):
                    s = sub.strip()
                    if s:
                        final.append(s.title())
                break
        else:
            final.append(p.title())
    return final[:6]

# build business -> categories mapping
biz_cats = {}
for rec in biz_accept:
    bid = rec.get('business_id')
    cats = extract_categories(rec)
    biz_cats[bid] = cats

# aggregate counts and ratings
cat_counts = {}
cat_biz_avg_ratings = {}
for bid, cats in biz_cats.items():
    primary = cats[0] if cats else 'Unknown'
    cat_counts[primary] = cat_counts.get(primary, 0) + 1
    # compute business average rating if reviews exist
    rlist = ratings_by_business.get(bid)
    if rlist:
        avg_biz = sum(rlist)/len(rlist)
        cat_biz_avg_ratings.setdefault(primary, []).append(avg_biz)

# compute average rating per category
cat_avg = {}
for c, lst in cat_biz_avg_ratings.items():
    if lst:
        cat_avg[c] = sum(lst)/len(lst)

# find category with max count
if cat_counts:
    max_cat = max(cat_counts.items(), key=lambda x: x[1])[0]
    max_count = cat_counts[max_cat]
    avg_rating = cat_avg.get(max_cat)
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
