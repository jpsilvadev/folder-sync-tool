# folder-sync-tool

Implementation of one-way folder synchronization

## Usage
- See the available flags

```bash
$ python3 main.py --help
```

```bash
usage: main.py [-h] --source SOURCE --replica REPLICA --log LOG --interval INTERVAL

Folder Sync Tool

options:
  -h, --help            show this help message and exit
  --source, -s SOURCE   Source folder path
  --replica, -r REPLICA
                        Replica folder path
  --log, -l LOG         Log file path
  --interval, -i INTERVAL
                        Interval in seconds
```

- For example, to sync the `Downloads` folder in a Windows machine:

```bash
$ python3 main.py --source C:\Users\user\Downloads --replica C:\Users\user\some-cloud-provider\Downloads --log C:\Users\user\sync_log.txt --interval 60 
```
> Note: `source` and `replica` flags can be used with relative paths

### Sample Log Output
```bash
[INFO] - 2025-02-26 22:15:08,644 - Started Folder Synchronization: C:\Users\user\Downloads -> C:\Users\user\some-cloud-provider\Downloads
[INFO] - 2025-02-26 22:15:08,644 - Created directory: C:\Users\user\some-cloud-provider\Downloads\.
[INFO] - 2025-02-26 22:15:08,645 - Copied file: C:\Users\user\Downloads\desktop.ini -> C:\Users\user\some-cloud-provider\Downloads\.\desktop.ini
[INFO] - 2025-02-26 22:15:08,645 - Synchronization complete. Sleeping for 60 seconds...
[INFO] - 2025-02-26 22:16:08,652 - Created directory: C:\Users\user\some-cloud-provider\Downloads\backgrounds
[INFO] - 2025-02-26 22:16:08,655 - Copied file: C:\Users\user\Downloads\backgrounds\backiee-119980-landscape.jpg -> C:\Users\user\some-cloud-provider\Downloads\backgrounds\backiee-119980-landscape.jpg
[INFO] - 2025-02-26 22:16:08,660 - Copied file: C:\Users\user\Downloads\backgrounds\mountain_dark.png -> C:\Users\user\some-cloud-provider\Downloads\backgrounds\mountain_dark.png
[INFO] - 2025-02-26 22:16:08,664 - Copied file: C:\Users\user\Downloads\backgrounds\mountain_dark_resized.png -> C:\Users\user\some-cloud-provider\Downloads\backgrounds\mountain_dark_resized.png
[INFO] - 2025-02-26 22:16:08,665 - Copied file: C:\Users\user\Downloads\backgrounds\mpiwnicki_smoke.jpg -> C:\Users\user\some-cloud-provider\Downloads\backgrounds\mpiwnicki_smoke.jpg
[INFO] - 2025-02-26 22:16:08,666 - Copied file: C:\Users\user\Downloads\backgrounds\planet-1697196943666-116.jpg -> C:\Users\user\some-cloud-provider\Downloads\backgrounds\planet-1697196943666-116.jpg
[INFO] - 2025-02-26 22:16:08,667 - Synchronization complete. Sleeping for 60 seconds...
[INFO] - 2025-02-26 22:17:08,730 - Deleted file: C:\Users\user\some-cloud-provider\Downloads\backgrounds\backiee-119980-landscape.jpg
[INFO] - 2025-02-26 22:17:08,731 - Deleted file: C:\Users\user\some-cloud-provider\Downloads\backgrounds\mountain_dark_resized.png
[INFO] - 2025-02-26 22:17:08,732 - Synchronization complete. Sleeping for 60 seconds...
[INFO] - 2025-02-26 22:17:10,662 - Stopped Folder Synchronization. Exiting...
```
