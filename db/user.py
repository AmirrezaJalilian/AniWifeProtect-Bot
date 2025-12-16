from db.db import DB
from bot_config import OWNER_ID

user = DB("users")


def is_staff(userid):
    return bool(is_owner(userid) or is_admin(userid) or is_moderator(userid))


def is_owner(userid):
    return bool(userid == OWNER_ID)


def is_admin(userid):
    return bool(get_user_role(userid) == "admin")


def is_moderator(userid):
    return bool(get_user_role(userid) == "moderator")


def is_mute(userid):
    return bool(str(userid) in get_mutes())


def is_ban(userid):
    return bool(str(userid) in get_bans())


def exist_user(userid):
    return bool(str(userid) in get_users())


def get_user(userid):
    return get_users().get(str(userid))


def get_users_username():
    usernames = []
    users = get_users()
    for userid in users:
        usernames.append(get_user_username(userid))
    return usernames


def get_users():
    return user.get_all()["users"]


def get_mutes():
    return user.get_all()["mutes"]


def get_bans():
    return user.get_all()["bans"]


def add_user(user_id, username):
    user.set_nested(["users", user_id], {
        'role': 'member',
        'username': username
    })


def add_mute(user_id):
    user.set_nested(["mutes", user_id], True)


def add_ban(user_id):
    user.set_key(["bans", str(user_id)], True)


def remove_user(userid):
    user.remove_nested(["users", str(userid)])


def remove_mute(user_id):
    user.remove_nested(["mutes", str(user_id)])


def remove_ban(user_id):
    user.remove_nested(["bans", str(user_id)])


def get_user_role(userid):
    return get_user(userid)['role']


def get_user_username(userid):
    return get_user(userid).get('username')


def set_role(userid, role: str = "member"):
    user.set_nested(['users', userid, 'role'], role)
