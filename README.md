使用说明：
点开文件prompt-template-ecom-copywriter-v1.md，可修改机器人扮演角色、输出格式
点开文件.env修改调用的API KEY
点开文件call_deepseek.py，在product行的双引号部分可替换需要推广的产品#   d e e p s e e k - c o p y w r i t e r - d e m o

## 工作流作品 2：天气查询机器人

- 功能：输入城市名，调用 Open-Meteo 天气 API，返回自然语言天气回复
- 文件：`workflows/day10-weather-bot.yml`
- 节点：开始 → LLM提取城市 → 代码节点转经纬度 → HTTP请求天气 → LLM生成回复 → 结束
- 支持城市：北京、上海、广州、深圳 

## 工作流作品 3：客服查询机器人

- 功能：自动识别客户意图（订单/物流/营业时间/其他），订单和物流分支自动调用模拟 API 查询
- 文件：`workflows/day11-customer-service-bot.yml`
- 节点：开始 → 问题分类器 → 4 个分支（LLM提取+HTTP请求或直接回复）→ 变量聚合器 → 结束
- 测试用例：
  - 我的订单 3 到哪了？
  - 帮我查一下快递 5 的物流
  - 你们几点开门？
  - 你们支持退款吗？ 
 