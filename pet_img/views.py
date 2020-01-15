from django.shortcuts import render

def post_list(request):
    return render(request, 'pet_img/post_list.html', {})

