def test_home_response(client):
    """
    **Given** Luiza está acessando a API,
    **When** ela informa a rota/endpoint `/`
    **Then** a api deve responder um objeto com a chave `['hello']`,
    **And** seu conteúdo deve ser `world by apps`
    """
    import json


    response = client.get('/')

    data = json.loads(response.data.decode('utf-8'))

    assert data['hello'] == 'world by apps'