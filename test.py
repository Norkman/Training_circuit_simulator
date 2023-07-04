import requests
import json
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Fonction pour récupérer les données de l'API Meraki
def get_meraki_data():
    # Insérer ici les informations d'identification pour l'API Meraki (clé d'API, nom d'organisation, nom de réseau)
    api_key = 'YOUR_API_KEY'
    org_name = 'YOUR_ORG_NAME'
    net_name = 'YOUR_NET_NAME'
    
    # Requête pour récupérer les données de l'API Meraki
    url = 'https://api.meraki.com/api/v0/organizations/{}/networks/{}/devices'.format(org_name, net_name)
    headers = {'X-Cisco-Meraki-API-Key': api_key}
    response = requests.get(url, headers=headers)
    
    # Vérifier si la requête a réussi
    if response.status_code != 200:
        raise ValueError('Erreur lors de la récupération des données de l\'API Meraki')
    
    # Renvoyer les données sous forme de dictionnaire
    return response.json()

# Fonction pour envoyer les données à Prometheus
def send_data_to_prometheus(data):
    # Initialiser le registre de collecteurs Prometheus
    registry = CollectorRegistry()
    
    # Créer un indicateur de type jauge pour chaque donnée
    for device in data:
        device_gauge = Gauge(device['name'], 'Informations sur le dispositif', registry=registry)
        device_gauge.set(device['status'])
    
    # Envoyer les données au serveur Prometheus
    push_to_gateway('http://prometheus-server:9091', job='meraki_data', registry=registry)

# Programme principal
if __name__ == '__main__':
    # Récupérer les données de l'API Meraki
    data = get_meraki_data()
    
    # Envoyer les données à Prometheus
    send_data_to_prometheus(data)
