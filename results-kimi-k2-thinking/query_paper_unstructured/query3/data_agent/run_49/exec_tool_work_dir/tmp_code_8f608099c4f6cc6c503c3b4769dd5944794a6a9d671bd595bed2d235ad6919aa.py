code = """import json
import re

# Get the file path
file_path = locals()['var_functions.query_db:10']

# Read all papers
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Process all papers to find empirical papers after 2016
empirical_papers = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Find most recent year in text (look for 20xx pattern)
    year_matches = re.findall(r'20\d{2}', text)
    year = None
    if year_matches:
        # Take the largest year that is > 2016
        valid_years = [int(y) for y in year_matches if int(y) > 2016]
        if valid_years:
            year = max(valid_years)
    
    # Check if empirical in text (case-insensitive)
    has_empirical = 'empirical' in text.lower()
    
    if year and has_empirical:
        empirical_papers.append(title)

# Now get citation data
print("Empirical papers after 2016 found:", len(empirical_papers))

result = {
    'empirical_papers': empirical_papers,
    'count': len(empirical_papers)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1, 'papers': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:16': {'count': 0, 'papers': []}, 'var_functions.execute_python:18': {'count': 0, 'papers': []}, 'var_functions.execute_python:20': {'count': 0, 'papers': []}, 'var_functions.execute_python:22': [{'title': 'A Lived Informatics Model of Personal Informatics', 'years_found': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013', '2013', '2012', '2014', '2006', '2005', '2015', '2015', '2013', '2006', '2010', '2014', '2014', '2006', '2007', '2013', '2014', '2010', '2011', '2006', '2011', '2011', '2012', '2015', '2011', '2014', '2015', '2010', '2005', '2014', '2014', '2014', '2005', '2010', '2015', '2008', '2014'], 'has_empirical': False, 'text_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'years_found': ['2010', '2010', '2010', '2010', '2010', '2005', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2010', '2009', '2009', '2009', '2008', '2009', '2003', '2006', '2010', '2001', '2006', '2008', '2003', '2007', '2009', '2009', '2006', '2006', '2006', '2008', '2002', '2003', '2009', '2009', '2010', '2010'], 'has_empirical': False, 'text_snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'years_found': ['2018', '2018', '2018', '2018', '2018', '2018', '2007', '2008', '2003', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2018', '2006', '2006', '2005', '2006', '2006', '2016', '2016', '2010', '2009', '2009', '2009', '2007', '2007', '2000', '2000', '2018', '2018', '2018', '2011', '2011', '2017', '2017', '2006', '2003', '2003', '2005', '2005', '2000', '2000', '2006', '2009', '2016', '2013', '2005', '2006', '2004', '2004', '2018', '2018', '2018'], 'has_empirical': True, 'text_snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'years_found': ['2019', '2019', '2019', '2019', '2019', '2019', '2019', '2018', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2048', '2019', '2019', '2019', '2048', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2048', '2019', '2019', '2019', '2048', '2048', '2048', '2019', '2019', '2019', '2019', '2019', '2019', '2011', '2014', '2017', '2002', '2011', '2005', '2008', '2057', '2008', '2002', '2011', '2008', '2009', '2019', '2019', '2019', '2014', '2015', '2000', '2014', '2017', '2017', '2013', '2013', '2013', '2016', '2010', '2016', '2006', '2017', '2018', '2017', '2034', '2011', '2016', '2014', '2017', '2004', '2015', '2016', '2015', '2014', '2014', '2014', '2016', '2015', '2014', '2014', '2014', '2011', '2011', '2011', '2019', '2019', '2019', '2018', '2001', '2011', '2018', '2018', '2015', '2007', '2015', '2012', '2018', '2008', '2017', '2048', '2048', '2019', '2019', '2019'], 'has_empirical': True, 'text_snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'years_found': ['2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2016', '2011', '2039', '2039', '2011', '2011', '2011', '2011', '2014', '2011', '2013', '2006', '2014', '2014', '2013', '2011', '2004', '2015', '2013', '2011', '2010', '2010', '2014', '2011', '2064', '2064', '2064', '2016', '2016', '2010', '2013', '2015', '2015', '2015', '2015', '2015', '2014', '2014', '2014', '2014', '2015', '2014', '2014', '2015', '2005', '2014', '2014', '2008', '2008', '2016', '2016'], 'has_empirical': False, 'text_snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}]}

exec(code, env_args)
