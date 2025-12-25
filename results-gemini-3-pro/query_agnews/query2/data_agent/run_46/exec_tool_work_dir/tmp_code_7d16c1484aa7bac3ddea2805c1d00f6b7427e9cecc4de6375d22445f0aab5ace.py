code = """import json
import os

# key from previous step
data_key = 'var_function-call-18392777885130959803'
data_val = locals()[data_key]

# Load data
if isinstance(data_val, str) and os.path.exists(data_val) and data_val.endswith('.json'):
    with open(data_val, 'r') as f:
        articles = json.load(f)
elif isinstance(data_val, str):
    # It might be a JSON string if it wasn't saved to file but passed as string
    try:
        articles = json.loads(data_val)
    except:
        # If it's the preview string or something else, this might fail.
        # But usually the system handles storage. 
        # If it's a list object directly:
        articles = []
elif isinstance(data_val, list):
    articles = data_val
else:
    articles = []

# Keywords
categories = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'computing', 'computer', 'software', 'hardware', 
        'internet', 'web', 'online', 'cyber', 'digital', 'network', 'data', 'server', 
        'virus', 'hacker', 'security', 'encryption', 'code', 'program', 'app', 
        'mobile', 'phone', 'smartphone', 'wireless', 'broadband', 'telecom', 'satellite', 'gps',
        'space', 'nasa', 'astronomy', 'universe', 'planet', 'mars', 'moon', 'galaxy', 'orbit', 'solar',
        'biology', 'chemistry', 'physics', 'research', 'study', 'lab', 'scientist', 'experiment', 'dna', 'gene',
        'robot', 'ai', 'artificial intelligence', 'gadget', 'device', 'innovation', 'invention',
        'game', 'gaming', 'video game', 'console', 'nintendo', 'xbox', 'playstation', 'wii', 'gamer',
        'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'windows', 'browser', 'firefox', 'explorer'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 
        'cricket', 'rugby', 'racing', 'f1', 'nascar', 'olympic', 'medal', 'game', 'match', 
        'team', 'coach', 'player', 'athlete', 'champion', 'cup', 'league', 'tournament', 
        'win', 'loss', 'score', 'goal', 'touchdown', 'homerun', 'wicket', 'race', 'stadium', 
        'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'open'
    ],
    'Business': [
        'business', 'economy', 'market', 'stock', 'share', 'trade', 'finance', 'financial', 'money', 
        'bank', 'invest', 'profit', 'loss', 'revenue', 'sale', 'price', 'cost', 'deal', 'merger', 
        'acquisition', 'company', 'corp', 'inc', 'firm', 'ceo', 'executive', 'manager', 'industry', 
        'production', 'oil', 'gas', 'mining', 'gold', 'dollar', 'euro', 'currency', 'rate', 'inflation', 
        'tax', 'budget', 'debt', 'fed', 'wall street', 'dow', 'nasdaq'
    ],
    'World': [
        'world', 'international', 'politics', 'government', 'president', 'minister', 'official', 
        'election', 'vote', 'war', 'peace', 'military', 'army', 'attack', 'bomb', 'blast', 
        'kill', 'dead', 'disaster', 'storm', 'hurricane', 'earthquake', 'flood', 'terror', 
        'police', 'crime', 'court', 'law', 'un', 'united nations', 'country', 'nation', 'state',
        'iraq', 'iran', 'china', 'usa', 'eu', 'uk', 'israel', 'palestine'
    ]
}

scitech_count = 0
total_count = len(articles)

# Debug list
classified_scitech = []

for art in articles:
    text = (art.get('title', '') + ' ' + art.get('description', '')).lower()
    
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple check, can be improved with word boundaries but simple inclusion often works for these tasks
            if kw in text:
                scores[cat] += 1
                
    # Adjustment for "game"
    if 'game' in text:
        # Check context
        tech_context = any(x in text for x in ['video', 'console', 'nintendo', 'xbox', 'playstation', 'software', 'computer'])
        sport_context = any(x in text for x in ['football', 'baseball', 'basketball', 'league', 'coach', 'season'])
        
        if tech_context and not sport_context:
            scores['Science/Technology'] += 2
        elif sport_context and not tech_context:
            scores['Sports'] += 2
            # Remove the generic point if it was added to Scitech solely because of "game" keyword if I didn't remove it from list
            # But "game" is in both lists. So it added +1 to both.
            # This adjustment helps tilt it.
    
    # Adjustment for Apple/Google etc (Tech vs Business)
    if any(x in text for x in ['apple', 'google', 'microsoft']):
        if any(x in text for x in ['stock', 'share', 'market', 'profit']):
            scores['Business'] += 2
        else:
            scores['Science/Technology'] += 1

    # Get max score
    if max(scores.values()) > 0:
        best_cat = max(scores, key=scores.get)
    else:
        best_cat = 'World' # Default or Unknown
        
    if best_cat == 'Science/Technology':
        scitech_count += 1
        classified_scitech.append(art.get('title'))

fraction = scitech_count / total_count if total_count > 0 else 0

result = {
    "total": total_count,
    "scitech_count": scitech_count,
    "fraction": fraction,
    "example_scitech": classified_scitech[:5]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13537257212664467500': [{'author_id': '218'}], 'var_function-call-5795812948484354417': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-15291064105337959156': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-18392777885130959803': [{'_id': '6944bd03ccbbae8c297964fc', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bd03ccbbae8c29796cad', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bd03ccbbae8c29796f58', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bd03ccbbae8c29796fe7', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bd03ccbbae8c297971b7', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
