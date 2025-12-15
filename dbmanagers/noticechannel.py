from database import DB

notice_channel = DB("noticechannel")


def set_message_map(channel_msg_id, group_msg_id):
    notice_channel.set_key(str(channel_msg_id), group_msg_id)


def get_group_message_id(channel_msg_id):
    return notice_channel.get_key(str(channel_msg_id))
