import xbmc

def acesso_mac(mac):

    dir = xbmc.translatePath("special://home/addons/plugin.video.kodishvip/data")
    config = ""+dir+"/playLists.txt"
    file = open(""+config+"","w")

    file.write('[')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/filmes.m3u", ')
    file.write('        "logos": "http://www.tefenews.com.br/wp-content/uploads/2014/07/Logo-CINEMA.jpg/", ')
    file.write('        "image": "http://www.tefenews.com.br/wp-content/uploads/2014/07/Logo-CINEMA.jpg", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Filmes"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/americanpie.m3u", ')
    file.write('        "logos": "", ')
    file.write('        "image": "http://173.249.8.202/home/lista/users/'+mac+'/lista/img/americanpie.jpg", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Coletania American PIE"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/harrypotter.m3u", ')
    file.write('        "logos": "http://173.249.8.202/home/lista/users/'+mac+'/lista/img/hp.jpg/", ')
    file.write('        "image": "http://173.249.8.202/home/lista/users/'+mac+'/lista/img/hp.jpg", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Coletanea Harry Potter"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/vandamme.m3u", ')
    file.write('        "logos": "", ')
    file.write('        "image": "https://image.ibb.co/iBDsy8/van.png", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Coletanea Jean-Claude Van Damme"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/mazaropi.m3u", ')
    file.write('        "logos": "", ')
    file.write('        "image": "http://173.249.8.202/home/lista/users/'+mac+'/lista/img/mazzaropi.jpg", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Coletanea Mazzaropi"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/tropaestrelares.m3u", ')
    file.write('        "logos": "", ')
    file.write('        "image": "http://173.249.8.202/home/lista/users/'+mac+'/lista/img/tropasestrelares.jpg", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Coletanea Das Tropas Estrelares"')
    file.write('    }, ')
    file.write('    {')
    file.write('        "url": "http://173.249.8.202/home/lista/users/'+mac+'/lista/tutles.m3u", ')
    file.write('        "logos": "", ')
    file.write('        "image": "", ')
    file.write('        "cache": 0, ')
    file.write('        "name": "Triologia Tartarugas Ninjas"')
    file.write('    }')
    file.write(']')
    
