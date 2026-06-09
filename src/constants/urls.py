from src.utils.config import get_env


BASE_URL = get_env("BASE_URL_1", get_env("BASE_URL", "http://localhost:3000"))
APP_ROUTE_PREFIX = "/ai-helpy-chat"
CHAT_HOME_PATH = APP_ROUTE_PREFIX
CHATS_PATH = f"{APP_ROUTE_PREFIX}/chats"
TOOLS_PATH = f"{APP_ROUTE_PREFIX}/tools"
AGENTS_PATH = f"{APP_ROUTE_PREFIX}/agents"
AGENTS_MINE_PATH = f"{AGENTS_PATH}/mine"
AGENTS_BUILDER_PATH = f"{AGENTS_PATH}/builder"
