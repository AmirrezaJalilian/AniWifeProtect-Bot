from commands.commandRouter import CommandRouter
from commands.routercommands.admin import add_admin_,remove_admin_
from commands.routercommands.moderator import add_moderator_,remove_moderator_

router = CommandRouter()

router.add("staff.add.admin", add_admin_)
router.add("staff.remove.admin", remove_admin_)
router.add("staff.add.moderator", add_moderator_)
router.add("staff.remove.moderator", remove_moderator_)