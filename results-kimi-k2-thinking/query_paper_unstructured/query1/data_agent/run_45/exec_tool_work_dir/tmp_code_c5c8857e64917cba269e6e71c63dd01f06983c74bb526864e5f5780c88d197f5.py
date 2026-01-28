code = """import json
import pandas as pd

# Access stored query results
# var_functions.query_db:2 contains paper docs, var_functions.query_db:5 contains citations

# Read the paper documents data
paper_docs_path = str(var_functions.query_db:2)
citations_path = str(var_functions.query_db:5)

print(f"Reading paper docs from: {paper_docs_path}")
print(f"Reading citations from: {citations_path}")

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(paper_docs)} paper docs, {len(citations)} citations")

# Extract titles and domains from paper docs
paper_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if paper is in food domain (case insensitive)
    is_food = 'food' in text.lower()
    paper_info.append({'title': title, 'is_food_domain': is_food})

paper_df = pd.DataFrame(paper_info)

# Process citations
citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Merge data on title
food_papers = paper_df[paper_df['is_food_domain'] == True]
food_titles = set(food_papers['title'].tolist())

# Filter citations for food papers
food_citations = citations_df[citations_df['title'].isin(food_titles)]

# Calculate total citations for food domain
total_citations = food_citations['citation_count'].sum()
num_unique_food_papers = food_citations['title'].nunique()

result = {
    'total_citations_for_food_papers': int(total_citations),
    'number_of_unique_food_papers': int(num_unique_food_papers),
    'total_food_papers_in_docs': len(food_papers)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'id': '182', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '71', 'citation_year': '2016'}, {'id': '183', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '22', 'citation_year': '2017'}, {'id': '184', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '34', 'citation_year': '2018'}, {'id': '185', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '68', 'citation_year': '2019'}, {'id': '186', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '78', 'citation_year': '2020'}, {'id': '187', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '55', 'citation_year': '2021'}, {'id': '188', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '28', 'citation_year': '2022'}, {'id': '189', 'title': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'citation_count': '70', 'citation_year': '2023'}, {'id': '190', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '92', 'citation_year': '2016'}, {'id': '191', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '40', 'citation_year': '2017'}, {'id': '192', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '52', 'citation_year': '2018'}, {'id': '193', 'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'citation_count': '86', 'citation_year': '2019'}, {'id': '319', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '41', 'citation_year': '2019'}, {'id': '320', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '97', 'citation_year': '2020'}, {'id': '321', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '10', 'citation_year': '2021'}, {'id': '322', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '2', 'citation_year': '2022'}, {'id': '323', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '59', 'citation_year': '2023'}, {'id': '324', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '80', 'citation_year': '2024'}, {'id': '325', 'title': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'citation_count': '73', 'citation_year': '2025'}, {'id': '544', 'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'citation_count': '16', 'citation_year': '2017'}, {'id': '545', 'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'citation_count': '59', 'citation_year': '2018'}, {'id': '546', 'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'citation_count': '18', 'citation_year': '2019'}, {'id': '547', 'title': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'citation_count': '60', 'citation_year': '2020'}, {'id': '746', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '34', 'citation_year': '2016'}, {'id': '747', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '44', 'citation_year': '2017'}, {'id': '748', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '36', 'citation_year': '2018'}, {'id': '749', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '77', 'citation_year': '2019'}, {'id': '750', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '90', 'citation_year': '2020'}, {'id': '751', 'title': 'Why and What Did We Throw out?: Probing on Reflection Through the Food Waste Diary', 'citation_count': '36', 'citation_year': '2021'}, {'id': '871', 'title': 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'citation_count': '23', 'citation_year': '2018'}, {'id': '872', 'title': 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'citation_count': '71', 'citation_year': '2019'}, {'id': '873', 'title': 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'citation_count': '10', 'citation_year': '2020'}, {'id': '874', 'title': 'Supporting Patient-Provider Collaboration to Identify Individual Triggers Using Food and Symptom Journals', 'citation_count': '21', 'citation_year': '2021'}, {'id': '1054', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '76', 'citation_year': '2018'}, {'id': '1055', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '43', 'citation_year': '2019'}, {'id': '1056', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '13', 'citation_year': '2020'}, {'id': '1057', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '57', 'citation_year': '2021'}, {'id': '1058', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '13', 'citation_year': '2022'}, {'id': '1059', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '68', 'citation_year': '2023'}, {'id': '1060', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '59', 'citation_year': '2024'}, {'id': '1061', 'title': 'TummyTrials: A Feasibility Study of Using Self-Experimentation to Detect Individualized Food Triggers', 'citation_count': '2', 'citation_year': '2025'}, {'id': '1073', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '49', 'citation_year': '2020'}, {'id': '1074', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '41', 'citation_year': '2021'}, {'id': '1075', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '81', 'citation_year': '2022'}, {'id': '1076', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '92', 'citation_year': '2023'}, {'id': '1077', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '98', 'citation_year': '2024'}, {'id': '1078', 'title': 'Co-Designing Food Trackers with Dietitians: Identifying Design Opportunities for Food Tracker Customization', 'citation_count': '63', 'citation_year': '2025'}, {'id': '1103', 'title': 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', 'citation_count': '88', 'citation_year': '2020'}, {'id': '1104', 'title': 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', 'citation_count': '24', 'citation_year': '2021'}, {'id': '1105', 'title': 'Identifying and Planning for Individualized Change: Patient-Provider Collaboration Using Lightweight Food Diaries in Healthy Eating and Irritable Bowel Syndrome', 'citation_count': '22', 'citation_year': '2022'}]}

exec(code, env_args)
