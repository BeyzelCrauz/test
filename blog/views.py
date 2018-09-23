from django.shortcuts import render
from django.utils import timezone
from .models import Post, Flat


def post_list(request, ):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts[:4], })


def blog(request,):
    post = Post.objects.all()
    return render(request, 'blog/blog.html', {'post': post, })

def flats(request,):
    flat = Flat.objects.all()
    return render(request, 'blog/flatsShort.html', {'flat': flat, })


def blog_post(request, idef):
    post = Post.objects.filter(identif=idef)
    return render(request, 'blog/blog_item.html', {'post': post, })

#def flat_short(request, type, district, ):
#    post = Flat.objects.filter(type_Flat_Land=type,district=district, )
 #

#def flat_buy (request, type, district, startPrice, endPrice, rooms, sqs, sqe, lsqs, lsqe, ksqs, ksqe, fs, fe, fss, fse, es, ee, house_type, house_material ):
 #   flats = Flat.objects.filter(type_Flat_Land=type,district=district, price__range=(startPrice, endPrice), room__range=(rooms, 1024),
 #                               square__range=(sqs,sqe), live_square__range=(lsqs,lsqe), kitchen_square__range=(ksqs,ksqe), floor__range=(fs,fe), floors__range=(fss,fse), year__range=(es,ee), house_type=(house_type),house_material=(house_material) )
  #  return render(request, 'blog/flats.html', {'flats': flats})


def flat (request, idef):
    flat = Flat.objects.filter(idef=idef)
    return render(request, 'blog/flat.html', {'flat': flat})