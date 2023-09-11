from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('autenticar/', include('autenticar.urls')),

]
#vai procurar no array o que eu fizer na aplicação algum request na app
#vai entrar direto e procurar la 