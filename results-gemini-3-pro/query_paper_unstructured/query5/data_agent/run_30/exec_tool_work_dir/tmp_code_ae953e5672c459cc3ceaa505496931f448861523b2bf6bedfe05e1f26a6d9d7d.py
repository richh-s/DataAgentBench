code = """import json
import re

with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

with open(locals()['var_function-call-15227609533641263682'], 'r') as f:
    paper_docs_data = json.load(f)

paper_map = {}
for doc in paper_docs_data:
    if 'filename' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc['text']

total_citations = 0
chi_papers_count = 0
matches_count = 0

for record in citations_data:
    title = record['title']
    if title in paper_map:
        matches_count += 1
        text = paper_map[title]
        header = text[:2000]
        
        # Check for CHI
        # Looking for CHI as a word, or the full conference name
        if re.search(r'\bCHI\b', header) or "Conference on Human Factors in Computing Systems" in header:
             count = int(record['citation_count'])
             total_citations += count
             chi_papers_count += 1

result = {
    "total_citations": total_citations,
    "chi_papers_count": chi_papers_count,
    "total_docs_loaded": len(paper_docs_data),
    "matches_found": matches_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json', 'var_function-call-5326245820750148638': 16, 'var_function-call-17055580434800668848': {'total_citations': 0, 'chi_papers_count': 0, 'matched_titles_preview': []}, 'var_function-call-1860412936554148787': {'venue_counts': {'CHI': 0, 'Ubicomp': 0, 'CSCW': 0, 'Other': 4}, 'chi_citations': 0}, 'var_function-call-36950570922871518': {'num_citations': 188, 'num_docs': 5, 'intersection_count': 4, 'sample_cit_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"], 'sample_doc_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_function-call-15227609533641263682': 'file_storage/function-call-15227609533641263682.json'}

exec(code, env_args)
