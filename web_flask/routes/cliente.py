from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Clientes

    - /clientes/ (GET) - Listar os clientes
    - /clientes/ (POST) - inserir o cliente no servidor
    - /clientes/new (GET) - renderizar o formulario para criar um cliente
    - /clientes/<id> (GET) - obter os dados de um cliente
    - /clientes/<id>/edit (GET) - renderizar um formulario para editar um cliente
    - /clientes/<id>/update (PUT) - atualizar os dados do cliente
    - /cliente/<id>/delete (DELETE) - deleta o registro do cliente
"""


@cliente_route.route('/')
def lista_clientes():
    """ listar os clientes """
    return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods=['POST'])
def inserir_clientes():
    """ inserir dados do cliente """
    
    data = request.json
    
    novo_usuario = {
        'id': len(CLIENTES) + 1,
        'nome': data['nome'],
        'email': data['email'], 
    }
    
    CLIENTES.append(novo_usuario)
    
    
    return render_template('item_cliente.html', cliente=novo_usuario)


@cliente_route.route('/new')
def form_cliente():
    """ formulario para cadastrar um cliente """
    return render_template('form_cliente.html')


@cliente_route.route('/<int:client_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhes do cliente """
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulario para editar um cliente """
    cliente = None
    for c in CLIENTES:
        if c['id'] == cliente_id:
            cliente = c
    
    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:client_id>/update', methods=['PUT'])
def update_cliente(cliente_id):
    """ atualizar os dados do cliente """
    pass


@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):   
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c['id'] != cliente_id ]
    return {'deleted': 'ok'}
