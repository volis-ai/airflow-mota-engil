"""Tools for formatting URLs for better compatibility."""

from airflow.plugins_manager import AirflowPlugin
from urllib.parse import quote


class URLFormat(AirflowPlugin):
    """Define macros to work with URL in jinja."""

    name = "url_format"
    macros = [quote]
