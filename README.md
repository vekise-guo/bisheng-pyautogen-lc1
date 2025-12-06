# bisheng-pyautogen-lc1

`bisheng-pyautogen-lc1` 是 `bisheng-pyautogen` 的一个分支，**仅针对 LangChain v1+** 版本。
它保留了原始的导入路径 (`import autogen`)，同时将旧的导入更新为当前的 LangChain 包布局（例如 `langchain_core.*`）。

## 关键点

- **仅支持 LangChain v1**: 此分支有意**不支持**旧版本的 LangChain。
- **导入路径不变**: 您的应用程序代码继续使用 `import autogen`。
- **分支目的**: 进行最小化修补，以解除使用最新 LangChain 版本的项目的阻塞。

## 安装

### 从 GitHub 安装 (pip)

替换 `<OWNER>` 和可选的 `<REF>` (分支/标签/提交):

```bash
pip install "git+https://github.com/<OWNER>/bisheng-pyautogen-lc1.git@main"
```

### 开发

安装开发依赖:

```bash
pip install pytest pytest-asyncio
```

运行测试:

```bash
pytest tests/
```
