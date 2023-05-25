from flask import Blueprint, request
import logging

logger = logging.getLogger('auth')
auth= Blueprint('auth',__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    None


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    None 
