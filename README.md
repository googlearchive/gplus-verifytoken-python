# Token Verification for Python 

## System requirements

*   [Python 2.7](http://www.python.org/getit/)

Requirements that are installed as part of this sample:

*   [Flask](http://flask.pocoo.org/)
*   [Flask-KVSession](https://pypi.python.org/pypi/Flask-KVSession)
*   [Google APIs Client Library for Python](https://developers.google.com/api-client-library/python/start/installation)

## Step 1: Enable the Google+ API

Create a Google APIs Console project, OAuth 2.0 client ID, and register your
JavaScript origins:


1.  In the [Google APIs Console](https://developers.google.com/console), select
    **Create** from the pull-down menu on the left, and enter a project name
    (such as "Sample").
1.  In the [Services pane](https://code.google.com/apis/console/?api=plus#:services),
    enable the **Google+ API** and any other APIs that your app requires.
1.  In the [API Access](https://code.google.com/apis/console/#:access)
    pane, click **Create an OAuth 2.0 Client ID**.
    
    1. In the **Product name** field, enter a name for your application
        (such as "Sample"), and click **Next**. Providing a product logo is optional.
    1. In the **Client ID** Settings section, do the following:
          * Select **Web application** for the Application type.
          * Click the **more options** link.
          * In the **Authorized Redirect URIs** field, delete the example URI.
          * In the **Authorized JavaScript Origins** field, add the
              first of the following URLs for development. The last example is of a production URL.
              * `http://localhost:4567`
              * `https://mysite.example.com`

          * Click the **Create client ID** button.
1.  In the [API Access pane](https://code.google.com/apis/console/#:access),
    locate the section **Client ID for web applications** and note or copy
    the **Client ID** and **Client secret** that you will need later to
    run the sample

## Step 2: Set up the Python token verification app

1. Get the latest version of the token verification app. One way is to use git to clone
   the application repository.

        git clone https://github.com/googleplus/gplus-verifytoken-python.git

      Or, [download the application as a zip file](https://github.com/googleplus/gplus-verifytoken-python/archive/master.zip), and extract the library and sample code:

        wget https://github.com/googleplus/gplus-verifytoken-python/archive/master.zip
        unzip gplus-verifytoken-python-master.zip

1. Change directory into the sample app

        cd gplus-verifytoken-python

1. Install the requirements of this token verification app

        pip install -r requirements.txt

1. Edit `client_secrets.json`, and replace `YOUR_CLIENT_ID`
   with the values that you generated in Step 1.

## Step 3: Run the application

After you set up your Google API project and configure the sample app,
the app is ready to run.

Because you registered `http://localhost:4567` as an **Authorized JavaScript
origin** in the [Google APIs Console](//code.google.com/apis/console/#:access),
you will run the sample from that location.

1. Run the Python token verification app:

        python verify.py

1. Browse to your token verification app, which by default is at
   [http://localhost:4567](http://localhost:4567).

After you sign in, the application uses the JavaScript client to retrieve your
profile and uses the Python client library to retrieve the
people visible to the app.

