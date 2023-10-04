# Empowering-Disabled-Gamers-with-Gesture-Controls-for-Tetris
This is the github project page for my project "Inclusive Gaming Nexus - Empowering Disabled Gamers with Gesture-Controls for Tetris".
Project is made for the contest "Build2gether Inclusive Innovation Challenge".

**What problem are you going to solve?**
Many disabled individuals face barriers when trying to engage in online gaming, which can limit their access to entertainment, social interaction, and skill development. Traditional gaming interfaces may not be adaptable to their needs, making it difficult for them to fully participate in the gaming community.

**What are you going to build to solve this problem? How is it different from existing solutions? Why is it useful?**
I will build an innovative and customizable solution that enables disabled gamers to enjoy a classic game, Tetris, on the online platform tetr.io, using gesture controls. Unlike existing solutions that offer limited adaptability and inclusivity, my project leverages Google Coral Dev Board Micro and Teachable Machine to provide a personalized gaming experience. Users can define their own gesture poses through Teachable Machine, which is then translated into in-game actions, fostering an inclusive and interactive gaming environment.

**How does the solution work?**
My solution operates through a seamless integration of hardware, creating an accessible and enjoyable gaming experience for disabled individuals:

Customizable Gestures:
Users utilize Teachable Machine to train the AI model to recognize their unique hand gestures.
These gestures are personalized to match each user's capabilities and preferences, forming the foundation of their gaming controls.

Gesture Recognition and Translation:
The Google Coral Dev Board Micro, equipped with advanced AI capabilities, processes the real-time visual input of the personalized gestures.
The AI model quickly analyzes the gestures and translates them into corresponding game commands.

Arduino Leonardo Integration:
The Arduino Leonardo acts as an intermediary, receiving the translated commands from the Coral Dev Board Micro.
It then emulates these commands as keyboard inputs, making them compatible with any PC and game.

Tetris on tetr.io Gameplay:
The PC, hosting the Tetris game on tetr.io, receives the keyboard inputs from the Arduino.
The game responds to the commands, enabling users to control the Tetris blocks, rotate, drop, and strategize in real time.

----------------------------------------------------------------------------------------------------------------

My solution offers the following key features:

* Customizable Gestures: Using Teachable Machine, players can train the system to recognize their preferred hand gestures for specific in-game actions, making the gameplay experience tailored to their capabilities.

* Seamless PC Integration: The Arduino Leonardo, acting as a keyboard input device, connects to the PC, ensuring compatibility with any computer setup.

* Real-time Gesture Translation: The Google Coral Dev Board Micro interprets user-defined gestures and converts them into corresponding keystrokes for controlling the Tetris game.

* Accessible Gaming: Through gesture control, disabled gamers can actively participate in both solo, multiplayer and custom games on tetr.io, fostering a sense of community and enabling them to compete and collaborate with other disabled individuals.

* Empowerment and Inclusivity: Our solution is engineered with a focus on disabled individuals, empowering them to overcome traditional interface limitations and participate fully in the gaming world.

* Im thinking about also adding voice recognition using the Google Coral Dev board micro onboard mic to save and use blocks in tetr.io using speach ("Save" and "Use"). It would use google ai voice recognition or opencv voice recognition.

**List the hardware and software you will use to build this**
* Google Coral Dev Board Micro: To interpret user-defined gestures and enable real-time AI-powered gesture recognition.
* Teachable Machine: To customize and teach the AI model to recognize individual user gestures.
* Arduino Leonardo: To translate gesture signals into keystrokes for controlling the Tetris game.
* PC: To host the Tetris game on tetr.io and receive input commands from the Arduino.
* Tetris on tetr.io: The online gaming platform where the gesture-controlled game will be played.
* Arduino IDE
* Visual studio code
* C++, Python
* OpenCV (maybe)
* Tensorflow
