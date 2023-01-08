# Pip installing
FROM python:3.8

# Working directory
COPY ./src/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:./src"
CMD ["/bin/bash"]
