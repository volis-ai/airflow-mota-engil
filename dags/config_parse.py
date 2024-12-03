"""Utility functions for parsing DAG configurations."""

from airflow.datasets import Dataset
from airflow.exceptions import AirflowConfigException


def parse_schedule(schedule):
    """Create an Airflow compatible schedule from a configuration dictionary."""
    if not schedule:
        return None
    if isinstance(schedule, dict):
        if 'datasets' in schedule:
            return [Dataset(dataset) for dataset in schedule['datasets']]
        if 'cron' in schedule:
            return schedule['cron']
    if isinstance(schedule, str):
        return schedule
    raise AirflowConfigException("Invalid schedule configuration")


def parse_outlets(outlets):
    """Create Airflow compatible outlets from a configuration list."""
    if not outlets:
        return None
    return [Dataset(outlet) for outlet in outlets]
