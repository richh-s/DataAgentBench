code = """import json
import re

file_path = locals()['var_function-call-7930120477363260112']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Expanded Keywords
categories = {
    'Sports': {
        'sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby',
        'boxing', 'racing', 'olympics', 'olympic', 'medal', 'athlete', 'stadium', 'championship', 'tournament', 'world cup',
        'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'super bowl', 'games', 'game', 'team', 'coach',
        'score', 'cup', 'match', 'league', 'athens', 'greece', 'gold', 'silver', 'bronze', 'record', 'race', 'run', 'swim',
        'cycling', 'doping', 'marathon', 'sprint', 'touchdown', 'goal', 'homerun', 'f1', 'nascar', 'wrestling', 'volleyball',
        'badminton', 'archery', 'gymnastics', 'skiing', 'skating', 'fencing', 'judo', 'karate', 'referee', 'umpire',
        'playoff', 'quarterback', 'striker', 'goalkeeper', 'midfielder', 'defender', 'pitcher', 'batter', 'inning'
    },
    'Business': {
        'business', 'economy', 'economic', 'market', 'stock', 'stocks', 'trade', 'investment', 'investor', 'profit', 'revenue',
        'bank', 'banking', 'finance', 'financial', 'dollar', 'euro', 'currency', 'inflation', 'fed', 'federal', 'reserve',
        'oil', 'price', 'prices', 'company', 'corp', 'inc', 'merger', 'acquisition', 'ceo', 'cfo', 'wall', 'street', 'nasdaq',
        'dow', 'jones', 'sales', 'retail', 'growth', 'fund', 'funds', 'rate', 'rates', 'tax', 'jobs', 'unemployment', 'deficit',
        'budget', 'shareholders', 'dividends', 'earnings', 'quarterly', 'bond', 'treasury', 'recession', 'deal', 'bid'
    },
    'Sci/Tech': {
        'technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile',
        'phone', 'wireless', 'network', 'google', 'microsoft', 'apple', 'intel', 'linux', 'windows', 'server', 'virus', 'hacker',
        'space', 'nasa', 'astronomy', 'biology', 'physics', 'research', 'study', 'scientific', 'processor', 'ibm', 'spam',
        'search', 'engine', 'broadband', 'satellite', 'robot', 'ai', 'artificial', 'intelligence', 'biotech', 'genome', 'stem',
        'cell', 'clone', 'cloning', 'orbit', 'mars', 'moon', 'galaxy', 'telescope', 'laboratory', 'experiment', 'discovery',
        'innovation', 'gadget', 'device', 'laptop', 'desktop', 'browser', 'operating', 'system', 'unix', 'code', 'developer',
        'programmer', 'bug', 'patch', 'update', 'version', 'release', 'beta', 'download', 'upload', 'email', 'file', 'data',
        'database', 'chip', 'semiconductor', 'nanotech', 'laser', 'screen', 'display', 'monitor', 'keyboard', 'mouse'
    },
    'World': {
        'world', 'international', 'government', 'politics', 'political', 'president', 'minister', 'prime', 'election', 'war',
        'military', 'army', 'navy', 'peace', 'treaty', 'un', 'united', 'nations', 'security', 'terror', 'terrorism', 'iraq',
        'iran', 'china', 'russia', 'usa', 'uk', 'israel', 'palestine', 'europe', 'asia', 'africa', 'latin', 'america',
        'official', 'authorities', 'police', 'bomb', 'blast', 'kill', 'attack', 'troops', 'afghanistan', 'nuclear', 'weapon',
        'korea', 'darfur', 'sudan', 'gaza', 'baghdad', 'kabul', 'syria', 'lebanon', 'jordan', 'egypt', 'saudi', 'arabia',
        'pakistan', 'india', 'venezuela', 'colombia', 'peru', 'brazil', 'mexico', 'canada', 'australia', 'germany', 'france',
        'italy', 'spain', 'parliament', 'senate', 'congress', 'diplomat', 'ambassador', 'hostage', 'kidnap', 'insurgent',
        'guerrilla', 'rebellion', 'conflict', 'crisis', 'disaster', 'quake', 'flood', 'storm', 'hurricane', 'typhoon'
    }
}

def classify(text):
    words = set(re.findall(r'\w+', text.lower()))
    scores = {}
    for cat, kws in categories.items():
        count = 0
        for kw in kws:
            if kw in words:
                count += 1
        scores[cat] = count
    return scores

best_article = None
max_desc_len = -1
sports_candidates = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', ''))
    scores = classify(text)
    
    # Strict winner
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    winner, score = sorted_scores[0]
    runner_up_score = sorted_scores[1][1]
    
    if winner == 'Sports' and score > runner_up_score and score > 0:
        sports_candidates.append(art)
    elif winner == 'Sports' and score > 0:
        # Tie?
        # If tie with Business or World, maybe it is Sports if it has specific keywords?
        # But to be safe, I'll inspect only strict winners first.
        # If I get no results, I'll relax.
        sports_candidates.append(art) # Let's include ties for now but prioritize strict later?
        # Actually, let's just include them.

# Find longest description
for art in sports_candidates:
    desc = art.get('description', '')
    if len(desc) > max_desc_len:
        max_desc_len = len(desc)
        best_article = art

print("__RESULT__:")
print(json.dumps(best_article))"""

env_args = {'var_function-call-8759093046017392632': ['articles'], 'var_function-call-8759093046017390813': ['authors', 'article_metadata'], 'var_function-call-16077717350409753983': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2782645133135892755': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5354562691669940980': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7930120477363260112': 'file_storage/function-call-7930120477363260112.json', 'var_function-call-2596779725741786289': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-6027864298235635890': None, 'var_function-call-14334331421813516376': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Money Funds Fell in Latest Week (AP)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Safety Net (Forbes.com)', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Wall St. Bears Claw Back Into the Black', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': "Oil and Economy Cloud Stocks' Outlook", 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'No Need for OPEC to Pump More-Iran Gov', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Non-OPEC Nations Should Up Output-Purnomo', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Google IPO Auction Off to Rocky Start', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Dollar Falls Broadly on Record Trade Gap', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Rescuing an Old Saver', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'Kids Rule for Back-to-School', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'In a Down Market, Head Toward Value Funds', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': 'US trade deficit swells in June', 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}, {'title': "Shell 'could be target for Total'", 'scores': {'Sports': 0, 'Business': 0, 'Sci/Tech': 0, 'World': 0}}], 'var_function-call-1848776840446859234': {'_id': '69447aefbeeefe51a60f0daa', 'article_id': '183', 'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}}

exec(code, env_args)
