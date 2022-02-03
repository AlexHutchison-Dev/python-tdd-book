from django.shortcuts import render


def home_page(request):
    print(f"**** Request **** \n{request.POST}")
    return render(
        request, "home.html", {"new_item_text": request.POST.get("item_text", "")}
    )
