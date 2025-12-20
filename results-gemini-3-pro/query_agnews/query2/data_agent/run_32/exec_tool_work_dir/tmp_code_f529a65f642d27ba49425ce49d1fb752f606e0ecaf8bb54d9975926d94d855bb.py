code = """import json
import re

# Load articles
with open(locals()['var_function-call-16807799237591624192'], 'r') as f:
    articles = json.load(f)

# Define keywords with weights
keywords = [
    # Sci/Tech Strong
    ("science", "Sci/Tech", 5), ("technology", "Sci/Tech", 5), ("computer", "Sci/Tech", 5),
    ("software", "Sci/Tech", 5), ("hardware", "Sci/Tech", 5), ("internet", "Sci/Tech", 5),
    ("space", "Sci/Tech", 5), ("nasa", "Sci/Tech", 5), ("astronomy", "Sci/Tech", 5),
    ("microsoft", "Sci/Tech", 5), ("google", "Sci/Tech", 5), ("apple", "Sci/Tech", 5),
    ("intel", "Sci/Tech", 5), ("ibm", "Sci/Tech", 5), ("linux", "Sci/Tech", 5),
    ("virus", "Sci/Tech", 5), ("hacker", "Sci/Tech", 5), ("robot", "Sci/Tech", 5),
    ("video game", "Sci/Tech", 10), ("console", "Sci/Tech", 5), ("nintendo", "Sci/Tech", 5),
    ("sony", "Sci/Tech", 5), ("xbox", "Sci/Tech", 5), ("gameboy", "Sci/Tech", 5),
    ("playstation", "Sci/Tech", 5), ("wii", "Sci/Tech", 5), ("ipod", "Sci/Tech", 5),
    ("iphone", "Sci/Tech", 5), ("mobile phone", "Sci/Tech", 5), ("cell phone", "Sci/Tech", 5),
    ("wireless", "Sci/Tech", 3), ("broadband", "Sci/Tech", 3), ("satellite", "Sci/Tech", 3),
    ("physics", "Sci/Tech", 5), ("biology", "Sci/Tech", 5), ("chemistry", "Sci/Tech", 5),
    ("physicist", "Sci/Tech", 5), ("scientist", "Sci/Tech", 5), ("scientific", "Sci/Tech", 5),
    ("discovery", "Sci/Tech", 3), ("biotech", "Sci/Tech", 5), ("genome", "Sci/Tech", 5),
    ("research", "Sci/Tech", 2), ("lab", "Sci/Tech", 2), ("laboratory", "Sci/Tech", 2), ("study", "Sci/Tech", 1),
    ("tech", "Sci/Tech", 3), ("online", "Sci/Tech", 2), ("web", "Sci/Tech", 3),
    ("digital", "Sci/Tech", 3), ("network", "Sci/Tech", 2), ("server", "Sci/Tech", 3),
    ("database", "Sci/Tech", 3), ("browser", "Sci/Tech", 3), ("app", "Sci/Tech", 2),
    ("search engine", "Sci/Tech", 5), ("blog", "Sci/Tech", 3), ("spam", "Sci/Tech", 3),
    ("semiconductor", "Sci/Tech", 5), ("chip", "Sci/Tech", 3),

    # Sports Strong
    ("sport", "Sports", 5), ("football", "Sports", 5), ("soccer", "Sports", 5),
    ("basketball", "Sports", 5), ("baseball", "Sports", 5), ("tennis", "Sports", 5),
    ("golf", "Sports", 5), ("hockey", "Sports", 5), ("olympic", "Sports", 5),
    ("nfl", "Sports", 5), ("nba", "Sports", 5), ("mlb", "Sports", 5), ("nhl", "Sports", 5),
    ("fifa", "Sports", 5), ("cup", "Sports", 2), ("league", "Sports", 3),
    ("championship", "Sports", 3), ("champion", "Sports", 3), ("champions", "Sports", 3),
    ("tournament", "Sports", 3), ("match", "Sports", 2),
    ("game", "Sports", 1), ("win", "Sports", 1), ("team", "Sports", 1), ("player", "Sports", 1),
    ("coach", "Sports", 1), ("score", "Sports", 1), ("medal", "Sports", 3),
    ("athlete", "Sports", 3), ("stadium", "Sports", 2), ("race", "Sports", 2),
    ("quarter-final", "Sports", 5), ("semi-final", "Sports", 5), ("final", "Sports", 2),
    ("wimbledon", "Sports", 5), ("us open", "Sports", 5), ("australian open", "Sports", 5),
    ("french open", "Sports", 5), ("pro bowl", "Sports", 5), ("super bowl", "Sports", 5),
    ("cornerback", "Sports", 5), ("quarterback", "Sports", 5), ("receiver", "Sports", 3),
    ("umpire", "Sports", 3), ("referee", "Sports", 3), ("inning", "Sports", 3),
    ("batter", "Sports", 3), ("pitcher", "Sports", 3), ("homerun", "Sports", 3),
    ("injury", "Sports", 3), ("club", "Sports", 2), ("liverpool", "Sports", 5),
    ("arsenal", "Sports", 5), ("chelsea", "Sports", 5), ("united", "Sports", 2),
    ("real madrid", "Sports", 5), ("barcelona", "Sports", 5),
    
    # Business Strong
    ("business", "Business", 5), ("company", "Business", 3), ("market", "Business", 3),
    ("stock", "Business", 5), ("share", "Business", 3), ("economy", "Business", 5),
    ("finance", "Business", 5), ("profit", "Business", 3), ("revenue", "Business", 3),
    ("invest", "Business", 3), ("bank", "Business", 3), ("dollar", "Business", 2),
    ("oil", "Business", 3), ("price", "Business", 2), ("corp", "Business", 2),
    ("inc", "Business", 2), ("deal", "Business", 1), ("sales", "Business", 1),
    ("trade", "Business", 2), ("industry", "Business", 2), ("inflation", "Business", 4),
    ("ceo", "Business", 3), ("earnings", "Business", 3), ("wall street", "Business", 5),
    ("wto", "Business", 5), ("imf", "Business", 5), ("fed", "Business", 3),
    ("merger", "Business", 5), ("acquisition", "Business", 5),
    
    # World Strong
    ("world", "World", 2), ("president", "World", 3), ("minister", "World", 3),
    ("government", "World", 3), ("war", "World", 5), ("peace", "World", 3),
    ("military", "World", 4), ("army", "World", 3), ("police", "World", 2),
    ("attack", "World", 2), ("bomb", "World", 3), ("kill", "World", 2),
    ("election", "World", 3), ("vote", "World", 2), ("united nations", "World", 5),
    ("eu", "World", 3), ("iraq", "World", 3), ("iran", "World", 3),
    ("nuclear", "World", 3), ("politics", "World", 4), ("crisis", "World", 2),
    ("country", "World", 1), ("nation", "World", 1), ("international", "World", 2),
    ("west bank", "World", 10), ("gaza", "World", 5), ("palestin", "World", 5),
    ("israel", "World", 3), ("blast", "World", 3), ("parliament", "World", 3),
    ("senate", "World", 3), ("congress", "World", 3), ("law", "World", 2)
]

def classify(title, desc):
    text = (title + " " + desc).lower()
    words = set(re.findall(r'[a-z0-9]+', text))
    
    scores = {"Sci/Tech": 0, "Sports": 0, "Business": 0, "World": 0}
    
    for word, cat, weight in keywords:
        if " " in word:
            # Phrase
            if word in text:
                scores[cat] += weight
        else:
            # Single word
            if word in words:
                scores[cat] += weight
                
    if max(scores.values()) == 0:
        return "World" # Fallback
    
    return max(scores, key=scores.get)

sci_tech_articles = []
total_count = 0

for article in articles:
    cat = classify(article.get('title', ''), article.get('description', ''))
    total_count += 1
    if cat == "Sci/Tech":
        sci_tech_articles.append({"title": article['title'], "cat": cat})

sci_tech_count = len(sci_tech_articles)
fraction = sci_tech_count / total_count if total_count else 0

print("__RESULT__:")
print(json.dumps({
    "sci_tech_count": sci_tech_count, 
    "total_count": total_count, 
    "fraction": fraction,
    "sci_tech_list_titles": [a['title'] for a in sci_tech_articles]
}))"""

