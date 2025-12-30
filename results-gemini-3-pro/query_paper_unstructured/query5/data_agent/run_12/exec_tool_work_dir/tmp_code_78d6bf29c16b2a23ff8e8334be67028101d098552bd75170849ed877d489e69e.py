code = """import json
import re

papers_file = locals()['var_function-call-6614480246128303859']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Papers
p_ubicomp = next((p for p in papers_data if "Lived Informatics Model" in p['filename']), None)
p_chi1 = next((p for p in papers_data if "Stage-based Model" in p['filename']), None)
p_chi2 = next((p for p in papers_data if "Sundroid" in p['filename']), None)

res = {}

def check_paper(p, label):
    if not p:
        return {label: "Not Found"}
    text = p['text']
    head = text[:500]
    tail = text[-500:]
    return {
        label: {
            "head_CHI": "CHI" in head,
            "tail_CHI": "CHI" in tail,
            "head_Ubicomp": "Ubicomp" in head or "UBICOMP" in head,
            "tail_Ubicomp": "Ubicomp" in tail or "UBICOMP" in tail,
            "head_snippet": head[:100].replace(chr(10), ' '),
            "tail_snippet": tail.replace(chr(10), ' ')
        }
    }

res.update(check_paper(p_ubicomp, "Ubicomp_Paper"))
res.update(check_paper(p_chi1, "CHI_Paper_1"))
res.update(check_paper(p_chi2, "CHI_Paper_2"))

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-10006919701169471588': 'file_storage/function-call-10006919701169471588.json', 'var_function-call-10006919701169474509': 'file_storage/function-call-10006919701169474509.json', 'var_function-call-6614480246128303859': 'file_storage/function-call-6614480246128303859.json', 'var_function-call-327744894284243669': {'total_citations': 0, 'chi_paper_count': 0, 'matched_citation_records': 0}, 'var_function-call-1851706690900800953': {'paper_headers': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'citation_titles': ['Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application"]}, 'var_function-call-6042658328295858495': {'first_1000': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b'}, 'var_function-call-13281423024631751496': [], 'var_function-call-11749639393055592578': {'p1_last': 'D.R. \nof \nhealth  management \nInvestigating \nindividuals with diabetes. CHI’06, 2006, pp. 927-936. \n18. Mankoff, J., Kravets, R., and Blevis, E. Some Computer \nin  Creating  a  Sustainable  World. \n\nScience  Issues \nComputer, 41(8), 2008, pp. 102-105. \n\npractices \n\n19. Pousman,  Z.,  Stasko,  J.T.,  and  Mateas,  M.  Casual \nInformation  Visualization:  Depictions  of  Data \nin \nEveryday Life. IEEE Transactions on Visualization and \nComputer Graphics, 2002, pp. 1145-1152. \n\n20. Scollon,  C.,  Kim-Prieto,  C.,  and  Diener,  E.  Experience \nSampling:  Promises  and  Pitfalls,  Strengths  and \nWeaknesses. Journal of Happiness Studies, 4, 2003, pp. \n5-34. \n\n21. Wolf,  G.  Know  Thyself:  Tracking  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}, 'var_function-call-16315113409078468787': {'p1_counts': {'CHI': 0, 'Ubicomp': 4, 'CSCW': 0, 'header': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'footer': 'ng  Every  Facet  of  Life, \nfrom  Sleep  to  Mood  to  Pain,  24/7/365.  Wired,  17.07, \n2009, pp. 92-95. \n\n22. Yau,  N. and Schneider,  J.  Self-Surveillance.  Bulletin of \n\nASIS&T, June/July 2009, pp. 24-30. \n\nCHI 2010: Performance, Stagecraft, and MagicApril 10–15, 2010, Atlanta, GA, USA566 \n \n\x0c'}}, 'var_function-call-8483906321779667365': {'filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'p1_chi_count': 14}}

exec(code, env_args)
