from database import DB

staff = DB('staff.json')


def admin(user_id):
    return bool(str(user_id) in admins())


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


def moderator(user_id):
    return bool(str(user_id) in moderators())
