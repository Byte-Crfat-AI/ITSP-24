#Project Setup
After activating git in your folder and importing the code in it, make sure you activate a virtual env by the name of 'vienv' and then install any libraries as needed. 
Before beginning do 'pip install -r requirements.txt' , that will download all the necessary libraries with thier versions.
Also if you install a new one , make sure you install after activating venv and at end do 'pip freeze > requirements.txt'

!!Warning: Please Push the commits with cautions, check if all the features work and none of the other code is disturbed by the changes before pushing.


# ITSP-24
Our project involves a lot of learning and requires consistent work everyday.. Learn and do at your own pace.. We will assign small tasks once in 2 days for everyone.. and check whether the task is been done and if faces any issue tag the mentor and ask the doubts
Subtasks:
  Create a Backend with Django or nodejs
  Do research on how to integrate our IoT with this backend
  Learn encryption and decryption and integrate with the backend
  Once all these are done and the webserver's backend part completely done make a frontend for it
Application:
  to be started only when the webserver part is done
  Learn Computer Vision and Open CV
  get data set in order to train our model
  CV requires a lot of memory , but a CCTV camera cannot have that much memory, think on how to use cloud storage for this and research on this. But there is a disadvantage of using cloud storage , there will be a lag as it requires time to transmit ----> find an optimum way to do this
  make an app associated with this and the app should send notification to the user once spots an unknown person, make a database that has known faces... Some features of this app are user register and login via OTP through SMS and email(2 step verification), able to select and delete the saved faces or update (POST, PATCH,DELETE,PUT) using all these methods
