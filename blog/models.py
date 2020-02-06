from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model): 
#Post es un objeto, siempre el nombre inicia en mayuscula
#models.Model -> modelo de Django
#a continuacion se definen propiedades
	author=models.ForeignKey('auth.User',on_delete=models.CASCADE) #ForeingKey= link con otro modelo
	title=models.CharField(max_length=200) #CharField= # limitado de caracteres
	text=models.TextField()#TextField= texto largo sin limites
	created_date=models.DateTimeField(
		default=timezone.now) #DataTime...= fecha y hora
	published_date=models.DateTimeField(blank=True, null=True)
	def publish(self): #metodo
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title
		
class Comment(models.Model):
	post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	approved_comment = models.BooleanField(default=False)
	def approve(self):
		self.approved_comment = True
		self.save()
	def __str__(self):
		return self.text