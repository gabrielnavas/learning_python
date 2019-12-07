from requests import get
from bs4 import BeautifulSoup

is_online = lambda website: get(website).status_code == 200
get_html = lambda url: get(url)
get_soup = lambda html: BeautifulSoup(html.text, 'html.parser')


#
#url = 'https://www.python.org/'
#
#def web_site_python(url):
#    
#    if(is_online(url)):
#        print('site online')
#        
#        html_soup = get_soup(get_html(url))
#        type(html_soup)
#        
#        divs_container = html_soup.find_all('div', class_='slide-copy')
#        type(divs_container)
#        len(divs_container)
#        
#        dir(divs_container[0])
#        divs_container[0].text
#        
#        for i in divs_container:
#            print(i)
#            
#            
##def web_site_wallhaven(url):
#


def download_img(url, diretorio='./', nome='img_.jpg'):
    f = open(diretorio + nome, 'wb')
    f.write(get(url).content)
    f.close()

url2 = 'https://wallhaven.cc/toplist?page=50'
if(is_online(url2)):
    #site on!!
    print('site online')
    
    
    #pega html, transofmra em soup pra manipualacao    
    soup = get_soup(get_html(url2))
#    type(soup)
#    len(soup)
    
#    pega somente os a com class preview é onde tem os link para as imagens
    wall_cont = soup.find_all('a', {'class':'preview'})
#    wall_cont[1].attrs['href']
    
    #itera sobre os links entrando e pegando as imagens
    for link in wall_cont:
        print(link.attrs['href'])
        
    
    
    #test --------------------------------------
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
        download_img(link_img, '/home/navas/Desktop/', 'foto')
        
    link = wall_cont[2].attrs['href']
    dir(link)
    type(link)
    
    #entrei no link, ja tenho o soup dele
    soup_in_photo = get_soup(get_html(link))
    len(soup_in_photo)
    
    tag_img = soup_in_photo.find_all('img', {'id':'wallpaper'})
    len(tag_img)
    print(tag_img)
    type(tag_img[0])
    dir(tag_img[0])
    link_img = tag_img[0].attrs['src']
    
    download_img(link_img, '/home/navas/Desktop/', 'foto')
    
    
    
    