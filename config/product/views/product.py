from django.views import generic
# from django.views.generic import ListView,DetailView,TemplateView
from django.shortcuts import render
from product.models import Variant,ProductVariant,Product,ProductVariantPrice


class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context

class ListView(generic.ListView):
    queryset = ProductVariantPrice.objects.all()
    template_name = 'products/list.html'
    def get_context_data(self,*args, **kwargs):
        context = super(ListView, self).get_context_data(*args, **kwargs)
        context['ProductVariantPrice'] = ProductVariant.objects.all()
        return context

# class ProductlistView(ListView):
#    queryset = ProductVariant.objects.all()
#    template_name = 'classBasedView/list_view.html'

def list_view(request):
    ProductVariantPrice_qs = ProductVariantPrice.objects.all()
    product_qs =Product.objects.all()
    ProductVariant_qs = ProductVariant.objects.all()

    context={
        'ProductVariantPrice_qs':ProductVariantPrice_qs,
        'product_qs':product_qs,
        'ProductVariant_qs':ProductVariant_qs

    }
    return render(request,'products/list.html',context)