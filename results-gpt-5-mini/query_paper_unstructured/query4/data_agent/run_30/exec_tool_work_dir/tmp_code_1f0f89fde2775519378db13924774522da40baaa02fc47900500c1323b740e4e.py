code = """import json, re
# Load Mongo query results (papers with 'physical activity' and '2016')
path_mongo = var_call_R6gwTreaDcfvqovoD3OXntlB
with open(path_mongo, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)

# Load citation totals grouped
path_cit = var_call_MLumbxhqVF3nCqRedTvljr8a
with open(path_cit, 'r', encoding='utf-8') as f:
    cit_records = json.load(f)

# build citation dict
cit_dict = {}
for rec in cit_records:
    title = rec.get('title','')
    total = rec.get('total_citations', 0)
    try:
        total_int = int(total)
    except:
        try:
            total_int = int(float(total))
        except:
            total_int = None
    cit_dict[title] = total_int

results = []
seen = set()
for rec in mongo_records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    # detect publication year
    pub_year = None
    if re.search(r'\b2016\b', text):
        pub_year = 2016
    else:
        years = re.findall(r'\b(20\d{2})\b', text)
        for y in years:
            if 2000 <= int(y) <= 2026:
                pub_year = int(y)
                break
    if pub_year == 2016:
        if title in seen:
            continue
        seen.add(title)
        total = cit_dict.get(title)
        results.append({"title": title, "total_citations": total})

# Sort results by title
results = sorted(results, key=lambda x: x['title'])
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json', 'var_call_SoNIw3qUMrpUQj9KJImwD4pv': [], 'var_call_KIGFc7rvmzz7P8e6jgdMDxDI': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years': [], 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years': [], 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'years': [], 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'years': [], 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years': [], 'has_physical_activity': True}], 'var_call_xY5jFhX2kmhWZxFrIZamyzd8': ['Citations', 'sqlite_sequence'], 'var_call_MLumbxhqVF3nCqRedTvljr8a': 'file_storage/call_MLumbxhqVF3nCqRedTvljr8a.json', 'var_call_4mFzuOqu9whawkhIoJrvVOOs': 'file_storage/call_4mFzuOqu9whawkhIoJrvVOOs.json'}

exec(code, env_args)
