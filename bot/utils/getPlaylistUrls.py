import re
import urllib.request
import urllib.error

from django.utils.datastructures import OrderedSet

def getPlaylistUrls(youtubeUrl):
    if 'http' not in youtubeUrl:
        url = 'https://' + youtubeUrl
    else:
        url = youtubeUrl

    sTUBE = ''
    cPL = ''

    urls = OrderedSet()

    if 'list=' in url:
        p = re.compile(r'list=([^&]*)')
        match = p.search(url)
        listStr = match.group()
        eq = listStr.rfind('=') + 1
        cPL = listStr[eq:]
    else:
        print('Incorrect Playlist.')
        exit(1)

    try:
        yTUBE = urllib.request.urlopen('https://www.youtube.com/playlist?list='+cPL).read()
        sTUBE = str(yTUBE)
    except urllib.error.URLError as e:
        print(e.reason)

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, sTUBE)

    if mat:
        for PL in mat:
            yPL = str(PL)
            if '&' in yPL:
                yPL_amp = yPL.index('&')
            urls.add('https://www.youtube.com/' + yPL[:yPL_amp])

    return urls