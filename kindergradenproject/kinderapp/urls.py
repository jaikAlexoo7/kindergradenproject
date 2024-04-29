from django.urls import path
from kinderapp import views

app_name = "bodyandmind"
urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.home,name="home"),
    path('lessons/<int:p>',views.lessons,name="lessons"),
    path('register1',views.register1,name="register1"),
    path('register2',views.register2,name="register2"),
    path('insert/<int:p>',views.insert,name="insert"),
    path('edit/<int:p>',views.edit1,name="edit1"),
    path('edit2/<int:p>',views.edit2,name="edit2"),
    path('login',views.qlogin,name="qlogin"),
    path('logout',views.qlogout,name="qlogout"),
    path('mail/<int:p>',views.mailto,name="mailto"),
    path('enlarge/<int:p>',views.enlarge,name="enlarge"),
    path('rating/<int:p>',views.rating,name='rating'),
    path('video/',views.video,name='video'),
    path('audio/',views.audio,name='audio'),
    path('likes/<p>',views.like,name='like'),
    path('comment/<p>',views.comment,name='comment'),
    path('payment',views.payment,name="payment")

]