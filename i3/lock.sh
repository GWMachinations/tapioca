#configure lock screen
#https://michaelabrahamsen.com/posts/custom-lockscreen-i3lock/
# set the icon and a temporary location for the screenshot to be stored
icon="~/.config/i3/thin-logo.png"
tmpbg='/tmp/screen.png'

# take a screenshot
scrot "$tmpbg"

# blur the screenshot by resizing and scaling back up
convert "$tmpbg" -filter Gaussian -thumbnail 20% -sample 500% "$tmpbg"

# overlay the icon onto the screenshot
convert "$tmpbg" "$icon" -gravity center -composite "$tmpbg"

# lock the screen with the blurred screenshot
i3lock -i "$tmpbg"

#lock screen and set power timeout
#set power management features
#xset -display :1 dpms 0 300 0
