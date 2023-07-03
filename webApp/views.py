from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
from .forms import CreateTag
from .models import Tag
from .yahoo_query import financial_analysis as fn

# Create your views here.
def data_ordering(request):
    if request.method == 'POST':
        filter_selected = json.loads(request.body)
        tags_tuples = db_tags.consult_all_tags_saved().values_list()
        tags = []
        for tup in tags_tuples:
            tags.append(tup[1])
        financial_data_tags = Aux.t
        columns = financial_data_tags[0]
        index = columns.index(filter_selected[0:-1])
        if filter_selected[-1] == "s":
            for i in range(1, len(financial_data_tags)):
                for j in range(i + 1, len(financial_data_tags)):
                    if (float(financial_data_tags[j][index]) > float(financial_data_tags[i][index])):
                        financial_data_tags[i], financial_data_tags[j] = financial_data_tags[j], financial_data_tags[i]
            
        elif filter_selected[-1] == "i":
            for i in range(1, len(financial_data_tags)):
                for j in range(i + 1, len(financial_data_tags)):
                    if (float(financial_data_tags[j][index]) < float(financial_data_tags[i][index])):
                        financial_data_tags[i], financial_data_tags[j] = financial_data_tags[j], financial_data_tags[i]      
        
        Aux.t = financial_data_tags

    return(redirect("home", permanent=True))     

def delete_tag(request):
    if request.method == 'POST':
        tag_names = json.loads(request.body)
        for tag_name in tag_names:
            db_tags.delete_tag(db_tags.consult_tags_by_filter(tag_name))

    return(redirect("home", permanent=True))   

def create_tag(request):
        inserted_name = str(request.POST.get("nombre")).upper()
        tags_tuples = db_tags.consult_all_tags_saved().values_list()
        tags = []
        for tup in tags_tuples:
            tags.append(tup[1])
        if((len(Aux.t) - 1) == 0 or (len(Aux.t) - 1 != len(tags))):
            financial_data_tags = fn.financeAnalisis((tags))
            for j in range(0, len(financial_data_tags)):
                for i in range(0, len(financial_data_tags[j])):
                    if type(financial_data_tags[j][i]) == float:
                        financial_data_tags[j][i] = round(financial_data_tags[j][i], 3)
            Aux.t = financial_data_tags
        else:
            financial_data_tags = Aux.t
        form = CreateTag(request.POST)
        if inserted_name is None or inserted_name ==  "Formato erróneo, inténtelo de nuevo":
            inserted_name = ""
        if(request.method == "POST"):
            if(len(inserted_name) == str(inserted_name).count(" ") or str(inserted_name).count(" ") > len(str(inserted_name))//2):
                initial_data = {'nombre': "Formato erróneo, inténtelo de nuevo"}
                return render(request, "create_tag.html", {'form':CreateTag(initial=initial_data), "headers_title_list":financial_data_tags[0], "financial_data_tags":financial_data_tags[1:], 'len_tags':len(tags), 'comprobation_create_tag':True})
            elif(len(inserted_name) <= 6):
                for tuple in list(tags_tuples):
                    if(inserted_name.lower() in str(tuple[1]).lower()):
                        if(form.is_valid()):
                            nombre_form = form.cleaned_data['nombre']
                            initial_data = {'nombre': nombre_form}
                        else:
                            initial_data = {'nombre': "Formato erróneo, inténtelo de nuevo"}
                        return render(request, "create_tag.html", {'form':CreateTag(initial=initial_data), "headers_title_list":financial_data_tags[0], "financial_data_tags":financial_data_tags[1:], 'len_tags':len(tags), 'comprobation_create_tag':True})
                db_tags.create_new_tag(inserted_name)
            elif(len(inserted_name) > 6):
                names_unfixed = list(inserted_name)
                names_fixed = []
                if(names_unfixed[-1] != ","):
                    names_unfixed.append(",")
                while True:
                    for w in names_unfixed:
                        if(w == ","):
                            conf = True
                            index = names_unfixed.index(w)
                            names_fixed = names_unfixed[0 : index]
                            del names_unfixed[0 : index + 2]
                            for tuple in list(tags_tuples):
                                if("".join(names_fixed) in tuple[1]):
                                    conf = False
                            if(conf and str(names_fixed).count(" ") != len(str(names_fixed))):
                                db_tags.create_new_tag("".join(names_fixed))
                            names_fixed = []
                    if(len(names_unfixed) == 0):
                        break
            return redirect('/create_tag/')
        else:
            return render(request, "create_tag.html", {'form':CreateTag(), "headers_title_list":financial_data_tags[0], "financial_data_tags":financial_data_tags[1:], 'len_tags':len(tags), 'comprobation_create_tag':False})

def home(request):
    tags_tuples = db_tags.consult_all_tags_saved().values_list()
    tags = []
    for tup in tags_tuples:
        tags.append(tup[1])
    if((len(Aux.t) - 1) == 0 or (len(Aux.t) - 1 != len(tags))):
        financial_data_tags = fn.financeAnalisis((tags))
        for j in range(0, len(financial_data_tags)):
            for i in range(0, len(financial_data_tags[j])):
                if type(financial_data_tags[j][i]) == float:
                    financial_data_tags[j][i] = round(financial_data_tags[j][i], 3)
        Aux.t = financial_data_tags
    else:
        financial_data_tags = Aux.t

    return(render(request, "home.html", {"headers_title_list":financial_data_tags[0], "financial_data_tags":financial_data_tags[1:], 'len_tags':len(tags)}))

class Database_Tags():
    def consult_all_tags_saved(self):
        return(Tag.objects.using('data_tags_db').all())
    def create_new_tag(self, name):
        Tag.objects.using('data_tags_db').create(nombre = name)
    def consult_tags_by_filter(self, filter):
        return(Tag.objects.using('data_tags_db').filter(nombre = filter))
    def delete_tag(self, queryset):
        queryset.delete()

class Aux():
    t = []

db_tags = Database_Tags()