FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

WORKDIR /workspaces

RUN pip install beautifulsoup4 requests