code = """import json

file_path = locals()['var_functions.query_db:12']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Let's search more broadly for any articles that might be sports
sports_related = []
for article in articles:
    title_lower = article.get('title', '').lower()
    desc_lower = article.get('description', '').lower()
    
    # Look for any sport-related terms
    sport_terms = ['sport', 'game', 'team', 'player', 'coach', 'athlete', 'competition', 'championship', 'tournament']
    
    has_sport_term = any(term in title_lower or term in desc_lower for term in sport_terms)
    
    # Look for specific sports
    specific_sports = ['football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby']
    has_specific_sport = any(sport in title_lower or sport in desc_lower for sport in specific_sports)
    
    if has_sport_term or has_specific_sport:
        sports_related.append({
            'title': article.get('title'),
            'description': article.get('description'),
            'desc_len': len(article.get('description', '')),
            'has_specific_sport': has_specific_sport
        })

# Sort by description length
sports_related.sort(key=lambda x: x['desc_len'], reverse=True)

result_titles = []
for article in sports_related:
    result_titles.append(article['title'] + ' (' + str(article['desc_len']) + ' chars, specific: ' + str(article['has_specific_sport']) + ')')

result = ' | '.join(result_titles[:10]) if result_titles else 'No potential sports articles found'

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'_id': '69696948203b0b87ea9f48a0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696948203b0b87ea9f48a1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696948203b0b87ea9f48a2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696948203b0b87ea9f48a3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696948203b0b87ea9f48a4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': 'No sports articles found', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': 'Technology as Fashion', 'var_functions.execute_python:22': 'Technology as Fashion', 'var_functions.execute_python:26': 'AMD starts shipping 90-nanometer chips to customers', 'var_functions.execute_python:28': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:30': 'Technology as Fashion', 'var_functions.execute_python:32': 'Pretty Log4J', 'var_functions.execute_python:34': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:36': "1. AMD starts shipping 90-nanometer chips to customers (810 chars) | 2. Technology as Fashion (749 chars) | 3. The Austral-Asian Strike Fighter (735 chars) | 4. LinuxWorld, IDs, and Privacy (709 chars) | 5. RuntimeProperties... Reflection from System Properties (708 chars) | 6. Pretty Log4J (708 chars) | 7. Ron Regan Jr is My Kinda Guy (708 chars) | 8. Java3D - Half Right (708 chars) | 9. Kerry's Disgusting Ad (708 chars) | 10. Americans and Freedom (708 chars) | 11. Why Windows isn't Unix (708 chars) | 12. Microsoft, IE and Bloat (708 chars) | 13. I Confess.  I'm a Software Pirate. (708 chars) | 14. Al Qaeda member surrenders (706 chars) | 15. Saudis: Bin Laden associate surrenders (691 chars)"}

exec(code, env_args)
