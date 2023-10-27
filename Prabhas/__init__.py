from Prabhas.core.bot import Prabhas
from Prabhas.core.dir import dirr
from Prabhas.core.git import git
from Prabhas.core.userbot import Userbot
from Prabhas.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Prabhas()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
