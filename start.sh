if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/ankitkhandal74/-yuji-itadori.git /-yuji-itadori
else
 echo "Cloning Custom Repo from $UPSTREAM_REPO "
 git clone $UPSTREAM_REPO /-yuji-itadori
fi
cd /-yuji-itadori
#pip3 install -U -r requirements.txt
echo "Starting -yuji-itadori"
python3 bot.py
