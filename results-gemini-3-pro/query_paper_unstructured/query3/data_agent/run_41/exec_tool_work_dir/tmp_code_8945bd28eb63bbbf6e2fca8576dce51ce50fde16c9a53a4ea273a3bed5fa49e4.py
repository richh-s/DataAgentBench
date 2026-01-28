code = """import json
import re

papers_path = locals()['var_function-call-11129089221235827665']
citations_path = locals()['var_function-call-3385159612181082423']

try:
    with open(citations_path, 'r') as f:
        citations_data = json.load(f)
    
    citation_map = {}
    for row in citations_data:
        t = row['title']
        try:
            val = int(row['total_citations'])
        except:
            val = 0
        citation_map[t] = citation_map.get(t, 0) + val

    with open(papers_path, 'r') as f:
        papers = json.load(f)

    results = []
    
    for doc in papers:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '')
        
        # Search first 2000 chars to be safe
        header = text[:2000]
        
        # Aggressive regex for year
        # Find any "20xx"
        years_4d = re.findall(r"20\d{2}", header)
        
        # Find any "'xx"
        years_2d = re.findall(r"'(\d{2})", header)
        
        found_year = None
        
        # Check 4d
        for y in years_4d:
            iy = int(y)
            if 2000 <= iy <= 2025:
                # Exclude if it looks like a page number? (e.g. 2015 is unlikely page number in header)
                found_year = iy
                break
        
        # Check 2d if 4d failed
        if not found_year:
            for y in years_2d:
                iy = int("20" + y)
                if 2000 <= iy <= 2025:
                    found_year = iy
                    break
        
        # Filter
        if found_year and found_year > 2016:
            if "empirical" in text.lower():
                if title in citation_map:
                    results.append({
                        "title": title,
                        "citation_count": citation_map[title]
                    })
                else:
                    # Try case insensitive match
                    for c_title, count in citation_map.items():
                        if c_title.lower() == title.lower():
                            results.append({
                                "title": c_title,
                                "citation_count": count
                            })
                            break

    print("__RESULT__:")
    print(json.dumps(results))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps({"error": str(e)}))"""

env_args = {'var_function-call-12008909793186569857': ['paper_docs'], 'var_function-call-12008909793186566274': 'file_storage/function-call-12008909793186566274.json', 'var_function-call-12008909793186566787': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-7300462932011158786': 'file_storage/function-call-7300462932011158786.json', 'var_function-call-3385159612181082423': 'file_storage/function-call-3385159612181082423.json', 'var_function-call-15182070709462479705': 'check_complete', 'var_function-call-17779314564341058459': [], 'var_function-call-14079571341064099093': {'error': "[Errno 2] No such file or directory: 'var_function-call-7300462932011158786.json'"}, 'var_function-call-1918080602887774637': {'year_counts': {}, 'empirical_count': 2, 'after_2016_count': 0, 'both_count': 0}, 'var_function-call-7311144611923919482': 'debug_done', 'var_function-call-1686346562381530303': {'total_papers': 5, 'header_repr': '"UBICOMP \'15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\\n\\nA Lived Informatics Model of Personal Informatics \\n\\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \\n1Computer Science & Engineering, 2Human Centered Design & Engineering \\nDUB Group, University of Washington \\n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \\n\\nABSTRACT \\nCurrent  models  of  how  people  use  personal  informatics \\nsystems are largely based in behavior change goals. They do \\nnot  adequately  characteriz"', 'matches_20xx': [], 'matches_short': []}, 'var_function-call-11129089221235827665': 'file_storage/function-call-11129089221235827665.json', 'var_function-call-8320219813278591190': [], 'var_function-call-699105815560496221': {'papers_loaded': 99, 'citations_loaded': 259, 'after_2016_count': 0, 'empirical_count': 0, 'both_count': 0, 'matched_title_count': 0, 'sample_years': [], 'sample_titles_after_2016': [], 'sample_citation_titles': ['Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Pictures Worth a Thousand Words: Reflections on Visualizing Personal Blood Glucose Forecasts for Individuals with Type 2 Diabetes', 'Personal Health Oracle: Explorations of Personalized Predictions in Diabetes Self-Management', 'Fostering User Engagement: Improving Sense of Identity Through Cosmetic Customization in Wearable Trackers', 'Snot, Sweat, Pain, Mud, and Snow: Performance and Experience in the Use of Sports Watches']}}

exec(code, env_args)
