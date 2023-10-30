import http.client

def send_http_request(host, http_method, url, user_agent, encoding, connection):
    # Definir los valores válidos para User-Agent
    user_agents = {
        '1': 'Navegacion desde Google Chrome en Windows 10',
        '2': 'Navegacion desde Safari en Mac05',
        '3': 'Navegacion por Mozilla Firefox Ubuntu',
    }

    # Validar los parámetros
    if user_agent not in user_agents:
        print("Opción de User-Agent no válida. Debe ser 1, 2 o 3.")
        return

    if http_method not in ['GET', 'HEAD']:
        print("Método HTTP no válido. Debe ser GET o HEAD.")
        return

    if connection not in ['keep-alive', 'close']:
        print("Opción de conexión no válida. Debe ser keep-alive o close.")
        return

    # Crear una conexión HTTP al servidor
    conn = http.client.HTTPConnection(host)

    # Construir la solicitud HTTP
    request = f"{http_method} {url} HTTP/1.1\r\n"
    request += f"Host: {host}\r\n"
    request += f"User-Agent: {user_agents[user_agent]}\r\n"
    request += f"Accept-Encoding: {encoding}\r\n"
    request += f"Connection: {connection}\r\n\r\n"

    # Enviar la solicitud
    conn.request(http_method, url, headers={
        'User-Agent': user_agents[user_agent],
        'Accept-Encoding': encoding,
        'Connection': connection,
    })

    # Obtener la respuesta
    response = conn.getresponse()

    # Imprimir la respuesta
    print(f"Response Status: {response.status}")
    print("Response Headers:")
    for header, value in response.getheaders():
        print(f"{header}: {value}")
    print("\nResponse Body:")
    print(response.read().decode())

    # Cerrar la conexión
    conn.close()

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 7:
        print("Uso: python clientHTTP.py host http_method url user_agent encoding connection")
    else:
        host, http_method, url, user_agent, encoding, connection = sys.argv[1:7]
        send_http_request(host, http_method, url, user_agent, encoding, connection)
