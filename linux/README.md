# How to use

This script installs many PACKAGES (which you can find in assets/PACKAGES.json) and
configures various things, such as fish shell (alongside aliases etc, which can be
found in assets/config.fish).

To use this script, simply run:
```bash
curl https://raw.githubusercontent.com/sby051/configs/main/linux/setup.sh | bash
```

or more conveniently

```bash
curl -L https://tinyurl.com/linconf | bash
```

All externally installed programs (such as manually installed with curl etc) should be placed in
the ```/opt``` directory.
