from django.http import HttpResponse
from django.shortcuts import render

from bingo_master.models import BingoBoard


def index(request):
    return render(request, "index.html")


def list(request):
    return render(request, "list.html")


def game(request):
    return render(request, "game.html")


def history(request):
    return render(request, "history.html")
