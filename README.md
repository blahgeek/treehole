#人人树洞发布

例子参见[清华树洞](http://thutreehole.tk).

由于2013年5月24号左右开始，人人的cookie会在每天零点时过期，需要重新登录，因此现在使用api方式发布状态。
但是未审核的api每用户每小时最多只能发布30条状态（好像），之后可以尝试采用多个api key或者多个用户的方式。

## 使用说明

修改`treehole/settings.py`中的`PAGE_ID, LINKS, SECRET_KEY`，
运行`python2 manage.py syncdb`初始化数据库，
准备Api等，如下。

## 关于Api

- 用个人的人人帐号在[这里](http://app.renren.com/developers/app)申请一个应用，注意在未审核的情况下只有管理员和开发者才能
使用该应用。
- 在应用信息的域名、安全设置的回调地址中填`localhost:8090`。
- 在应用根文件夹下新建一个`client_secrets.json`文件，文件格式如下：

    {
        "installed": {
            "client_id": "YOUR API KEY", 
            "client_secret": "YOUR SECRET KEY", 
            "redirect_uris": ["http://graph.renren.com/oauth/login_success.html"], 
            "auth_uri": "https://graph.renren.com/oauth/authorize", 
            "token_uri": "https://graph.renren.com/oauth/token"
        }
    }

- 运行`./manage.py auth`认证。

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
