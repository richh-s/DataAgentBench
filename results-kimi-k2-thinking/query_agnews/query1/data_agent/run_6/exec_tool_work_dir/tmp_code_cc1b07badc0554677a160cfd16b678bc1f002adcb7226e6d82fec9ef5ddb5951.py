code = """import json

# Read the articles from the file
data_file = locals()['var_functions.query_db:10']
with open(data_file, 'r') as f:
    articles = json.load(f)

# Very specific sports detection
def is_sports_article(title, description):
    combined = (title + ' ' + description).lower()
    
    # Keywords that strongly indicate sports
    strong_sports_terms = [
        # Sports and athletes names
        'giants', 'phillies', 'yankees', 'mets', 'dodgers', 'cubs', 'red sox',
        'michael phelps', 'phelps', 'thorpe', 'roddick', 'venus', 'navratilova',
        'mcgahee', 'bills', 'broncos', 'pronger', 'singh', 'leonard', 'haas',
        'zahringer', 'peyton', 'manning', 'brady', 'favre', 'woods', 
        
        # Sport-specific actions
        'touchdown', 'home run', 'strikeout', 'goal', 'points', 'score',
        'defeated', 'victory', 'defeat', 'win', 'loss', 'champion',
        'quarterback', 'pitcher', 'striker', 'defender', 'midfielder',
        
        # Events
        'world series', 'super bowl', 'nba finals', 'world cup', 'olympics',
        'championship game', 'playoff', 'semifinal', 'quarterfinal',
        
        # Context
        'game', 'match', 'season', 'tournament', 'league', 'team', 'player',
        'coach', 'stadium', 'arena', 'field', 'court'
    ]
    
    # Tech/science terms that indicate NOT sports
    tech_terms = [
        'windows', 'unix', 'linux', 'software', 'computer', 'internet',
        'technology', 'tech', 'digital', 'online', 'server', 'satellite',
        'space flight', 'oil prices', 'trade deficit', 'economy', 'federal reserve',
        'flu shot', 'medical', 'health', 'software', 'google', 'microsoft'
    ]
    
    # Count sports terms
    sports_matches = sum(1 for term in strong_sports_terms if term in combined)
    
    # Count tech terms  
    tech_matches = sum(1 for term in tech_terms if term in combined)
    
    # It's sports if it has sports-specific terms AND doesn't have many tech terms
    return sports_matches >= 2 and tech_matches < 2

# Find all sports articles and identify the one with longest description
longest_desc_length = 0
longest_sports_article = None
all_sports = []

for article in articles:
    if is_sports_article(article['title'], article['description']):
        desc_length = len(article['description'])
        all_sports.append({
            'title': article['title'],
            'length': desc_length,
            'article_id': article['article_id']
        })
        
        if desc_length > longest_desc_length:
            longest_desc_length = desc_length
            longest_sports_article = article

# Sort to see top sports articles
all_sports.sort(key=lambda x: x['length'], reverse=True)

if longest_sports_article:
    result = {
        'title': longest_sports_article['title'],
        'description_length': longest_desc_length,
        'article_id': longest_sports_article['article_id'],
        'total_sports_articles': len(all_sports),
        'top_10_sports_articles': all_sports[:10]
    }
else:
    result = {'error': 'No sports articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969666e3efec42e10016862', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969666e3efec42e10016863', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969666e3efec42e10016864', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969666e3efec42e10016865', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969666e3efec42e10016866', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:8': {'found_sports_articles': 0, 'message': 'No sports articles found'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 1000}, 'var_functions.execute_python:14': {'title': "Why Windows isn't Unix", 'description_length': 708, 'total_sports_articles_found': 268}, 'var_functions.execute_python:16': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'total_sports_articles_found': 136, 'article_id': '279'}, 'var_functions.execute_python:18': {'title': 'RuntimeProperties... Reflection from System Properties', 'description_length': 708, 'total_sports_articles_found': 217, 'article_id': '167', 'top_5_longest': [{'title': 'RuntimeProperties... Reflection from System Properties', 'length': 708}, {'title': 'Pretty Log4J', 'length': 708}, {'title': "Kerry's Disgusting Ad", 'length': 708}, {'title': 'My Blog as a Time Machine', 'length': 602}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'length': 580}]}, 'var_functions.execute_python:20': {'random_samples': [{'article_id': '975', 'title': 'Sybase upgrades PowerBuilder, plots RFID move', 'description_preview': 'Sybase Inc. released a new version of its application development tool on Monday, called PowerBuilde...', 'desc_length': 276}, {'article_id': '391', 'title': "'Insider' Information Puts City Blogs on the Map", 'description_preview': 'Locally focused group "metro" blogs -- compilations of events, reflections, recommendations, news an...', 'desc_length': 192}, {'article_id': '866', 'title': "Sysco Corp.'s 4Q Profit Up 16 Percent", 'description_preview': "Sysco's fiscal fourth-quarter profit rose 16 percent due to an extra week in the quarter, customer-s...", 'desc_length': 144}, {'article_id': '834', 'title': 'AccuRev touts software configuration management approach', 'description_preview': 'AccuRev on Monday will release an upgrade to its SCM (software configuration management) package tha...', 'desc_length': 177}, {'article_id': '922', 'title': 'The Sponsor Moves In', 'description_preview': "The Days, owned by its advertisers, may boost ABC'S bottom line. But will they control content?", 'desc_length': 95}, {'article_id': '625', 'title': 'Giants Top Phillies 3-1 to Finish Sweep (AP)', 'description_preview': 'AP - Brett Tomko allowed one run in six innings for his first win in nearly a month and helped San F...', 'desc_length': 192}, {'article_id': '70', 'title': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul", 'description_preview': "LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide ...", 'desc_length': 272}, {'article_id': '546', 'title': "Oil and Economy Cloud Stocks' Outlook", 'description_preview': ' NEW YORK (Reuters) - Soaring crude prices plus worries  about the economy and the outlook for earni...', 'desc_length': 199}, {'article_id': '158', 'title': 'Mauritanian Capital Battles Locust Swarm (AP)', 'description_preview': 'AP - Residents burned tires and trash in the streets Thursday trying to drive off swarms of locusts ...', 'desc_length': 207}, {'article_id': '476', 'title': 'Haas in fine form', 'description_preview': 'HAVEN, Wis. -- If he were acting his age, Jay Haas would have had the weekend off, resting on his la...', 'desc_length': 167}, {'article_id': '700', 'title': 'Afghans Hail Chance for a Choice', 'description_preview': 'BAZARAK, Afghanistan&lt;br&gt;Like virtually every adult in this Panjshir Valley village, Rahmal Beg...', 'desc_length': 297}, {'article_id': '172', 'title': 'Pretty Log4J', 'description_preview': "\\\\I've been a big fan of Log4J  for a while now but haven't migrated any code\\over for one central r...", 'desc_length': 708}, {'article_id': '171', 'title': 'NTP in Debian', 'description_preview': '\\\\The Network Time Daemon (NTP  Daemon) implementation within Debian leaves a\\lot to be desired.\\\\Fi...', 'desc_length': 679}, {'article_id': '463', 'title': 'Singh Leads, but Leonard Is Following', 'description_preview': 'Avoiding the late trouble that knocked other contenders off track, Vijay Singh held a one-stroke lea...', 'desc_length': 178}, {'article_id': '964', 'title': 'No Respite for Microsoft', 'description_preview': 'European antitrust regulators extend their review of Microsoft-Time Warner deal. Also: Gateway plans...', 'desc_length': 230}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description_preview': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and oc...', 'desc_length': 214}, {'article_id': '114', 'title': 'Weak Version of Most Powerful Explosions Found (SPACE.com)', 'description_preview': 'SPACE.com - Gamma-ray bursts are the most powerful events in the universe, temporary outshining seve...', 'desc_length': 160}, {'article_id': '85', 'title': 'Open Source Apps Developer SugarCRM Releases Sugar.Sales 1.1 (TechWeb)', 'description_preview': 'TechWeb - News - August 13, 2004', 'desc_length': 32}, {'article_id': '264', 'title': 'Locusts Inspire Technology That May Prevent Car Crashes', 'description_preview': 'Locusts are commonly associated with plagues, food shortages, and death. But they are also inspiring...', 'desc_length': 169}, {'article_id': '836', 'title': 'HP pushes parity for Itanium, PA-RISC servers', 'description_preview': 'At its annual HP World user conference in Chicago this week, Hewlett-Packard Co. (HP) will announce ...', 'desc_length': 255}], 'sports_candidates': [{'article_id': '279', 'title': 'China Begins Countdown for Next Manned Space Flight', 'term_found': 'nba', 'desc_length': 580}, {'article_id': '290', 'title': "Last Year's Flu Shot Imperfect But Effective", 'term_found': 'nfl', 'desc_length': 440}, {'article_id': '469', 'title': 'Rehabbing his career', 'term_found': 'basketball', 'desc_length': 402}, {'article_id': '562', 'title': 'Zahringer Leads Field at U.S. Amateur (AP)', 'term_found': 'golf', 'desc_length': 366}, {'article_id': '537', 'title': 'Phelps, Thorpe Advance in 200 Freestyle', 'term_found': 'nba', 'desc_length': 361}, {'article_id': '582', 'title': 'Phelps, Rival Thorpe in 200M-Free Semis', 'term_found': 'nba', 'desc_length': 361}, {'article_id': '688', 'title': 'McGahee Helps Bills Beat Broncos 16-6 (AP)', 'term_found': 'nfl', 'desc_length': 360}, {'article_id': '533', 'title': 'Phelps, Thorpe Advance in 200 Freestyle', 'term_found': 'nba', 'desc_length': 358}, {'article_id': '744', 'title': 'Pronger opts out of World Cup', 'term_found': 'world cup', 'desc_length': 352}, {'article_id': '603', 'title': 'Roddick, Venus, Navratilova Win Openers (AP)', 'term_found': 'tennis', 'desc_length': 350}], 'total_sports_candidates': 67}}

exec(code, env_args)