env_args = {'var_function-call-13530167711218597416': [{'author_id': '218'}], 'var_function-call-2039518021578433563': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-2120325614100718992': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-16787211040643364345': [{'_id': '6944ac495017b3003ef4bff8', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ac495017b3003ef4c7a9', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ac495017b3003ef4ca54', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ac495017b3003ef4cae3', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ac495017b3003ef4ccb3', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-16227552929909231218': {'sci_tech_count': 1, 'total_count': 5, 'fraction': 0.2, 'sample_classifications': [{'id': '192', 'title': 'GameBoy mini-games win prize', 'category': 'Sci/Tech'}, {'id': '2161', 'title': 'Bailey Tries WR', 'category': 'Unknown'}, {'id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Sports'}, {'id': '2987', 'title': 'Energy from waves  teenager wins science award', 'category': 'Unknown'}, {'id': '3451', 'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}]}, 'var_function-call-2489265392574596892': 5, 'var_function-call-16807799237591624192': 'file_storage/function-call-16807799237591624192.json', 'var_function-call-9796892164346223757': {'sci_tech_count': 0, 'total_count': 111, 'fraction': 0.0, 'sample': [{'title': 'GameBoy mini-games win prize', 'cat': 'World'}, {'title': 'Bailey Tries WR', 'cat': 'World'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'World'}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'World'}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'World'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'World'}, {'title': 'Even in win, nasty vibes', 'cat': 'World'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'World'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'title': 'Somalians sworn in', 'cat': 'World'}]}, 'var_function-call-11187854486591670590': {'sci_tech_count': 20, 'total_count': 111, 'fraction': 0.18018018018018017, 'sample': [{'title': 'GameBoy mini-games win prize', 'cat': 'Sci/Tech'}, {'title': 'Bailey Tries WR', 'cat': 'World'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Sci/Tech'}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'Sci/Tech'}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'World'}, {'title': 'Even in win, nasty vibes', 'cat': 'Sports'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'World'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'title': 'Somalians sworn in', 'cat': 'World'}, {'title': 'Muenzer races for gold', 'cat': 'Sports'}, {'title': 'Israelis to Expand West Bank Settlements', 'cat': 'Business'}, {'title': 'Stocks End Up as Oil Prices Fall', 'cat': 'Business'}, {'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'cat': 'Business'}, {'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'cat': 'World'}, {'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'cat': 'World'}, {'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'cat': 'Business'}, {'title': 'Calm as Kathmandu curfew lifted', 'cat': 'World'}, {'title': 'Israeli Missiles Kill 13 Militants', 'cat': 'World'}, {'title': 'Serena Blasts Umpire After Dramatic Defeat', 'cat': 'World'}]}, 'var_function-call-1584004407248846373': {'sci_tech_count': 21, 'total_count': 111, 'fraction': 0.1891891891891892, 'sci_tech_list': [{'title': 'GameBoy mini-games win prize', 'cat': 'Sci/Tech'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Sci/Tech'}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'Sci/Tech'}, {'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'cat': 'Sci/Tech'}, {'title': 'Space Probe Fails to Deploy Its Parachute and Crashes', 'cat': 'Sci/Tech'}, {'title': 'Shuttle repair price tag soars', 'cat': 'Sci/Tech'}, {'title': 'Microsoft settles with UK phone maker', 'cat': 'Sci/Tech'}, {'title': 'EMC Unveils E-mail Storage For Microsoft Exchange', 'cat': 'Sci/Tech'}, {'title': 'Liverpool prepares for life without Gerrard', 'cat': 'Sci/Tech'}, {'title': 'TechBrief: Vodafone seeks new frontiers', 'cat': 'Sci/Tech'}, {'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'cat': 'Sci/Tech'}, {'title': 'Texas Instruments Posts Higher 3Q Profits (AP)', 'cat': 'Sci/Tech'}, {'title': 'Satellite write-downs widen DirecTV #39;s loss', 'cat': 'Sci/Tech'}, {'title': 'Revealed: why the fear factor runs with the pack', 'cat': 'Sci/Tech'}, {'title': 'HP to launch  #39;virus-throttling #39; software', 'cat': 'Sci/Tech'}, {'title': 'XM CEO Sees Satellite Radio on Cell Phones', 'cat': 'Sci/Tech'}, {'title': "EBay Adds 'Want It Now' Feature (Reuters)", 'cat': 'Sci/Tech'}, {'title': 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'cat': 'Sci/Tech'}, {'title': 'Paypal and Apple iTunes link-up', 'cat': 'Sci/Tech'}, {'title': 'US mobile groups confirm merger', 'cat': 'Sci/Tech'}, {'title': 'Log on to be a satellite spy', 'cat': 'Sci/Tech'}]}}

exec(code, env_args)
