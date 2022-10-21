# Yi-Ban_clock-in
易班自动打卡
简单配置:
如果运行daka.py提示缺少requests，requests安装：pip install requests
daka.py里面的中文都要url编码，不然可能出现乱码，url编码解码：http://tool.chinaz.com/tools/urlencode.aspx
以及start中的daka.py的文件绝对路径要改成自己的daka.py文件绝对路径
点击start.bat就ok了直接添加到windows的计划任务中每天早上，中午，晚上打开
必须要保证windows不能关机否则计划任务无法执行，有服务器最好挂在服务器上一劳永逸
最后要删除计划任务的运行delete.bat
