code = """import json
# Load the citations aggregation result
path = var_call_XcSb27QbArGXyjoYM8rd2vqw
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Filter citations for titles that likely are in 'physical activity' domain by substring match in title or from known list
physical_keywords = ['physical activity','activity','exercise','fitness','steps']
physical_titles = []
for rec in citations:
    title = rec.get('title','')
    low = title.lower()
    if any(k in low for k in physical_keywords):
        # convert total_citations to int
        try:
            total = int(rec.get('total_citations',0))
        except:
            total = 0
        physical_titles.append({'title': title, 'total_citations': total})

# Now we need to find which of these were published in 2016. We need to map titles back to paper_docs to find year.
# Load a list of paper docs filenames and try to find year ==2016 in their texts for matching titles
# Query the paper_docs collection for files whose filename (without .txt) is in physical_titles

# Build set of titles without surrounding quotes
candidate_titles = set([t['title'].strip('"') for t in physical_titles])

# For efficiency, write out candidate_titles to print for next step
print('__RESULT__:')
print(json.dumps(list(candidate_titles)))"""

env_args = {'var_call_ueY8ny6tvVKcJ9NNvBSzXQv9': 'file_storage/call_ueY8ny6tvVKcJ9NNvBSzXQv9.json', 'var_call_k4guTGoCsoObrR3VeZLLdU84': [], 'var_call_zQema5txZszizqodvhPu7Oxr': 'file_storage/call_zQema5txZszizqodvhPu7Oxr.json', 'var_call_akrROVWBvQUPsCMRHuNVpUJU': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_call_jiSj5ODYQsrRs6zMyYqQsuSt': 'file_storage/call_jiSj5ODYQsrRs6zMyYqQsuSt.json', 'var_call_1eCuQsCsWNeZ3DNvrZ81xW1q': [], 'var_call_XcSb27QbArGXyjoYM8rd2vqw': 'file_storage/call_XcSb27QbArGXyjoYM8rd2vqw.json'}

exec(code, env_args)
