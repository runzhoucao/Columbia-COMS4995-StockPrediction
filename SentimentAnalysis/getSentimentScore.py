from __future__ import print_function

import argparse
import json
import os
import tempfile
import csv

from rosette.api import API, DocumentParameters, RosetteException
urlPrefix = 'https://www.reuters.com'


def run(key, url, alt_url='https://api.rosette.com/rest/v1/'):
    """ Run the example """
    # Create default file to read from
    

    # Create an API instance
    api = API(user_key=key, service_url=alt_url)

    params = DocumentParameters()
    params["language"] = "eng"
    params["contentUri"] = url

    # Use an HTML file to load data instead of a string
    #params.load_document_file(temp_file.name)
    try:
        result = api.sentiment(params)

    except RosetteException as exception:
        print(exception)
    finally:
        # Clean up the file
        #temp_file.close()
          
        return result


PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 description='Calls the ' +
                                 os.path.splitext(os.path.basename(__file__))[0] + ' endpoint')
PARSER.add_argument('-k', '--key', help='Rosette API Key', required=True)
PARSER.add_argument('-u', '--url', help="Alternative API URL",
                    default='https://api.rosette.com/rest/v1/')

def extractUrl(ARGS):
    newlist = []
    filename = 'test.csv'
    with open(filename, 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = str(row['date'])
            url = urlPrefix + str(row['url'])
            print(url)
            RESULT = run(ARGS.key, url,  ARGS.url)
            data = json.loads(json.dumps(RESULT, indent=2, ensure_ascii=False,
                     sort_keys=True).encode("utf8"))

            entityLabel = ''
            conf = ''
            for entity in data['entities']:
                if entity['mention'] == 'Apple' :
                    entityLabel = entity['sentiment']['label']
                    conf = entity['sentiment']['confidence']

            newlist.append({
            'date' : date,
            'label' : data['document']['label'],
            'confidence' : data['document']['confidence'],
            'entity-label' : entityLabel,
            'entity-confidence' : conf
            #'entityLabel' : data['entity']
            })
    return newlist


if __name__ == '__main__':
    out = 'result4001-end.csv'
    ARGS = PARSER.parse_args()
    #url = 'https://www.reuters.com/article/petriepartners-rothschild/rothschild-petrie-partners-form-energy-restructuring-partnership-idUSL1N13I1HA20151123'
    #extractUrl()
    
    finalResult = extractUrl(ARGS)
    
    #we only care about confidence and label here
    with open(out, "wb") as csvfile:
        fieldnames = ('date', 'label', 'confidence', 'entity-label', 'entity-confidence')
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        
        for row in finalResult: 
            writer.writerow(row)