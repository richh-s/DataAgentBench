code = """import json
import re

file_path_papers = locals()['var_function-call-13988065293045164664']
with open(file_path_papers, 'r') as f:
    papers = json.load(f)

file_path_citations = locals()['var_function-call-13250865307003414177']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

citations_map = {}
for row in citations_data:
    title = row['title']
    citations_map[title] = citations_map.get(title, 0) + int(row['citation_count'])

results = []

for p in papers:
    text = p['text']
    title_doc = p['filename'].replace('.txt', '')
    
    # Year Extraction: find years in first 1000 chars
    # Headers usually contain the year.
    candidates = re.findall(r'20[12]\d', text[:1000])
    published_year = 0
    if candidates:
        # Taking the first one is a good heuristic for headers
        # e.g. "CHI 2017"
        published_year = int(candidates[0])
    
    # Check for empirical
    is_empirical = "empirical" in text.lower()
    
    if published_year > 2016 and is_empirical:
        # Try to match title
        if title_doc in citations_map:
            results.append({
                "title": title_doc,
                "total_citation_count": citations_map[title_doc]
            })

results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7935345724835477289': ['paper_docs'], 'var_function-call-7935345724835476096': ['Citations', 'sqlite_sequence'], 'var_function-call-16552409283485233225': 'file_storage/function-call-16552409283485233225.json', 'var_function-call-935925181228650257': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'contribution_occurrences': 1}, 'var_function-call-13988065293045164664': 'file_storage/function-call-13988065293045164664.json', 'var_function-call-13250865307003414177': 'file_storage/function-call-13250865307003414177.json', 'var_function-call-4057180574021518467': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False}], 'var_function-call-6894808242716340866': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}], 'var_function-call-17632168996933328964': {'first_200': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'first_200_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Hu"', 'index_2015': 29, 'index_empirical': -1}, 'var_function-call-7568948339170241372': [], 'var_function-call-258404618994076077': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'has_empirical': False, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'has_empirical': False, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'has_empirical': True, 'header_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'has_empirical': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'has_empirical': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}]}

exec(code, env_args)
