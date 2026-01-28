code = """import json
import os
import re

# Read the full paper documents from the file path
file_path = locals()['var_functions.query_db:10']
print("Reading from file:", file_path)

with open(file_path, 'r') as f:
    papers = json.load(f)

print("Total papers loaded:", len(papers))

# Extract paper information
paper_info = []
for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    
    # Try to find a 4-digit year first (1900-2099)
    year_match = re.search(r'(?:20|19)\d{2}', text)
    if year_match:
        year = int(year_match.group())
        # Validate year is reasonable
        if year < 2000 or year > 2025:
            year = None
    
    # If no 4-digit year, try to find venue year pattern like "'15" or "'16"
    if not year:
        venue_year_match = re.search(r"[A-Z]+\s+'(\d{2})", text)
        if venue_year_match:
            year_str = venue_year_match.group(1)
            year_val = int(year_str)
            # Convert to 4-digit year assuming 2000s for 00-25, 1900s for 26-99
            if year_val <= 25:
                year = 2000 + year_val
            else:
                year = 1900 + year_val
    
    # Check the publication info line format like "UbiComp '15, September 7-11, 2015"
    if not year or (year < 2000 or year > 2025):
        pub_match = re.search(r"'\d{2}.+?(\d{4})", text)
        if pub_match:
            year = int(pub_match.group(1))
    
    # Validate year
    if not year or (year < 2000 or year > 2025):
        year = None
    
    # Determine contribution type
    contribution = []
    text_lower = text.lower()
    
    # Count occurrences of contribution keywords
    if 'empirical' in text_lower or 'empirically' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or ('theory' in text_lower and 'theoretical' not in text_lower):
        contribution.append('theoretical')
    if 'survey' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or ('method' in text_lower and 'methodological' not in text_lower):
        contribution.append('methodological')
    
    # Deduplicate
    contribution = list(set(contribution))
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'has_empirical': 'empirical' in contribution
    })

# Filter papers published after 2016 with empirical contribution
filtered_papers = []
for p in paper_info:
    if p['year'] and p['year'] > 2016 and p['has_empirical']:
        filtered_papers.append(p)

print("Total papers analyzed:", len(paper_info))
print("Papers after 2016 with empirical contribution:", len(filtered_papers))

# Show some examples
print("First 10 papers with empirical contribution after 2016:")
for p in filtered_papers[:10]:
    contrib_str = ', '.join(p['contribution'])
    print("  -", p['title'], "(", p['year'], ") -", contrib_str)

# Save the filtered paper titles for joining with citations
filtered_titles = [p['title'] for p in filtered_papers]

print('__RESULT__:')
print(json.dumps({
    'filtered_titles': filtered_titles,
    'count': len(filtered_papers)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a86f', 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a872', 'filename': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a874', 'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a876', 'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt'}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a879', 'filename': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt'}, {'_id': '694f5530284b10b11dc0a87a', 'filename': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87c', 'filename': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
