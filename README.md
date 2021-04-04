photo-frame-bin
===============
Raspberry Pi Photo Frame Scripts

Details:

* `autostart`
  * Startup script
* `display-init`, `display-status`, `display-power`
  * Manage DPMS state for remote monitor blanking
  * `rest-api.py`
    * Rest API server written in Flask
* `sync-photos.sh`
  * Sync photos from NFS mount to a local cache
    * Once an hour interval by default
      * Defined in crontab
* `start-feh.sh`
  * Watchdog behavior if feh crashes

Dependencies:

* `feh`
*  `xscreensaver`
*  `flask`

Installation:

1. Clone repo

  ```
  git clone https://github.com/therivenman/photo-frame-bin.git ~/bin
  ```

2. Install startup script

  ```
  rm ~/.config/lxsession/LXDE-pi/autostart
  ln -s ~/bin/autostart ~/.config/lxsession/LXDE-pi/autostart
  ```
3. Install crontab

  Add this in to your crontab (`crontab -e`):

  ```
  0 * * * * /home/pi/bin/sync-photos.sh
  ```
  
4. Add NFS mount

  Add this line to the end of `/etc/fstab`:

   ```
   nas:/volume1/Photos /nas-photos nfs defaults 0 0
   ```
