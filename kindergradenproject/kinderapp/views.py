from django.shortcuts import render, redirect
from django.core.mail import send_mail
from kinderapp.models import CustomUser, Postupload, values, Rating, saw
from django.core.mail import EmailMessage
from django.conf import settings
import json

# Create your views here.
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):
    return render(request, 'content.html')


def home(request):
    v = values.objects.all()
    p = {}
    for i in v:
        v1 = values.objects.get(numberss=i.numberss)
        w = Postupload.objects.filter(pv=v1, vari='NOT VARIFIED')
        o = 0
        for b in w:
            o = o + 1
        v1.g = o
        v1.save()
    v = values.objects.all()
    return render(request, 'home.html', {'v': v, 'l': p})


# for user interface
def lessons(request, p):
    k = Postupload.objects.filter(vari='VARIFIED', pv__id=p)

    for i in k:
        try:
            k12 = saw.objects.get(user__username = request.user.username, pos=i)
        except:
            # If the object does not exist, create a new one
            k12 = saw.objects.create(user=request.user, pos=i, isseen="not_seen", colors="#FA7070")
            k12.save()

    try:
      b7 = 0
      g8 = 0
      for g in k:
            g8 = g8 + 1

      k1 = saw.objects.filter(user=request.user,pos__pv__id =p)
      for j in k1:
            if j.isseen == "true":
                b7 = b7 + 1

      g8 = g8 - b7

    except:
         b7 = 0
         g8 = 0
         for g in k:
             g8 = g8 + 1

    data = {
        'seen': b7,
        'not_seen': g8
    }
    serialized_data = json.dumps(data)
    k = Postupload.objects.filter(vari='VARIFIED', pv__id=p)

    k2 = saw.objects.filter(user=request.user,pos__pv__id=p)

    b = request.user.username

    return render(request, 'contentsinside.html',
                  {'k': k, 'b': b, 'serialized_data': serialized_data, 'data': data, 'l': k2})


def edit1(request, p):
    h = Postupload.objects.filter(vari="NOT VARIFIED", pv=p)
    m = 0
    for i in h:
        m = m + 1
    return render(request, 'editcontent.html', {'k': h, 'm': m})


def edit2(request, p):
    b = Postupload.objects.get(yourprimarykeyfield=p)
    b.vari = "VARIFIED"
    b.save()
    s = b.pv
    h = Postupload.objects.filter(vari="NOT VARIFIED", pv=s)
    m = 0
    for i in h:
        m = m + 1
    return render(request, 'editcontent.html', {'k': h, 'm': m})


import random


def register1(request):
    v9 = CustomUser.objects.all()
    m = ""
    global k
    k = random.randint(1000, 9999)
    subject = "conformation email"
    message = "enter this conformation code in the box" + " " + str(k)
    sender = 'ariseforcivicsense@gmail.com'
    if (request.method == "POST"):
        global l, u, p, p1, e, f
        l = request.POST['c']
        recipient = [l]
        send_mail(subject, message, sender, recipient)
        u = request.POST['u']

        for i in v9:
            if i.username == u:
                m = "Username is taken"
                return render(request, 'register.html', {"m": m})
            else:
                m = ""
                p = request.POST['p']
                p1 = request.POST['p1']
                e = request.POST['f']
                f = request.POST['l']
                return render(request, 'register2.html')
    return render(request, 'register.html', {"m": m})


def register2(request):
    if (request.method == "POST"):
        k1 = int(request.POST['g'])
        if k1 == k and p == p1:
            u1 = CustomUser.objects.create_user(username=u, password=p, first_name=e, last_name=f, email=l)
            u1.save()
            return redirect("bodyandmind:qlogin")
        else:
            return render(request, 'register.html')

    return render(request, 'register2.html')


def qlogin(request):
    m = ""
    if request.method == "POST":
        u4 = request.POST['u']
        p4 = request.POST['p']
        user = authenticate(username=u4, password=p4)
        if user:
            login(request, user)
            return home(request)
        elif user and user.is_editor == True:
            login(request, user)
            return home(request)
        elif user and user.is_contributer == True:
            login(request, user)
            return home(request)
        else:
            m = "wrong password or username"
    return render(request, 'login.html', {'m': m})


# for contributers
def insert(request, p):
    h = values.objects.get(id=p)
    if request.method == "POST":
        try:
            a = request.FILES['a']

        except:
            a = None

        try:
            b = request.FILES['b']
        except:
            b = None

        try:
            c = request.FILES['c']
        except:
            c = None

        if a == None and b == None and c == None:
            pass
        else:
            u5 = Postupload.objects.create(video=a, audio=b, pv=h, image=c, uploader=request.user)
            u5.save()

    m = Postupload.objects.filter(vari="NOT VARIFIED", pv=h)
    return render(request, 'contentinsideforcontributers.html', {'m': m})


def qlogout(request):
    logout(request)
    return index(request)


