from django.shortcuts import render
from django.http import HttpResponse
import requests 

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    def buscar_info(URL):
        PARAMS = {}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()
        if data['info']['next']:
            data["results"] += buscar_info(data['info']['next'])
        return data["results"]
    URL = "https://integracion-rick-morty-api.herokuapp.com/api/episode"
    aux = buscar_info(URL)
    context = {"info": aux}
    return render(request, 'index.html', context)

def personaje(request, personaje_id):
    url = "https://integracion-rick-morty-api.herokuapp.com/api/character/" + str(personaje_id)
    PARAMS = {}
    r = requests.get(url, params = PARAMS)
    context = r.json()
    lista_cap = []
    for elem in context['episode']:
        aux = {}
        cap = requests.get(elem, params=PARAMS).json()
        aux['name'] = cap['name']
        aux['id'] = cap['id']
        lista_cap.append(aux)
        
    if context['location']['name'] == 'unknown':
        location_id = 0
    else:
        location = requests.get(context['location']['url'], params=PARAMS).json()
        location_id = location['id']

    if context['origin']['name'] == 'unknown':
        origen_id = 0
    else:
        origen = requests.get(context['origin']['url'], params=PARAMS).json()
        origen_id = origen['id']
    enviar = {'context': context, 'cap': lista_cap, 'location': location_id, 'origen': origen_id}
    return render(request, 'personaje.html', enviar)

def lugar(request, lugar_id):
    url = "https://integracion-rick-morty-api.herokuapp.com/api/location/" + str(lugar_id)
    PARAMS = {}
    r = requests.get(url, params = PARAMS)
    context = r.json()
    lista = []
    for elem in context['residents']:
        personaje = requests.get(elem, params=PARAMS).json()
        aux = {}
        aux['name'] = personaje['name']
        aux['id'] = personaje['id']
        lista.append(aux)
    
    enviar = {'context': context, 'residentes': lista}
    return render(request, 'lugar.html', enviar)

def capitulo(request, capitulo_id):
    url = "https://integracion-rick-morty-api.herokuapp.com/api/episode/" + str(capitulo_id)
    PARAMS = {}
    r = requests.get(url, params = PARAMS)
    context = r.json()
    lista = []
    for elem in context['characters']:
        personaje = requests.get(elem, params=PARAMS).json()
        aux = {}
        aux['name'] = personaje['name']
        aux['id'] = personaje['id']
        lista.append(aux)
    enviar = {'context': context, 'personajes': lista}
    return render(request, 'capitulo.html', enviar)

def not_found(request, lugar_id):
    data = {}
    return render(request, 'not_found.html', data)
