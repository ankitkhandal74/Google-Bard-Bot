if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  rm -rf /Google-Bard-Bot  # Remove the directory if it exists
  git clone https://github.com/ankitkhandal74/Google-Bard-Bot.git /Google-Bard-Bot
else
 echo "Cloning Custom Repo from $UPSTREAM_REPO "
 rm -rf /Google-Bard-Bot  # Remove the directory if it exists
 git clone $UPSTREAM_REPO /Google-Bard-Bot
fi
cd /Google-Bard-Bot
#pip3 install -U -r requirements.txt
echo "Starting -yuji-itadori"
python3 bot.py
