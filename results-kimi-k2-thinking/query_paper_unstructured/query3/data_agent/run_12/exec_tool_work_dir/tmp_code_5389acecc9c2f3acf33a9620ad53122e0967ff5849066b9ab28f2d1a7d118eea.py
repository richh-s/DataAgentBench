code = """import json
import re

# Read the full MongoDB query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Let's systematically extract years from all papers
all_papers_info = []

for i, paper in enumerate(papers):
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year using multiple approaches
    year = None
    
    # Approach 1: Look for conference notation with year
    # e.g., UBICOMP '15, CHI 2016, CSCW'17
    conf_pattern = r"(UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?(\d{2})\b"
    match = re.search(conf_pattern, text)
    if match:
        year_str = match.group(2)
        year = 2000 + int(year_str)
    
    # Approach 2: Look for full year with conference
    if not year:
        conf_pattern_full = r"(UBICOMP|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[^\d]{0,50}(20\d{2})"
        match = re.search(conf_pattern_full, text)
        if match:
            year = int(match.group(2))
    
    # Approach 3: Look for copyright year
    if not year:
        copyright_pattern = r"Copyright\s+(?:\(c\)\s+)?(?:\d{4}\s+)?(20\d{2})"
        match = re.search(copyright_pattern, text, re.IGNORECASE)
        if match:
            year = int(match.group(1))
    
    # Approach 4: Look for year in first 1000 chars
    if not year:
        intro = text[:1000]
        year_match = re.search(r"\b(20\d{2})\b", intro)
        if year_match:
            year = int(year_match.group(1))
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    all_papers_info.append({
        'index': i,
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Debug: Show distribution of years
years_found = [p['year'] for p in all_papers_info if p['year'] is not None]
year_counts = {}
for year in years_found:
    year_counts[year] = year_counts.get(year, 0) + 1

# Find empirical papers post-2016
empirical_post_2016 = [p for p in all_papers_info if p['has_empirical'] and p['year'] and p['year'] > 2016]

result = {
    'total_papers': len(papers),
    'papers_with_years': len(years_found),
    'year_distribution': sorted(year_counts.items()),
    'empirical_papers_found': len([p for p in all_papers_info if p['has_empirical']]),
    'empirical_post_2016': empirical_post_2016
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}, {'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity'}], 'var_functions.execute_python:14': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.execute_python:16': [], 'var_functions.execute_python:18': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:20': [], 'var_functions.execute_python:24': {'total_empirical_papers': 2, 'empirical_papers': [{'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}]}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'all_empirical_with_years': [], 'post_2016_empirical': []}, 'var_functions.execute_python:30': {'year_distribution': [], 'total_papers_with_years': 0, 'post_2016_papers': [], 'post_2016_count': 0}, 'var_functions.execute_python:32': {'first_2000_chars': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their lived informatics experiences. We develop a \nmodel characterizing tracker processes of deciding to track \nand selecting a tool, elaborate on tool usage during collection, \nintegration,  and  reflection  as  components  of  tracking  and \nacting,  and  discuss  the  lapsing  and  potential  resuming  of \ntracking.  We  use  our  model  to  surface  underexplored \nchallenges  in  lived  informatics,  thus  identifying  future \ndirections for personal informatics design and research.  \n\nAuthor Keywords \nLived Informatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  increasingly  prevalent.  Personal \ninformatics can serve a goal-driven purpose, such as tracking \nweight loss, increasing physical activity, having a record of \nplaces  visited,  or  tracking "}}

exec(code, env_args)
