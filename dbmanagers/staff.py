from database import DB
from bot_config import OWNER

staff = DB('staff.json')


def admins():
    return staff.get_nested(["admins"])


def add_admin(user_id):
    staff.set_nested("admins", user_id)


def remove_admin(user_id):
    staff.remove_nested(["admins", user_id])


def moderators():
    return staff.get_nested(["moderators"])


def add_moderator(user_id):
    staff.set_nested("moderators", user_id)


def remove_moderator(user_id):
    staff.remove_nested(["moderators", user_id])
