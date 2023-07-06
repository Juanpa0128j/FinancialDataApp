from django.shortcuts import render, redirect
import json
from .forms import CreateTag
from .models import Tag
from .yahoo_query import financial_analysis as fn


# Create your views here.
def data_ordering(request):
    if request.method == "POST":
        filter_selected = json.loads(request.body)
        columns = [
            "symbol",
            "shortName",
            "debt/Equ",
            "%Insiders",
            "Price",
            "t.Price",
            "Upside",
            "t.PE",
            "f.PE",
            "t.Eps",
            "f.Eps",
            "ROA",
            "ROE",
            "profit.M",
            "Myscore",
            "Mycount",
        ]
        index_filter = columns.index(filter_selected[0:-1])
        if filter_selected[-1] == "s":
            for i in range(0, len(Auxiliar_Class.auxiliar_table)):
                for j in range(i + 1, len(Auxiliar_Class.auxiliar_table)):
                    if (
                        Auxiliar_Class.auxiliar_table[j][index_filter]
                        > Auxiliar_Class.auxiliar_table[i][index_filter]
                    ):
                        (
                            Auxiliar_Class.auxiliar_table[i],
                            Auxiliar_Class.auxiliar_table[j],
                        ) = (
                            Auxiliar_Class.auxiliar_table[j],
                            Auxiliar_Class.auxiliar_table[i],
                        )

        elif filter_selected[-1] == "i":
            for i in range(0, len(Auxiliar_Class.auxiliar_table)):
                for j in range(i + 1, len(Auxiliar_Class.auxiliar_table)):
                    if (
                        Auxiliar_Class.auxiliar_table[j][index_filter]
                        < Auxiliar_Class.auxiliar_table[i][index_filter]
                    ):
                        (
                            Auxiliar_Class.auxiliar_table[i],
                            Auxiliar_Class.auxiliar_table[j],
                        ) = (
                            Auxiliar_Class.auxiliar_table[j],
                            Auxiliar_Class.auxiliar_table[i],
                        )

    return redirect("home", permanent=True)


def delete_tag(request):
    if request.method == "POST":
        tag_symbols = json.loads(request.body)
        for tag_symbol in tag_symbols:
            Database_Tags.delete_tag(Database_Tags.consult_tags_by_filter(tag_symbol))

    return redirect("home", permanent=True)


def create_tag(request):
    inserted_symbol = str(request.POST.get("symbol"))
    tags_database_data = list(Database_Tags.consult_all_tags_saved().values_list())
    if len(Auxiliar_Class.auxiliar_table) == 0 or len(
        Auxiliar_Class.auxiliar_table
    ) != len(tags_database_data):
        Auxiliar_Class.auxiliar_table = tags_database_data
    else:
        tags_database_data = Auxiliar_Class.auxiliar_table
    form_symbol = CreateTag(request.POST)

    if (
        inserted_symbol is None
        or inserted_symbol == "Formato erróneo, inténtelo de nuevo"
    ):
        inserted_symbol = ""

    inserted_symbol = inserted_symbol.upper()

    if request.method == "POST":
        if (
            len(inserted_symbol) == inserted_symbol.count(" ")
            or inserted_symbol.count(" ") > len(inserted_symbol) // 2
        ):
            initial_data = {"symbol": "Formato erróneo, inténtelo de nuevo"}
            return render(
                request,
                "create_tag.html",
                {
                    "form": CreateTag(initial=initial_data),
                    "headers_title_list": [
                        "symbol",
                        "shortName",
                        "debt/Equ",
                        "%Insiders",
                        "Price",
                        "t.Price",
                        "Upside",
                        "t.PE",
                        "f.PE",
                        "t.Eps",
                        "f.Eps",
                        "ROA",
                        "ROE",
                        "profit.M",
                        "Myscore",
                        "Mycount",
                    ],
                    "financial_data_tags": tags_database_data,
                    "len_tags": len(tags_database_data),
                    "comprobation_create_tag": True,
                },
            )
        elif len(inserted_symbol) <= 6:
            row_with_data = fn.financeAnalisis(inserted_symbol)
            Database_Tags.create_new_tag(row_with_data)
            tags_database_data = list(
                Database_Tags.consult_all_tags_saved().values_list()
            )
            for row_with_data in tags_database_data:
                if inserted_symbol in str(row_with_data[0]).upper():
                    if form_symbol.is_valid():
                        symbol_form = form_symbol.cleaned_data["symbol"]
                        initial_data = {"symbol": symbol_form}
                    else:
                        initial_data = {"symbol": "Formato erróneo, inténtelo de nuevo"}
                    return render(
                        request,
                        "create_tag.html",
                        {
                            "form": CreateTag(initial=initial_data),
                            "headers_title_list": [
                                "symbol",
                                "shortName",
                                "debt/Equ",
                                "%Insiders",
                                "Price",
                                "t.Price",
                                "Upside",
                                "t.PE",
                                "f.PE",
                                "t.Eps",
                                "f.Eps",
                                "ROA",
                                "ROE",
                                "profit.M",
                                "Myscore",
                                "Mycount",
                            ],
                            "financial_data_tags": tags_database_data,
                            "len_tags": len(tags_database_data),
                            "comprobation_create_tag": False,
                        },
                    )
        elif len(inserted_symbol) > 6:
            names_unfixed = list(inserted_symbol)
            names_fixed = []
            if names_unfixed[-1] != ",":
                names_unfixed.append(",")
            while True:
                for w in names_unfixed:
                    if w == ",":
                        conf = True
                        index = names_unfixed.index(w)
                        names_fixed = names_unfixed[0:index]
                        del names_unfixed[0 : index + 2]
                        for tag_data in tags_database_data:
                            if "".join(names_fixed) in tag_data[0]:
                                conf = False
                        if conf and names_fixed.count(" ") != len(names_fixed):
                            row_with_data = fn.financeAnalisis("".join(names_fixed))
                            Database_Tags.create_new_tag(row_with_data)
                        names_fixed = []
                if len(names_unfixed) == 0:
                    break
        return redirect("/create_tag/")
    else:
        return render(
            request,
            "create_tag.html",
            {
                "form": CreateTag(),
                "headers_title_list": [
                    "symbol",
                    "shortName",
                    "debt/Equ",
                    "%Insiders",
                    "Price",
                    "t.Price",
                    "Upside",
                    "t.PE",
                    "f.PE",
                    "t.Eps",
                    "f.Eps",
                    "ROA",
                    "ROE",
                    "profit.M",
                    "Myscore",
                    "Mycount",
                ],
                "financial_data_tags": tags_database_data,
                "len_tags": len(tags_database_data),
                "comprobation_create_tag": False,
            },
        )


