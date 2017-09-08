from django.shortcuts import render,redirect
import random
import json
import datetime
from django.utils import timezone
from .models import Question,Submission,connection
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

numberofplayers = 4

# Create your views here.
@login_required
def home(request):
	user=request.user.username
	obj=Submission.objects.filter(username=user).order_by('-created_at')
	return render(request, 'home.html',{'Tasks':obj})

@login_required
def checking(request):
	global numberofplayers
	if request.method=="POST":
		req=request.POST
		con=req.get('con')
		que=json.loads(req.get('que'))
		ans=json.loads(req.get('ans'))
		minutes = json.loads(req.get('min'))
		seconds = json.loads(req.get('sec'))
		obj1=Submission.objects.create(username=request.user.username,que1=que[0],que2=que[1],que3=que[2],que4=que[3],que5=que[4],ans1=ans[0],ans2=ans[1],ans3=ans[2],ans4=ans[3],ans5=ans[4],conn=con,state=1)
		obj1.save()
		x=datetime.datetime.now()
		x=x.replace(microsecond=0,hour=0)
		x=x.replace(minute=minutes[0],second=seconds[0])
		obj1.time1=x.time()
		x=x.replace(minute=minutes[1],second=seconds[1])
		obj1.time2=x.time()
		x=x.replace(minute=minutes[2],second=seconds[2])
		obj1.time3=x.time()
		x=x.replace(minute=minutes[3],second=seconds[3])
		obj1.time4=x.time()
		x=x.replace(minute=minutes[4],second=seconds[4])
		obj1.time5=x.time()
		obj1.save()
		print(con)
		if con==-1 or con=='-1':
			obj1.state=0
			obj1.save()
		else :
			obj2=Submission.objects.get(id=con)
			if obj2.Sub<numberofplayers:
				obj2.Sub+=1
				obj2.save()
				connect = connection.objects.create(submission1=con,submission2=obj1.id)
				connect.save()
				if obj2.Sub==numberofplayers:
					matching_process(con)
			else :
				obj1.state=0
				obj1.save()
		return redirect("/")

def matching_process(con):
	list_of_pair_ids = connection.objects.filter(submission1=con)
	listofsubmissions = []
	obj=Submission.objects.get(id=con)
	for x in list_of_pair_ids:
		listofsubmissions.append(Submission.objects.get(id=x.submission2))
	score=0
	if all([x.ans1==obj.ans1 for x in listofsubmissions]):
		score+=1
	if all([x.ans2==obj.ans2 for x in listofsubmissions]):
		score+=1
	if all([x.ans3==obj.ans3 for x in listofsubmissions]):
		score+=1
	if all([x.ans4==obj.ans4 for x in listofsubmissions]):
		score+=1
	if all([x.ans5==obj.ans5 for x in listofsubmissions]):
		score+=1
	print(score)
	print("matching")
	listofsubmissions.append(obj)
	for x in listofsubmissions:
		x.score=score
		x.state=2
		x.save()
		player1=User.objects.get(username=x.username)
		player1.profile.coins+=score
		player1.save()





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
	global numberofplayers
	objects = Submission.objects.filter(state=0)
	flag=0
	for obj in objects:
		print (obj.state)
		if obj.peers<numberofplayers:
			a=[obj.que1,obj.que2,obj.que3,obj.que4,obj.que5,obj.id]
			obj.conn_at=timezone.now()
			obj.peers+=1
			obj.save()
			flag=1
			return a
		else:
			a=obj.conn_at
			b=timezone.now()
			c=b-a
			minutes,seconds=divmod(c.days*86400 + c.seconds,60)
			if minutes > 30:
				li =[obj.que1,obj.que2,obj.que3,obj.que4,obj.que5,obj.id]
				obj.conn_at=timezone.now()
				obj.save()
				flag=1
				return li
	if flag==0:
		a=random.sample(range(1,16),5)
		a.append(-1)
		return a



