from command.command_router import CommandRouter
from command.routercommands.admin import add_admin, remove_admin
from command.routercommands.moderator import add_moderator, remove_moderator
from command.routercommands.mute import mute, unmute, list_mute
from command.routercommands.ban import ban, unban, list_ban
from command.routercommands.pin import pin, unpin

router = CommandRouter(".")

router.add("staff.add.admin", add_admin)
router.add("staff.remove.admin", remove_admin)
router.add("staff.add.moderator", add_moderator)
router.add("staff.remove.moderator", remove_moderator)
router.add("mute", mute)
router.add("unmute", unmute)
router.add("list.mute", list_mute)
router.add("ban", ban)
router.add("unban", unban)
router.add("list.ban", list_ban)
router.add("pin", pin)
router.add("unpin", unpin)

