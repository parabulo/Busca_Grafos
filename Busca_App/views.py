from django.shortcuts import render
from .forms import Form_Busca
from Busca_App.Graph_Mod import Busca_SemPeso
from Busca_App.Graph_Mod import func_auxs as auxs
import json
import os

MAPA_PATH = os.path.join(os.getcwd(), 'data', 'mapa.txt')

# Create your views here.
def form_search_view(request):
    form = Form_Busca(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        tipo_busca = form.cleaned_data['tipo_busca']
        node_start = form.cleaned_data['node_start']
        node_end = form.cleaned_data['node_end']
        limite_busca = form.cleaned_data.get('limite_busca', None)

        nos, grafo = auxs.Gera_Problema_Grafo(MAPA_PATH)
        
        if node_start == node_end:
            form.add_error('node_start', 'Nós de Início e Fim não podem ser os mesmos')
            return render(request, 'index.html', {'form': form})

        match tipo_busca:
            case 'a':
                result = Busca_SemPeso.busca.amplitude(node_start, node_end, nos, grafo)
            case 'p':
                result = Busca_SemPeso.busca.profundidade(node_start, node_end, nos, grafo)
            case 'pl':
                result = Busca_SemPeso.busca.prof_limitada(node_start, node_end, nos, grafo, limite_busca)
            case 'ai':
                result = Busca_SemPeso.busca.aprof_iterativo(node_start, node_end, nos, grafo, limite_busca)
            case 'b':
                result = Busca_SemPeso.busca.bidirecional(node_start, node_end, nos, grafo)

        # Construct the graph data
        graph_data = {
            'nodes': [{'id': node} for node in nos],
            'links': []
        }

        for idx, neighbors in enumerate(grafo):
            for neighbor in neighbors:
                graph_data['links'].append({
                    'source': nos[idx],
                    'target': neighbor
                })
        
        tamanho_caminho = len(result)

        context = {
            'form': form,
            'graph_data': json.dumps(graph_data),
            'tamanho_caminho': json.dumps(tamanho_caminho),
            'result': json.dumps(result),
            'caminho_falho': result == "caminho não encontrado"
        }
        return render(request, 'results.html', context)
    else:
        form = Form_Busca()

    return render(request, 'index.html', {'form': form})