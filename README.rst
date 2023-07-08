#pygwidgets  (pronounced as: "pig wijits")

An open collection of user interface widgets for use with pygame development.

7/23  Version 1.1

        SpriteSheetAnimationCollection class added
        
        AnimationCollection class added
        
        TextRadioButton: Added optional color for text and circle (radio button)
        
        Added ability to work with PyInstaller to create executable application
        |            (builds proper paths on-the-fly)
                    
        SoundEffect class added
        
        BackgroundSound class added
        
        Button classes: added activationKeysList to press a button based on any list of keys    
        |    (enterToActivate still works and builds the list of activation keys for you)
            
        CheckBox classes: Added toggleValue() method
        
3/23 Version 1.0.4

        Image - fixed two scale and rotate bugs (thanks to Lando Chan)
        
        TextInput - add setLoc to work correctly when moving an input field (thanks to Renato Monteiro)
        
        SpriteSheetAnimation - fixed bug in splitting images (thanks to Alex Stamps)
        
        Button classes: 'soundOnClick' didn't do anything ... now plays the sound on click



To install, open the command line and enter the following:

  python3 -m pip install -U pip --user
  
  python3 -m pip install -U pygwidgets --user
  
The first command ensures that you have the latest version of pip (the installer).

The second line installs the latest version of pygwidgets from PyPI into the
site-packages folder on your computer, so that this package is available to all
of your Python programs.

Documentation can be found at:  https://pygwidgets.readthedocs.io/en/latest/


If you have questions or are interested in making additions, please contact me:  

Irv at furrypants dot com