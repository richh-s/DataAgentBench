code = """import json
import re

# Load papers
file_path_papers = locals()['var_function-call-13988065293045164664']
with open(file_path_papers, 'r') as f:
    papers = json.load(f)

# Analyze first 5 papers
preview = []
for p in papers[:5]:
    text = p['text']
    # Year extraction attempt
    year_match = re.search(r'\b(20\d{2})\b', text[:500])
    year = int(year_match.group(1)) if year_match else None
    
    # Check for "empirical"
    has_empirical = "empirical" in text.lower()
    
    # Check context of "contribution"
    contrib_indices = [m.start() for m in re.finditer(r'contribution', text.lower())]
    contrib_contexts = [text[max(0, i-50):min(len(text), i+100)] for i in contrib_indices]
    
    preview.append({
        "title": p['filename'],
        "extracted_year": year,
        "has_empirical": has_empirical,
        "contrib_contexts": contrib_contexts[:3], # show first 3 contexts
        "first_line": text.split('\n')[0]
    })

print("__RESULT__:")
print(json.dumps(preview))"""

env_args = {'var_function-call-7935345724835477289': ['paper_docs'], 'var_function-call-7935345724835476096': ['Citations', 'sqlite_sequence'], 'var_function-call-16552409283485233225': 'file_storage/function-call-16552409283485233225.json', 'var_function-call-935925181228650257': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'contribution_occurrences': 1}, 'var_function-call-13988065293045164664': 'file_storage/function-call-13988065293045164664.json', 'var_function-call-13250865307003414177': 'file_storage/function-call-13250865307003414177.json'}

exec(code, env_args)
