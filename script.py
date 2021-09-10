from TextSummary import TextSummary
from FetchData import FetchData
import json

if __name__ == '__main__':

    url = input('Enter a URL: ')

    # Fetch the document
    fd = FetchData()
    document, jsonData = fd.fetchData(url)

    # generate summary of document
    ts = TextSummary(document)
    textSummary = ts.getSummary()

    # append summary to jsonData
    jsonData['textSummary'] = textSummary

    # Write json to file
    with open('output.json', 'w') as outfile:
        outfile.write(json.dumps(jsonData, indent=4))
    
    print('Task Completed')