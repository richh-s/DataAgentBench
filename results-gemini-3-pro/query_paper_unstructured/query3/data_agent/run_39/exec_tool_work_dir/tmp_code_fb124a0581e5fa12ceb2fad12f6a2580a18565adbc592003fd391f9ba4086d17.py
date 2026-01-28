code = """import json
import re

file_path_papers = locals()['var_function-call-13988065293045164664']
with open(file_path_papers, 'r') as f:
    papers = json.load(f)

debug_list = []
for p in papers[:20]:
    text = p['text']
    filename = p['filename']
    years = re.findall(r'\b(20[12]\d)\b', text[:1000])
    extracted_year = int(years[0]) if years else None
    has_empirical = "empirical" in text.lower()
    
    debug_list.append({
        "title": filename,
        "extracted_year": extracted_year,
        "has_empirical": has_empirical,
        "header_snippet": text[:100]
    })

print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-7935345724835477289': ['paper_docs'], 'var_function-call-7935345724835476096': ['Citations', 'sqlite_sequence'], 'var_function-call-16552409283485233225': 'file_storage/function-call-16552409283485233225.json', 'var_function-call-935925181228650257': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'contribution_occurrences': 1}, 'var_function-call-13988065293045164664': 'file_storage/function-call-13988065293045164664.json', 'var_function-call-13250865307003414177': 'file_storage/function-call-13250865307003414177.json', 'var_function-call-4057180574021518467': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'extracted_year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'extracted_year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'extracted_year': None, 'is_empirical': False}], 'var_function-call-6894808242716340866': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'contrib_text': 'NOT FOUND', 'year': 'NOT FOUND'}], 'var_function-call-17632168996933328964': {'first_200': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'first_200_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Hu"', 'index_2015': 29, 'index_empirical': -1}, 'var_function-call-7568948339170241372': []}

exec(code, env_args)
