from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .helpers import FindIndex

# Create your views here.


@api_view(['POST'])
def get_index(request):
    """

    post:

        Retorna o indice de fechamento do brackets
        \n

        {
            "indice": 0,
            "texto": "[ABC[23]][89]"
        }

        *** Resposta de sucesso ***

        {
            "data": {
                "indice": 0,
                "texto": "[ABC[23]][89]"
            },
            "retorno": 8
        }
    """

    data = request.data

    try:

        f = FindIndex(data['indice'], data['texto'])

        if not f.validation_data():
            return Response({
                'erro': 'Indice de entrada inválido'
            }, status=status.HTTP_400_BAD_REQUEST)

    except KeyError:
        return Response({'erro': 'parametros não informados'}, status=status.HTTP_400_BAD_REQUEST)

    except (TypeError, ValueError):
        return Response({'erro': 'parametros inválidos'}, status=status.HTTP_400_BAD_REQUEST)

    indice_retorno = f.get_index()

    return Response({'data': {**data}, 'retorno': indice_retorno}, status=status.HTTP_200_OK)
