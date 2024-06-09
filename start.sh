if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ankitkhandal74/Google-Bard-Bot.git /Google-Bard-Bot
else
 echo "Cloning Custom Repo from $UPSTREAM_REPO "
 git clone $UPSTREAM_REPO /Google-Bard-Bot
fi
echo ls
cd /Google-Bard-Bot
#pip3 install -U -r requirements.txt
echo "Starting Google bard"
python3 bot.py
