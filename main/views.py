import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item

def lista_compras(request):
    itens = Item.objects.all().order_by('-criado_em')
    return render(request, 'lista_compras.html', {'itens': itens})

@csrf_exempt
def update_quantity(request, item_id):
    if request.method == 'POST':
        try:
            # Verificar se é uma requisição AJAX
            if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'error': 'Requisição inválida'
                }, status=400)
                
            data = json.loads(request.body)
            item = get_object_or_404(Item, id=item_id)
            delta = int(data.get('delta', 0))
            
            # Validar delta
            if delta not in [-1, 1]:
                return JsonResponse({
                    'success': False,
                    'error': 'Delta inválido'
                }, status=400)
                
            nova_quantidade = item.quantidade + delta
            
            if nova_quantidade < 1:
                return JsonResponse({
                    'success': False,
                    'error': 'Quantidade mínima é 1'
                }, status=400)
                
            item.quantidade = nova_quantidade
            item.save()
            
            return JsonResponse({
                'success': True,
                'nova_quantidade': item.quantidade
            })
            
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'error': 'Dados inválidos'
            }, status=400)
            
        except ValueError:
            return JsonResponse({
                'success': False,
                'error': 'Quantidade inválida'
            }, status=400)
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
            
    return JsonResponse({
        'success': False,
        'error': 'Método não permitido'
    }, status=405)

def adicionar_item(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        if nome:
            Item.objects.create(nome=nome)
        return redirect('lista_compras')
    return redirect('lista_compras')
