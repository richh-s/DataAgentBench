code = """import json
import re

# Load articles
with open(locals()['var_function-call-5617771522699572231'], 'r') as f:
    articles = json.load(f)

def classify(title, description):
    text = (title + " " + description).lower()
    
    scores = {'Sci/Tech': 0, 'Business': 0, 'Sports': 0, 'World': 0}
    
    # Sci/Tech Keywords
    sci_tech_keywords = [
        'science', 'technology', 'tech', 'computer', 'internet', 'web', 'software', 'hardware', 
        'digital', 'mobile', 'phone', 'cell', 'wireless', 'network', 'satellite', 'space', 'nasa', 
        'astronomy', 'physics', 'biology', 'genetics', 'robot', 'gadget', 'device', 'video game', 
        'nintendo', 'sony', 'microsoft', 'google', 'apple', 'intel', 'chip', 'processor', 'linux', 
        'windows', 'browser', 'virus', 'hacker', 'cyber', 'online', 'data', 'system', 'innovation', 
        'invention', 'research', 'lab', 'scientist', 'engineer', 'shuttle', 'mars', 'moon', 'galaxy',
        'telescope', 'microscope', 'solar', 'energy', 'battery', 'fuel cell', 'autonomous', 'drone',
        'artificial intelligence', 'virtual reality', 'gameboy', 'spam', 'spyware', 'worm', 'trojan',
        'encryption', 'firewall', 'algorithm', 'database', 'programmer', 'developer', 'coding', 
        'open source', 'biotech', 'nanotech', 'silicon', 'semiconductor', 'ibm', 'amd', 'nvidia',
        'samsung', 'playstation', 'xbox', 'wii', 'console', 'server', 'wifi', 'broadband',
        'defies gravity', 'supercomputer', 'cloning', 'stem cell', 'genome', 'dna'
    ]
    
    # Business Keywords
    business_keywords = [
        'business', 'economy', 'market', 'stock', 'trade', 'finance', 'bank', 'company', 'corp', 'inc', 
        'profit', 'loss', 'revenue', 'earn', 'invest', 'deal', 'merge', 'acquire', 'ceo', 'executive', 
        'industry', 'price', 'rate', 'dollar', 'euro', 'oil', 'gold', 'wall street', 'dow', 'nasdaq',
        'sales', 'retail', 'consumer', 'spending', 'inflation', 'fed', 'treasury', 'bond', 'deficit',
        'budget', 'tax', 'employment', 'job', 'hiring', 'firing', 'layoff', 'bankruptcy', 'debt',
        'loan', 'mortgage', 'interest', 'currency', 'exchange', 'export', 'import', 'tariff'
    ]
    
    # Sports Keywords
    sports_keywords = [
        'sport', 'football', 'baseball', 'basketball', 'soccer', 'hockey', 'tennis', 'golf', 'cricket', 
        'rugby', 'team', 'game', 'match', 'player', 'coach', 'score', 'win', 'lose', 'tie', 'champion', 
        'cup', 'league', 'season', 'olympic', 'medal', 'athlete', 'stadium', 'club', 'nba', 'nfl', 'mlb',
        'nhl', 'fifa', 'uefa', 'nascar', 'f1', 'formula 1', 'racing', 'race', 'tournament', 'championship',
        'playoff', 'final', 'semi-final', 'quarter-final', 'touchdown', 'homerun', 'goal', 'basket',
        'wicket', 'inning', 'penalty', 'foul', 'referee', 'umpire', 'manager', 'squad', 'roster'
    ]
    
    # World Keywords
    world_keywords = [
        'world', 'news', 'politics', 'government', 'president', 'minister', 'country', 'nation', 
        'international', 'war', 'peace', 'conflict', 'army', 'military', 'police', 'court', 'law', 
        'crime', 'disaster', 'storm', 'flood', 'quake', 'election', 'vote', 'party', 'parliament', 
        'congress', 'senate', 'diplomat', 'ambassador', 'treaty', 'agreement', 'negotiation', 'sanction',
        'nuclear', 'weapon', 'terror', 'bomb', 'attack', 'kill', 'wound', 'casualty', 'death', 'dead',
        'refugee', 'immigrant', 'border', 'security', 'united nations', 'un', 'eu', 'european union',
        'nato', 'iraq', 'afghanistan', 'iran', 'korea', 'china', 'russia', 'usa', 'uk', 'france',
        'germany', 'japan', 'israel', 'palestine', 'middle east', 'africa', 'asia', 'europe', 'america'
    ]

    for word in sci_tech_keywords:
        if word in text:
            scores['Sci/Tech'] += 1
            
    for word in business_keywords:
        if word in text:
            scores['Business'] += 1
            
    for word in sports_keywords:
        if word in text:
            scores['Sports'] += 1
            
    for word in world_keywords:
        if word in text:
            scores['World'] += 1

    # Heuristics to resolve specific overlaps
    if "game" in text:
        if any(x in text for x in ["video", "console", "nintendo", "xbox", "playstation", "sony", "software", "computer", "mobile", "app", "boy", "mini-game"]):
            scores['Sci/Tech'] += 5
        else:
            scores['Sports'] += 1 # "game" alone usually sports
            
    if any(x in text for x in ["microsoft", "google", "apple", "intel", "ibm"]):
        if any(x in text for x in ["stock", "profit", "revenue", "earn", "market", "trade"]):
            scores['Business'] += 2
        else:
            scores['Sci/Tech'] += 2
            
    if "oil" in text or "gas" in text:
        if "price" in text or "market" in text:
            scores['Business'] += 2
            
    if "nasa" in text or "space" in text:
        scores['Sci/Tech'] += 3

    # Special handling for explicit category mentions in description (sometimes occurs)
    
    best_cat = max(scores, key=scores.get)
    # If all 0, default to World or check for specific unmatched words? 
    # For this task, we assume covered by keywords.
    
    return best_cat

sci_tech_count = 0
total_count = len(articles)
sci_tech_articles = []

for article in articles:
    cat = classify(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_articles.append(article['title'])

print("__RESULT__:")
print(json.dumps({
    "total": total_count,
    "sci_tech_count": sci_tech_count,
    "sci_tech_titles": sci_tech_articles
}))"""

env_args = {'var_function-call-15528725958592451348': [{'author_id': '218'}], 'var_function-call-1578166081036399350': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-16030178928395895073': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-10746133605277861360': [{'_id': '6944a74a0741a8bd2860bc34', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a74a0741a8bd2860c3e5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a74a0741a8bd2860c690', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a74a0741a8bd2860c71f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a74b0741a8bd2860c8ef', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2352657671891290551': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'var_function-call-4959353213615004144': 5, 'var_function-call-5617771522699572231': 'file_storage/function-call-5617771522699572231.json'}

exec(code, env_args)
