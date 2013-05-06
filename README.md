#人人树洞发布

例子参见[清华树洞](http://thutreehole.tk).

## 使用说明

修改`treehole/settings.py`中的`PAGE_ID, LINKS, SECRET_KEY`，
运行`python2 manage.py syncdb`初始化数据库，
在`cookie.txt`中写入cookie，就能使用了。

## 关于Cookie

- 申请一个公共主页后，另外申请一个马甲帐号A
- 将A添加为公共主页的管理员
- 在电脑隐身窗口登录A，切换至公共主页管理，记录下cookie写入`cookie.txt`
- 直接关闭浏览器，从此不在浏览器上登录

另外，为防止cookie过期，需要定时刷页面，向`crontab`中加入
`*/15 * * * * /path/to/manage.py refresh`，每15分钟刷新一次。

## 关于textarea的placeholer

通过`./manage.py placeholder -a CONTENT`添加，将会将CONTENT添加入数据库。
生成页面时会从数据库中随机挑选一条。

该命令还能列出和删除，详见`./manage.py placeholder -h`。

## 手动发布状态

`./manage.py poststatu CONTENT`：发布一条状态（包含编号）并且存入数据库。
`./manage.py poststatu -r CONTENT`：发布一条状态（不包含编号）。

