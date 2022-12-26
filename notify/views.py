from flask import Blueprint, request
from notify.database import UserToken
from notify.api_exception import exceptions_error
from notify.functions import to_one_user, to_all_users


views = Blueprint("views", __name__, url_prefix="/send")


@views.post('/<userId>')
def start_func(userId):
    profile = UserToken.query.filter_by(userId=userId).first()
    senderId = request.headers.get('senderId')

    message = request.get_json().get('message', '')
    notificationType = request.get_json().get('notificationType', '')

    if not senderId:
        return exceptions_error("Title is empty", 400)
    if not notificationType:
        return exceptions_error("Type is empty", 400)

    return to_one_user(profile, senderId, message, notificationType)



@views.post('/all')
def send_all():
    profiles = UserToken.query.all()
    senderId = request.headers.get('senderId')

    message = request.get_json().get('message', '')
    notificationType = request.get_json().get('notificationType', '')

    if not senderId:
        return exceptions_error("Title is empty", 400)
    if not notificationType:
        return exceptions_error("Type is empty", 400)

    return to_all_users(profiles, senderId, message, notificationType)
