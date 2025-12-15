from commands.commandRouter import CommandRouter
from commands.routercommands.admin import add_admin_, remove_admin_
from commands.routercommands.moderator import add_moderator_, remove_moderator_
from commands.routercommands.mute import *
from commands.routercommands.ban import *
from commands.routercommands.pin import *

router = CommandRouter()

router.add("staff.add.admin", add_admin_)
router.add("staff.remove.admin", remove_admin_)
router.add("staff.add.moderator", add_moderator_)
router.add("staff.remove.moderator", remove_moderator_)
router.add("mute", mute_)
router.add("unmute", unmute_)
router.add("list.mute", mute_list_bot)
router.add("ban", ban_)
router.add("unban", unban_)
router.add("list.ban", ban_list)
router.add("pin", pin)
router.add("unpin", unpin)

