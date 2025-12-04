from database import DataBase

group=DataBase('groups.json')

def new_group(group_id,data):
    group.list_add(group_id,data)