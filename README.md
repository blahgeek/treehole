#人人树洞发布

例子参见[清华树洞](http://thutreehole.tk).

由于2013年5月24号左右开始，人人的cookie会在每天零点时过期，需要重新登录，
~~因此现在使用api方式发布状态~~
。
但是未审核的api每用户每小时最多只能发布30条状态（好像），之后可以尝试采用多个api key或者多个用户的方式。

2013年7月12号左右开始，由于人人公共主页的调整，通过api发布的内容不会在新鲜事中出现，需要点击公共主页右侧的“状态”才能看到，
因此使用3g人人页面发布。

新增发布量统计页面，在`/chart_hour`和`/chart_day`。

## 使用说明

- 申请一个公共主页后，另外申请一个马甲帐号A
- 将A添加为公共主页的管理员
- 在电脑隐身窗口登录A至`http://3g.renren.com`，在底部的“设置”中切换至公共主页，记录下cookie写入cookie.txt
- 直接关闭浏览器

修改`treehole/settings.py`中的`PAGE_ID, LINKS, SECRET_KEY`，
运行`python2 manage.py syncdb`初始化数据库，

## 关于textarea的placeholer

通过`./manage.py placeholder -a CONTENT`添加，将会将CONTENT添加入数据库。
生成页面时会从数据库中随机挑选一条。

该命令还能列出和删除，详见`./manage.py placeholder -h`。

## 手动发布状态

- `./manage.py poststatu CONTENT`：发布一条状态（包含编号）并且存入数据库。
- `./manage.py poststatu -r CONTENT`：发布一条状态（不包含编号）。

## 屏蔽一个IP地址

- `./manage.py IP`： 屏蔽该IP地址发布状态。
- `./manage.py -r IP`：解除该IP的屏蔽。
