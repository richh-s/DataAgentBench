code = """import json
import re

papers_file = locals()['var_function-call-6614480246128303859']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

chi_filenames = []

for p in papers_data:
    text = p['text']
    fname = p['filename']
    
    # Header and Footer
    header = text[:1000]
    footer = text[-1000:]
    combined = header + " " + footer
    
    # Check for CHI
    # \bCHI\b matches CHI surrounded by non-word chars.
    has_chi = bool(re.search(r"\bCHI\b", combined))
    
    # Check for Ubicomp
    has_ubicomp = bool(re.search(r"\bUbicomp\b", combined, re.IGNORECASE))
    
    # Check for CSCW
    has_cscw = bool(re.search(r"\bCSCW\b", combined))
    
    if has_chi:
        if has_ubicomp or has_cscw:
            # Ambiguous? 
            # Usually header wins.
            if re.search(r"\bCHI\b", header):
                chi_filenames.append(fname)
            elif re.search(r"\bUbicomp\b", header, re.IGNORECASE):
                pass # It's Ubicomp
            elif re.search(r"\bCSCW\b", header):
                pass
            else:
                # If CHI is in footer but not header
                # Check if footer looks like venue line.
                # Look for CHI followed by year
                if re.search(r"CHI\s*.?\s*\d{2}", footer):
                    chi_filenames.append(fname)
                # Also if "CHI" appears multiple times?
        else:
            chi_filenames.append(fname)

# Filter citations
citations_file = locals()['var_function-call-10006919701169471588']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

chi_titles = set(f.replace('.txt', '') for f in chi_filenames)

total_citations = 0
for c in citations_data:
    # SQL already filtered for 2020
    if c['title'] in chi_titles:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_filenames)}))"""

env_args = {'var_function-call-10006919701169471588': 'file_storage/function-call-10006919701169471588.json', 'var_function-call-10006919701169474509': 'file_storage/function-call-10006919701169474509.json', 'var_function-call-6614480246128303859': 'file_storage/function-call-6614480246128303859.json', 'var_function-call-327744894284243669': {'total_citations': 0, 'chi_paper_count': 0, 'matched_citation_records': 0}, 'var_function-call-1851706690900800953': {'paper_headers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-6042658328295858495': {'first_1000': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b'}, 'var_function-call-13281423024631751496': [], 'var_function-call-11749639393055592578': {'p1_last': 'D.R. \nof \nhealth  management \nInvestigating \nindividuals with diabetes. CHI’06, 2006, pp. 927-936. \n18. Mankoff, J., Kravets, R., and Blevis, E. Some Computer \nin  Creating  a  Sustainable  World. \n\nScience  Issues \nComputer, 41(8), 2008, pp. 102-105. \n\npractices \n\n19. Pousman,  Z.,  Stasko,  J.T.,  and  Mateas,  M.  Casual \nInformation  Visualization:  Depictions  of  Data \nin \nEveryday Life. IEEE Transactions on Visualization and \nComputer Graphics, 2002, pp. 1145-1152. \n\n20. Scollon,  C.,  Kim-Prieto,  C.,  and  Diener,  E.  Experience \nSampling:  Promises  and  Pitfalls,  Strengths  and \nWeaknesses. Journal of Happiness Studies, 4, 2003, pp. \n5-34. \n\n21. Wolf,  G.  Know  Thyself:  Tracking  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}, 'var_function-call-16315113409078468787': {'p1_counts': {'CHI': 0, 'Ubicomp': 4, 'CSCW': 0, 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'footer': 'ng  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}}, 'var_function-call-8483906321779667365': {'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'p1_chi_count': 14}, 'var_function-call-6030020370752155172': {'Ubicomp_Paper': {'head_CHI': False, 'tail_CHI': False, 'head_Ubicomp': True, 'tail_Ubicomp': False, 'head_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'tail_snippet': ' Inferring Meal Eating Activities in Real World Settings  from Ambient Sounds: A Feasibility Study. IUI 2015,  427-431.   40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M.   Encouraging Physical Activity in Teens: Can  Technology Help Reduce Barriers to Physical Activity  in Adolescent Girls? PervasiveHealth 2008, 218-221.  41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On   the Integration of Self-tracking Data amongst  Quantified Self Members. HCI 2014, 151-160.    742        \x0c'}, 'CHI_Paper_1': {'head_CHI': False, 'tail_CHI': True, 'head_Ubicomp': False, 'tail_Ubicomp': False, 'head_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'tail_snippet': 'm-Prieto,  C.,  and  Diener,  E.  Experience  Sampling:  Promises  and  Pitfalls,  Strengths  and  Weaknesses. Journal of Happiness Studies, 4, 2003, pp.  5-34.   21. Wolf,  G.  Know  Thyself:  Tracking  Every  Facet  of  Life,  from  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07,  2009, pp. 92-95.   22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of   ASIS&T, June/July 2009, pp. 24-30.   CHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566    \x0c'}, 'CHI_Paper_2': 'Not Found'}, 'var_function-call-12019709028775006204': []}

exec(code, env_args)
