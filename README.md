# AI Agent 入职冲刺

这是程宏杰的独立工程训练仓库。训练代码、测试和运行文档都放在这里，不与上级目录中的求职材料混合提交。

## Day 1：最小健康 Agent loop

目标：不依赖大型 Agent 框架，实现并解释以下数据流：

`用户问题 -> 决定是否调用工具 -> 查询合成睡眠/HRV数据 -> 观察工具结果 -> 回答或停止`

通过标准：

- 工具有明确的输入/输出 schema；
- 工具失败时返回可定位的错误；
- loop 有最大步数和停止条件；
- 至少覆盖正常路径和失败路径测试；
- 能从干净环境按文档运行程序和测试。

## 当前环境

```bash
cd "/Users/wind/Documents/AI agent求职准备/01_Agent入职冲刺"
source .venv/bin/activate
python --version
```

预期 Python 版本：`3.13.9`。
