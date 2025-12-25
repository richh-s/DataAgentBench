code = """# Reuse previous setup code (implicit in logic, need to copy-paste or assume state? No, state is not preserved)
# I need to rerun the loading and classification.

import json
import re
from collections import Counter

with open(locals()['var_function-call-10118669966329867769'], 'r') as f:
    id_data = json.load(f)
    target_ids = set(id_data['article_ids'])
    id_to_region = {int(k): v for k, v in id_data['id_to_region'].items()}

with open(locals()['var_function-call-10182139380038142378'], 'r') as f:
    articles = json.load(f)

relevant_articles = [a for a in articles if int(a['article_id']) in target_ids]

categories = {
    "Sports": ["sport", "game", "cup", "match", "team", "win", "won", "loss", "lost", "score", "olympic", "championship", "champion", "league", "football", "baseball", "basketball", "hockey", "tennis", "golf", "soccer", "athlete", "coach", "medal", "tournament", "stadium", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "racing", "driver", "f1", "cricket", "rugby"],
    "Business": ["oil", "price", "market", "stock", "share", "trade", "profit", "loss", "economy", "economic", "bank", "company", "firm", "corp", "inc", "ceo", "cfo", "merger", "acquisition", "deal", "dollar", "euro", "yen", "currency", "inflation", "rate", "fed", "reserve", "wall street", "nasdaq", "dow", "invest", "revenue", "sales", "quarter", "growth", "budget", "deficit", "finance", "financial"],
    "Sci/Tech": ["technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "microsoft", "google", "apple", "intel", "ibm", "server", "chip", "science", "space", "nasa", "orbit", "research", "study", "scientist", "drug", "virus", "cancer", "medical", "phone", "mobile", "wireless", "broadband", "satellite", "robot", "linux", "browser", "spam", "hacker", "digital", "gadget"],
    "World": ["war", "peace", "military", "army", "troop", "soldier", "rebel", "attack", "kill", "dead", "died", "bomb", "blast", "president", "minister", "parliament", "government", "official", "election", "vote", "party", "leader", "politic", "congress", "senate", "bush", "kerry", "putin", "blair", "iraq", "iran", "israel", "palestine", "gaza", "syria", "afghanistan", "darfur", "sudan", "russia", "china", "un", "united nations", "treaty", "nuclear", "weapon", "crisis", "hostage", "terror", "police", "court", "law", "legal", "trial", "judge", "security", "protest", "strike", "talks", "diplomat", "foreign", "international", "hurricane", "storm", "typhoon", "quake", "tsunami"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, keywords in categories.items():
            if word in keywords:
                scores[cat] += 1
    
    if "iraq" in text or "baghdad" in text: scores["World"] += 2
    if "olympic" in text: scores["Sports"] += 5
    if "microsoft" in text or "google" in text: scores["Sci/Tech"] += 2
    if "stocks" in text or "dow jones" in text: scores["Business"] += 2
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "World" 
    return best_cat

samples = {"North America": [], "Europe": []}
for article in relevant_articles:
    text = article['title'] + " " + article['description']
    category = classify(text)
    if category == "World":
        aid = int(article['article_id'])
        region = id_to_region.get(aid)
        if region in samples and len(samples[region]) < 5:
            samples[region].append(article['title'])

print("__RESULT__:")
print(json.dumps(samples))"""

env_args = {'var_function-call-13078718259946536180': 'file_storage/function-call-13078718259946536180.json', 'var_function-call-10118669966329867769': 'file_storage/function-call-10118669966329867769.json', 'var_function-call-3403215652805393396': 6696, 'var_function-call-1384210166536825512': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-1480447670109302999': [{'_id': '6944fdfd639e7f14cbca1f34', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6944fdfd639e7f14cbca1f35', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6944fdfd639e7f14cbca1f36', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '6944fdfd639e7f14cbca1f37', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '6944fdfd639e7f14cbca1f38', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-17543352879014527113': 5, 'var_function-call-10182139380038142378': 'file_storage/function-call-10182139380038142378.json', 'var_function-call-3079227003685926854': {'Africa': 565, 'North America': 569, 'Asia': 552, 'Europe': 567, 'South America': 563}}

exec(code, env_args)
