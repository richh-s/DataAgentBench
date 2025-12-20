code = """import json
import re

file_path = locals()['var_function-call-7338206399480502302']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords definition (same as before but maybe refined)
st_keywords = [
    'science', 'technology', 'tech', 'computer', 'software', 'hardware', 
    'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'wireless', 
    'broadband', 'network', 'satellite', 'space', 'nasa', 'astronomy', 
    'galaxy', 'planet', 'mars', 'orbit', 'robot', 'ai', 'artificial intelligence', 
    'gadget', 'device', 'chip', 'processor', 'microsoft', 'google', 'apple', 
    'ibm', 'intel', 'linux', 'windows', 'mac', 'ios', 'android', 'video game', 
    'gaming', 'nintendo', 'sony', 'playstation', 'xbox', 'gameboy', 'hacker', 
    'virus', 'security', 'cyber', 'data', 'server', 'cloud', 'program', 'code', 
    'app', 'browser', 'search engine', 'email', 'spam', 'blog', 'social media', 
    'facebook', 'twitter', 'amazon', 'ebay', 'yahoo', 'telecom', 'physics', 
    'biology', 'chemistry', 'genetics', 'genome', 'medical', 'research', 'lab', 
    'scientist', 'engineer', 'innovation', 'ipod', 'itunes', 'firefox', 'explorer',
    'semiconductor', 'lcd', 'plasma', 'dvd', 'mp3', 'gps', 'biotech', 'cloning',
    'stem cell', 'supercomputer', 'nanotech', 'probe', 'shuttle', 'telescope',
    'defcon', 'voip', 'wifi', 'bluetooth', 'spyware', 'malware'
]

categories = {
    "Science/Technology": st_keywords,
    "Sports": ['sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympic', 'championship', 'tournament', 'league', 'cup', 'medal', 'player', 'coach', 'team', 'athlete', 'stadium', 'match', 'score', 'win', 'loss', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'wimbledon', 'nascar', 'f1', 'racing', 'cricket', 'rugby', 'game', 'quarterback', 'receiver', 'pitcher', 'homerun', 'touchdown', 'gold', 'silver', 'bronze'],
    "Business": ['business', 'economy', 'market', 'stock', 'trade', 'company', 'profit', 'loss', 'bank', 'finance', 'dollar', 'euro', 'yen', 'currency', 'oil', 'gas', 'energy', 'price', 'corp', 'inc', 'ltd', 'investment', 'investor', 'share', 'revenue', 'sales', 'deal', 'merger', 'acquisition', 'ceo', 'cfo', 'manager', 'executive', 'industry', 'manufacturing', 'retail', 'inflation', 'fed', 'rates', 'wall street', 'dow jones', 'nasdaq', 'nyse', 'deficit', 'budget', 'spending', 'consumer'],
    "World": ['world', 'war', 'peace', 'politics', 'president', 'minister', 'government', 'country', 'nation', 'iraq', 'iran', 'china', 'usa', 'america', 'uk', 'britain', 'eu', 'europe', 'un', 'united nations', 'treaty', 'election', 'vote', 'poll', 'military', 'army', 'police', 'attack', 'bomb', 'blast', 'terrorism', 'terrorist', 'disaster', 'quake', 'tsunami', 'storm', 'hurricane', 'flood', 'kill', 'die', 'death', 'hostage', 'baghdad', 'kabul', 'gaza', 'israel', 'palestine', 'nuclear', 'prime minister', 'parliament', 'official', 'protest', 'strike']
}

def categorize(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, kws in categories.items():
        for kw in kws:
            # Word boundary check for short words to avoid false matches
            if len(kw) <= 4:
                # \b matches word boundary
                if re.search(r'\b' + re.escape(kw) + r'\b', text):
                    scores[cat] += 1
            else:
                if kw in text:
                    scores[cat] += 1
    
    # Context rules
    if "game" in text:
        # if "game" is present, check context
        tech_context = any(x in text for x in ["video", "console", "nintendo", "sony", "xbox", "computer", "software", "tech", "gaming", "gameboy", "arcade", "mario", "zelda"])
        sports_context = any(x in text for x in ["sport", "football", "soccer", "team", "league", "cup", "stadium", "score", "player", "coach", "olympic", "championship"])
        
        if tech_context and not sports_context:
            scores["Science/Technology"] += 2
        elif sports_context and not tech_context:
            scores["Sports"] += 2
        elif tech_context and sports_context:
            # "EA Sports game" -> Tech/Business usually, but the topic is the game software.
            scores["Science/Technology"] += 1
            
    if "oil" in text or "gas" in text:
         scores["Business"] += 1
    
    if "nuclear" in text:
        # Nuclear can be World (war/weapons) or Science (energy/physics) or Business (energy)
        # Usually World in news (Iran nuclear talks etc.)
        if "weapon" in text or "bomb" in text or "talks" in text or "treaty" in text:
            scores["World"] += 2
        elif "plant" in text or "energy" in text or "physics" in text:
            scores["Science/Technology"] += 1
            scores["Business"] += 1

    # Heuristics for specific companies that might be ambiguous
    if "apple" in text:
        if "fruit" not in text and "pie" not in text:
             scores["Science/Technology"] += 1
             scores["Business"] += 1 # It's a company too

    if sum(scores.values()) == 0:
        # Default fallback? Or return Unknown
        # Maybe check for specific patterns
        return "Unknown"
    
    # Priority: if Science/Technology has max score, return it.
    # If tie, we need a tie breaker.
    # Usually "Science/Technology" vs "Business" is the main confusion for tech companies.
    # If the article is about "profits", "shares", "stocks" of a tech company -> Business.
    # If about "release", "new product", "feature", "hack" -> Tech.
    
    best_cat = max(scores, key=scores.get)
    
    # Refined tie-breaking/adjustment
    if scores["Science/Technology"] == scores["Business"] and scores["Science/Technology"] > 0:
        # Check for business specific terms
        biz_terms = ['stock', 'share', 'profit', 'revenue', 'quarter', 'market', 'wall street', 'investor']
        tech_terms = ['software', 'hardware', 'app', 'new', 'launch', 'feature', 'device']
        biz_score = sum(1 for t in biz_terms if t in text)
        tech_score = sum(1 for t in tech_terms if t in text)
        if biz_score > tech_score:
            return "Business"
        else:
            return "Science/Technology"
            
    return best_cat

st_count = 0
total = 0
results = []

for article in articles:
    total += 1
    cat = categorize(article.get('title', ''), article.get('description', ''))
    is_st = (cat == "Science/Technology")
    if is_st:
        st_count += 1
    results.append({
        "title": article.get('title'),
        "category": cat,
        "is_st": is_st
    })

fraction = st_count / total if total > 0 else 0

# Print the result and some examples for verification
print("__RESULT__:")
print(json.dumps({
    "st_count": st_count,
    "total": total,
    "fraction": fraction,
    "sample_st": [r['title'] for r in results if r['is_st']][:5],
    "sample_other": [r['title'] + " (" + r['category'] + ")" for r in results if not r['is_st']][:5]
}))"""

env_args = {'var_function-call-15392532606870454627': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-13831368158755182800': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'title': 1, 'description': 1}}, 'var_function-call-16257297644781231984': [{'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-281867425968629856': {'st_count': 2, 'total': 5, 'fraction': 0.4, 'sample_classifications': [['GameBoy mini-games win prize', 'ST'], ['Bailey Tries WR', 'Unknown'], ['Students Win \\$100,000 in National Team Science Competition', 'World'], ['Energy from waves  teenager wins science award', 'ST'], ['China #39;s appetite boosts BHP', 'Business']]}, 'var_function-call-7973401665590639291': {'count': 5, 'type': "<class 'list'>"}, 'var_function-call-8494642040961561930': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'projection': {'_id': 0, 'title': 1, 'description': 1}, 'limit': 1000}, 'var_function-call-7338206399480502302': 'file_storage/function-call-7338206399480502302.json'}

exec(code, env_args)
