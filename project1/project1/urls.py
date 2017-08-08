"""copy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app1.views import personal, order_page, extract_from_exel, correction, model_creating, register, user_login, index, available_orders
import app1.views as views

urlpatterns = [
    url(r'^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^personal/$', personal),
    #url(r'^create_order$', extract_from_exel),
    url(r'^create_order/$', extract_from_exel),
    url(r'^correction_page/$', correction),
    url(r'^done/$', views.model_creating),
    url(r'^register/$', register),
    url(r'^login/$', user_login),
    url(r'^available_orders/$', available_orders),
    url(r'^logout/$', views.user_logout),
    url(r'^upload_order_file/$', views.upload_order_file),
    url(r'^for_check/$', views.for_check),
    url(r'^results_of_checking/$', views.results_of_checking),
    url(r'^my_orders_on_checking/$', views.on_checking_orders),
    url(r'^completed_orders/$', views.completed_orders),
    url(r'^in_progress_orders/$', views.in_progress_orders),
    url(r'^apply_order/$', views.apply_order),
    url(r'^to_apply_order_list/$', views.to_apply_list),
    url(r'^set_writer/$', views.set_writer),
    url(r'^for_precheck_list/$', views.for_precheck_list),
    #url(r'^controller_comment/$', views.return_from_precheck),
    url(r'^returned_from_precheck_list/$', views.returnen_from_precheck_list),
    url(r'^create_message/$', views.create_message),
    url(r'^add_file_to_order/$', views.add_file_to_order),
    url(r'^add_final_file_to_order/$', views.upload_final_order_file),
    url(r'^personal_cabinet/$', views.writers_personal_cabinet),
    url(r'^orders_on_checking/$', views.writers_orders_on_checking),
    url(r'^done_writers_orders/$', views.done_writers_orders),
    url(r'^returned_for_revision_writers_orders/$', views.returned_for_revision_writers_orders),
    url(r'^controller_cabinet/$', views.controller_cabinet),
    url(r'^take_for_check/$', views.take_for_check),
    url(r'^(?P<number>\d+)/$', views.order_page_a),
    url(r'^(?P<number>\w+)/$', order_page),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
