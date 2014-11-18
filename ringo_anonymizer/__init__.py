import logging
from ringo.lib.extension import register_modul
from ringo.lib.helpers import dynamic_import

# Import models so that alembic is able to autogenerate migrations
# scripts.
from ringo_anonymizer.model import Extension

log = logging.getLogger(__name__)

modul_config = {
    "name": "anonymizer",
    "label": "",
    "clazzpath": "ringo_anonymizer.model.Extension",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete"]
}


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    Extension._modul_id = modul.get_value("id")