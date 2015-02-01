#Falcon WordPress RESTful API

1.generate db model

    python -m pwiz -e mysql "MK_xunzhao" -uroot > blog_models.py
    
2.run server
    
    gunicorn server:app
