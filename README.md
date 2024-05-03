# ZAGI
Release the power of GPT

# ChatGPT Chrome插件
1. 功能示例
![image](https://github.com/sands321/zagi/blob/master/screenshots/cr_demo.png)

2. 安装方法
![image](https://github.com/sands321/zagi/blob/master/screenshots/cr_install.png)

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

1. [知乎：GPTs和本地代码打通](https://zhuanlan.zhihu.com/p/667558479)

## 看下效果

![image](https://github.com/sands321/zagi/blob/master/screenshots/plot.jpg)
![image](https://github.com/sands321/zagi/blob/master/screenshots/fn.jpg)

## 联系方式
* WeChat：zhucheng798
* 知乎：[星辰](https://www.zhihu.com/people/xing-chen-78-84)



