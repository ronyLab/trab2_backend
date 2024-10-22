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

class ContatoCreateView(CreateView):
    model = Contato
    fields = ['tipo', 'detalhe', 'fornecedor']
    success_url = reverse_lazy('contato_list')

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