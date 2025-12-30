code = """import json

# Load citations
with open(locals()['var_function-call-14258248544266261240'], 'r') as f:
    citations_data = json.load(f)

# Load paper filenames
with open(locals()['var_function-call-3130238576704173766'], 'r') as f:
    papers_list = json.load(f)

citation_titles = set(entry['title'] for entry in citations_data)
# citation map for later
citation_map = {entry['title']: entry['citation_count'] for entry in citations_data}

matched_filenames = []
for p in papers_list:
    filename = p.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check match (case insensitive or exact?)
    # Citations titles seem to be cleaner. Filenames might have issues?
    # Let's try exact match first.
    if title in citation_titles:
        matched_filenames.append(filename)

print("DEBUG: Matched filenames count:", len(matched_filenames))

# Prepare the list for next step
print("__RESULT__:")
print(json.dumps(matched_filenames))"""

env_args = {'var_function-call-14258248544266261240': 'file_storage/function-call-14258248544266261240.json', 'var_function-call-14258248544266263107': 'file_storage/function-call-14258248544266263107.json', 'var_function-call-18048887829581669547': 'file_storage/function-call-18048887829581669547.json', 'var_function-call-15377559382259389158': 0, 'var_function-call-8390217922804451433': 'Done', 'var_function-call-4517849310577425133': {'matched_count': 4, 'samples': [{'title': 'A Lived Informatics Model of Personal Informatics', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sea"}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBe'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana'}]}, 'var_function-call-6446625202661210868': {'citations_count': 188, 'papers_count': 5, 'matches': 4}, 'var_function-call-3130238576704173766': 'file_storage/function-call-3130238576704173766.json'}

exec(code, env_args)
