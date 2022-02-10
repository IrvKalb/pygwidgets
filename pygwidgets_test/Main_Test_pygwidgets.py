#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

# 1 - Import libraries
import os
import sys
# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets


# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30

# The function and Test class and method below are not required.
# These are only here as a demonstration of how you could use a callback approach to handling events if you want to.

# Define a function to be used as a "callBack"
def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, a button was clicked')
    else:
        print('In myFunction, the button named', theNickname, 'was clicked')

# Define a class with a method to be used as a "callBack"
class Test():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, a button was clicked')
        else:
            print('In myMethod, the button named', theNickname, 'was clicked')


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # create a clock object
oTest = Test()
 
# 4 - Load assets: image(s), sounds,  etc.
oBackgroundImage = pygwidgets.Image(window, (0, 0), 'images/background.jpg')
oDisplayTextTitle = pygwidgets.DisplayText(window, (0, 20), 'pygwidgets example by Irv Kalb', 
                                    fontSize=36, width= 640, textColor=BLACK, justified='center')

oInputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text',
                                    textColor=WHITE, backgroundColor=BLACK,
                                    fontSize=24, width=250)

oInputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True,
                                    textColor=(0, 0, 255),
                                    fontSize=28)  # add: , mask='*' for passwords


oDisplayTextA = pygwidgets.DisplayText(window, (20, 300), 'Here is some display text', 
                                    fontSize=24, textColor=WHITE, justified='center')

oDisplayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text', 
                                    fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oRestartButton = pygwidgets.CustomButton(window, (100, 430), 
                                    'images/restartButtonUp.png',
                                    down='images/restartButtonDown.png',
                                    over='images/restartButtonOver.png',
                                    disabled='images/restartButtonDisabled.png',
                                    soundOnClick='sounds/blip.wav',
                                    nickname='restartButton',
                                    callBack=myFunction)  #  callBack here is not required

# oCheckBoxA controls the availability the custom radio buttons
# oCheckBoxB controls the availability of the text radio buttons
oCheckBoxA = pygwidgets.CustomCheckBox(window, (450, 110), value=True,
                            on='images/checkBoxOn.png', off='images/checkBoxOff.png', 
                            onDown='images/checkBoxOnDown.png', offDown='images/checkBoxOffDown.png', 
                            onDisabled='images/checkBoxOnDisabled.png', offDisabled='images/checkBoxOffDisabled.png')

oRadioCustom1 = pygwidgets.CustomRadioButton(window, (500, 150), 'Custom Group', 
                            on='images/RadioLowOn.png', off='images/RadioLowOff.png', 
                            onDown='images/RadioLowOnDown.png', offDown='images/RadioLowOffDown.png', 
                            onDisabled='images/RadioLowOnDisabled.png', offDisabled='images/RadioLowOffDisabled.png', 
                            value=True, nickname='Low')

oRadioCustom2 = pygwidgets.CustomRadioButton(window, (500, 190), 'Custom Group', 
                            on='images/RadioMedOn.png', off='images/RadioMedOff.png', 
                            onDown='images/RadioMedOnDown.png', offDown='images/RadioMedOffDown.png', 
                            onDisabled='images/RadioMedOnDisabled.png', offDisabled='images/RadioMedOffDisabled.png', 
                            value=False, nickname='Med')

oRadioCustom3 = pygwidgets.CustomRadioButton(window, (500, 230), 'Custom Group', 
                            on='images/RadioHighOn.png', off='images/RadioHighOff.png', 
                            onDown='images/RadioHighOnDown.png', offDown='images/RadioHighOffDown.png', 
                            onDisabled='images/RadioHighOnDisabled.png', offDisabled='images/RadioHighOffDisabled.png', 
                            value=False, nickname='High')

oCheckBoxB = pygwidgets.TextCheckBox(window, (450, 295), 'Allow Radio Buttons')

oRadioText1 = pygwidgets.TextRadioButton(window, (500, 320), 'Default Group', 'Radio Text 1', 
                                      value=False)

oRadioText2 = pygwidgets.TextRadioButton(window, (500, 360), 'Default Group', 'Radio Text 2', 
                                      value=True)

oRadioText3 = pygwidgets.TextRadioButton(window, (500, 400), 'Default Group', 'Radio Text 3', 
                                      value=False)

oStatusButton = pygwidgets.TextButton(window, (500, 430), 'Show Status',
                                     callBack=oTest.myMethod)  # callBack here is not required

oDragger = pygwidgets.Dragger(window, (300, 200), 
                        'images/dragMeUp.png', 
                        'images/dragMeDown.png', 
                        'images/dragMeOver.png', 
                        'images/dragMeDisabled.png', 
                        nickname='My Dragger')

oPythonIcon = pygwidgets.Image(window, (15, 500), 'images/pythonIcon.png')

oImageCollection = pygwidgets.ImageCollection(window, (400, 490), 
                                {'start':'imageStart.jpg', 
                                 'left':'imageLeft.jpg', 
                                 'right':'imageRight.jpg', 
                                 'up':'imageUp.jpg', 
                                 'down':'imageDown.jpg'}, 
                                'start', path='images/')

oImageInstructions = pygwidgets.DisplayText(window, (400, 595), 'Click then type l, r, d, u, s, or Space')


oIconInstructions = pygwidgets.DisplayText(window, (15, 595),
                                          'Click then up or down arrow to resize,\n' + 
                                          'left or right arrow to rotate, \n' + 
                                          'h or v to flip horizontal or vertical')