def mailto(request, p):
    element = Postupload.objects.get(yourprimarykeyfield=p)
    mail_to = element.uploader.email
    file_data = ""
    file_name = ""
    content_type = ""
    mail = ""
    if element.image:
        file_data = element.image.read()
        file_name = element.image.name
        content_type = 'image/jpeg'  # Set the appropriate content type for images
        file_extension = file_name.split('.')[-1]
        if file_extension.lower() == 'png':
            content_type = 'image/png'
        elif file_extension.lower() == 'gif':
            content_type = 'image/gif'

    # Check if the file field contains a video
    elif element.video:
        file_data = element.video.read()
        file_name = element.video.name
        content_type = 'video/mp4'  # Set the appropriate content type for videos

    # Check if the file field contains an audio
    elif element.audio:
        file_data = element.audio.read()
        file_name = element.audio.name
        content_type = 'audio/mpeg'  # Set the appropriate content type for audio
    if request.method == 'POST':
        s = request.POST['s']
        m = request.POST['m']
        # Create an email message object
        email = EmailMessage(
            subject=s,
            body=m,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[mail_to],  # Replace with the recipient's email address
        )

        # Attach the file to the email
        email.attach(file_name, file_data, content_type)
        # Send email
        email.send()
        mail = "mail send"
    return render(request, 'emailsending.html', {'element': element, "mail": mail})


def enlarge(request, p):

    global post7
    post7 = Postupload.objects.get(yourprimarykeyfield=p)

    global g
    g = post7.yourprimarykeyfield

    if post7.video:
        pass
    elif post7.audio:
        pass
    else:
            s = saw.objects.get(pos=post7, user=request.user)
            s.isseen = "true"
            s.colors = "#4B61D1"
            s.save()





    try:
        f = Rating.objects.filter(post=post7, rating=1)
        m = 0
        for i in f:
            m = m + 1
    except:
        m = 0

    try:
        f = Rating.objects.filter(post=post7)
    except:
        f = None

    return render(request, 'enlargeimgvideoaudio.html', {'post': post7, 'r': m, 'm1': f})


def video(request):
    post3 = ""
    if request.method == "POST":
        my_received_value = request.POST.get('signal', None)
        if my_received_value is not None:
            post1 = Postupload.objects.get(yourprimarykeyfield=g)
            s = saw.objects.get(pos=post1, user=request.user, isseen="not_seen")
            s.isseen = "true"
            s.colors = "#4B61D1"
            s.save()

            post3 = post7
    return render(request, 'enlargeimgvideoaudio.html', {'post': post3})


def audio(request):
    post4 = ""
    if request.method == "POST":
        my_received_value = request.POST.get('signal', None)
        if my_received_value is not None:
            post1 = Postupload.objects.get(yourprimarykeyfield=g)

            s = saw.objects.get(pos=post1, user=request.user, isseen="not_seen")
            s.isseen = "true"
            s.colors = "#4B61D1"
            s.save()
            post4 = post7
    return render(request, 'enlargeimgvideoaudio.html', {'post': post4})


def rating(request):
    pass


def like(request, p):
    m = ""
    post1 = Postupload.objects.get(yourprimarykeyfield=p)
    try:
        try:
            f = Rating.objects.get(post=post1, user=request.user, rating=0)
            f.rating = 1
            f.save()
            j = 0
            f1 = Rating.objects.filter(post=post1, rating=1)
            for i in f1:
                j = j + 1
            try:
                g10 = Rating.objects.filter(post=post1)
            except:
                g10 = ""

            return render(request, 'enlargeimgvideoaudio.html', {'post': post1, 'r': j, 'm': m, 'm1': g10})
        except:
            f = Rating.objects.get(post=post1, rating=1, user=request.user)
            f.save()
            j = 0
            f1 = Rating.objects.filter(post=post1, rating=1)
            for i in f1:
                j = j + 1
                m = "your like is already counted"
            try:
                g10 = Rating.objects.filter(post=post1)
            except:
                g10 = ""

            return render(request, 'enlargeimgvideoaudio.html', {'post': post1, 'r': j, 'm': m, 'm1': g10})
    except:
        f = Rating.objects.create(post=post1, rating=1, user=request.user)
        f.save()
        j = 0
        f1 = Rating.objects.filter(post=post1, rating=1)
        for i in f1:
            j = j + 1
        m = ""
        try:
            g10 = Rating.objects.filter(post=post1)
        except:
            g10 = ""

        return render(request, 'enlargeimgvideoaudio.html', {'post': post1, 'r': j, 'm': m, 'm1': g10})


def comment(request, p):
    post1 = Postupload.objects.get(yourprimarykeyfield=p)
    if request.method == "POST":
        n = request.POST['n']
        try:
            f10 = Rating.objects.get(post=post1, user=request.user)
            f10.comments = n
            f10.save()

        except:
            f10 = Rating.objects.create(post=post1, comments=n, user=request.user)
            f10.save()
    try:
        g10 = Rating.objects.filter(post=post1)
    except:
        g10 = ""
    try:
        j = 0
        f1 = Rating.objects.filter(post=post1, rating=1)
        for i in f1:
            j = j + 1
    except:
        j = 0

    return render(request, 'enlargeimgvideoaudio.html', {'post': post1, 'r': j, 'm1': g10})

def payment(request):
    return render(request,'payment.html')
