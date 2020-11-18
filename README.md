# Django-Blog Project 🖥️

### Entry level Blog project using Python django framework

➡️ Python was used.\n
➡️ sqlite3 was used.
➡️ Bootstrap was used.

![](https://github.com/TAYFUN-KAYA/Django-Blog/blob/main/media/1.png)

- Can add articles
- new users can be registered
- The article can be edited
- the article can be deleted

![](https://github.com/TAYFUN-KAYA/Django-Blog/blob/main/media/4.png)

- user category can be set
- User task and group assignment can be made
- comments can be added, can be deleted


### ADDİNG CODE TO COMMENTS LİNES

TO -->> settings.py

MIDDLEWARE = [
 'django.middleware.security.SecurityMiddleware',
 'django.contrib.sessions.middleware.SessionMiddleware',
 'django.middleware.locale.LocaleMiddleware',
 'django.middleware.common.CommonMiddleware',
 'django.middleware.csrf.CsrfViewMiddleware',
 'django.contrib.auth.middleware.AuthenticationMiddleware',
 'django.contrib.messages.middleware.MessageMiddleware',
 'app_mainpage.middleware.MakdosEkleMiddleware',
 ]
 
 ### ONE MORE
 
 -- >>app_mainpage > middleware.py
 
 class MakdosEkleMiddleware(object):
 def __init__(self, get_response):
  self.get_response = get_response
 def __call__(self, request):
  response = self.get_response(request)
  response.content = response.content.decode('utf-8').replace('</html>', '<p>Makdos</p></html>')
  return response

Code can be added to comment lines 🖥️


![](https://github.com/TAYFUN-KAYA/Django-Blog/blob/main/media/resim_2020-11-18_235840.png)

### Let's not forget that the ckeditor is important for ui / ux. It is very useful for form.




