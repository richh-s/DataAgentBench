code = """import json

# Load paper_docs
with open(locals()['var_function-call-11279368106067526868'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-3552239526712038918'], 'r') as f:
    citations = json.load(f)

matching_titles = []
debug_matches = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    header = text[:1000]
    content_search = text[:5000].lower()
    
    # Check Year 2016
    if "2016" in header:
        # Check Domain
        if "physical activity" in content_search:
            matching_titles.append(title)
            debug_matches.append({"title": title, "header": header[:100]})

# Filter citations
results = {}
for citation in citations:
    c_title = citation.get('title')
    try:
        c_count = int(citation.get('citation_count', 0))
    except:
        c_count = 0
    
    if c_title in matching_titles:
        if c_title not in results:
            results[c_title] = 0
        results[c_title] += c_count

print("Matching papers:", json.dumps(debug_matches))
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5218844926592326471': ['paper_docs'], 'var_function-call-5218844926592327304': ['Citations', 'sqlite_sequence'], 'var_function-call-3045611188522186041': 'file_storage/function-call-3045611188522186041.json', 'var_function-call-13906461946553771185': 'file_storage/function-call-13906461946553771185.json', 'var_function-call-3552239526712038918': 'file_storage/function-call-3552239526712038918.json', 'var_function-call-12956520315501172365': {}, 'var_function-call-11308566918737790029': 'debug_done', 'var_function-call-4610303297687271524': {'total_docs': 5, 'count_2016': 0, 'count_phys': 2, 'intersection': [], 'sample_header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_function-call-2105951630806919793': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-11279368106067526868': 'file_storage/function-call-11279368106067526868.json'}

exec(code, env_args)
