from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# In django these are called views but they act as controllers
def index(request):
  return HttpResponse('<h1>Its a cat collector</h1>')

def about(request):
  lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a lorem non elit interdum congue ut vitae nibh. Nam maximus laoreet dui, hendrerit auctor ex convallis faucibus. Morbi posuere id nulla vitae facilisis. Morbi fermentum libero in varius malesuada. Cras condimentum lobortis neque, eu auctor dolor interdum quis. Nulla nec facilisis ante, vel efficitur nibh. Quisque venenatis augue condimentum nisi mollis rhoncus sit amet et leo.'
  return HttpResponse(lorem)