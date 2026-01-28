code = """import json
import re

# Read the citation data file
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Read paper documents from previous step
paper_docs_file = locals()['var_functions.query_db:6']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information and identify empirical papers after 2016
empirical_paper_titles = []
papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    if has_empirical and year and year > 2016:
        empirical_paper_titles.append(title)
        papers_info.append({
            'title': title,
            'year': year
        })

# Create a mapping for case-insensitive and partial matching
def normalize_title(t):
    return t.lower().strip()

# Build citation map for faster lookup
citation_map = {}
for citation in citations_data:
    cit_title = citation['title']
    normalized_cit_title = normalize_title(cit_title)
    citation_map[normalized_cit_title] = {
        'original_title': cit_title,
        'total_citations': int(citation['total_citations'])
    }

# Match empirical papers with their citations
results = []
for paper in papers_info:
    paper_title_norm = normalize_title(paper['title'])
    
    # Direct match
    if paper_title_norm in citation_map:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_map[paper_title_norm]['total_citations']
        })
    else:
        # Try partial matching
        for cit_norm, cit_data in citation_map.items():
            if paper_title_norm in cit_norm or cit_norm in paper_title_norm:
                results.append({
                    'title': paper['title'],
                    'year': paper['year'],
                    'total_citations': cit_data['total_citations']
                })
                break

# Sort by citations (descending)
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'empirical_papers_after_2016_found': len(empirical_paper_titles),
    'papers_with_citation_data': len(results),
    'papers': results
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': {'total_papers': 99, 'empirical_papers_count': 21, 'empirical_papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'has_empirical': True, 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'has_empirical': True, 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings', 'year': 2018, 'has_empirical': True, 'text_preview': 'Common Barriers to the Use of Patient-Generated Data\nAcross Clinical Settings\nPeter West1, Max Van Kleek2, Richard Giordano1, Mark J. Weal3, Nigel Shadbolt2\n2Dept. of Computer Science\nUniversity of Oxford, UK\nmax.van.kleek@cs.ox.ac.uk\nnigel.shadbolt@cs.ox.ac.uk\n\n1Faculty of Health Sciences\nUniversity of Southampton, UK\np.west@soton.ac.uk\nr.giordano@soton.ac.uk\n\n3Web and Internet Science\nUniversity of Southampton, UK\nmjw@ecs.soton.ac.uk\n\nABSTRACT\nPatient-generated data, such as data from wearable'}, {'title': 'Communicating Uncertainty in Fertility Prognosis', 'year': 2019, 'has_empirical': True, 'text_preview': 'Communicating Uncertainty in Fertility Prognosis\n\nHanna Schneider\nLMU Munich\nhanna.schneider@ifi.lmu.de\n\nMariam Hassib\nBundeswehr University Munich\nmariam.hassib@unibw.de\n\nJulia Wayrauther\nLMU Munich\njulia.wayrauther@gmail.com\n\nAndreas Butz\nLMU Munich\nandreas.butz@ifi.lmu.de\n\nABSTRACT\nCommunicating uncertainty has been shown to provide pos-\nitive effects on user understanding and decision-making.\nSurprisingly however, most personal health tracking appli-\ncations fail to disclose the accuracy of '}, {'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'year': 2018, 'has_empirical': True, 'text_preview': 'Does Journaling Encourage Healthier Choices?\nAnalyzing Healthy Eating Behaviors of Food Journalers\n\nPalakorn Achananuparp\nSingapore Management University\nSingapore, Singapore\npalakorna@smu.edu.sg\n\nEe-Peng Lim\nSingapore Management University\nSingapore, Singapore\neplim@smu.edu.sg\n\nVibhanshu Abhishek\nCarnegie Mellon University\nPittsburgh, PA\nvibs@andrew.cmu.edu\n\nABSTRACT\nPast research has shown the benefits of food journaling in promot-\ning mindful eating and healthier food choices. However, the li'}, {'title': 'Entangled with Numbers: Quantified Self and Others in a Team-Based Online Game', 'year': 2018, 'has_empirical': True, 'text_preview': 'Entangled with Numbers: Quantified Self  \nand Others in a Team-Based Online Game  \n\nYUBO KOU, Florida State University, USA \nXINNING GUI, University of California, Irvine, USA \n\nQuantification  is  a  process  that  produces  and  communicates  numbers,  imbued  with  the  expectation  of \ngenerating  knowledge  and  optimizing  human  behavior  and  social  process.  In  this  paper,  we  explore  how \nquantification  mediates  virtual  teamwork  through  an  ethnographic  study  of  quantifica'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'year': 2019, 'has_empirical': True, 'text_preview': 'Goal-setting And Achievement In Activity Tracking Apps: A Case\nStudy Of MyFitnessPal\n\nMitchell L. Gordon\nStanford University\nmgord@cs.stanford.edu\n\nTim Althoff\nUniversity of Washington\nalthoff@cs.washington.edu\n\nJure Leskovec\nStanford University\njure@cs.stanford.edu\n\nABSTRACT\nActivity tracking apps often make use of goals as one of their\ncore motivational tools. There are two critical components to this\ntool: setting a goal, and subsequently achieving that goal. Despite\nits crucial role in how a'}, {'title': 'Heed: Exploring the Design of Situated Self-Reporting Devices', 'year': 2018, 'has_empirical': True, 'text_preview': 'XX \n\n132 \n\nHeed: Exploring the Design of Situated Self-Reporting Devices \n\nGAURAV PARUTHI, University of Michigan \nSHRITI RAJ, University of Michigan \nSEUNGJOO BAEK, University of Michigan \nCHUYAO WANG, University of Michigan \nCHUAN-CHE HUANG, University of Michigan \nYUNG-JU CHANG, National Chiao Tung University \nMARK W. NEWMAN, University of Michigan \n\nIn-situ self-reporting is a widely used data collection technique for understanding people’s behavior in context. Characteristics \nof smartphone'}, {'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'year': 2018, 'has_empirical': True, 'text_preview': 'I’ll Be Back: On the Multiple Lives of Users\nof a Mobile Activity Tracking Application\n\nZhiyuan Lin\nStanford University\nzylin@cs.stanford.edu\n\nTim Althoff\nStanford University\nalthoff@cs.stanford.edu\n\nJure Leskovec\nStanford University\njure@cs.stanford.edu\n\nABSTRACT\nMobile health applications that track activities, such as exercise,\nsleep, and diet, are becoming widely used. While these activity\ntracking applications have the potential to improve our health,\nuser engagement and retention are criti'}, {'title': 'Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'year': 2017, 'has_empirical': True, 'text_preview': 'Making \xa0Sense \xa0of \xa0Sleep \xa0Sensors: \xa0How \xa0Sleep \xa0Sensing \xa0\nTechnologies \xa0Support \xa0and \xa0Undermine \xa0Sleep \xa0Health \xa0\nRuth Ravichandran1, Sang-Wha Sien3, Shwetak N. Patel1,2, Julie A. Kientz3, & Laura R. Pina2,3 \n1Electrical Engineering, 2Computer Science & Engineering, 3Human Centered Design & Engineering \nUniversity of Washington, Seattle, WA USA \n{vinisha, elgreco, jkientz}@uw.edu, {shwetak, lpina}@cs.washington.edu \n\nABSTRACT \xa0\nSleep is an important aspect of our health, but it is difficult \nfor '}]}, 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
