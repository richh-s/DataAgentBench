code = """import json
# Data from previous tool calls
chi_docs = var_call_3cOu9b8NbBldekMpffrl9Z0b
citations = var_call_vf7KMhl8dBW9gsrmSxnUlJug

# Extract titles from filenames (strip .txt)
chi_titles = [d['filename'].rsplit('.txt', 1)[0] for d in chi_docs]

# Filter citation records to those whose title is in CHI titles
per_paper = []
total = 0
for rec in citations:
    title = rec.get('title')
    if title in chi_titles:
        try:
            count = int(rec.get('citation_count', 0))
        except:
            count = 0
        per_paper.append({'title': title, 'citation_count': count})
        total += count

# Sort per_paper by title for consistency
per_paper = sorted(per_paper, key=lambda x: x['title'])

result = {'per_paper': per_paper, 'total_citations_2020': total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3cOu9b8NbBldekMpffrl9Z0b': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_call_vf7KMhl8dBW9gsrmSxnUlJug': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citation_count': '16'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': '98'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'citation_count': '52'}]}

exec(code, env_args)
