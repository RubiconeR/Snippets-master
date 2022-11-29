from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index_page, name="home"),
                  path('snippets/add', views.add_snippet_page, name="snippets-add"),
                  path('snippets/list', views.snippets_page, name="snippets-list"),
                  path('snippet/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
                  path('snippet/<int:snippet_id>/delete/', views.snippet_delete, name="snippet-delete"),
                  path('login', views.login_page, name='login'),
                  path('logout', views.logout_page, name='logout'),
                  path('registration', views.registration, name='registration'),
                  path('comment/add', views.comment_add, name="comment_add"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)