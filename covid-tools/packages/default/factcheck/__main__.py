import os
API_KEY = os.environ.get('GOOGLE_FACTCHECK_API_KEY')

def main(args):
    res_temp = {"headers": {'content-type': 
                'application/json; charset=UTF-8'}, 
                "body": ""}
    try:
        import os
        query = args.get("query", "coronavirus vaccine arrived ?")
        lang = args.get("lang", "en")
        result_json = call_factcheck_api(query, lang)
        res_temp['body'] = result_json

    except Exception as e:
        res_temp['body'] = {'error': str(e)}

    return res_temp


def call_factcheck_api(q, lang = 'en'):
    import requests
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    # API_KEY = ''
    payload = {'key': API_KEY,
            'languageCode': lang,
            'maxAgeDays': '365',
            'pageSize':5, 
            'query': q}
    result_dict = {}
    try:
        r = requests.get(url, params=payload)
        rj = r.json()
        claims_found = rj.get('claims', [])
        for i, claim_dict in enumerate(claims_found):
            store_dict = {}
            store_dict['claim_text'] = claim_dict.get('text', "")
            store_dict['claim_by'] = claim_dict.get('claimant',"")
            review_claim = claim_dict['claimReview'][0]
            store_dict['review_site'] = review_claim['publisher'].get('site', "")
            store_dict['review_url'] = review_claim.get('url', "")
            store_dict['review_date'] = review_claim.get('reviewDate', "")
            store_dict['factual_rating'] = review_claim.get('textualRating', "")
            store_dict['review_title'] = review_claim.get('title', "")

            if not len(store_dict['review_title']):
                store_dict['review_title'] = store_dict['review_url']

            result_dict[i] = store_dict
    
    except Exception as e:
        result_dict['errors'] = str(e)
        print(e)

    return result_dict


if __name__ == "__main__":
    q = 'coronavirus vaccine arrived ?'
    # print(q)
    result_json = call_factcheck_api(q, lang = 'en')