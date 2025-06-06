from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('products/',views.product_list),
    # path('products/info/',views.product_info),
    # path('products/<int:pk>',views.product_detail),
    # path('orders/',views.order_list),

    path('products/',views.ProductListCreateAPIView.as_view()),
    path('products/info/',views.ProductInfoAPIView.as_view()),
    path('products/<int:product_id>',views.ProductDetailView.as_view()),
    # path('orders/',views.OrderListAPIView.as_view()),

    # path('user-orders/',views.UserOrderListAPIView.as_view(),name='user-orders'),
]

router = DefaultRouter()
router.register('orders', views.OrderViewSet)
urlpatterns += router.urls