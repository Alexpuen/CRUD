import sys

clients =[
{
    'name': 'Pablo',
    'company': 'Google',
    'email': 'pablo@google.com',
    'position':'Software engineer',
},
{
    'name': 'Ricardo',
    'company': 'Facebook',
    'email': 'ricardo@facebook.com',
    'position':'Data engineer',
}]

def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client(client_id, updated_client):
    global clients

    if len(clients) -1  >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in the client\'s list')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _print_welcome():
    print('Welcome to sales plataform')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    return field


def _get_client_from_user():
    client = {
        'name':_get_client_field('name'),
        'company':_get_client_field('company'),
        'email':_get_client_field('email'),
        'position':_get_client_field('position'),
    }
    return client


def run():
    _print_welcome()
    command = input()
    command = command.upper()

    if command == 'C':
        client = _get_client_from_user()
        create_client(client)
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()
        update_client(client_id, updated_client)
        list_clients()

    elif command == 'D':
        client_id = int(_get_client_field('id'))
        delete_client(client_id)
        list_clients()
    elif command == 'S':
        client_name=_get_client_field('name')
        found = search_client(client_name)
        list_clients()

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in the client\'s list'.format(client_name))
    
    else:
        print('Invalid command')


if __name__ == "__main__":
    run()