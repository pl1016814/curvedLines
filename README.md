Pi:

uvicorn apiWaveshare:app --host 0.0.0.0 --port 8000

Computer:

python3 server.py

open gui.html


If it doesn't work, test:

curl http://192.168.240.150:8000/
