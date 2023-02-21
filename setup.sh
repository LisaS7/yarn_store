# Install venv and create virtual environment
read -p "Install venv and create virtual environment? y/n: " answer
if [[ $answer = y ]]; then
    sudo apt-get install -y python3-venv
    python3 -m venv venv/
fi

source venv/bin/activate

# If venv is active then install requirements
read -p "Install requirements.txt? y/n: " answer
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Failed to activate venv. Check venv exists and script is being run from the correct location."
    exit 1
elif [[ $answer = y ]]; then
    pip install -r requirements.txt
fi