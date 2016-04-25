# Django-Turbo-Crate
Demo Server used to showcase a file server from which a user can upload and
download files.

File actions are limited to the user who uploaded them and there is a max file
size which can be set by an administrator in forms.py

Additionally, the server demonstrates both POST and GET calls, the former being
used for uploading and the later for downloads.

==================
RUNNING THE SERVER
==================

From the file server directory:
> python manage.py runserver [port number]

=====================
USING THE APPLICATION
=====================

Creating a new login:

The login form doubles for both logging in and signing up. If an email address
is entered which does not exist in the database, it will immediately create a
new account using that address. In either case, the user will be redirected to
the upload page unless they enter an incorrect password, in which case they will
be redirected back to the login page.

Uploading and Downloading:

File uploading is accomplished by selecting a file and then pressing the upload
button. File size validation is only done server side so as to avoid Additional
complexity and if the file is too large it will simply be dropped. Whether
the upload is successful or not, the user will be redirected back to the upload
page. However, if upload is successful, a new download link will appear on this
page. The server itself will of course also hold a new copy of the uploaded
file.

Trying to access either the upload or downloading pages without being logged in
will redirect the user to the login page. This can be tested by manually typing
in the url "/logout", which will terminate the current login credentials.
