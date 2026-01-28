code = """import json
import re

# Read all articles from the database
full_result_file = locals()['var_functions.query_db:22']
with open(full_result_file, 'r') as f:
    all_articles = json.load(f)

# Get Amy Jones' article IDs from metadata
article_ids_data = locals()['var_functions.query_db:2']
amy_article_ids = [int(item['article_id']) for item in article_ids_data]

# Find Amy Jones' articles
amy_articles = []
for article in all_articles:
    if int(article['article_id']) in amy_article_ids:
        amy_articles.append(article)

# Categorize articles into one of four categories
science_tech_keywords = [
    'science', 'technology', 'tech', 'research', 'university', 'laboratory', 'innovation',
    'computer', 'software', 'algorithm', 'data', 'internet', 'digital', 'game', 'gaming',
    'genetics', 'physics', 'chemistry', 'biology', 'engineering', 'robotics', 'ai',
    'artificial intelligence', 'machine learning', 'telecom', 'mobile', 'chip', 'semiconductor'
]

sports_keywords = [
    'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics',
    'game', 'player', 'team', 'coach', 'league', 'championship', 'score', 'win',
    'coach', 'quarterback', 'touchdown', 'goal', 'match', 'race', 'run'
]

business_keywords = [
    'economy', 'stock', 'market', 'trade', 'profit', 'company', 'business', 'finance',
    'dollar', 'investment', 'shares', 'earnings', 'revenue', 'growth', 'inflation',
    'bank', 'oil', 'price', 'market', 'wall st', 'nasdaq', 'dow jones'
]

world_keywords = [
    'war', 'peace', 'government', 'president', 'minister', 'election', 'vote',
    'conflict', 'attack', 'bomb', 'military', 'troops', 'soldier', 'iraq', 'iran',
    'afghanistan', 'china', 'japan', 'europe', 'united nations', 'security', 'crisis'
]

def categorize_article(article):
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    text = title + ' ' + description
    
    # Check for each category
    has_science_tech = any(keyword in text for keyword in science_tech_keywords)
    has_sports = any(keyword in text for keyword in sports_keywords)
    has_business = any(keyword in text for keyword in business_keywords)
    has_world = any(keyword in text for keyword in world_keywords)
    
    # Prioritize Science/Tech, then Sports, then Business, then World
    if has_science_tech:
        return 'Science/Technology'
    elif has_sports:
        return 'Sports'
    elif has_business:
        return 'Business'
    elif has_world:
        return 'World'
    else:
        return 'Unknown'

# Categorize Amy's articles
category_counts = {'World': 0, 'Sports': 0, 'Business': 0, 'Science/Technology': 0, 'Unknown': 0}
for article in amy_articles:
    category = categorize_article(article)
    category_counts[category] += 1

print('__RESULT__:')
print(json.dumps({
    'total_articles': len(amy_articles),
    'category_counts': category_counts,
    'sample_articles_with_categories': [
        {
            'article_id': article['article_id'],
            'title': article['title'],
            'category': categorize_article(article)
        }
        for article in amy_articles[:5]
    ]
}))"""

