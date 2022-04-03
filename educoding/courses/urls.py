from django.urls import path
from django.urls import include
from courses.views import CoursesHub, CourseInstruct, SectorGroupingCourse

# EduCoding Routing schema

urlpatterns = [
    #indexpage endpoint route
    path('', CoursesHub.as_view()),
    #informatie per cursus endpoint route
    path('information/<uuid:courseUUID>/', CourseInstruct.as_view()),
    #cursussen in sectoren ophalen endpoint route (Course Lijst)
    path('<uuid:sectorUUID>/', SectorGroupingCourse.as_view()),
    # search functie van course lijst endpoint
    path('search/<str:searchWords_lookup_from_q>/', SearchCourse.as_view())
]
