code = """import json
import os

# List available files in tmp directory
tmp_files = []
if os.path.exists('/tmp'):
    tmp_files = os.listdir('/tmp')
    print("Files in /tmp:", tmp_files)

# Read from the correct file path - should be based on the storage key
# Based on the previous result, the file should be available
# Let's try a different approach - the data should be available through the storage variable

# Let's first check what's available in variables
available_vars = list(locals().keys())
print("Available variables:", available_vars)

# Check for the result variable from query_db
result_var = None
for var_name in available_vars:
    if 'var_functions.query_db:4' in var_name:
        result_var = var_name
        break

print("Result variable:", result_var)

# Now let's try to access it properly
if result_var:
    papers = locals()[result_var]
    print(f"Number of papers loaded: {len(papers)}")
    
    # Extract paper information
    paper_info = []
    for paper in papers:
        filename = paper['filename']
        text = paper['text']
        
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        # Extract year from text
        year = None
        import re
        
        # Try to find a 4-digit year first
        year_match = re.search(r'(?:20|19)\d{2}', text)
        if year_match:
            year = int(year_match.group())
        else:
            # Try to find venue year pattern like "'15" or "'16"
            venue_year_match = re.search(r"[A-Z]+\s+'(\d{2})", text)
            if venue_year_match:
                year_str = venue_year_match.group(1)
                if year_str.startswith('0') or year_str.startswith('1'):
                    year = 2000 + int(year_str)
                else:
                    year = 1900 + int(year_str)
        
        # Check if we have a valid year
        if year and (year < 2000 or year > 2025):
            year = None
        
        # Determine contribution type
        contribution = []
        text_lower = text.lower()
        
        if 'empirical' in text_lower:
            contribution.append('empirical')
        if 'artifact' in text_lower:
            contribution.append('artifact')
        if 'theoretical' in text_lower:
            contribution.append('theoretical')
        if 'survey' in text_lower:
            contribution.append('survey')
        if 'methodological' in text_lower:
            contribution.append('methodological')
        
        paper_info.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })
    
    # Filter papers published after 2016 with empirical contribution
    filtered_papers = []
    for paper in paper_info:
        if paper['year'] and paper['year'] > 2016 and 'empirical' in paper['contribution']:
            filtered_papers.append(paper)
    
    print(f"Total papers: {len(paper_info)}")
    print(f"Papers after 2016 with empirical contribution: {len(filtered_papers)}")
    
    for p in filtered_papers[:10]:
        print(f"{p['title']} - {p['year']} - Empirical: {'empirical' in p['contribution']}")
    
    # Save the filtered paper titles for joining with citations
    filtered_titles = [p['title'] for p in filtered_papers]
    
    print('__RESULT__:')
    print(json.dumps({
        'filtered_titles': filtered_titles,
        'count': len(filtered_papers)
    }))
else:
    print('__RESULT__:')
    print(json.dumps({'error': 'No data found'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'_id': '694f5530284b10b11dc0a86e', 'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'_id': '694f5530284b10b11dc0a86f', 'filename': 'Barriers to Engagement with a Personal Informatics Productivity Tool.txt'}, {'_id': '694f5530284b10b11dc0a870', 'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'_id': '694f5530284b10b11dc0a871', 'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'_id': '694f5530284b10b11dc0a872', 'filename': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone.txt'}, {'_id': '694f5530284b10b11dc0a873', 'filename': 'Charting Design Preferences on Wellness Wearables.txt'}, {'_id': '694f5530284b10b11dc0a874', 'filename': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units.txt'}, {'_id': '694f5530284b10b11dc0a875', 'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt"}, {'_id': '694f5530284b10b11dc0a876', 'filename': 'Common Barriers to the Use of Patient-Generated Data Across Clinical Settings.txt'}, {'_id': '694f5530284b10b11dc0a877', 'filename': 'Communicating Uncertainty in Fertility Prognosis.txt'}, {'_id': '694f5530284b10b11dc0a878', 'filename': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt'}, {'_id': '694f5530284b10b11dc0a879', 'filename': 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps.txt'}, {'_id': '694f5530284b10b11dc0a87a', 'filename': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym.txt'}, {'_id': '694f5530284b10b11dc0a87b', 'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'_id': '694f5530284b10b11dc0a87c', 'filename': 'DataSelfie: Empowering People to Design Personalized Visuals to Represent Their Data.txt'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
