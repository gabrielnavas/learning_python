from requests import get
from bs4 import BeautifulSoup

    
class Wallhaven(object):
    
    def __init__(self):
        self.qntd_pages = 20
        self.url = ''
        
        
    def select_url_top_list_page(self):
        if len(self.url) == 0:
            return 'Please setting one page', False
        else:
            self.url = 'https://wallhaven.cc/toplist?page={}'.format(self.qntd_pages)
            return 'Loading', True
        
    def select_url_random_page(self):
        if len(self.url) == 0:
            return 'Please setting one page', False
        else:
            self.url = 'https://wallhaven.cc/random?seed=j4Nsa&page={}'.format(self.qntd_pages)
            return 'Loading', True
        
    def select_url_search_page(self, key_search='python'):
        if len(self.url) == 0:
            return 'Please setting one page', False
        else:
            self.url = 'https://wallhaven.cc/search?q={}&categories=111&purity=100&sorting=random&order=desc&seed=jdpR7&page={amount}'.format(key_search, amount=self.qntd_pages)
            return 'Loading', True
                
    def set_amount_pages(self, amount=20):
        self.qntd_pages = amount
    
    def __download_img(self, url, diretorio='./', nome='img_.jpg'):
        f = open(diretorio + nome, 'wb')
        f.write(get(url).content)
        f.close()    
    
    def init_download(self):
    
        is_online = lambda website: get(website).status_code == 200
        get_html = lambda url: get(url)
        get_soup = lambda html: BeautifulSoup(html.text, 'html.parser')
        
        if(is_online(self.url)):
            #site on!!
            print('domain online')
            
            #pega html, transofmra em soup pra manipualacao    
            soup = get_soup(get_html(self.url))
        #    type(soup)
        #    len(soup)
            
        #    pega somente os a com class preview é onde tem os link para as imagens
            wall_cont = soup.find_all('a', {'class':'preview'})
        #    wall_cont[1].attrs['href']
            
            print('init download of toplist.')
            #peguei o link, iterar sobre todos as tags de link
            for tag_wall in wall_cont:
                link = tag_wall.attrs['href']
                
                #entrar no link para pegar a photo
                soup_in_photo = get_soup(get_html(link))
                
                #tag da photo em questao
                tag_img = soup_in_photo.find_all('img', {'id':'wallpaper'})
                
                #link da photo
                link_img = tag_img[0].attrs['src']
                
                
                #download da img
                file_name_img = link_img.rsplit('/')[-1]
                
                print('download of {}'.format(file_name_img))
                self.__download_img(link_img, '/home/navas/Desktop/', '{}'.format(file_name_img))
        
    
w = Wallhaven()   
w.init_download() 