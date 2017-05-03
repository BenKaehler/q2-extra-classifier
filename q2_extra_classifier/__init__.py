import importlib
import pkg_resources

__version__ = pkg_resources.get_distribution('q2-extra-classifier').version

importlib.import_module('q2_extra_classifier._extra')
