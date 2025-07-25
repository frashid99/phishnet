from flask import Blueprint, render_template, request
from .model import predict_email

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    result = None
    confidence = None
    if request.method == 'POST':
        email_text = request.form.get('email_text', '')
        result, confidence = predict_email(email_text)
    return render_template('index.html', result=result, confidence=confidence)
