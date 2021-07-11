"""backend_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from dj_rest_auth.registration.views import VerifyEmailView, SocialLoginView


from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter




class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:5500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-auth/', include('dj_rest_auth.urls')),
    #url(r"^rest-auth/registration/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$", VerifyEmailView.as_view(), name="account_confirm_email"),
    path('rest-auth/registration/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    #path('rest-auth/', include('allauth.urls')),
    url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login')
]
