from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from .models import Porter, CustomUser, Evaluation

def student_signin(request):
  if request.method == "POST": 
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None:
      login(request, user)
      message = "Sign in successful"
      return redirect('list-evaluation')
    else:
      message = "Invalid email or password" 
      return render(request, "user.html", {'message': message})
  return render(request, "user.html")

def admin_signin(request):
  if request.method == "POST": 
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, username=email, password=password)
    if user is not None and user.is_superuser:
      login(request, user)
      message = "Sign in successful"
      return redirect("add-student", message='Login successful')
    else:
      message = "Invalid email or password" 
      return render(request, "admin.html", {'message': message})
  return render(request, "admin.html")

@login_required(login_url='admin-login')
def add_student(request, message): 
  if not request.user.is_superuser:
    return redirect('admin-login')
  if request.method == "POST": 
    post_data = {}
    for key in request.POST.keys():
      if key != "csrfmiddlewaretoken": post_data[key] = request.POST.get(key)
    post_data['password'] = post_data["email"]
    post_data['username'] = post_data["email"]
    try:
      CustomUser.objects.create_user(**post_data)
    except IntegrityError: 
      return redirect('add-student', message="Email already exists")  
    return redirect('add-student', message="Student Created")
  return render(request, 'student.html', {'message': message})

@login_required(login_url='admin-login')
def add_porter(request):
  if not request.user.is_superuser:
    return redirect('admin-login')
  if request.method == "POST": 
    name = request.POST['name']
    image = request.FILES['image']
    hall = request.POST['hall']
    is_admin = request.POST.get('admin') == "on"
    Porter.objects.create(
      name = name, 
      hall = hall, 
      image = image, 
      is_admin = is_admin
    )
    return render(request, 'PorterFill.html', {'message': "Porter added"})
  return render(request, 'PorterFill.html')

def list_evaluation(request, message): 
  context = {
    'porters': Porter.objects.all(), 
    'message': message
  }
  return render(request, 'EvalTabs.html', context)

def evaluation(request, porter_id):
  if request.method == "POST": 
    data = get_post_data(request)
    data['student'] = request.user
    data['porter'] = Porter.objects.get(id=porter_id)
    print(data)
    Evaluation.objects.check(**data)
    return redirect('list-evaluation', message="Evaluation successful")
  return render(request, "Evaluation.html")

def get_post_data(request): 
  post_data = {}
  for key in request.POST.keys():
    if key != "csrfmiddlewaretoken": post_data[key] = request.POST.get(key)
  return post_data

def logout_user(request): 
  logout(request)
  return redirect('student-login')


# apis
# class SignUpView(APIView):
#   def post(self, request):
#     user_serializer = UserSerializer(data=request.data)
#     user_serializer.is_valid(raise_exception=True)
#     if user_serializer.is_valid():
#       user = user_serializer.save()
#       token, created = Token.objects.get_or_create(user=user)
#       serializer = CustomTokenSerializer(data={'token': token.key, 'user': UserSerializer(user).data})
#       serializer.is_valid()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)

# class SignInView(APIView):
#   permission_classes = [AllowAny]

#   def post(self, request):
#     serializer = LoginSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
#       if user:
#         token, created = Token.objects.get_or_create(user=user)
#         serializer = CustomTokenSerializer(data={'token': token.key, 'user': UserSerializer(user).data})
#         serializer.is_valid()
#         return Response(serializer.data)
#       else: 
#         return Response("Wrong username or password", status=400)
      
# class GradeView(APIView): 
#   permission_classes = [IsAuthenticated, IsStudent]
  
#   def post(self, request): 
#     grade_serializer = GradeSerializer(data=request.data)
#     grade_serializer.is_valid(raise_exception=True)
#     grade_serializer.save()
#     return Response(grade_serializer.data)
  