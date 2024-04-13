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
python -m venv .venv
```

- Activate venv.
``` bash
source ./.venv/bin/activate
```

- Install libraries.
``` bash
pip install -r requirements.txt
```

### Add execute permission for shell scripts.
``` bash
sudo chmod 755 ./startup.sh
sudo chmod 755 ./shellscripts/*/*.sh
```

## Manual startup.

1. Change your deployment directory.
2. Execute command `./startup.sh`.

## Auto startup by systemd service.

1. Copy  of `_raspicam-server.service` file in `systemd` directory, after rename to `raspicam-server.service`.
2. Modify your `<Deployment path>` in `raspicam-server.service` of line 5.
3. Create symbolic link in `/etc/systemd/system/raspicam-server.service` from your `raspicam-server.service` file.
    - Sample command
``` shell
$ sudo ln -s /<Deployment path>/raspicam-server/systemd/raspicam-server.service /etc/systemd/system/raspicam-server.service
```
4. Reboot your system.
