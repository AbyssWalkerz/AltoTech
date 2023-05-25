from flask import Blueprint, request
import logging

logger = logging.getLogger('auth')
main= Blueprint('api',__name__, url_prefix="/api")

@main.route('/login', methods=['GET', 'POST'])
def login():
    print(__name__)
    return 'Hello, World!'


@main.route('/logout', methods=['GET', 'POST'])
def logout():
    None 
