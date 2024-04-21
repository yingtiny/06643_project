import requests
import json

def abstract_id(paper_id):
    url = f'https://api.openalex.org/works/{paper_id}'
    req = requests.get(url)
    

    if req.status_code != 200:
        print(f"Failed to retrieve abstract for paper {paper_id}. Status code: {req.status_code}")
        return None
    
    try:
        data = req.json()
        abstract = data.get('abstract_inverted_index')

        return abstract
    except json.JSONDecodeError:
        print(f"Failed to decode JSON for paper {paper_id}. Response: {req.text}")
        return None

def openalex_search(query, start_year, end_year):
    all_results = []

    for year in range(start_year, end_year + 1): 
        url = f'https://api.openalex.org/works?search={query}&filter=publication_year:{year},has_abstract:true,open_access.is_oa:true'
        req = requests.get(url)
        data = req.json()
        all_results.extend(data['results'])

    sorted_results = sorted(all_results, key=lambda x: x.get('cited_by_count', 0), reverse=True)
    top20 = sorted_results[:20]


    return top20

def convert_text(inverted_index):
    abstract_text = ""
    for fragment, positions in inverted_index.items():
        positions.sort()  
        for position in positions:
            abstract_text += f" {fragment}"
    return abstract_text.strip()  
