code = """import json
import re

with open(locals()['var_function-call-1645148403302341982'], 'r') as f:
    papers = json.load(f)
with open(locals()['var_function-call-2108608692273987200'], 'r') as f:
    citations = json.load(f)

citation_titles = set(c['title'] for c in citations)
print(f"Total citations records: {len(citations)}")
print(f"Unique citation titles: {len(citation_titles)}")
print(f"Total papers: {len(papers)}")

debug_info = []

empirical_count = 0
post_2016_count = 0

for i, p in enumerate(papers):
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # Year
    match = re.search(r'20\d{2}', text[:1000])
    year = int(match.group(0)) if match else 0
    
    # Empirical
    has_empirical = "empirical" in text.lower()
    
    if has_empirical:
        empirical_count += 1
    if year > 2016:
        post_2016_count += 1
        
    in_citations = title in citation_titles
    
    if i < 5:
        debug_info.append({
            "title": title,
            "year": year,
            "has_empirical": has_empirical,
            "in_citations": in_citations
        })

print(f"Papers with 'empirical': {empirical_count}")
print(f"Papers > 2016: {post_2016_count}")
print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json', 'var_function-call-1673231077875897011': {'count': 5, 'first_paper_len': 68339, 'last_1000': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'contribution_match': 'Not found', 'year_match': 'Not found'}, 'var_function-call-1645148403302341982': 'file_storage/function-call-1645148403302341982.json', 'var_function-call-16548406697322182489': []}

exec(code, env_args)
