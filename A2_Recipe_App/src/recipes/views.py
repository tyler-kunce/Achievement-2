from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .forms import RecipesSearchForm
from .utils import get_chart, get_recipename_from_id

import pandas as pd

# Create your views here.
def home(request):
    return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'

    def get(self, request, template_name):
        form = RecipesSearchForm(None)
        recipes = Recipe.objects.all()

        context = {
            'form': form,
            'recipes': recipes,
        }

        return render(request, template_name, context)
    
    def post(self, request, template_name):
        form = RecipesSearchForm(request.POST)
        recipes = Recipe.objects.all()
        recipes_df = None
        chart = None

        if request.method == 'POST':
            recipe_name = request.POST.get('recipe_name')
            chart_type = request.POST. get('chart_type')

            qs = Recipe.objects.filter(recipe__name=recipe_name)
            if qs:
                recipes_df = pd.DataFrame(qs.values())
                recipes_df['recipe_id'] = recipes_df['recipe_id'].apply(get_recipename_from_id)
                chart = get_chart(chart_type, recipes_df, labels = recipes_df['recipe_id'].values)
                recipes_df = recipes_df.to_html()

        context = {
            'form': form,
            'recipes_df': recipes_df,
            'chart': chart,
        }

        return render(request, template_name, context)
    

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/recipes_detail.html'