code = """import json

# Load citations
with open(locals()['var_function-call-14258248544266261240'], 'r') as f:
    citations_data = json.load(f)

# Load paper documents
with open(locals()['var_function-call-18048887829581669547'], 'r') as f:
    papers_data = json.load(f)

c_titles = [x['title'] for x in citations_data]
p_filenames = [x.get('filename', '') for x in papers_data]

print("DEBUG: Citations count:", len(c_titles))
print("DEBUG: Papers count:", len(p_filenames))
print("DEBUG: First 5 Citations Titles:", c_titles[:5])
print("DEBUG: First 5 Papers Filenames:", p_filenames[:5])

# Normalization check
c_titles_norm = set(t.strip().lower() for t in c_titles)
matches = 0
for p in p_filenames:
    if p.endswith('.txt'):
        t = p[:-4].strip().lower()
        if t in c_titles_norm:
            matches += 1

print("DEBUG: Normalized matches:", matches)

print("__RESULT__:")
print(json.dumps({"citations_count": len(c_titles), "papers_count": len(p_filenames), "matches": matches}))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json', 'var_function-call-15377559382259389158': 0, 'var_function-call-8390217922804451433': 'Done', 'var_function-call-4517849310577425133': {'matched_count': 4, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sea"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBe'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana'}]}}

exec(code, env_args)
