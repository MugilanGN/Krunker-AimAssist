# Krunker AimAssist
Automatically moves the mouse to enemies surrounding the player's crosshair. This increases the user's chances of getting a kill and can be considered a hack

It uses OpenCV to process screenshots from the browser window in order to find enemy healthbar's. Through the healthbar it can assume where the enemy is located through distance and size manipulation.

After finding the enemy, it uses Pyautogui to move the mouse exactly and instantaneously to the enemy, leaving the user with only the task of clicking

# V1:

Used the enemies username to find their location. Some issues inlcuded the inability to identify whether the target is a teammate or not. Also somewhat inaccurate due to different length usernames, and the leaderboard score next to the username interfering with detection. False positives in maps such as Littletown, and especially Subzero, render it nearly unusable.

# V2:

Instead of looking for the usernames, the strategy has shifted to finding the healthbars, due to their consistent width and height for all players, and their scaling effect at distances. This version faces far less detection issues due to the red nature of enemy healthbars, but the green color of teammate healthbar's. Improvements include:

  - Teammate detection, therefore it no longer tracks teammates in Deathmatch and Hardpoints
  
  - Increased accuracy due to the healthbars being uneditable and uniform
  
  - Less false positives due to the red hues of the healthbar being very unique to it, compared to the white usernames which would       accidently see lamps and the snow in Subzero
  
  - Depth detection helps increase accuracy as the healthbar scales over distance. There are some intrinsic problems as the healthbar does not follow a constant scale factor, due to the integer property of pixels. This is still a work in progress
 
