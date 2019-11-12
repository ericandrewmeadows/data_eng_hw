import os
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader


class DatabaseTools(object):
    def __init__(
        self, template_dir_path: str, templates_folder: str, *args, **kwargs
    ):
        template_dir = os.path.join(
            os.path.dirname(template_dir_path), templates_folder
        )
        loader = FileSystemLoader(searchpath=template_dir)
        self.template_environment = Environment(loader=loader)

    def load_jinja_query_template(
        self, template_file: str, params: Dict[str, Any]
    ) -> str:
        template = self.template_environment.get_template(template_file)
        rendered_query = template.render(params)
        return rendered_query
