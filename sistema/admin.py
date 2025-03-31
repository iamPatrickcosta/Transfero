from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário
@admin.register(models.Usuário)
class UsuárioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','sobrenome','email','ativo',)   

@admin.register(models.Filme)
class Usuárioadmin(admin.ModelAdmin):
    list_display =  ('nome_do_filme','ano_de_lancamento','estudio','genero','sinopse','data_cadastro',)

@admin.register(models.Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nome','data_cadastro',)    