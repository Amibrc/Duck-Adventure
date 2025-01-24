from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "Assets"

DISPLAY_CONFIG_PATH = BASE_DIR / "config" / "display_config.json"
FONT_PATH = ASSETS_DIR / "Fonts" / "PixelatedEleganceRegular-ovyAA.ttf"

BACKGROUND_STATIC_PATHS = (
    ASSETS_DIR / "Background" / "parallax-mountain-bg.png",
    ASSETS_DIR / "Background" / "parallax-mountain-montain-far.png"
)

BACKGROUND_SCROLL_PATHS = (
    ASSETS_DIR / "Background" / "parallax-mountain-mountains.png",
    ASSETS_DIR / "Background" / "parallax-mountain-trees.png",
    ASSETS_DIR / "Background" / "parallax-mountain-foreground-trees.png"
)

DUCK_MIDDLE_IDLE_PATHS = (
    ASSETS_DIR / "Duck" / "Idle" / "Idle 001.png",
    ASSETS_DIR / "Duck" / "Idle" / "Idle 002.png"
)

DUCK_IDLE_PATHS = (
    ASSETS_DIR / "Duck" / "Idle" / "Idle 003.png",
    ASSETS_DIR / "Duck" / "Idle" / "Idle 004.png"
)

DUCK_WALKING_PATHS = (
    ASSETS_DIR / "Duck" / "Walking-Running" / "Walking 001.png",
    ASSETS_DIR / "Duck" / "Walking-Running" / "Walking 002.png"
)

DUCK_RUNNING_PATHS = (
    ASSETS_DIR / "Duck" / "Walking-Running" / "Running 001.png",
    ASSETS_DIR / "Duck" / "Walking-Running" / "Running 002.png"
)

DUCK_CROUCHING_PATHS = (
    ASSETS_DIR / "Duck" / "Crouching" / "Crouching 001.png",
    ASSETS_DIR / "Duck" / "Crouching" / "Crouching 002.png"
)

DUCK_JUMPING_PATH = ASSETS_DIR / "Duck" / "Jumping" / "Jumping 001.png"
DUCK_CROUCHING_IDLE_PATH = ASSETS_DIR / "Duck" / "Idle" / "Idle-Crouching 001.png"
DUCK_RUDE_PATH = ASSETS_DIR / "Duck" / "Rude" / "Rude 001.png"
DUCK_DEAD_PATH = ASSETS_DIR / "Duck" / "Dead" / "Dead 001.png"

SLIME_WALKING_PATH = (
    ASSETS_DIR / "Mobs" / "Slime" / "Walking" / "walking 001.png",
    ASSETS_DIR / "Mobs" / "Slime" / "Walking" / "walking 002.png",
    ASSETS_DIR / "Mobs" / "Slime" / "Walking" / "walking 003.png"
)

SLIME_DEATH_PATH = (
    ASSETS_DIR / "Mobs" / "Slime" / "Death" / "death 001.png",
    ASSETS_DIR / "Mobs" / "Slime" / "Death" / "death 002.png",
    ASSETS_DIR / "Mobs" / "Slime" / "Death" / "death 003.png"
)

ROYAL_SCARAB_WALKING_PATH = (
    ASSETS_DIR / "Mobs" / "RoyalScarab" / "RoyalScarab 001.png",
    ASSETS_DIR / "Mobs" / "RoyalScarab" / "RoyalScarab 002.png",
    ASSETS_DIR / "Mobs" / "RoyalScarab" / "RoyalScarab 003.png",
    ASSETS_DIR / "Mobs" / "RoyalScarab" / "RoyalScarab 004.png"
)

GIANT_ROYAL_SCARAB_WALKING_PATH = (
    ASSETS_DIR / "Mobs" / "GiantRoyalScarab" / "GiantRoyalScarab 001.png",
    ASSETS_DIR / "Mobs" / "GiantRoyalScarab" / "GiantRoyalScarab 002.png",
    ASSETS_DIR / "Mobs" / "GiantRoyalScarab" / "GiantRoyalScarab 003.png",
    ASSETS_DIR / "Mobs" / "GiantRoyalScarab" / "GiantRoyalScarab 004.png"
)

RED_BRICK_PATH = ASSETS_DIR / "Objects" / "brick 001.png"
GREY_BRICK_PATH = ASSETS_DIR / "Objects" / "brick 002.png"
STONE_PATH = ASSETS_DIR / "Objects" / "stone 001.png"

COIN_PATHS = (
    ASSETS_DIR / "Objects" / "Coin" / "coin 001.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 002.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 003.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 004.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 005.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 006.png",
    ASSETS_DIR / "Objects" / "Coin" / "coin 007.png"
)

DIAMOND_PATHS = (
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 001.png",
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 002.png",
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 003.png",
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 004.png",
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 005.png",
    ASSETS_DIR / "Objects" / "Diamond" / "diamond 006.png"
)

START_BUTTON_PATHS = (
    ASSETS_DIR / "Menu" / "Start_Button" / "start_button 001.png",
    ASSETS_DIR / "Menu" / "Start_Button" / "start_button 002.png",
    ASSETS_DIR / "Menu" / "Start_Button" / "start_button 003.png"
)

SETTINGS_BUTTON_PATHS = (
    ASSETS_DIR / "Menu" / "Settings_Button" / "settings_button 001.png",
    ASSETS_DIR / "Menu" / "Settings_Button" / "settings_button 002.png",
    ASSETS_DIR / "Menu" / "Settings_Button" / "settings_button 003.png"
)

QUIT_BUTTON_PATHS = (
    ASSETS_DIR / "Menu" / "Quit_Button" / "quit_button 001.png",
    ASSETS_DIR / "Menu" / "Quit_Button" / "quit_button 002.png",
    ASSETS_DIR / "Menu" / "Quit_Button" / "quit_button 003.png"
)


BEE_FLYING_PATHS = (
    ASSETS_DIR / "Mobs" / "Bee" / "Flying" / "Bee_Flying 001.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Flying" / "Bee_Flying 002.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Flying" / "Bee_Flying 003.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Flying" / "Bee_Flying 004.png"
)

BEE_DEATH_PATHS = (
    ASSETS_DIR / "Mobs" / "Bee" / "Death" / "Bee_Death 001.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Death" / "Bee_Death 002.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Death" / "Bee_Death 003.png",
    ASSETS_DIR / "Mobs" / "Bee" / "Death" / "Bee_Death 004.png"
)