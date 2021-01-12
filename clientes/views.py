from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    
    # Ordenação dos campos no backend (api)
    # Chamando as requisiçoes, por exemplo --> Ordenar, Buscar
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # Declarando o campo para a ordenação
    ordering_fields = ['nome']
    # Declarando o campo para a busca
    search_fields = ['nome', 'cpf']
    # Declarando a busca por ativos ou não
    filterset_fields = ['ativo']
