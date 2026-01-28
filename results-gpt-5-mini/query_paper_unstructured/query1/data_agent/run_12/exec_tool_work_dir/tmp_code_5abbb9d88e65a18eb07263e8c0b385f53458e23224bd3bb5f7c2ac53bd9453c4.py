code = """import json
# Access stored tool results
food_var = var_call_3sNuDLBSxnelovrLOLzBzfEy
cit_var = var_call_5qb2CAF3JZrBtZiOGoxW1QJQ

# Load citations data (could be a filepath or a list)
if isinstance(cit_var, str):
    with open(cit_var, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_var

# Load food papers data
if isinstance(food_var, str):
    with open(food_var, 'r', encoding='utf-8') as f:
        food_records = json.load(f)
else:
    food_records = food_var

# Extract titles from filenames (remove .txt)
food_titles = []
for r in food_records:
    if isinstance(r, dict) and 'filename' in r:
        name = r['filename']
        if name.lower().endswith('.txt'):
            name = name[:-4]
        food_titles.append(name)
    elif isinstance(r, str):
        s = r
        if s.lower().endswith('.txt'):
            s = s[:-4]
        food_titles.append(s)

# Build citation mapping: lowercased title -> total_citations (int)
cit_map = {}
for rec in citations:
    title = rec.get('title', '')
    key = title.strip().lower()
    # possible fields for count
    val = rec.get('total_citations') if 'total_citations' in rec else rec.get('citation_count')
    try:
        iv = int(val)
    except:
        try:
            iv = int(float(val))
        except:
            iv = 0
    cit_map[key] = cit_map.get(key, 0) + iv

# Sum citations for food titles using case-insensitive exact or substring match
total = 0
matched = []
unmatched = []
for ft in food_titles:
    key = ft.strip().lower()
    if key in cit_map:
        total += cit_map[key]
        matched.append(ft)
    else:
        # try substring match
        found = False
        for ctitle, val in cit_map.items():
            if key in ctitle or ctitle in key:
                total += val
                matched.append(f"{ft} -> {ctitle}")
                found = True
                break
        if not found:
            unmatched.append(ft)

result = {"total_citations_for_food_domain": total, "matched": matched, "unmatched": unmatched}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_uSubUneGuuAWY52T6NYY6ceY': ['paper_docs'], 'var_call_dSHK3QDz3ZB4zLN4ShJ2UHwd': 'file_storage/call_dSHK3QDz3ZB4zLN4ShJ2UHwd.json', 'var_call_ZfCgkdil8Hs25ecnA269m03f': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_3hg9pvcbtNf1OVwmemQygfct': ['Citations', 'sqlite_sequence'], 'var_call_5qb2CAF3JZrBtZiOGoxW1QJQ': 'file_storage/call_5qb2CAF3JZrBtZiOGoxW1QJQ.json', 'var_call_3sNuDLBSxnelovrLOLzBzfEy': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt'}]}

exec(code, env_args)
