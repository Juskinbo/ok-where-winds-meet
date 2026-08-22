# ok-where-winds-meet

[English](README_en.md) | 中文

ok-where-winds-meet 是一个基于 [ok-script](https://github.com/ok-oldking/ok-script) 的《燕云十六声》(Where Winds Meet) Windows 自动化应用。

## 文档

完整文档见 MkDocs 网站：

- [文档首页](docs/index.md)
- [快速开始](docs/getting-started.md)
- [应用与运行目标配置](docs/configuration.md)
- [任务开发](docs/tasks.md)
- [打包与发布](docs/release.md)
- [English documentation](docs/en/index.md)

## 快速预览

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --index-url https://pypi.org/simple/ --upgrade pip
python -m pip install --index-url https://pypi.org/simple/ --no-deps --upgrade -r requirements.txt
python main_debug.py
```

直接依赖统一维护在 `pyproject.toml`。`requirements.txt` 是 Qt profile 的锁定文件，请勿直接编辑。

## 致谢

- [ok-script](https://github.com/ok-oldking/ok-script)
- [OnnxOCR](https://github.com/ok-oldking/OnnxOCR)
- [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)