from django.shortcuts import render
from .models import Fornecedor, Contato, Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# Create your views here.

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
    success_url = reverse_lazy('Fornecedor_list')



# Contato Views
class ContatoListView(ListView):
    model = Contato
    template_name = 'contato_list.html'
# 


class ContatoCreateView(CreateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']

    # Retorna para a página anterior usando HTTP_REFERER/mantém na página de criação
    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER')




class ContatoUpdateView(UpdateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']
    success_url = reverse_lazy('contato_list')

class ContatoDeleteView(DeleteView):
    model = Contato
    success_url = reverse_lazy('contato_list')

# Produto Views
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto_list')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco', 'fornecedor']
    success_url = reverse_lazy('produto_list')

class ProdutoDeleteView(DeleteView):
    model = Produto
    success_url = reverse_lazy('produto_list')
    
    
    
    # views.py

# views.py

from django.views.generic import DetailView
from .models import Fornecedor

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
