from .views import StudentList,AllUser
from rest_framework.routers import SimpleRouter
app_name='api'
router=SimpleRouter()
router.register('user',AllUser,basename='user')
router.register('student',StudentList,basename='student')
urlpatterns=router.urls
