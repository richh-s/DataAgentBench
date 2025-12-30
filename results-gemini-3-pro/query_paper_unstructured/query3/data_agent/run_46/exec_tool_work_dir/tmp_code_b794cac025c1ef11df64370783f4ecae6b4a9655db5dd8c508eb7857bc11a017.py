code = """import json

path_papers = globals()['var_function-call-8213230676134798959']
with open(path_papers, 'r') as f:
    papers = json.load(f)
path_citations = globals()['var_function-call-13928865052096685953']
with open(path_citations, 'r') as f:
    citations = json.load(f)

cit_map = {}
min_year_map = {}

for c in citations:
    t = c['title']
    y = int(c['citation_year'])
    count = int(c['citation_count'])
    
    cit_map[t] = cit_map.get(t, 0) + count
    
    if t not in min_year_map:
        min_year_map[t] = y
    else:
        if y < min_year_map[t]:
            min_year_map[t] = y

results = []
venues = ["CHI", "UbiComp", "CSCW", "DIS", "IUI", "OzCHI", "TEI", "AH", "PervasiveHealth", "WWW"]
years = range(2017, 2026)

for p in papers:
    text = p['text']
    title = p['filename'].replace('.txt', '')
    
    # Check citations first
    min_cit = min_year_map.get(title)
    if min_cit is not None and min_cit < 2017:
        continue # Published before 2017 (citations exist earlier)

    # Year Extraction from text
    found_year = 0
    header = text[:1000]
    for y in years:
        if str(y) in header:
            found_year = y
            break
            
    if not found_year:
        footer = text[-2000:]
        for y in years:
            short_y = str(y)[2:]
            for v in venues:
                if f"{v} {y}" in footer or f"{v} '{short_y}" in footer or f"{v} {short_y}" in footer:
                    found_year = y
                    break
            if found_year: break

    if not found_year:
        for y in years:
            if f"Copyright {y}" in text or f"Copyright \u00a9 {y}" in text:
                found_year = y
                break

    # Empirical check
    body = text
    if 'REFERENCES' in text:
        body = text.split('REFERENCES')[0]
    elif 'References' in text:
        body = text.split('References')[0]
    
    # If no year found, but min_cit >= 2017, assume it is valid?
    # Yes, if min citation is 2017, likely published 2017.
    # But usually extract year works.
    # Let's rely on year found OR (min_cit >= 2017 and min_cit <= 2020)
    # Actually, if year not found, but citations start 2017+, it's likely relevant.
    
    is_empirical = 'empirical' in body.lower()
    
    if (found_year >= 2017 or (found_year == 0 and min_cit and min_cit >= 2017)) and is_empirical:
        count = cit_map.get(title, 0)
        results.append({"title": title, "citation_count": count})

results.sort(key=lambda x: x['citation_count'], reverse=True)
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-2278250218217025444': ['paper_docs'], 'var_function-call-2278250218217023235': ['Citations', 'sqlite_sequence'], 'var_function-call-2998795241881557550': 'file_storage/function-call-2998795241881557550.json', 'var_function-call-1711006908380685270': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'has_empirical': False, 'lines_contrib': ['contributions  through  survey  design  and  participant  interviews.']}, 'var_function-call-137540704590043028': 'file_storage/function-call-137540704590043028.json', 'var_function-call-13928865052096685953': 'file_storage/function-call-13928865052096685953.json', 'var_function-call-17219668882805826907': 'file_storage/function-call-17219668882805826907.json', 'var_function-call-16099994179568050611': [], 'var_function-call-13201249820402721104': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'has_empirical': False}], 'var_function-call-4194948760569301762': 'Done', 'var_function-call-5958747187753379489': {'p2': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'p4': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, 'var_function-call-14960923734253058658': {'all_years': ['2019', '2019', '2019', '2019', '2019', '2019', '2019', '2018', '2019', '2019'], 'copy_years': [], 'acm_years': [], 'last_500': 'f My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c'}, 'var_function-call-9100174544124919344': '  T.  Kortum  and  James  T.  Miller.  2008.  An \nEmpirical  Evaluation  of  the  System  Usability ', 'var_function-call-1425076029937721943': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'citation_count': 266}], 'var_function-call-9470605801246580505': {'count_recent': 1, 'count_empirical': 2, 'count_both': 1, 'recent_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App (2019)'], 'empirical_titles_sample': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-12187478931742809056': 'Done', 'var_function-call-14048434587788115304': {'error': 'Paper not found'}, 'var_function-call-7190125306206797753': [], 'var_function-call-5604621208438096538': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-2661815892818634406': 'file_storage/function-call-2661815892818634406.json', 'var_function-call-10381406401695488055': 5, 'var_function-call-8213230676134798959': 'file_storage/function-call-8213230676134798959.json', 'var_function-call-6515939717666535492': [{'title': "We'Ve Bin Watching You: Designing for Reflection and Social Persuasion to Promote Sustainable Lifestyles", 'citation_count': 489}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'citation_count': 467}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': 442}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'citation_count': 402}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': 316}, {'title': 'Understanding Personal Productivity: How Knowledge Workers Define, Evaluate, and Reflect on Their Productivity', 'citation_count': 306}, {'title': 'Modeling Interdependent and Periodic Real-World Action Sequences', 'citation_count': 296}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': 270}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'citation_count': 268}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'citation_count': 265}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'citation_count': 264}, {'title': 'Turn to the Self in Human-Computer Interaction: Care of the Self in Negotiating the Human-Technology Relationship', 'citation_count': 235}, {'title': "Supporting Coping with Parkinson's Disease Through Self Tracking", 'citation_count': 191}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'citation_count': 190}, {'title': 'From Nobody Cares to Way to Go!: A Design Framework for Social Sharing in Personal Informatics', 'citation_count': 160}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'citation_count': 139}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'citation_count': 98}, {'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'citation_count': 72}]}

exec(code, env_args)
