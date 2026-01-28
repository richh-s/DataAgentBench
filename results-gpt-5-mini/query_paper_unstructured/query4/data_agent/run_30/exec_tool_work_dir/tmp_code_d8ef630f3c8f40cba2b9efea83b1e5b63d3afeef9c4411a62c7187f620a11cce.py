code = """import json
path = var_call_MLumbxhqVF3nCqRedTvljr8a
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Filter citations records for titles that likely are in 'physical activity' domain.
# Use substring matching: look for titles that contain keywords like 'activity', 'exercise', 'fitness', 'physical'
keywords = ['activity','exercise','fitness','physical','track','tracking']
filtered = []
for rec in records:
    title = rec.get('title','')
    total = rec.get('total_citations',0)
    t_low = title.lower()
    if any(k in t_low for k in keywords):
        try:
            total_int = int(total)
        except:
            try:
                total_int = int(float(total))
            except:
                total_int = None
        filtered.append({'title': title, 'total_citations': total_int})

print('__RESULT__:')
print(json.dumps(filtered[:200]))"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json', 'var_call_SoNIw3qUMrpUQj9KJImwD4pv': [], 'var_call_KIGFc7rvmzz7P8e6jgdMDxDI': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years': [], 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years': [], 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'years': [], 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'years': [], 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'years': [], 'has_physical_activity': True}], 'var_call_xY5jFhX2kmhWZxFrIZamyzd8': ['Citations', 'sqlite_sequence'], 'var_call_MLumbxhqVF3nCqRedTvljr8a': 'file_storage/call_MLumbxhqVF3nCqRedTvljr8a.json'}

exec(code, env_args)
