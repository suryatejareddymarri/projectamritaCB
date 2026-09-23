import re
import streamlit as st
PAGES = [
        {
        "id" : "atlas",
        "tilte" : "The Atlas of the Open Web",
        "domain" : "atlas.example",
        "text" : "A field guide to hyperlinks ,browsers ,protocol and the people who keep the web open and connected.",
        "links" : ["protocols", "commons", "ranking", "libraries"],
        },
        "id" : "ranking",
        "title" : "Ranking Pages by Importance",
        "domain" : "ranking.example",
        "text" : "A plain-language tour of PageRank, authority, damping and why a link can be a vote with damping.",
        "links" : ["atlas", "algorithms", "search", "commons"],
        },
        "id" : "algorithms",
        "title" : "Algorithms for curious people",
        "domain" : "patterns.example",
        "text" : "A visual introduction to algorithms: sort, traverse, score, and use feedback to improve a system.",
        "links" : ["ranking", "search", "code"],
        }'
        "id" : "protocols",
        "title" : "How the web works",
        "domain" : "fieldnotes.example"
        "text" : "URLs, DNS, HTTP requests, servers, and the quiet sequence of events behind every page you open.",
        "links" : ["atlas", "code", "libraries"],
        },
        {
        "id": "commons",
        "title": "The Knowledge Commons",
        "domain": "commons.example",
        "text": "How communities document what they know, share it freely, and build durable public infrastructure.",
        "links": ["atlas", "libraries", "search"],
        },
        {
        "id": "libraries",
        "title": "A Library of Small Tools",
        "domain": "workbench.example",
        "text": "Thoughtful software tools for reading, making, searching, and turning scattered notes into useful knowledge.",
        "links": ["code", "commons", "algorithms"],
        },
        {
        "id": "search",
        "title": "Inside a Search Engine",
        "domain": "research.example",
        "text": "Crawling, indexing, matching, and ranking: the pipeline that turns a question into a useful set of pages.",
        "links": ["ranking", "algorithms", "code"],
        },
        {
        "id": "code",
        "title": "Notes on Building Software",
        "domain": "workbench.example",
        "text": "Practical notes on debugging, interfaces, data structures, and making complex software feel simple.",
        "links": ["algorithms", "libraries", "protocols"],
        },
        ]


@st.cache_data
def calculate_pagerank(damping, iterations):
    total_pages = len(PAGES)

    scores = {}
    for page in PAGES:
    scores[page["id"]] = 1/total_pages

    for _ in range(iterations):
        next_scores = {}
        
        for page in PAGES
        next_scores[page["id"]] = (1 - damping/total_pages)

        for page in PAGES
        num_link = lens[page["link"]]
            if num_link == 0
                num_link  = 1
          share_per_link = scores[page["link"]] / num_link
      for target_id in page["links"]:
          next_scores[target_id] += damping * share_per_link

      scores = next_scores  # this round's result becomes next round's start
return scores


def tokenize(text):
  words = re.findall(r"[a-z0-9]+", text.lower())
    return words


def search_pages(query, damping, iteration):
  ranks = calculate_pagerank(damping, iteration)
  highest_rank = max(ranks.values())
    query_words = tokenize(query)

  results = []
    for page in PAGES:
        page_words = tokenize(page["title"] + " " + page["text"] + " " + page["domain"])
    match_count = 0
        for word in query_words:
            match_count += page_words.count(word)
        if query_words:
            relevance = min(match_count / len(query_words), 1)
        else:
            relevance = 0

        authority = ranks[page["id"]] / highest_rank
        score = relevance * 0.68 + authority * 0.32

        if relevance or not query_words:
            page_with_scores = dict(page)  # copy the page dict
            page_with_scores["relevance"] = relevance
            page_with_scores["authority"] = authority
            page_with_scores["score"] = score
            results.append(page_with_scores)
          results.sort(key=lambda page: page["score"], reverse=True)
    return results




        
        
        
        
