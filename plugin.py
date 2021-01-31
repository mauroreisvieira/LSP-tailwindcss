from .consts import EXTENSION_UID
from .consts import EXTENSION_VERSION
from .consts import SERVER_BINARY_PATH
from .helpers.vs_marketplace_lsp_utils import configure_lsp_like_vscode
from .helpers.vs_marketplace_lsp_utils import DOWNLOAD_FROM_MARKETPLACE
from .helpers.vs_marketplace_lsp_utils import VsMarketplaceClientHandler
from LSP.plugin.core.typing import Any, Optional
import sublime


def plugin_loaded() -> None:
    configure_lsp_like_vscode()
    LspTailwindCssPlugin.setup()


def plugin_unloaded() -> None:
    # the cleanup() will delete the downloaded server
    # we don't want this during developing this plugin...
    if not LspTailwindCssPlugin.get_plugin_setting("developing"):
        LspTailwindCssPlugin.cleanup()


class LspTailwindCssPlugin(VsMarketplaceClientHandler):
    package_name = __package__.split(".")[0]

    extension_uid = EXTENSION_UID
    extension_version = EXTENSION_VERSION
    server_binary_path = SERVER_BINARY_PATH
    execute_with_node = True
    pretend_vscode = False
    download_from = DOWNLOAD_FROM_MARKETPLACE

    # resources directories will be copied into the server directory during server installation
    resource_dirs = []

    # -------------- #
    # custom methods #
    # -------------- #

    @classmethod
    def get_plugin_setting(cls, key: str, default: Optional[Any] = None) -> Any:
        return sublime.load_settings(cls.package_name + ".sublime-settings").get(key, default)
