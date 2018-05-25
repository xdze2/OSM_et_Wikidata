import requests
from urllib.parse import unquote



def imgUrlToFilename(url):
    ''' Takes an url as "'http://commons.wikimedia.org/wiki/Special:FilePath/Douaumont%20au%20Printemps.jpeg'"
        and return the string: "Douaumont au Printemps.jpeg"
        
         - used to feed the function 'getThumburl'
    '''
    return unquote(url.split('/')[-1])


def getThumburl(imagename_decoded):
    ''' Query the mediawiki API do get the url
        of the thumbail image 
        
        Example format of the input: 'Douaumont au Printemps.jpeg'
    '''
    imagename_decoded = 'FILE:' + imagename_decoded
    
    params = {
        'action':'query',
        'format':'json',
        'titles': imagename_decoded,#'|'.join( imagename_decoded ),
        'prop':'imageinfo',
        'iiprop':'url', #|size',
        "iiurlwidth":300
    }
    
    headers = { 'User-Agent': 'osm_vs_Merimee',
                'From': 'https://github.com/xdze2'}

    url = "https://commons.wikimedia.org/w/api.php"
    r = requests.get(url, params=params, headers=headers)
    
    result = r.json()
    thumburl = list( result['query']['pages'].values() )[0]['imageinfo'][0]['thumburl']
    
    return thumburl