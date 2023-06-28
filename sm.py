import os
import bluetooth

def send_file_over_bluetooth(file_path, target_device):
    # Verificar se o arquivo existe
    if not os.path.exists(file_path):
        print("Arquivo não encontrado.")
        return

    # Verificar se o dispositivo Bluetooth está disponível
    if target_device not in bluetooth.discover_devices():
        print("Dispositivo Bluetooth não encontrado.")
        return

    try:
        # Estabelecer a conexão Bluetooth
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((target_device, 1))

        # Enviar o arquivo
        with open(file_path, 'rb') as file:
            for data in file:
                socket.send(data)

        # Fechar a conexão
        socket.close()
        print("Arquivo enviado com sucesso.")

    except Exception as e:
        print("Ocorreu um erro ao enviar o arquivo:", str(e))

def list_devices():
    devices = bluetooth.discover_devices()

    print("Dispositivos Bluetooth encontrados:")
    for i, device in enumerate(devices):
        device_name = bluetooth.lookup_name(device)
        print(f"{i+1}. {device_name} ({device})")

    return devices

# Obter o caminho do arquivo
file_path = input("Digite o caminho do arquivo: ")

# Listar dispositivos Bluetooth disponíveis
devices = list_devices()

# Obter a escolha do usuário
choice = input("Digite o número do dispositivo para enviar o arquivo: ")
choice = int(choice) - 1

# Verificar se a escolha é válida
if choice < 0 or choice >= len(devices):
    print("Escolha inválida.")
    exit()

# Obter o endereço do dispositivo escolhido
target_device = devices[choice]

# Chamar a função para enviar o arquivo
send_file_over_bluetooth(file_path, target_device)
