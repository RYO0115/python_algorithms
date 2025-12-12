# syntax=docker/dockerfile:1
FROM python:3.13.4-bookworm

RUN pip3 install numpy pandas pymupdf ipykernel

RUN mkdir -p /workspace/python_workspace

WORKDIR /workspace

