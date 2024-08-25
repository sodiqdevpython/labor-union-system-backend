from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IdCardsView, ProfessionView, EmployeView, RoleNoteView, HandicappedView, UnderAgeChildrenView, errorHandle

routerIdCardsView = DefaultRouter()
routerIdCardsView.register(r'', IdCardsView)

routerProfessionView = DefaultRouter()
routerProfessionView.register(r'', ProfessionView)

routerRoleNoteView = DefaultRouter()
routerRoleNoteView.register(r'', RoleNoteView)

routerHandicappedView = DefaultRouter()
routerHandicappedView.register(r'', HandicappedView)

routerUnderAgeChildrenView = DefaultRouter()
routerUnderAgeChildrenView.register(r'', UnderAgeChildrenView)

urlpatterns = [
    path('id-card/', include(routerIdCardsView.urls)),
    path('profession/', include(routerProfessionView.urls)),
    path('role-note/', include(routerRoleNoteView.urls)),
    path('hadicapped/', include(routerHandicappedView.urls)),
    path('under-age-children/', include(routerUnderAgeChildrenView.urls)),
    path('employe/', EmployeView.as_view()),
    path('employe/<int:id>/', EmployeView.as_view())
]
