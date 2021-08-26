from django.urls import path,include
from . import views
from rest_framework import routers

# modelviewsets need routers
router = routers.SimpleRouter()
# register the routers
router.register("categories",views.CategoryModelViewSet,basename="category")
router.register("transactions",views.TransactionModelViewSet,basename="transaction")

urlpatterns =[
    path("",views.CurrencyListAPiView.as_view(),name="currency"),
    path('api/', include(router.urls)),
]