code = """import json
import re

# Load documents (file path stored in var_call_VHUBb79gMr7rnViIIojE4OH5)
with open(var_call_VHUBb79gMr7rnViIIojE4OH5, 'r') as f:
    docs = json.load(f)

# Citations variable
citations = var_call_FboBebDHKGnqk26qrfP9zZmQ

# Helper to get total citations by title
cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []

for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # Find publication year: search first 800 chars for a 4-digit year 2000-2024, else search whole text
    year = None
    head = text[:2000]
    m = re.search(r'\b(20\d{2})\b', head)
    if m:
        y = int(m.group(1))
        if 2000 <= y <= 2024:
            year = y
    if year is None:
        m = re.search(r'\b(20\d{2})\b', text)
        if m:
            y = int(m.group(1))
            if 2000 <= y <= 2024:
                year = y
    # Domain detection: look for 'physical activity' substring anywhere
    domain = None
    if re.search(r'physical\s*activity', text, re.I):
        domain = 'physical activity'
    # Append parsed info
    results.append({'title': title, 'year': year, 'domain': domain, 'total_citations': cit_map.get(title)})

# Filter for year 2016 and domain physical activity
filtered = [ {'title': r['title'], 'total_citations': r['total_citations'] if r['total_citations'] is not None else 0}
            for r in results if r['year'] == 2016 and r['domain'] == 'physical activity']

# Prepare output
out = filtered

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_LoAS7jJZv6Hq2gHMPVDaMQ4s': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_call_VHUBb79gMr7rnViIIojE4OH5': 'file_storage/call_VHUBb79gMr7rnViIIojE4OH5.json', 'var_call_FboBebDHKGnqk26qrfP9zZmQ': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}]}

exec(code, env_args)
