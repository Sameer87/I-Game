from django.shortcuts import render,redirect
import random
import json
from django.utils import timezone
from .models import Question,Submission
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	user=request.user.username
	obj=Submission.objects.filter(username=user).order_by('-created_at')
	return render(request, 'home.html',{'Tasks':obj})

@login_required
def checking(request):
	if request.method=="POST":
		req=request.POST
		con=req.get('con')
		que=json.loads(req.get('que'))
		ans=json.loads(req.get('ans'))
		obj1=Submission.objects.create(username=request.user.username,que1=que[0],que2=que[1],que3=que[2],que4=que[3],que5=que[4],ans1=ans[0],ans2=ans[1],ans3=ans[2],ans4=ans[3],ans5=ans[4],conn=con,state=2)
		obj1.save()
		print(con)
		if con==-1 or con=='-1':
			obj1.state=0
			obj1.save()
		else :
			obj2=Submission.objects.get(id=con)
			if obj2.state==1:
				obj2.state=2
				obj2.save()
				matching(obj1,obj2)
			else :
				obj1.state=0
				obj1.save()
		return redirect("/")



@login_required
def Game_view(request):
	if request.method=="GET":
		x=get_questions()
		a=[]
		for i in range(5):
			a.append(Question.objects.get(id=x[i]))
		con=x[5]
		return render(request,'game.html',{'que':a,'con':con})



def matching(obj1,obj2):
	x=0
	if obj1.ans1==obj2.ans1:
		x+=1
	if obj1.ans2==obj2.ans2:
		x+=1
	if obj1.ans3==obj2.ans3:
		x+=1
	if obj1.ans4==obj2.ans4:
		x+=1
	if obj1.ans5==obj2.ans5:
		x+=1
	obj1.score=obj2.score=x
	player1=User.objects.get(username=obj1.username)
	player1.profile.coins+=x
	player1.save()
	player2=User.objects.get(username=obj2.username)
	player2.profile.coins+=x
	player2.save()
	obj1.save()
	obj2.save()

def get_questions():
	objects = Submission.objects.all()
	flag=0
	for obj in objects:
		print (obj.state)
		if obj.state==0:
			a=[obj.que1,obj.que2,obj.que3,obj.que4,obj.que5,obj.id]
			obj.conn_at=timezone.now()
			obj.state=1
			obj.save()
			flag=1
			return a
		elif obj.state==1:
			a=obj.conn_at
			b=timezone.now()
			c=b-a
			minutes,seconds=divmod(c.days*86400 + c.seconds,60)
			if minutes > 30:
				li =[obj.que1,obj.que2,obj.que3,obj.que4,obj.que5,obj.id]
				obj.conn_at=timezone.now()
				obj.state=1
				obj.save()
				flag=1
				return li
	if flag==0:
		a=random.sample(range(1,16),5)
		a.append(-1)
		return a



