mkdir -p ~/.streamlit/
echo “\
[general]\n\
email = \”bthtus001@myuct.ac.za\”\n\
“ > ~/.streamlit/credentials.toml
echo “\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
“ > ~/.streamlit/config.toml
