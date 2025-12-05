from database import DataBase

user=DataBase('user.json')

def add_ban(user_id):
    user.set_path(["bans"],user_id)
    
def remove_ban(user_id):
    user.remove_path(["bans"],user_id)
    
def get_bans():
    return user.all()['bans'] if not {} else None

def is_mute(user_id):
    return user.get_path(["mutes"],user_id)

def mute(user_id):
    user.set_path(["mutes"],user_id)
    
def unmute(user_id):
    user.remove_path(["mutes"],user_id)
    
def get_mutes():
    return user.get_path(["mutes"])