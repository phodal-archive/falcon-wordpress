#Falcon WordPress RESTful API

> A example on build wordpress api with falcon

1.change config.py 

2.run server
    
    gunicorn server:app


use peewee generate db model

    python -m pwiz -e mysql "MK_xunzhao" -uroot > blog_models.py
    

License

© 2015 [Phodal Huang](http://www.phodal.com). This code is distributed under the MIT license.