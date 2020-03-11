from django.shortcuts import render, redirect


def index(request):
    return redirect('comment:hello1')


def hello1(request):
    context = {
        "name": "주혜민",
        "age": 20,
    }
    return render(request, "comment/hello1.html", context)


def hello2(request):
    if request.method == "GET":
        value = request.GET.get('whatisyourname')

        context = {
            "message": f"GET 요청이 왔습니다. <br/> 필드 값 : {value}",
        }

        return render(request, "comment/hello2.html", context)

    elif request.method == "POST":
        city = request.POST.get('city')

        context = {
            "message": f"POST 요청이 왔습니다. <br/> 도시 이름 : {city}",
        }

        return render(request, "comment/hello2.html", context)
