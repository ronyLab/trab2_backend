from django.shortcuts import render
from .models import Fornecedor, Contato, Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

#DetailView facilita a exibição de detalhes de um único registro, como um fornecedor, junto com suas informações relacionadas.
from django.views.generic import DetailView

# views do Fornecedor
class FornecedorListView(ListView):
    model = Fornecedor
    template_name= 'cadfor/fornecedor_list.html'
    
class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields = ["nome", "cnpj", "endereco", "telefone", "email"]
    success_url = reverse_lazy("fornecedor_list")

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    fields = ['nome', 'cnpj', 'endereco', 'telefone', 'email']
    success_url = reverse_lazy('fornecedor_list')

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor_list')

    # Sobrescreva o método post para adicionar a lógica de exclusão dos contatos e produtos
    def post(self, request, *args, **kwargs):
        fornecedor = self.get_object()

        # Excluir todos os contatos relacionados
        Contato.objects.filter(fornecedor=fornecedor).delete()
        
        # Excluir todos os produtos relacionados
        Produto.objects.filter(fornecedor=fornecedor).delete()

        # Chama o método de exclusão padrão do DeleteView
        fornecedor.delete()

        # Redireciona após a exclusão
        return self.request.META.get('HTTP_REFERER')

# views do contato
class ContatoCreateView(CreateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']

    # Retorna para a página anterior usando HTTP_REFERER/mantém na página de criação
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')


# adicionando contatolist pra conseguir editar e excluir individualmente todos os itens da lista
class ContatoListView(ListView):
    model = Contato
    template_name = 'cadfor/contato_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fornecedor_id = self.kwargs.get('pk')
        context['fornecedor'] = Fornecedor.objects.get(id_fornecedor=fornecedor_id)
        context['contatos'] = Contato.objects.filter(fornecedor=context['fornecedor'])
        context['fornecedor_id'] = fornecedor_id  # Passa o fornecedor_id para o template, necessário para o bottão voltar para perfil, vá levando o id e funcione da melhor forma corretamente
        return context
    

class ContatoUpdateView(UpdateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']
    template_name = 'cadfor/contato_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obter o fornecedor do contato sendo editado
        fornecedor = self.object.fornecedor
        # Filtrar contatos relacionados a este fornecedor
        context['contatos'] = Contato.objects.filter(fornecedor=fornecedor)
        return context

    def get_success_url(self):
        # Redireciona para a lista de contatos filtrada pelo fornecedor após a atualização
        return reverse_lazy('contato_list', kwargs={'pk': self.object.fornecedor.id_fornecedor})

    

class ContatoDeleteView(DeleteView):
    model = Contato
    success_url = reverse_lazy('contato_list')


# Views do produto
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
        # Retorna para a página anterior usando HTTP_REFERER/Permanece na página de criação quando salva algum
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')
    

# Detalhe do Fornecedor
class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'cadfor/fornecedor_detail.html'
    context_object_name = 'fornecedor'

    # Sobrescrever o método para adicionar os contatos e produtos no contexto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contatos'] = self.object.contatos.all()  # Contatos relacionados ao fornecedor
        context['produtos'] = self.object.produtos.all()  # Produtos relacionados ao fornecedor
        return context