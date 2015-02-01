#Falcon WordPress RESTful API

一个以WordPress作为编辑，Falcon + Peewee作为发布的项目。

> A project basis on WordPress as Editing, Falcon as Publishing.


1.change config.py 

2.run server
    
    gunicorn server:app


use peewee generate db model

    python -m pwiz -e mysql "MK_xunzhao" -uroot > blog_models.py
    

License

[待我代码编成，娶你为妻可好](http://www.xuntayizhan.com/person/ji-ke-ai-qing-zhi-er-shi-dai-wo-dai-ma-bian-cheng-qu-ni-wei-qi-ke-hao-wan/)

© 2015 [Phodal Huang](http://www.phodal.com). This code is distributed under the MIT license.