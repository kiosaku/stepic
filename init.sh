sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask.conf /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart
