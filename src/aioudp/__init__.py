from aioudp.server import UDPServer
from distutils.version import LooseVersion

__version__ = "0.0.6"
__version_info__ = tuple(LooseVersion(__version__).version)
__all__ = [
    "UDPServer"
]
