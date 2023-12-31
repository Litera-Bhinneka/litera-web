import json
from django.shortcuts import render, get_object_or_404
from review.models import Review
from catalog.models import Book
from manage_user.models import Wishlist
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from review.forms import ReviewForm
from django.urls import reverse
from django.core import serializers
from review.forms import ReviewForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_review(request):
    reviews = Review.objects.all().values()
    context = {
        'reviews': reviews,
    }

    return render(request, "show_review.html", context)

@login_required(login_url='/authentication/login/')
def see_book_review(request, id):
    book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book_title=book.title).order_by('-review_date')
    wishlist = Wishlist.objects.filter(user=request.user, book=book)

    context = {
        'book': book,
        'reviews': reviews,
        'name': request.user.username,
        'form': ReviewForm,
        'wishlist': wishlist,
        'stars': (1,2,3,4,5)
    }

    return render(request, "book_review.html", context)


def add_review(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        review = form.save(commit=False)
        review.reviewer_name = request.user.username 
        review.save()
        return HttpResponseRedirect(reverse('review:show_review'))

    context = {'form': form, 'name':request.user.username}
    return render(request, "add_review.html", context)


def get_review_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    review_item = Review.objects.filter(book_title=book.title).order_by('-review_date')
    return HttpResponse(serializers.serialize('json', review_item))


def get_book_json(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return HttpResponse(serializers.serialize('json', [book]))

def get_wishlist_json(request, book_id):
    wishlist = Wishlist.objects.filter(user=request.user, book=book_id)
    return HttpResponse(serializers.serialize('json', wishlist))


@csrf_exempt
def add_review_ajax(request, book_id1, book_id2):
    print(f"ini request {request}")
    print(request.POST)
    if request.method == 'POST':
        review_text = request.POST.get("review_text")
        review_summary = request.POST.get("review_summary")
        reviewer_name = request.user.username
        rating = int(request.POST.get("review_score"))
        book_title = get_object_or_404(Book, pk=book_id2).title

        new_review = Review(book_title=book_title,
                             reviewer_name=reviewer_name, 
                             review_score=rating,
                             review_summary=review_summary,
                             review_text=review_text)
        new_review.save()

        return HttpResponse(b"CREATED", status=201)
    print(request.method)

    return HttpResponseNotFound()


@csrf_exempt
def add_review_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_review = Review(book_title=data["book_title"],
                             reviewer_name=data["reviewer_name"], 
                             review_score=data["review_score"],
                             review_summary=data["review_summary"],
                             review_text=data["review_text"])
        new_review.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    

@csrf_exempt
def delete_object(request, object_id):
    try:
        obj = Review.objects.get(pk=object_id)
        obj.delete()
        return JsonResponse({'message': 'Object deleted successfully'})
    except Review.DoesNotExist:
        return JsonResponse({'error': 'Object not found'}, status=404)
