code = """import json
import re

papers_file = locals()['var_function-call-6614480246128303859']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Total papers: {len(papers_data)}")

venues = ["CHI", "Ubicomp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
venue_counts = {v: 0 for v in venues}
detected_chi = []

for p in papers_data:
    text = p['text']
    filename = p['filename']
    
    # Check Header (first 500) and Footer (last 500)
    # Combined snippet
    snippet = text[:500] + "\n" + text[-500:]
    
    # Simple check for "CHI"
    # Looking for CHI 20xx or CHI 'xx
    # Also "Conference on Human Factors..."
    
    is_chi = False
    
    # Regex: CHI followed by space, optional quote, digit
    if re.search(r"\bCHI\s*['\u2019]?\d{2}", snippet):
        is_chi = True
    elif "Conference on Human Factors in Computing Systems" in snippet:
        is_chi = True
    elif "CHI 20" in snippet: # Fallback
        is_chi = True
        
    # Exclude if Ubicomp is stronger?
    if re.search(r"Ubicomp\s*['\u2019]?\d{2}", snippet, re.IGNORECASE) or "Ubicomp" in text[:100]:
        # If Ubicomp is in the very header, it's Ubicomp.
        # Check if CHI is also there?
        if "Ubicomp" in text[:100]:
            is_chi = False
            
    if is_chi:
        detected_chi.append(filename)
        venue_counts["CHI"] += 1
    else:
        # Check other venues just for debug
        for v in venues:
            if v != "CHI" and (v in text[:100] or re.search(fr"{v}\s*['\u2019]?\d{{2}}", snippet, re.IGNORECASE)):
                venue_counts[v] += 1
                break

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(papers_data),
    "chi_count": venue_counts["CHI"],
    "other_counts": venue_counts,
    "sample_chi": detected_chi[:5]
}))"""

env_args = {'var_function-call-10006919701169471588': 'file_storage/function-call-10006919701169471588.json', 'var_function-call-10006919701169474509': 'file_storage/function-call-10006919701169474509.json', 'var_function-call-6614480246128303859': 'file_storage/function-call-6614480246128303859.json', 'var_function-call-327744894284243669': {'total_citations': 0, 'chi_paper_count': 0, 'matched_citation_records': 0}, 'var_function-call-1851706690900800953': {'paper_headers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-6042658328295858495': {'first_1000': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b'}, 'var_function-call-13281423024631751496': [], 'var_function-call-11749639393055592578': {'p1_last': 'D.R. \nof \nhealth  management \nInvestigating \nindividuals with diabetes. CHI’06, 2006, pp. 927-936. \n18. Mankoff, J., Kravets, R., and Blevis, E. Some Computer \nin  Creating  a  Sustainable  World. \n\nScience  Issues \nComputer, 41(8), 2008, pp. 102-105. \n\npractices \n\n19. Pousman,  Z.,  Stasko,  J.T.,  and  Mateas,  M.  Casual \nInformation  Visualization:  Depictions  of  Data \nin \nEveryday Life. IEEE Transactions on Visualization and \nComputer Graphics, 2002, pp. 1145-1152. \n\n20. Scollon,  C.,  Kim-Prieto,  C.,  and  Diener,  E.  Experience \nSampling:  Promises  and  Pitfalls,  Strengths  and \nWeaknesses. Journal of Happiness Studies, 4, 2003, pp. \n5-34. \n\n21. Wolf,  G.  Know  Thyself:  Tracking  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}, 'var_function-call-16315113409078468787': {'p1_counts': {'CHI': 0, 'Ubicomp': 4, 'CSCW': 0, 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'footer': 'ng  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}}, 'var_function-call-8483906321779667365': {'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'p1_chi_count': 14}, 'var_function-call-6030020370752155172': {'Ubicomp_Paper': {'head_CHI': False, 'tail_CHI': False, 'head_Ubicomp': True, 'tail_Ubicomp': False, 'head_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'tail_snippet': ' Inferring Meal Eating Activities in Real World Settings  from Ambient Sounds: A Feasibility Study. IUI 2015,  427-431.   40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M.   Encouraging Physical Activity in Teens: Can  Technology Help Reduce Barriers to Physical Activity  in Adolescent Girls? PervasiveHealth 2008, 218-221.  41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On   the Integration of Self-tracking Data amongst  Quantified Self Members. HCI 2014, 151-160.    742        \x0c'}, 'CHI_Paper_1': {'head_CHI': False, 'tail_CHI': True, 'head_Ubicomp': False, 'tail_Ubicomp': False, 'head_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'tail_snippet': 'm-Prieto,  C.,  and  Diener,  E.  Experience  Sampling:  Promises  and  Pitfalls,  Strengths  and  Weaknesses. Journal of Happiness Studies, 4, 2003, pp.  5-34.   21. Wolf,  G.  Know  Thyself:  Tracking  Every  Facet  of  Life,  from  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07,  2009, pp. 92-95.   22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of   ASIS&T, June/July 2009, pp. 24-30.   CHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566    \x0c'}, 'CHI_Paper_2': 'Not Found'}, 'var_function-call-12019709028775006204': []}

exec(code, env_args)
