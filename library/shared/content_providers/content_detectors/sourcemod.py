from pathlib import Path

from .....library.utils.path_utilities import backwalk_file_resolver
from ..content_provider_base import ContentProviderBase
from .source1_common import Source1Common


class SourceMod(Source1Common):
    @classmethod
    def scan(cls, path: Path) -> dict[str, ContentProviderBase]:
        smods_dir = backwalk_file_resolver(path, 'sourcemods')
        mod_root = None
        mod_name = None
        if smods_dir is not None and path.is_relative_to(smods_dir):
            mod_name = path.relative_to(smods_dir).parts[0]
            mod_root = smods_dir / mod_name
        if mod_root is None:
            return {}
        content_providers = {}
        cls.recursive_traversal(smods_dir, mod_name, content_providers)
        return content_providers

    @classmethod
    def register_common(cls, root_path: Path, content_providers: dict[str, ContentProviderBase]):
        super().register_common(root_path, content_providers)
