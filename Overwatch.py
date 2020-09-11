from urllib.request import Request, urlopen
import json
hdr = {'User-Agent': 'Mozilla/5.0'}
class Overwatch():
    def name(name, tag): 
        req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        return output['username']

    def level(name, tag):
        req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        return output['level']

    def profile(name, tag):
        req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        return output['portrait']

    def private(name, tag):
        req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        return output['private']

    def frame(name, tag):
        req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
        webpage = urlopen(req).read()
        output = json.loads(webpage)
        return output['endorsement']['frame']

    class playtime():
        def quickplay(name, tag):
            req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
            webpage = urlopen(req).read()
            output = json.loads(webpage)
            return output['playtime']['quickplay']

        def competitive(name, tag):
            req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
            webpage = urlopen(req).read()
            output = json.loads(webpage)
            return output['playtime']['competitive']

    class games():
        class quickplay():
            def won(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['quickplay']['won'] 

            def played(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['quickplay']['played'] 

        class competitive():
            def won(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['competitive']['won']
            
            def lost(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['competitive']['lost']
            
            def draw(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['competitive']['draw']

            def played(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['competitive']['played']

            def winrate(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['games']['competitive']['win_rate']

    class endorsement():
        class sportsmanship():
            def value(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['sportsmanship']['value']

            def rate(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['sportsmanship']['rate']

        class shotcaller():
            def value(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['shotcaller']['value']

            def rate(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['shotcaller']['rate']

        class teammate():
            def value(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['teammate']['value']

            def rate(name, tag):
                req = Request(f'http://owapi.io/profile/pc/asia/{name}-{tag}', headers=hdr)
                webpage = urlopen(req).read()
                output = json.loads(webpage)
                return output['endorsement']['teammate']['rate']
