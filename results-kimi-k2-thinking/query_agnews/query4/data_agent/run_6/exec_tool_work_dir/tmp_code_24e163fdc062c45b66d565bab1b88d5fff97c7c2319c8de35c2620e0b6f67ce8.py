code = """import json, re
articles = locals()['var_functions.query_db:26']

# Build set of titles and descriptions
sample = articles[:10]

def categorize(title, description):
    text = (title + ' ' + description).lower()
    # Define keyword patterns
    # World: political, countries, war, government, UN, international, climate
    world_keywords = [
        'war', 'iraq', 'iran', 'afghanistan', 'israel', 'palestin', 'china', 'india', 'pakistan',
        'nuclear', 'peace', 'un ', 'u.n.', 'government', 'election', 'political', 'terror',
        'climate', 'global warming', 'treaty', 'summit', 'world', 'international', 'diplom',
        'ambassador', 'korea', 'russia', 'putin', 'bush', 'obama', 'clinton', 'senate', 'congress',
        'syria', 'lebanon', 'egypt', 'libya', 'climate change', 'kyoto', 'united nations',
        'foreign', 'military', 'pentagon', 'security council', 'europe', 'asia', 'africa',
        'latin america', 'european union', 'eu ', 'nato', 'opec', 'world bank', 'imf',
        'genocide', 'human rights', 'diplomat', 'embassy', 'conflict', 'post-war',
        'anti-war', 'protest', 'dead', 'killed', 'attack'
    ]
    # Sports: sports terms
    sports_keywords = [
        ' game', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis',
        'golf', 'olympic', 'world cup', 'super bowl', 'coach', 'team', 'player',
        'season', 'quarter', 'score', 'win', 'lost', 'champion', 'tournament',
        'race', 'marathon', 'run', 'swim', 'coach ', 'olympics', 'fifa', 'nfl',
        'nba', 'mlb', 'nhl', 'draft', 'medal', 'gold', 'silver', 'bronze'
    ]
    # Business: stocks, markets, economy, companies, finance
    business_keywords = [
        'stock', 'market', 'economy', 'wall st', 'wall street', 'profit', 'loss',
        'company', 'corporate', 'investment', 'investors', 'bond', 'equity', 'share',
        'index', 'nasdaq', 'dow', 's&p', 'earnings', 'revenue', 'sales', 'quarter',
        'executive', 'ceo', 'fund', 'bank', 'oil prices', 'oil', 'energy', 'trade',
        'deficit', 'budget', 'fed ', 'federal reserve', 'inflation', 'unemployment',
        'job', 'work', 'labor', 'wto', 'commerce', 'business', 'deal', 'acquisition',
        'merge', 'carlyle', 'google ipo', 'ipo', 'initial public offering'
    ]
    # Sci/Tech: tech, science, software, internet
    scitech_keywords = [
        'software', 'internet', 'google', 'microsoft', 'intel', 'apple', 'computer',
        'chip', 'technology', 'tech', 'science', 'research', 'study', 'university',
        'scientist', 'satellite', 'space', 'nas', 'gene', 'dna', 'physics', 'chemistry',
        'medical', 'health', 'cancer', 'drug', 'clinical', 'treatment', 'digital',
        'online', 'web', 'browser', 'security', 'virus', 'worm', 'hacker', 'encryption',
        'broadband', 'wireless', 'mobile', 'phone', 'cellular', 'lcd', 'plasma',
        'robot', 'artificial intelligence', 'ai', 'quantum', 'laser', 'telecom',
        'fiber', 'optics', 'semiconductor', 'transistor', 'processor'
    ]
    # Count matches
    def count_matches(kws):
        cnt = 0
        for kw in kws:
            if kw in text:
                cnt += 1
        return cnt
    w = count_matches(world_keywords)
    s = count_matches(sports_keywords)
    b = count_matches(business_keywords)
    t = count_matches(scitech_keywords)
    # Choose max; tie -> world
    cats = [('World', w), ('Sports', s), ('Business', b), ('SciTech', t)]
    cats.sort(key=lambda x: x[1], reverse=True)
    return cats[0][0]

results = []
for a in sample:
    title = a.get('title', '')
    desc = a.get('description', '')
    cat = categorize(title, desc)
    results.append({'article_id': a['article_id'], 'title': title, 'category': cat})

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'count': 6696, 'message': 'Found 6696 articles from 2015'}, 'var_functions.query_db:10': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'total_articles_2015': 6696, 'articles_with_content': 0}, 'var_functions.execute_python:16': {'metadata_sample_ids': ['13', '18', '26', '51', '52'], 'articles_sample_ids': ['0', '1', '2', '3', '4']}, 'var_functions.execute_python:18': {'total_ids': 6696}, 'var_functions.execute_python:20': {'total_2015_articles': 6696, 'unique_article_count': 6696, 'sample_ids': ['55936', '54113', '28308', '58511', '74988', '5031', '59364', '14780', '89973', '48077'], 'region_sample': {'13': 'Europe', '18': 'South America', '26': 'Africa', '51': 'South America', '52': 'Africa'}}, 'var_functions.query_db:22': [], 'var_functions.query_db:24': [{'_id': '6969d4ae855c9d59985346f2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_functions.query_db:26': [{'_id': '6969d4ae855c9d59985346e5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d4ae855c9d59985346e6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d4ae855c9d59985346e7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d4ae855c9d59985346e8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d4ae855c9d59985346e9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'metadata_type': "<class 'str'>", 'metadata_is_str': True, 'articles_type': "<class 'list'>", 'articles_is_str': False, 'articles_is_list': True}, 'var_functions.execute_python:32': {'filtered_count': 0}, 'var_functions.execute_python:34': {'total_articles': 5, 'min_id': 0, 'max_id': 4, 'sample_ids': [0, 1, 2, 3, 4]}, 'var_functions.execute_python:36': {'min_id': 13, 'max_id': 127570, 'count': 6696, 'unique_count': 6696}, 'var_functions.execute_python:38': {'collection': 'articles', 'filter': {'article_id': {'$in': ['13', '18', '26', '51', '52']}}}, 'var_functions.query_db:40': [], 'var_functions.query_db:42': []}

exec(code, env_args)
