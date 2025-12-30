code = """import json
import re

path_papers = globals()['var_function-call-8213230676134798959']
with open(path_papers, 'r') as f:
    papers = json.load(f)

path_citations = globals()['var_function-call-13928865052096685953']
with open(path_citations, 'r') as f:
    citations = json.load(f)

cit_map = {}
for c in citations:
    t = c['title']
    if t not in cit_map:
        cit_map[t] = 0
    cit_map[t] += int(c['citation_count'])

results = []

for p in papers:
    text = p['text']
    title = p['filename'].replace('.txt', '')
    
    year = None
    # 1. Header
    m = re.search(r'\b(20[0-2][0-9])\b', text[:500])
    if m:
        year = int(m.group(1))
    else:
        # 2. Copyright
        m = re.search(r'Copyright\s+(?:©\s*)?(20[0-2][0-9])', text, re.IGNORECASE)
        if m:
            year = int(m.group(1))
        else:
            # 3. Footer Venue
            # Avoid non-ascii in code
            m = re.search(r'(?:CHI|UbiComp|CSCW|DIS|IUI|OzCHI|TEI|AH|PervasiveHealth|WWW)\s*[\']?\s*(?:20)?([0-2][0-9])', text[-1000:], re.IGNORECASE)
            if m:
                y_str = m.group(1)
                if len(y_str) == 2:
                    year = 2000 + int(y_str)
                else:
                    year = int(y_str)

    # Contribution
    parts = re.split(r'\nREFERENCES\n|\nReferences\n', text)
    body = parts[0]
    
    # Check for empirical
    # Also check if it's "Methodological" or "Theoretical" or "Artifact"
    # But question asks for "empirical contribution".
    # Assuming keyword "empirical" in body is sufficient.
    has_empirical = 'empirical' in body.lower()
    
    if year and year > 2016 and has_empirical:
        count = cit_map.get(title, 0)
        results.append({"title": title, "citation_count": count})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_function-call-2278250218217025444': ['paper_docs'], 'var_function-call-2278250218217023235': ['Citations', 'sqlite_sequence'], 'var_function-call-2998795241881557550': 'file_storage/function-call-2998795241881557550.json', 'var_function-call-1711006908380685270': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'end': '\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'has_empirical': False, 'lines_contrib': ['contributions  through  survey  design  and  participant  interviews.']}, 'var_function-call-137540704590043028': 'file_storage/function-call-137540704590043028.json', 'var_function-call-13928865052096685953': 'file_storage/function-call-13928865052096685953.json', 'var_function-call-17219668882805826907': 'file_storage/function-call-17219668882805826907.json', 'var_function-call-16099994179568050611': [], 'var_function-call-13201249820402721104': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year': 2015, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'year': None, 'has_empirical': False}], 'var_function-call-4194948760569301762': 'Done', 'var_function-call-5958747187753379489': {'p2': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'p4': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  conditi'}, 'var_function-call-14960923734253058658': {'all_years': ['2019', '2019', '2019', '2019', '2019', '2019', '2019', '2018', '2019', '2019'], 'copy_years': [], 'acm_years': [], 'last_500': 'f My Soul – How People Bond with Their \nMobile Phones. In Proc. ACM MobileHCI’08. \n\n[61]   Lois M. Verbrugg 1980. Health diaries. Medical care 18.1: 73-95. \n[62]  Graham  Wilson  and  Stephen  A.  Brewster.  2017.  Multi-Moji: \nCombining  Thermal,  Vibrotactile  &  Visual  Stimuli  to  Expand  the \nAffective Range of Feedback. In Proc. CHI’17. \n\n[63]   2048, https://en.wikipedia.org/wiki/2048_(video_game) \n\nCHI 2019 Paper  CHI 2019, May 4–9, 2019, Glasgow, Scotland, UKPaper 703Page 14 \n \n \n \n \n\x0c'}, 'var_function-call-9100174544124919344': '  T.  Kortum  and  James  T.  Miller.  2008.  An \nEmpirical  Evaluation  of  the  System  Usability ', 'var_function-call-1425076029937721943': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'citation_count': 266}], 'var_function-call-9470605801246580505': {'count_recent': 1, 'count_empirical': 2, 'count_both': 1, 'recent_titles': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App (2019)'], 'empirical_titles_sample': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-12187478931742809056': 'Done', 'var_function-call-14048434587788115304': {'error': 'Paper not found'}, 'var_function-call-7190125306206797753': [], 'var_function-call-5604621208438096538': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-2661815892818634406': 'file_storage/function-call-2661815892818634406.json', 'var_function-call-10381406401695488055': 5, 'var_function-call-8213230676134798959': 'file_storage/function-call-8213230676134798959.json'}

exec(code, env_args)
