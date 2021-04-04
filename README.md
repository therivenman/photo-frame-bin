photo-frame-bin
===============
Raspberry Pi Photo Frame Scripts

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
