code = """import json, re
with open(var_call_c8DwRj64MtSJYZW92sSCp2Oh, 'r') as f:
    businesses = json.load(f)
with open(var_call_n0S2syUfDJf7pjVSheCo8pDc, 'r') as f:
    reviews = json.load(f)

# US state codes
state_codes = set(['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'])

ref_to_state = {}
state_reviewcount = {}
pattern = re.compile(r'\b(' + '|'.join(state_codes) + r')\b')
for b in businesses:
    bid = b.get('business_id')
    desc = (b.get('description') or '')
    rc = b.get('review_count')
    try:
        rc_int = int(rc)
    except:
        try:
            rc_int = int(float(rc))
        except:
            rc_int = 0
    if not bid:
        continue
    parts = bid.split('_',1)
    if len(parts) != 2:
        continue
    bref = 'businessref_' + parts[1]
    # find state via regex
    m = pattern.search(desc)
    if m:
        state = m.group(1)
        ref_to_state[bref] = state
        state_reviewcount[state] = state_reviewcount.get(state, 0) + rc_int

# find top state
if not state_reviewcount:
    result = {"state": None, "total_reviews": 0, "average_rating": None}
else:
    state_max = max(state_reviewcount.items(), key=lambda x: x[1])[0]
    total_reviews = state_reviewcount[state_max]
    # collect ratings
    ratings = []
    for r in reviews:
        bref = r.get('business_ref')
        rating = r.get('rating')
        if bref in ref_to_state and ref_to_state[bref] == state_max:
            try:
                ratings.append(float(rating))
            except:
                pass
    avg_rating = round(sum(ratings)/len(ratings), 3) if ratings else None
    result = {"state": state_max, "total_reviews": total_reviews, "average_rating": avg_rating}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DyWkhUZrWhEw6LixAvfowfDs': ['business', 'checkin'], 'var_call_ZcivhTR0krr3WaNsPaY0wwdP': ['review', 'tip', 'user'], 'var_call_c8DwRj64MtSJYZW92sSCp2Oh': 'file_storage/call_c8DwRj64MtSJYZW92sSCp2Oh.json', 'var_call_n0S2syUfDJf7pjVSheCo8pDc': 'file_storage/call_n0S2syUfDJf7pjVSheCo8pDc.json', 'var_call_9oeTCPeOCg4UFqZcFJE93muh': {'state': None, 'total_reviews': 0, 'average_rating': None}, 'var_call_1laMVn0AMpbLxhZPrd1MMgLu': 'file_storage/call_1laMVn0AMpbLxhZPrd1MMgLu.json'}

exec(code, env_args)
