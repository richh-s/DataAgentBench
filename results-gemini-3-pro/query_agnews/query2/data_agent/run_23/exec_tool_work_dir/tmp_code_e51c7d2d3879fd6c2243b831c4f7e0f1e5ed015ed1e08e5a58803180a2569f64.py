code = """import json
import re

# Load data
# The previous result is stored in 'var_function-call-3074334308009898154'.
# It might be a list or a path to a json file.
data_raw = locals()['var_function-call-3074334308009898154']

if isinstance(data_raw, str) and data_raw.endswith('.json'):
    with open(data_raw, 'r') as f:
        articles = json.load(f)
else:
    articles = data_raw

# Classification logic
def classify_article(title, desc):
    text = (title + " " + desc).lower()
    
    scores = {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}
    
    keywords = {
        'Sports': ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 'rugby', 'hockey', 'f1', 'racing', 'athlete', 'player', 'team', 'coach', 'championship', 'tournament', 'cup', 'league', 'match', 'score', 'win', 'lose', 'olympic', 'medal', 'stadium', 'club', 'fifa', 'uefa', 'nfl', 'nba', 'mlb', 'nhl', 'wimbledon', 'open', 'bowl', 'super bowl', 'world cup', 'euro', 'sox', 'yankees', 'broncos', 'cowboys', 'lakers'],
        'Business': ['business', 'economy', 'market', 'stock', 'share', 'trade', 'finance', 'money', 'investment', 'bank', 'company', 'corporation', 'industry', 'profit', 'loss', 'revenue', 'turnover', 'deal', 'merger', 'acquisition', 'bid', 'offer', 'price', 'cost', 'sale', 'consumer', 'retail', 'inflation', 'rate', 'tax', 'budget', 'debt', 'ceo', 'cfo', 'oil', 'gold', 'dollar', 'euro', 'yen', 'nasdaq', 'dow', 'ftse', 'nikkei', 'wall street', 'mining', 'bhp', 'billiton', 'airline', 'airway', 'boeing', 'airbus', 'sales', 'growth', 'quarter'],
        'Sci/Tech': ['science', 'technology', 'tech', 'computing', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'cyber', 'mobile', 'phone', 'wireless', 'broadband', 'network', 'satellite', 'space', 'nasa', 'astronomy', 'physics', 'chemistry', 'biology', 'genetics', 'dna', 'stem cell', 'clone', 'medical', 'health', 'disease', 'virus', 'cancer', 'aids', 'hiv', 'drug', 'pharmaceutical', 'robot', 'gadget', 'device', 'console', 'video game', 'gaming', 'nintendo', 'sony', 'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'browser', 'search engine', 'email', 'spam', 'hacker', 'security', 'innovation', 'invention', 'research', 'study', 'experiment', 'lab', 'scientist', 'researcher', 'gameboy', 'ipod', 'mp3', 'dvd', 'blog', 'wi-fi', 'wifi', 'engine', 'machine', 'solar', 'energy', 'power'],
        'World': ['world', 'international', 'politics', 'government', 'president', 'prime minister', 'minister', 'parliament', 'congress', 'senate', 'election', 'vote', 'poll', 'campaign', 'party', 'democrat', 'republican', 'liberal', 'conservative', 'war', 'conflict', 'military', 'army', 'navy', 'air force', 'soldier', 'troop', 'weapon', 'nuclear', 'bomb', 'attack', 'terrorism', 'terrorist', 'police', 'crime', 'murder', 'kill', 'death', 'disaster', 'accident', 'crash', 'earthquake', 'tsunami', 'hurricane', 'flood', 'fire', 'storm', 'climate', 'environment', 'un', 'united nations', 'eu', 'nato', 'middle east', 'iraq', 'afghanistan', 'china', 'russia', 'usa', 'uk', 'france', 'germany', 'palestin', 'israel', 'iran', 'korea', 'darfur', 'sudan', 'baghdad']
    }
    
    for cat, words in keywords.items():
        for word in words:
            # Use regex to match whole words roughly
            if re.search(r'\b' + re.escape(word) + r'\b', text):
                scores[cat] += 1
                
    # Ambiguity handling
    if 'game' in text:
        if any(w in text for w in ['video', 'console', 'computer', 'mobile', 'online', 'nintendo', 'sony', 'xbox', 'playstation', 'gameboy', 'boy']):
            scores['Sci/Tech'] += 2
        elif any(w in text for w in ['match', 'league', 'cup', 'team', 'player', 'coach', 'stadium']):
            scores['Sports'] += 1
        else:
            # default slight boost to Sports for "game" unless context implies otherwise?
            # actually "video game" is covered above. "GameBoy" covered. 
            pass
            
    if 'apple' in text:
        if any(w in text for w in ['computer', 'tech', 'ipod', 'mac', 'music', 'store']):
            scores['Sci/Tech'] += 2
        elif any(w in text for w in ['share', 'stock', 'market', 'profit']):
            scores['Business'] += 2
            
    # Find max score
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "Unknown" # Fallback, or assume World? Or maybe Sci/Tech if unknown? Let's check "Unknown" ones.
    
    return max_cat

sci_tech_count = 0
total_count = len(articles)
sci_tech_titles = []
unknown_titles = []

for article in articles:
    cat = classify_article(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_titles.append(article['title'])
    elif cat == 'Unknown':
        unknown_titles.append(article['title'])

result = {
    "total": total_count,
    "sci_tech_count": sci_tech_count,
    "fraction": sci_tech_count / total_count if total_count > 0 else 0,
    "sci_tech_titles": sci_tech_titles,
    "unknown_titles": unknown_titles
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-16614489939861746560': [{'author_id': '218'}], 'var_function-call-8442787552881118364': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-144725998455292322': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-3074334308009898154': [{'_id': '6944a2b70411d00c5417375c', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a2b80411d00c54173f0d', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a2b80411d00c541741b8', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a2b80411d00c54174247', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a2b80411d00c54174417', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
