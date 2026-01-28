code = """import json
import re

# Load data
with open(locals()['var_function-call-1645148403302341982'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-2108608692273987200'], 'r') as f:
    citations = json.load(f)

# Build citation map
citation_map = {}
for c in citations:
    t = c['title']
    count = int(c['citation_count'])
    citation_map[t] = citation_map.get(t, 0) + count

# Process papers
results = []
debug_log = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    # Extract Year
    # Look for 4 digits in first 1000 chars
    # Prefer values between 2000 and 2025
    year_candidates = re.findall(r'\b(20\d{2})\b', text[:1000])
    year = None
    if year_candidates:
        # Take the first one? Or the one that appears most?
        # Usually the first one is the conference year.
        year = int(year_candidates[0])
    
    # Extract Contribution
    # Check for "empirical" in text (case insensitive)
    # Also check for "Contribution" keyword to be sure
    is_empirical = False
    
    # Heuristic 1: Look for "Contribution: ... empirical"
    # Heuristic 2: Look for "Contribution" line and see if it contains empirical
    # Heuristic 3: Just check if "empirical" appears in the text?
    
    # Let's try to find lines with "Contribution"
    contribution_lines = []
    lines = text.split('\n')
    for line in lines:
        if "contribution" in line.lower() and len(line) < 300:
            contribution_lines.append(line.strip())
            if "empirical" in line.lower():
                is_empirical = True
    
    # If no explicit "Contribution: Empirical" line, check the whole text for "empirical"
    # But be careful.
    if not is_empirical:
        if "empirical" in text.lower():
            # Check context?
            # For now, let's assume if it mentions "empirical" it might be relevant.
            # But the prompt implies classification.
            # Let's count "empirical" occurrences.
            count_emp = text.lower().count("empirical")
            if count_emp > 0:
                # Is it describing the paper? "We present an empirical study..."
                if "empirical study" in text.lower() or "empirical analysis" in text.lower() or "empirical investigation" in text.lower():
                    is_empirical = True
                elif "contribution" in text.lower() and "empirical" in text.lower():
                     # Maybe "The contribution is empirical..."
                     is_empirical = True # A bit loose
    
    # Store debug info for verification
    if year and year > 2016 and is_empirical:
        total_cites = citation_map.get(title, 0)
        results.append({
            "title": title,
            "citation_count": total_cites,
            "year": year
        })
    elif year and year > 2016:
         # Log why it failed empirical check
         pass

# Sort results by citation count descending
results.sort(key=lambda x: x['citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json', 'var_function-call-1673231077875897011': {'count': 5, 'first_paper_len': 68339, 'last_1000': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'contribution_match': 'Not found', 'year_match': 'Not found'}, 'var_function-call-1645148403302341982': 'file_storage/function-call-1645148403302341982.json'}

exec(code, env_args)
