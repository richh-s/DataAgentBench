code = """import json, re

# Load the paper docs result (file path stored in var_call_LspQyQbd0kcChbdh23YQrEF0)
with open(var_call_LspQyQbd0kcChbdh23YQrEF0, 'r') as f:
    docs = json.load(f)

# Load the citations aggregated file (file path stored in var_call_Yu8sRfoQ9H0o3vvDRCE7U41m)
with open(var_call_Yu8sRfoQ9H0o3vvDRCE7U41m, 'r') as f:
    citations = json.load(f)

# Build a map of citations
cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []

for doc in docs:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text', '')
    # Find year
    year = None
    head = text[:2000]
    m = re.search(r"\b(19|20)\d{2}\b", head)
    if m:
        y = int(m.group(0))
        if 1900 <= y <= 2024:
            year = y
    if year is None:
        m = re.search(r"\b(19|20)\d{2}\b", text)
        if m:
            y = int(m.group(0))
            if 1900 <= y <= 2024:
                year = y
    # Domain detection: physical activity substring
    domain = bool(re.search(r'physical\s*activity', text, re.I))
    if year == 2016 and domain:
        results.append({'title': title, 'total_citations': cit_map.get(title, 0)})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_LoAS7jJZv6Hq2gHMPVDaMQ4s': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}], 'var_call_VHUBb79gMr7rnViIIojE4OH5': 'file_storage/call_VHUBb79gMr7rnViIIojE4OH5.json', 'var_call_FboBebDHKGnqk26qrfP9zZmQ': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': '265'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': '266'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'total_citations': '271'}, {'title': 'Charting Design Preferences on Wellness Wearables', 'total_citations': '269'}], 'var_call_8s45VOTlZ7fFiRIv2lpI8sa4': [], 'var_call_qXBai4BehGQP9gBldKW7gLfZ': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}], 'var_call_BmR7PU1bDpsdOZe8ClB6oF8P': 'file_storage/call_BmR7PU1bDpsdOZe8ClB6oF8P.json', 'var_call_6hcauF4anM5LdjfCuMtqyqqe': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}], 'var_call_N1kPFVPmsE1lTLgsJjAA5Xqt': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}], 'var_call_LspQyQbd0kcChbdh23YQrEF0': 'file_storage/call_LspQyQbd0kcChbdh23YQrEF0.json', 'var_call_Yu8sRfoQ9H0o3vvDRCE7U41m': 'file_storage/call_Yu8sRfoQ9H0o3vvDRCE7U41m.json'}

exec(code, env_args)