oFrisbeeImage = pygwidgets.Image(window, (562, 2), 'images/frisbee.png')



# 5 - Initialize variables
counter = 0
angle = 0
pct = 100

# 6 - Loop forever
while True:

    # 7 - Check for and handle events

    for event in pygame.event.get():
       # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if oInputTextA.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextA.getValue()
            print('The text of oInputTextA is: ' + theText)

        if oInputTextB.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextB.getValue()
            print('The text of oInputTextB is: ' + theText)

        if oRestartButton.handleEvent(event):  # clicked
            counter = 0
            print('Content of first input text is:', oInputTextA.getValue())
            print('Content of second input text is:', oInputTextB.getValue())


        if oCheckBoxA.handleEvent(event):  # toggled
            aOn = oCheckBoxA.getValue()
            print('oCheckBoxA was clicked, new value is:', aOn)
            if aOn:
                oRadioCustom1.enable()
                oRadioCustom2.enable()
                oRadioCustom3.enable()
            else:
                oRadioCustom1.disable()
                oRadioCustom2.disable()
                oRadioCustom3.disable()
        if oRadioCustom1.handleEvent(event):  # selected
            print('Radio button custom1 was clicked')

        if oRadioCustom2.handleEvent(event):  # selected
            print('Radio button custom2 was clicked')

        if oRadioCustom3.handleEvent(event):  # selected
            print('Radio button custom3 was clicked')

        if oCheckBoxB.handleEvent(event):  # toggled
            bOn = oCheckBoxB.getValue()
            print('oCheckBoxB was clicked, new value is:', bOn)
            if bOn:
                oRadioText1.enableGroup()  # disable all buttons in this group
                # could alternatively have have used (does the same as):
                # oRadioText1.enable()
                # oRadioText2.enable()
                # oRadioText3.enable()
            else:
                oRadioText1.disableGroup()    # enable all radio buttons in group that contains this radio button
                # could alternatively have used (does the same as):
                # oRadioText1.disable()
                # oRadioText2.disable()
                # oRadioText3.disable()

        if oRadioText1.handleEvent(event):  # selected
            print('Radio button text1 was clicked')

        if oRadioText2.handleEvent(event):  # selected
            print('Radio button text2 was clicked')

        if oRadioText3.handleEvent(event):  # selected
            print('Radio button text3 was clicked')

        if oStatusButton.handleEvent(event):  # clicked
            nickname = oRadioCustom1.getSelectedRadioButton()
            print('The currently selected custom Radio Button is:', nickname)
            nickname = oRadioText1.getSelectedRadioButton()
            print('The currently selected Text Radio Button is:', nickname)

        if oDragger.handleEvent(event):
            print('Done dragging, dragger nickname was:', oDragger.getNickname())
            print('  Mouse up at:', oDragger.getMouseUpLoc())
            print('  Dragger is now located at', oDragger.getLoc())

        if oPythonIcon.handleEvent(event):
            print('Got click on the Python icon')

        if oImageCollection.handleEvent(event):
            print('Got click on image collection')

        if oFrisbeeImage.handleEvent(event):
            print('Got click on the frisbee image')


        if event.type == pygame.KEYDOWN:
            if oPythonIcon.getFocus():
                if event.key == pygame.K_h:
                    oPythonIcon.flipHorizontal()
                elif event.key == pygame.K_v:
                    oPythonIcon.flipVertical()
            if oImageCollection.getFocus():
                if event.key == pygame.K_l:
                    oImageCollection.replace('left')
                elif event.key == pygame.K_r:
                    oImageCollection.replace('right')
                elif event.key == pygame.K_u:
                    oImageCollection.replace('up')
                elif event.key == pygame.K_d:
                    oImageCollection.replace('down')
                elif event.key == pygame.K_s:
                    oImageCollection.replace('start')
                elif event.key == pygame.K_SPACE:
                    oImageCollection.replace('')



    keyPressedList = pygame.key.get_pressed()
    if keyPressedList[pygame.K_LEFT]:
        oPythonIcon.rotate(-5)
    if keyPressedList[pygame.K_RIGHT]:
        oPythonIcon.rotate(5)

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  oPythonIcon.rotateTo
    if keyPressedList[pygame.K_UP]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        pct = pct + 10
        oPythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        #print('Scaling up to', pct, '%')
    if keyPressedList[pygame.K_DOWN]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        if pct > 0:
            pct = pct - 10
        oPythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        #print('Scaling down to', pct, '%')
 


    # 8  Do any "per frame" actions
    counter = counter + 1
    oDisplayTextA.setValue('Here is some centered display text.\n' + 
                         'Showing the \nnumber of frames.\nLoop counter:' + str(counter))
    oDisplayTextB.setValue('Here is some display text.  Loop counter:' + str(counter))
    
    # 9 - Clear the window
    oBackgroundImage.draw()

    # 10 - Draw all window elements
    oPythonIcon.draw()
    oDisplayTextTitle.draw()
    oInputTextA.draw()
    oInputTextB.draw()
    oDisplayTextA.draw()
    oDisplayTextB.draw()
    oRestartButton.draw()
    oCheckBoxA.draw()
    oRadioCustom1.draw()
    oRadioCustom2.draw()
    oRadioCustom3.draw()
    oCheckBoxB.draw()
    oRadioText1.draw()
    oRadioText2.draw()
    oRadioText3.draw()
    oStatusButton.draw()
    oDragger.draw()
    oImageCollection.draw()
    oFrisbeeImage.draw()
    oImageInstructions.draw()
    oIconInstructions.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait 
