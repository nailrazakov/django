from django.shortcuts import render


# Create your views here.
def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} - e-mail: {email}\n>>>{message}")
    return render(request, 'catalog/feedback.html')


def main(request):
    return render(request, 'catalog/main.html')
