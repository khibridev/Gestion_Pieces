from .models import Piece

def nb_critiques(request):
    pieces = Piece.objects.all()
    nb = sum(1 for p in pieces if p.est_critique)
    return {'nb_critiques': nb}