def home(request):
    tags_database_data = list(Database_Tags.consult_all_tags_saved().values_list())
    if len(Auxiliar_Class.auxiliar_table) == 0 or len(
        Auxiliar_Class.auxiliar_table
    ) != len(tags_database_data):
        Auxiliar_Class.auxiliar_table = tags_database_data
    else:
        tags_database_data = Auxiliar_Class.auxiliar_table
    return render(
        request,
        "home.html",
        {
            "headers_title_list": [
                "symbol",
                "shortName",
                "debt/Equ",
                "%Insiders",
                "Price",
                "t.Price",
                "Upside",
                "t.PE",
                "f.PE",
                "t.Eps",
                "f.Eps",
                "ROA",
                "ROE",
                "profit.M",
                "Myscore",
                "Mycount",
            ],
            "financial_data_tags": tags_database_data,
            "len_tags": len(tags_database_data),
        },
    )


def update_data_tags(request):
    Database_Tags.update_tags_data()
    return redirect("/")


class Database_Tags:
    @classmethod
    def consult_all_tags_saved(cls):
        return Tag.objects.all()

    @classmethod
    def create_new_tag(cls, data_tag):
        Tag.objects.create(
            symbol=data_tag[0],
            short_name=data_tag[1],
            debt_equ=data_tag[2],
            insiders=data_tag[3],
            price=data_tag[4],
            t_price=data_tag[5],
            upside=data_tag[6],
            t_pe=data_tag[7],
            f_pe=data_tag[8],
            t_eps=data_tag[9],
            f_eps=data_tag[10],
            roa=data_tag[11],
            roe=data_tag[12],
            profit_m=data_tag[13],
            my_score=data_tag[14],
            my_count=data_tag[15],
        )

    @classmethod
    def consult_tags_by_filter(cls, filter):
        return Tag.objects.filter(symbol=filter)

    @classmethod
    def delete_tag(cls, queryset):
        queryset.delete()

    @classmethod
    def update_tags_data(cls):
        all_tags = list(cls.consult_all_tags_saved())
        for tag in all_tags:
            new_data = fn.financeAnalisis(tag.symbol)
            i = 0
            for field_to_modify in tag._meta.fields:
                setattr(tag, field_to_modify.name, new_data[i])
                i += 1
            tag.save()


class Auxiliar_Class:
    auxiliar_table = []
