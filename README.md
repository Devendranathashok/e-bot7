# e-bot7
Part 1: Basic docker application

Note: For docker images you may use anything that is available on docker hub. You may use the original images or build new images based on the originals as you see fit.

1.1 Simple web page

Create a docker image based on nginx which will serve a very simple web page. The contents of the page should be “Hello from e-bot7!”.

Secure the web app with HTTP basic auth. Add a user named admin with password e-bot7.

1.2 Access logs to MongoDB

Each access to the page should result in the creation of a new document in the MongoDB collection named access. We want to save the user agent string, the date of the access and the response code.

1.3 Notifications

Let's assume we want to be notified when the access was denied more than 10 times total, e.g. because the user entered the wrong password. Create a script that counts the number of access denials and sends an email to some address (you can send it to yourself for testing) if that number is above 10.

Note: the email might be rejected or marked as spam on the receiving end. Why would that happen and how could you mitigate it? (It's not necessary to fix this now since it might take up too much time, so just tell us what you would do.)

The access-denied counter script should be run periodically. Create an image that runs the script once every 20 minutes.

1.4 docker-compose file

Create a docker-compose file that manages the entire application described above. Running docker-compose up should start everything
