code = """import json
import collections

# Load the data
file_path = locals()['var_function-call-13638408336047913215']
if isinstance(file_path, str) and file_path.endswith('.json'):
    with open(file_path, 'r') as f:
        articles = json.load(f)
else:
    articles = file_path

# Keywords
keywords = {
    'Sports': ['sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'olympic', 'olympics', 'medal', 'champion', 'championship', 'league', 'tournament', 'cup', 'match', 'game', 'score', 'win', 'won', 'winner', 'loss', 'lost', 'defeat', 'team', 'squad', 'player', 'athlete', 'coach', 'manager', 'referee', 'umpire', 'stadium', 'arena', 'club', 'season', 'playoff', 'final', 'semi-final', 'quarter-final', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wta', 'atp', 'nascar', 'f1', 'formula 1', 'race', 'racing', 'driver', 'rider', 'touchdown', 'goal', 'homerun', 'strikeout', 'penalty', 'foul', 'red sox', 'yankees', 'lakers', 'bulls', 'broncos', 'cowboys', 'patriots', 'united', 'city', 'real madrid', 'barcelona', 'wr', 'cornerback', 'pro bowl', 'receiver', 'offense', 'defense'],
    'Business': ['business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'trading', 'finance', 'financial', 'bank', 'banking', 'investment', 'investor', 'money', 'currency', 'dollar', 'euro', 'yen', 'profit', 'revenue', 'loss', 'earnings', 'quarter', 'quarterly', 'fiscal', 'debt', 'loan', 'credit', 'interest', 'rate', 'tax', 'price', 'cost', 'sale', 'sales', 'deal', 'merger', 'acquisition', 'buyout', 'bid', 'offer', 'company', 'corporation', 'corp', 'inc', 'ltd', 'firm', 'enterprise', 'industry', 'sector', 'ceo', 'cfo', 'executive', 'manager', 'management', 'chairman', 'president', 'director', 'employment', 'job', 'unemployment', 'labor', 'strike', 'union', 'oil', 'gas', 'energy', 'fuel', 'crude', 'barrel', 'opec', 'mining', 'commodity', 'gold', 'silver', 'retail', 'store', 'shop', 'walmart', 'mcdonalds', 'cocacola', 'pepsi', 'airline', 'boeing', 'airbus', 'auto', 'car', 'manufacturer', 'production', 'factory', 'plant', 'fed', 'federal reserve', 'sec', 'wall street', 'dow jones', 'nasdaq', 's&p', 'bhp', 'billiton'],
    'Sci_Tech': ['science', 'technology', 'tech', 'sci-tech', 'computer', 'computing', 'software', 'hardware', 'internet', 'web', 'www', 'online', 'digital', 'cyber', 'network', 'networking', 'wireless', 'wifi', 'broadband', 'mobile', 'phone', 'cellphone', 'smartphone', 'telecom', 'telecommunication', 'satellite', 'gps', 'space', 'nasa', 'esa', 'astronaut', 'shuttle', 'rocket', 'launch', 'orbit', 'planet', 'mars', 'moon', 'sun', 'solar', 'galaxy', 'universe', 'astronomy', 'telescope', 'robot', 'robotics', 'gadget', 'device', 'electronics', 'chip', 'microchip', 'processor', 'semiconductor', 'intel', 'amd', 'microsoft', 'apple', 'google', 'search', 'engine', 'yahoo', 'amazon', 'ebay', 'facebook', 'myspace', 'twitter', 'youtube', 'blog', 'blogger', 'linux', 'unix', 'windows', 'mac', 'os', 'operating system', 'browser', 'explorer', 'firefox', 'virus', 'worm', 'trojan', 'spyware', 'malware', 'hacker', 'hacking', 'security', 'firewall', 'encryption', 'spam', 'email', 'mail', 'message', 'chat', 'im', 'messenger', 'game', 'gaming', 'gamer', 'videogame', 'console', 'nintendo', 'sony', 'playstation', 'xbox', 'wii', 'psp', 'ds', 'gameboy', 'ipod', 'mp3', 'player', 'itunes', 'dvd', 'hdtv', 'lcd', 'plasma', 'camera', 'camcorder', 'photography', 'pixel', 'video', 'audio', 'sound', 'multimedia', 'biotech', 'biotechnology', 'biology', 'biological', 'genome', 'genomics', 'dna', 'gene', 'genetic', 'cloning', 'clone', 'stem cell', 'medical', 'medicine', 'health', 'healthcare', 'drug', 'pharmaceutical', 'pharma', 'pill', 'treatment', 'therapy', 'cure', 'vaccine', 'disease', 'illness', 'sickness', 'virus', 'flu', 'influenza', 'bird flu', 'h5n1', 'cancer', 'tumor', 'aids', 'hiv', 'heart', 'attack', 'stroke', 'diabetes', 'obesity', 'research', 'researcher', 'study', 'scientist', 'laboratory', 'lab', 'experiment', 'discovery', 'innovation', 'invent', 'invention', 'patent', 'physics', 'physicist', 'chemistry', 'chemist', 'nanotech', 'nanotechnology', 'gyro-gen', 'machine', 'electricity'],
    'World': ['world', 'international', 'global', 'globe', 'nation', 'national', 'country', 'state', 'government', 'politic', 'politics', 'political', 'politician', 'president', 'prime minister', 'minister', 'chancellor', 'governor', 'senator', 'congress', 'parliament', 'election', 'vote', 'voter', 'voting', 'poll', 'campaign', 'candidate', 'party', 'democrat', 'republican', 'conservative', 'liberal', 'labour', 'war', 'conflict', 'battle', 'fight', 'fighting', 'army', 'military', 'soldier', 'troop', 'navy', 'air force', 'marine', 'weapon', 'gun', 'bomb', 'blast', 'explosion', 'suicide', 'terror', 'terrorist', 'terrorism', 'al-qaeda', 'bin laden', 'iraq', 'baghdad', 'iran', 'tehran', 'israel', 'jerusalem', 'palestine', 'gaza', 'west bank', 'afghanistan', 'kabul', 'pakistan', 'india', 'kashmir', 'china', 'beijing', 'russia', 'moscow', 'putin', 'europe', 'eu', 'european union', 'un', 'united nations', 'security council', 'treaty', 'agreement', 'talks', 'summit', 'conference', 'meeting', 'peace', 'crisis', 'disaster', 'catastrophe', 'tragedy', 'accident', 'crash', 'wreck', 'fire', 'storm', 'hurricane', 'typhoon', 'cyclone', 'tornado', 'flood', 'earthquake', 'tsunami', 'quake', 'volcano', 'eruption', 'climate', 'warming', 'environment', 'pollution', 'protest', 'demonstration', 'riot', 'strike', 'police', 'court', 'judge', 'trial', 'jury', 'verdict', 'sentence', 'prison', 'jail', 'crime', 'criminal', 'murder', 'kill', 'killing', 'death', 'dead', 'die', 'victim', 'casualty', 'hostage', 'kidnap', 'abduct', 'arrest', 'detain', 'refugee', 'immigrant', 'immigration', 'border']
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = collections.defaultdict(int)
    
    # Simple scoring
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
                
    # Adjustment for ambiguous words
    if 'game' in text:
        if any(w in text for w in ['video', 'console', 'nintendo', 'sony', 'xbox', 'software', 'computer', 'boy', 'mini-games']):
            scores['Sci_Tech'] += 2
        elif any(w in text for w in ['football', 'soccer', 'league', 'team', 'sport']):
            scores['Sports'] += 2
            
    if 'win' in text or 'won' in text:
        # Check context
        pass 
        
    # Get max
    if not scores:
        return "Unknown"
    
    return max(scores, key=scores.get)

results = []
sci_tech_count = 0
total = 0

for art in articles:
    cat = classify_article(art['title'], art['description'])
    results.append({'title': art['title'], 'category': cat})
    if cat == 'Sci_Tech':
        sci_tech_count += 1
    total += 1

fraction = sci_tech_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total": total, 
    "sci_tech_count": sci_tech_count, 
    "fraction": fraction,
    "sample_classifications": results[:10]
}))"""

env_args = {'var_function-call-2253230642220225240': [{'author_id': '218'}], 'var_function-call-1710435908922731774': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-3287649313065114963': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-13638408336047913215': [{'_id': '69448b47fb4019495daf56a9', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69448b47fb4019495daf5e5a', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69448b47fb4019495daf6105', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69448b47fb4019495daf6194', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69448b48fb4019495daf6364', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
