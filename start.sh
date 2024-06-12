# Remove the directory if it exists
if [ -d "/Google-Bard-Bot" ]; then
  echo "Removing existing /Google-Bard-Bot directory"
  rm -rf /Google-Bard-Bot
fi

# Clone the repository
if [ -z "$UPSTREAM_REPO" ]; then
  echo "Cloning main Repository"
  git clone https://github.com/ankitkhandal74/Google-Bard-Bot.git /Google-Bard-Bot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO"
  git clone $UPSTREAM_REPO /Google-Bard-Bot
fi

# Change to the repository directory
cd /Google-Bard-Bot || { echo "Failed to change directory to /Google-Bard-Bot"; exit 1; }

# Check if requirements.txt exists
if [ -f "requirements.txt" ]; then
  echo "Installing requirements"
  pip3 install -U -r requirements.txt
else
  echo "requirements.txt not found, skipping installation"
fi

echo "Starting -yuji-itadori"
python3 bot.py
