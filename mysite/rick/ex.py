import requests 

def buscar_caps():
    URL = "https://rickandmortyapi.com/api/episode"

    def buscar_info(URL):
        PARAMS = {}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        if data['info']['next']:
            data["results"] += buscar_info(data['info']['next'])
        return data["results"]

    context = buscar_info(URL)
    print(context)


def capitulo(capitulo_id):
    url = "https://rickandmortyapi.com/api/episode/" + str(capitulo_id)
    PARAMS = {}
    r = requests.get(url, params = PARAMS)
    context = r.json()
    lista = []
    for elem in context['characters']:
        personaje = requests.get(elem, params=PARAMS).json()
        aux = []
        aux.append(personaje['name'])
        aux.append(personaje['url'])
        aux.append(personaje['id'])
        lista.append(aux)
    for elem in lista:
        print(elem)


def personaje(id_personaje):
    url = "https://rickandmortyapi.com/api/charcter/" + str(id_personaje)
    PARAMS = {}
    r = requests.get(url, params = PARAMS)
    context = r.json()
    lista = []
    for elem in context['episode']:
        personaje = requests.get(elem, params=PARAMS).json()
        aux = []
        aux.append(personaje['name'])
        lista.append(aux)
    