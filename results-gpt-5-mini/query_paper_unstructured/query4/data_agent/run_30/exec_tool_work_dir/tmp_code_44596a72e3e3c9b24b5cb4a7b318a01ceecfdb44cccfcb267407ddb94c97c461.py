code = """import json, re
# Load grouped citation totals
path = var_call_MLumbxhqVF3nCqRedTvljr8a
with open(path, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# keywords to identify physical activity related titles
keywords = ['activity','exercise','fitness','physical','track','tracking','movement','step','steps','running','fit','fitness']
filenames = []
for rec in cit:
    title = rec.get('title','')
    t_low = title.lower()
    if any(k in t_low for k in keywords):
        fname = title + '.txt'
        filenames.append(fname)

# dedupe
filenames = sorted(list(dict.fromkeys(filenames)))
print('__RESULT__:')
print(json.dumps(filenames))"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json', 'var_call_SoNIw3qUMrpUQj9KJImwD4pv': [], 'var_call_KIGFc7rvmzz7P8e6jgdMDxDI': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years': [], 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years': [], 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'years': [], 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'years': [], 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years': [], 'has_physical_activity': True}], 'var_call_xY5jFhX2kmhWZxFrIZamyzd8': ['Citations', 'sqlite_sequence'], 'var_call_MLumbxhqVF3nCqRedTvljr8a': 'file_storage/call_MLumbxhqVF3nCqRedTvljr8a.json', 'var_call_4mFzuOqu9whawkhIoJrvVOOs': 'file_storage/call_4mFzuOqu9whawkhIoJrvVOOs.json', 'var_call_rbAUDp58fKuBnmBYq4rrtpcj': []}

exec(code, env_args)
