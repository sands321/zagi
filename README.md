# ZAGI
Release the power of GPT

# GPTs调用本地python，解决联网、调三方库问题

1. 创建GPTs
* 增加prompt, prompt填入gpts/prompt.txt
* 增加action, schema填入gpts/python_schema.json

2. 启动本地服务
* 安装依赖: pip install -r requirements.txt
* 启动notebook: jupyter lab --notebook-dir ./working
* 启动接口服务: uvicorn src.server:app

3. 暴漏服务到外网
* 方法1: 使用LocalTunnel
  * 安装: npm install -g localtunnel
  * 转发本地端口: lt --port 8000
  * 弊端: 重启lt后地址会变, 另外相对有点慢
* 方法2: 使用[花生壳](https://hsk.oray.com/price#personal)
  * 好处: 快, 地址固定

## 相关文章

1. [知乎：GPTs调本地python实现越狱](https://zhuanlan.zhihu.com/p/666467937)

## 看下效果

![image](https://github.com/sands321/zagi/blob/master/screenshots/plot.jpg)
![image](https://github.com/sands321/zagi/blob/master/screenshots/fn.jpg)



