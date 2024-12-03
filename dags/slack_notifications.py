"""Functions to send notifications to Slack for better monitoring."""

import os
from airflow.providers.slack.notifications.slack import send_slack_notification


ENV = os.getenv("ENV", "dev")


def notify_task_failure(context):
    """Send a notification to a Slack channel about a task failure."""
    if ENV == "prod":
        send_slack_notification(
            channel="#pipe-watch",
            text="A *Task* has failed:",
            attachments=[
                {
                    "color": "#FF0000",
                    "fields": [
                        {
                            "title": "DAG",
                            "value": "{{ dag.dag_id }}",
                            "short": True
                        },
                        {
                            "title": "Failed Task",
                            "value": "{{ ti.task_id }}",
                            "short": True
                        },
                        {
                            "title": "Run ID",
                            "value": "{{ run_id }}",
                            "short": False
                        },
                        {
                            "title": "Reason",
                            "value": (
                                "<https://airflow.volis.ai/dags/{{ dag.dag_id }}/grid?"
                                "tab=logs&dag_run_id={{ macros.url_format.quote(run_id) }}&"
                                "task_id={{ ti.task_id }}|View Task details>"
                            ),
                            "short": True
                        }
                    ]
                }
            ]
        )(context)


def notify_dag_failure(context):
    """Send a notification to a Slack channel about a DAG failure."""
    failed_tasks = ', '.join([
        t.task_id for t in context["dag_run"].get_task_instances(state='failed')
    ])
    if ENV == "prod":
        send_slack_notification(
            channel="#pipe-watch",
            text="A *DAG* has failed:",
            attachments=[
                {
                    "color": "#FF0000",
                    "fields": [
                        {
                            "title": "DAG",
                            "value": context["dag"].dag_id,
                            "short": True
                        },
                        {
                            "title": "Failed Tasks",
                            "value": failed_tasks,
                            "short": True
                        },
                        {
                            "title": "Run ID",
                            "value": context["run_id"],
                            "short": False
                        },
                        {
                            "title": "Reason",
                            "value": (
                                "<https://airflow.volis.ai/dags/{{ dag.dag_id }}/grid?"
                                "dag_run_id={{ macros.url_format.quote(run_id) }}|View DAG details>"
                            ),
                            "short": True
                        }
                    ]
                }
            ]
        )(context)
