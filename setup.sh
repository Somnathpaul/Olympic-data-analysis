mkdir -p ~/.streamlit/

echo "[theme]
primaryColor='#eaad19'
backgroundColor='#132143'
secondaryBackgroundColor='#1d2a50'
textColor='#ffffff'
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml