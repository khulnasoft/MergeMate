FROM python:3.10 as base

WORKDIR /app
ADD pyproject.toml .
ADD requirements.txt .
RUN pip install . && rm pyproject.toml requirements.txt
ENV PYTHONPATH=/app

FROM base as github_app
ADD mergemate mergemate
CMD ["python", "mergemate/servers/github_app.py"]

FROM base as bitbucket_app
ADD mergemate mergemate
CMD ["python", "mergemate/servers/bitbucket_app.py"]

FROM base as bitbucket_server_webhook
ADD mergemate mergemate
CMD ["python", "mergemate/servers/bitbucket_server_webhook.py"]

FROM base as github_polling
ADD mergemate mergemate
CMD ["python", "mergemate/servers/github_polling.py"]

FROM base as gitlab_webhook
ADD mergemate mergemate
CMD ["python", "mergemate/servers/gitlab_webhook.py"]

FROM base as test
ADD requirements-dev.txt .
RUN pip install -r requirements-dev.txt && rm requirements-dev.txt
ADD mergemate mergemate
ADD tests tests

FROM base as cli
ADD mergemate mergemate
ENTRYPOINT ["python", "mergemate/cli.py"]
