from flask import Blueprint

btdjy = Blueprint('btdjy',__name__)
from  . import views,errors