env_args = {'var_functions.query_db:0': [{'author_id': '218'}], 'var_functions.query_db:2': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_functions.query_db:5': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989d8768197271b50d4a5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989d8768197271b50d750', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989d8768197271b50d7df', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989d8768197271b50d9af', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.execute_python:8': {'total_articles': 111, 'sample_articles': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989d8768197271b50d4a5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989d8768197271b50d750', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}]}, 'var_functions.execute_python:10': {'total_article_ids': 111, 'num_batches': 3, 'batch_size': 50}, 'var_functions.query_db:12': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989d8768197271b50d4a5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989d8768197271b50d750', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '696989d8768197271b50d7df', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '696989d8768197271b50d9af', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_functions.query_db:14': [{'_id': '696989d9768197271b51bff8', 'article_id': '62404', 'title': 'Man remanded over Danielle murder', 'description': 'A 20-year-old man has been remanded in custody after appearing in court charged with the murder of Nottingham schoolgirl Danielle Beccan.'}, {'_id': '696989d9768197271b51c156', 'article_id': '62754', 'title': 'Two Soldiers Die After Crash in Iraq', 'description': 'BAGHDAD, Iraq - U.S. forces battled insurgents around the rebel stronghold of Fallujah on Sunday after two American soldiers died when their helicopters crashed south of Baghdad...'}, {'_id': '696989d9768197271b51c69a', 'article_id': '64102', 'title': 'Texas Instruments Posts Higher 3Q Profits (AP)', 'description': 'AP - Third quarter profits at Texas Instruments Inc. grew by  #36;116 million from a year ago due to rising demand for its chips used in high-end mobile phones and digital light processing systems for big-screen televisions.'}, {'_id': '696989da768197271b51d13f', 'article_id': '66827', 'title': 'Sergeant in Abu Ghraib Case Pleads Guilty to 8 Counts', 'description': 'The highest-ranking Army reservist charged in the Abu Ghraib scandal pleaded guilty on Wednesday to eight counts of abusing prisoners and described in graphic '}, {'_id': '696989da768197271b51d7d1', 'article_id': '68509', 'title': "'Treasure hunt' for bandit's loot", 'description': 'Police in India warn people not to look for bounty stashed by the outlaw Veerappan, after his death earlier in the week.'}], 'var_functions.execute_python:16': {'total_fetched': 15, 'total_expected': 111}, 'var_functions.list_db:18': ['articles'], 'var_functions.execute_python:20': {'total_expected': 111, 'total_retrieved': 15, 'unique_retrieved': 10, 'sample_retrieved': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '696989d8768197271b50d4a5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '696989d8768197271b50d750', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}]}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'author_id': '218'}], 'var_functions.execute_python:26': {'author_id': '218', 'articles_in_metadata': 111, 'articles_retrieved': 15, 'full_result_file': 'file_storage/functions.query_db:22.json'}, 'var_functions.execute_python:28': {'total_amy_articles_found': 1, 'total_amy_article_ids': 111, 'sample_articles': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}]}, 'var_functions.execute_python:30': {'total_amy_articles': 1, 'total_article_ids': 111, 'sample_articles': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}]}, 'var_functions.execute_python:32': {'total_ids': 111, 'sample_ids': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869'], 'full_result_file': 'file_storage/functions.query_db:22.json'}, 'var_functions.query_db:34': [{'_id': '696989d8768197271b50ccf4', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}], 'var_functions.query_db:36': [{'_id': '696989d8768197271b50cc34', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696989d8768197271b50cc35', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696989d8768197271b50cc36', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696989d8768197271b50cc37', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696989d8768197271b50cc38', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:38': {'articles_mentioning_amy': 4, 'sample_articles': [{'_id': '696989d8768197271b50cdfe', 'article_id': '458', 'title': 'Colander Misses Chance to Emulate Jones', 'description': ' ATHENS (Reuters) - But for a decision that enraged her  coach, LaTasha Colander might have been the Marion Jones of the  Athens Olympics.'}, {'_id': '696989d8768197271b50ce00', 'article_id': '460', 'title': 'NL Wrap: Jones Homers Twice as Braves Down Cards', 'description': " NEW YORK (Reuters) - Chipper Jones cracked two homers and  Julio Franco's two-run double in the seventh inning drove in  the winning runs as the streaking Atlanta Braves downed the St.  Louis Cardinals 9-7 in the National League Saturday."}, {'_id': '696989d8768197271b50cf62', 'article_id': '814', 'title': 'Williams Has No Problem Running with Jones', 'description': ' ATHENS (Reuters) - American sprinter Lauryn Williams said  on Monday she would have no problem competing on the same team  as Marion Jones in the Olympic 4x100 meters relay.'}, {'_id': '696989d8768197271b50cfa6', 'article_id': '882', 'title': 'Stocks Higher Despite Soaring Oil Prices', 'description': "NEW YORK - Wall Street shifted higher Monday as bargain hunters shrugged off skyrocketing oil prices and bought shares following an upbeat sales report from Wal-Mart Stores and a bright outlook from Lowe's.    The Dow Jones industrial average was up 84.07, or 0.9 percent, at 9,909.42, after edging 0.1 percent higher last week..."}]}}

exec(code, env_args)
