"""hamsterserv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from hamsterserv.admin import hamster_admin, suir_admin
from suir.views import *

urlpatterns = [
    path('hamster-admin/', hamster_admin.urls),
    path('hamster/', include('hamster.urls')),
    path('suir-admin/', suir_admin.urls),
    #path('suir/', include('suir.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', InicioView.as_view(), name='inicio'),
    #path('login/', LoginView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('noticias/', include([
        path('', ListaPublicacionesView.as_view(tipo='noticia'), name='lista_noticias'),
        path('buscar/', ListaFiltroPublicacionesView.as_view(tipo='noticia'), name='buscar_noticias'),
        #path('nuevo/', CreatePublicacionView.as_view(tipo='noticia'), name='nueva_noticia'),
        path('<slug:slug>/', DetallePublicacionView.as_view(), name='detalle_noticia'),
        path('<slug:slug>/update/', UpdatePublicacionView.as_view(), name='update_noticia'),
        ])),
    path('informes/', include([
        path('', ListaPublicacionesView.as_view(tipo='informe'), name='lista_informes'),
        path('buscar/', ListaFiltroPublicacionesView.as_view(tipo='informe'), name='buscar_informes'),
        #path('nuevo/', CreatePublicacionView.as_view(tipo='informe'), name='nuevo_informe'),
        path('<slug:slug>/', DetallePublicacionView.as_view(), name='detalle_informe'),
        path('<slug:slug>/update/', UpdatePublicacionView.as_view(), name='update_informe'),
        ])),
    path('indicadores/', include([
        path('', ListaIndicadoresView.as_view(), name='lista_indicadores'),
        path('buscar/', ListaFiltroIndicadoresView.as_view(), name='buscar_indicadores'),
        path('<int:pk>/', DetalleIndicadorView.as_view(), name='detalle_indicador'),
        #path('<int:pk>/valor/nuevo/', ValorIndicadorView.as_view(), name='create_valor_indicador'),
        path('valor/<int:pk>/', DetalleValorView.as_view(), name='detalle_valor_indicador'),
        #path('valor/<int:pk>/update/', UpdateValorIndicadorView.as_view(), name='update_valor_indicador'),
        ])),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
