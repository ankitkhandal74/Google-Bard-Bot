if [ -d "/Google-Bard-Bot" ]; then
    rm -rf /Google-Bard-Bot
fi
git clone https://github.com/ankitkhandal74/Google-Bard-Bot /Google-Bard-Bot
pip3 install -U -r requirements.txt
echo "Starting Google bard"
python bot.py
