from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnterpriseViewSet, EnterpriseMembershipViewSet, CarViewSet, PhoneNumberViewSet, UserProfileViewSet, \
    get_user_info

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet, basename='user-profile')
router.register(r'enterprises', EnterpriseViewSet)
router.register(r'enterprise-memberships', EnterpriseMembershipViewSet, basename='enterprise-membership')
router.register(r'cars', CarViewSet)
router.register(r'phone-numbers', PhoneNumberViewSet, basename='phone-number')

urlpatterns = [
    path('', include(router.urls)),
    # path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path("user/", get_user_info, name="user-info"),
]
