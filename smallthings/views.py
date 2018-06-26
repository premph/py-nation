from django.shortcuts import render, render_to_response, get_object_or_404 , redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,NewPost,Comments
from .forms import PostModelForm,UploadForm,RunQuery,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from smallthings.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
import json
from bs4 import BeautifulSoup
import urllib.request
import json
import os.path
#from aylienapiclient import textapi
#import django.contrib.auth.views.login



# Create your views here.
master_res = dict()
master_pp = dict()
response =[]


def soupthis(url):
    
    webdata = urllib.request.urlopen(url)
    soup = BeautifulSoup(webdata,"html.parser")
    return soup

def content(url):
    para = dict()
    newurl = url
    newsoup = soupthis(newurl)
    content = newsoup.find("div",{"class":"content__article-body from-content-api js-article__body"})
    links =content.findAll("p")
    print(len(links))
    for k in range(len(links)):
        para[str(k)]=links[k]
    return para

def dictionary(results,result_size):
    
    for x in range(result_size):
        pp=dict()
        res = dict()
        res['sectionName']=results[x]['sectionName']
        res['webPublicationDate']=results[x]['webPublicationDate']
        res['webTitle']=results[x]['webTitle']
        res['webUrl']=results[x]['webUrl']
        #res['pillarName']=results[x]['pillarName']
        res['type']=results[x]['type']
        master_res[str(x)]=res
        
        if (results[x]['type']=='article'):
            print('article')
            pp = content(results[x]['webUrl'])
            master_pp[str(x)]=pp
        
        else:
            print(results[x]['type'])
        print('------')
        
    return master_res,master_pp

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../index.html')
        
    else:
        form = SignUpForm()
        
    return render(request, 'signup.html', {'form': form})


def index(request):
    return render(request,'index.html')

@login_required
def post(request,slug):
    top=NewPost.objects.filter(published=True).order_by('title')[0:4]
    allpost=NewPost.objects.filter(published=True).order_by('-created')[0]
    
    alll=NewPost.objects.filter(published=True).order_by('-created')[0]
    com = Comments.objects.order_by('-created')
    return render_to_response('post.html',{
            'post':get_object_or_404(NewPost,slug=slug),'top':top,'allpost':allpost,'com':com,'alll':alll
            })
    
def home(request):
    allpostcar = NewPost.objects.filter(published=True).order_by('-created')[0:5]
    panel = NewPost.objects.filter(published=True).order_by('-created')[0:3]
    allpost=NewPost.objects.filter(published=True).order_by('-created')[5:10]
    
    gamingcar = NewPost.objects.filter(cat='Gaming').order_by('-created')[0]
    gaming = NewPost.objects.filter(cat='Gaming').order_by('-created')[1:5]
    
    technologycar = NewPost.objects.filter(cat='Technology').order_by('-created')[0]
    technology = NewPost.objects.filter(cat='Technology').order_by('-created')[1:5]
    
    studycar = NewPost.objects.filter(cat='Study').order_by('-created')[0]
    study = NewPost.objects.filter(cat='Study').order_by('-created')[1:5]
    
    lifestylecar = NewPost.objects.filter(cat='Lifestyle').order_by('-created')[0]
    lifestyle = NewPost.objects.filter(cat='Lifestyle').order_by('-created')[1:5]
    
    #print(allpost)
    
    top=NewPost.objects.filter(published=True).order_by('title')[0:4]
    
    return render(request, 'index.html',{'lifestyle':lifestyle,'gaming':gaming,'technology':technology,'allpost':allpost,'study':study,
                                         'top':top,'allpostcar':allpostcar,'gamingcar':gamingcar,'technologycar':technologycar,
                                         'studycar':studycar,'lifestylecar':lifestylecar,'panel':panel})


def catg(request):
   
    allpost=NewPost.objects.filter(published=True).order_by('-created')
    gaming = NewPost.objects.filter(cat='Gaming').order_by('-created')
    technology = NewPost.objects.filter(cat='Technology').order_by('-created')
    study = NewPost.objects.filter(cat='Study').order_by('-created')
    lifestyle = NewPost.objects.filter(cat='Lifestyle').order_by('-created')
    
    top=NewPost.objects.filter(published=True).order_by('title')[0:6]
    
    return render(request, 'catagory.html',{'lifestyle':lifestyle,'gaming':gaming,'technology':technology,'allpost':allpost,'study':study,
                                         'top':top,})
def postp(request):
    
    return render(request,'post.html')
