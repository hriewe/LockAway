# LockAway

This computationally expensive and impractical program locks your MacBook when you walk away from it.

## Overview

Apple is rumored to release a new generation of MacBook Pro computers soon. It is of my prdiction that the company will switch from TouchID to FaceID on the new rigs and this program is how I believe they could implement an optional feature to lock a users Mac when not in use. Using FaceID, the computer could keep tabs on if the owner or any registerd faces are currently working on the laptop, and if not, lock the screen until the user is back in front of it.

## My Implementation

This program uses OpenCV to continuously monitor the webcam for faces. If a face is not detected for a customaizable amount of frames, the Mac will lock. It is impractical and expensive becuase the webcam is running and frames are being analized in real-time. Apple would be able to use their FaceID technology to implement this in a better way. This is only a bad proof of concept that I thought would be fun to try and implement with Python.
