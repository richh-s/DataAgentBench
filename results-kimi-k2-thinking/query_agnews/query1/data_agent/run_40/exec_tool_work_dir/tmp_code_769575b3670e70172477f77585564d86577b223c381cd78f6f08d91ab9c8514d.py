code = """import json
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

# Track articles with sports keywords but also check if they're actually about sports
sports_candidates = []

for article in articles_data:
    title = article.get('title', '')
    desc = article.get('description', '')
    title_lower = title.lower()
    desc_lower = desc.lower()
    
    # Look for sports terms but avoid false positives
    sports_score = 0
    
    # Strong sports indicators (higher weight)
    if any(term in title_lower for term in ['nfl', 'nba', 'mlb', 'nhl', 'super bowl', 'world cup', 'olympics']):
        sports_score += 3
    if any(term in desc_lower for term in ['nfl', 'nba', 'mlb', 'nhl', 'super bowl', 'world cup', 'olympics']):
        sports_score += 2
    
    # Medium sports indicators
    medium_terms = ['football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'coach', 'player', 'team', 'game', 'match']
    sports_score += sum(1 for term in medium_terms if term in title_lower) * 2
    sports_score += sum(1 for term in medium_terms if term in desc_lower)
    
    # Only consider articles with significant sports indicators
    if sports_score >= 3:
        sports_candidates.append({
            'title': title,
            'desc': desc,
            'desc_length': len(desc),
            'sports_score': sports_score
        })

# Sort by description length to find the longest
if sports_candidates:
    sports_candidates.sort(key=lambda x: (x['desc_length'], x['sports_score']), reverse=True)
    longest_sports_title = sports_candidates[0]['title']
else:
    longest_sports_title = None

print('__RESULT__:')
print(json.dumps(longest_sports_title))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': "Why Windows isn't Unix", 'var_functions.execute_python:12': 1000, 'var_functions.execute_python:16': "Why Windows isn't Unix", 'var_functions.execute_python:20': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Examining 1000 articles for sports content'}

exec(code, env_args)
