# raspicam-server

## Requirements.
- Raspbery pi hardware. over than `model 4B`.
- Programing modules.
    - over than `Python 3.11`.
- External devices.
    - Microphone connect by usb cable.
    - Camera module connect by FFC cable.

## First step.

### Setup python environment.
- Create venv.
``` bash
$ python -m venv .venv
```

- Activate venv.
``` bash
$ source ./.venv/bin/actvate
```

- Install libraries.
``` bash
$ pip install -r requirements.txt
```

### Add execute permission for shell scripts.
``` bash
$ sudo chmod 755 ./startup.sh
$ sudo chmod 755 ./shellscripts/*/*.sh
```

## Add systemd service.

1. Copy  of `_raspicam-server.service` file in `systemd` directory, after rename to `raspicam-server.service`.
1. Modify your `<Deployment path>` in `raspicam-server.service` of line 5.
1. Create symbolic link in `/etc/systemd/system/raspicam-server.service` from your `raspicam-server.service` file.
    - Sample command
``` shell
$ sudo ln -s /<Deployment path>/raspicam-server/systemd/raspicam-server.service /etc/systemd/system/raspicam-server.service
```
1. Reboot your system.