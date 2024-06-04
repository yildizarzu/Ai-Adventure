# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9

WORKDIR /app

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt


COPY . .


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "train.py"]
