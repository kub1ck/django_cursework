from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

user_router = SimpleRouter()
user_router.register("users", UserViewSet)

urlpatterns = [

]

urlpatterns += user_router.urls
