from database import DB

user = DB("user.json")


def add_user(username_or_userid):
    user.set_nested(["users"], username_or_userid)


def remove_user(username_or_userid):
    user.set_nested(["users"], username_or_userid)


def get_users():
    return user.get_all().get("users", {})


def add_ban(user_id):
    user.set_key(["bans"], user_id)


def remove_ban(user_id):
    user.remove_nested(["bans", user_id])


def get_bans():
    return user.get_all().get("bans", {})


def mute(user_id):
    user.set_nested(["mutes"], user_id)


def unmute(user_id):
    user.remove_nested(["mutes", user_id])


def is_mute(user_id):
    mutes = user.get_nested(["mutes"])
    return user_id in mutes


def get_mutes():
    return user.get_nested(["mutes"])