def pagep(request):
    return render(request,'page.html')
def newsp(request):
    return render(request,'news.html')
def newsp2(request):
    return render(request,'news2.html')
def data(request):
    return render(request,'data.html')
def comp(request):
    com  = Comments.objects.order_by('-created')
    return render(request,'comm.html',{'com':com})
def analyse(request):
    com  = Comments.objects.order_by('-created')
    fname = 'C:\\Users\\SPARTAN\\mysite\\smallthings\\templates\\results\\reviews.txt'
    #print('file name is   ',fname)
    
    f = open(fname,"w")
    for x in com:
        print('comment is  ',x.body)
        f.write(x.body+str(0))
        
    return render(request,'analyse.html',{'response':response})

def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html',{'posts':posts})
    '''return render(request, 'upload.html', {
        'form': form,
    })'''
    

#def post_new(request):
 #   form = PostForm()
 #   return render(request, 'post.html', {'form': form})

@login_required
def upload_form(request):
    if request.method == 'GET':
        form = UploadForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = UploadForm(request.POST,request.FILES)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            #form.process()
            #m=NewPost.objects.get(pk=)
            form.title = form.cleaned_data['title']
            form.slug = form.cleaned_data['slug']
            form.summary = form.cleaned_data['summary']
            form.content = form.cleaned_data['content']
            form.published = form.cleaned_data['published']
            form.author = form.cleaned_data['author']
            form.keywords = form.cleaned_data['keywords']
            form.cat = form.cleaned_data['cat']
            form.image = form.cleaned_data['image']
            form.thumb = form.cleaned_data['thumb']
            
            post = NewPost.objects.create(title=form.title, content=form.content,slug=form.slug,summary=form.summary,published=form.published,
                                       author=form.author,cat=form.cat,keywords=form.keywords,
                                       image=form.image, thumb=form.thumb)
            
            return redirect('../index.html')
        
    
    return render(request, 'addpost.html', {
        'form': form,
    })
        
#def login(request):
    #return redirect('../../register/login.html')
  #   return render(request, 'login.html')
def Upload_comm(request):
    if request.method == 'GET':
        form = CommentForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = CommentForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            #form.process()
            #m=NewPost.objects.get(pk=)
            form.name = form.cleaned_data['name']
            form.post = form.cleaned_data['post']
            form.email = form.cleaned_data['email']
            form.body = form.cleaned_data['body']
            response.append(form.body)
            #fname = 'C:\\Users\\SPARTAN\\mysite\\smallthings\\templates\\response.txt'
            #print('file name is   ',fname)
            
            #f = open(fname,"w")

            
            p = Comments.objects.create(name=form.name, email=form.email,body=form.body,post=form.post)
            return redirect('../index.html')
        
    
    return render(request, 'comm.html', {
        'form': form,
    })
    
def people(request):
    posts = Post.objects.all()
    
    return render(request, 'people.html',{'posts':posts})


def search(request):
    if request.method == 'GET':
        form = RunQuery()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = RunQuery(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            #form.process()
            #m=NewPost.objects.get(pk=)
            query = form.cleaned_data['query']
            num = form.cleaned_data['num']
            order = form.cleaned_data['order']
            
            search =query
            order_by =order
            result_size = int(num)
            
            print(search,order_by,result_size)
            key = '20aa3bd8-063a-4088-9f68-8dc3b05cbc7c'
            
            f_search = search.replace(' ','%20')
            
            url = 'https://content.guardianapis.com/search?order-by='+order_by+'&page-size='+str(result_size)+'&q='+f_search+'&api-key='+key
            print(url)
            data = json.loads(soupthis(url).prettify())
            
            res = dict()
            pp=dict()
            dd=dict()
                        
            results = data['response']['results']
            #print('type of results',type(results))
            
            r,p = dictionary(results,result_size)
            
            print(r)
            print(p)

            for x in r.values():
                dd=dict(x)
                print('dd      ',dd)
                #print('dd',dd)
            
            for x in p.values():
                pp=dict(x)
                print('pp       ',pp)
            
            fname = 'C:\\Users\\SPARTAN\\mysite\\smallthings\\templates\\results\\data.html'
            print('file name is   ',fname)
            
            f = open(fname,"w")
            
            for x in pp.values():
                f.write(str(x))
            f.close()
            
            
 
  
            
            
            return render(request, 'news2.html',{'dd':dd,'keys':dd.items(),
                                                 'pp':pp,'keyp':pp.items()})
        
    
    return render(request, 'news.html')
