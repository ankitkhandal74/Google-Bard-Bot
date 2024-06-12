FROM python:3.10.8-slim-buster

# Update and install required packages
RUN apt update && apt upgrade -y && apt install git -y

# Copy requirements.txt and install dependencies
COPY requirements.txt /requirements.txt
RUN pip3 install -U pip && pip3 install -U -r /requirements.txt

# Create the bot directory and set it as the working directory
RUN mkdir -p /Google-Bard-Bot
WORKDIR /Google-Bard-Bot

# Copy start.sh script to the working directory
COPY start.sh /Google-Bard-Bot/start.sh

# Ensure start.sh is executable
RUN chmod +x /Google-Bard-Bot/start.sh

# Command to run the start.sh script
CMD ["/bin/bash", "/Google-Bard-Bot/start.sh"]
