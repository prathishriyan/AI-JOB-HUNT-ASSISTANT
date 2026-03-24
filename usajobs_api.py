import requests
from utils.config import USAJOBS_API_KEY

def fetch_usajobs(keyword, location="", results_per_page=5):

    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": "prathikshashriyan4@gmail.com",
        "Authorization-Key": USAJOBS_API_KEY
    }

    params = {
        "Keyword": keyword,
        "LocationName": location,
        "ResultsPerPage": results_per_page
    }

    response = requests.get(
        "https://data.usajobs.gov/api/search",
        headers=headers,
        params=params
    )

    print("Status:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        return data.get("SearchResult", {}).get("SearchResultItems", [])
    else:
        print(response.text)
        return []

if __name__ == "__main__":

    jobs = fetch_usajobs("Data Analyst", location="", results_per_page=10)

    print("Jobs found:", len(jobs))

    for job in jobs:
        title = job['MatchedObjectDescriptor']['PositionTitle']
        agency = job['MatchedObjectDescriptor']['OrganizationName']
        print(f"{title} at {agency}")