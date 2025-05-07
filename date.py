URBAN_ROUTES_URL = 'https://cnt-654badd9-8d43-411d-8329-4173760815f0.containerhub.tripleten-services.com?lng=pt'

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")



URBAN_ROUTES_URL= ' https://cnt-ed7d5aca-e7d2-4ae0-aab6-be2fb3d23139.containerhub.tripleten-services.com?lng=pt'
# Dados de teste
ADDRESS_FROM = 'East 2nd Street, 601'
ADDRESS_TO = '1300 1st St'
PHONE_NUMBER = '+1 123 123 12 12'
CARD_NUMBER = '1234 5678 9100'
CARD_CODE = '1111'
MESSAGE_FOR_DRIVER = 'Pare no bar de sucos'
