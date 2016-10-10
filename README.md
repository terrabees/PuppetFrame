# PuppetFrame
API bootstrap built using Falcon Framework.

When you want to build a RESTful API using Python, here you have the easiest way to kickstart. PuppetFrame contains all the files and classes that you can use to quickly deploy a working API in less than fifteen minutes.

## What is it?

1. Runs on Python 3.x
2. Built using [Falcon Framework](https://falconframework.org/)
3. Provides token-based authentication
  * *Uses Redis as session store*
4. Incorporates production grade data validation ([Voluptuous](https://github.com/alecthomas/voluptuous))
5. Full HTTP verbs support (OPTIONS, GET, POST, PUT, DELETE)
6. Uses [SQLAlchemy](http://www.sqlalchemy.org/) for ORM
6. Provides ready-to-use JSON output manager

## Installation

1. Fork this repository to your own account. DO NOT CLONE THIS REPO DIRECTLY.

2. Clone your fork.
    ```bash
    $ git clone https://github.com/<USERNAME>/PuppetFrame
    ```
    
3. Create a Python virtual environment (requires Python 3.x)
    ```bash
    $ python -m venv PuppetFrameEnv
    ```
    
    Read more about creating virtual environments [here](https://docs.python.org/3/library/venv.html).

4. Activate virtual environment
    ```bash
    $ source PuppetFrameEnv/bin/activate
    ```
    
5. Install required packages
    ```bash
    $ pip install -r PuppetFrame/requirements.txt
    ```
    
6. Invoke the web server
    ```bash
    $ cd PuppetFrame
    $ gunicorn index:app
    ```
    
    Now the API must be available at http://127.0.0.1:8000
    
## Configuring databases
Now you can't do pretty much anything until the databases are configured. MySQL is expected to be the master database and Redis for the session storage. Once you have the credentials for both MySQL and Redis, you must create a credential file in your home folder. Credential files are never a part of your version controlled codebase because of their sensitive nature.

* Create a file `~/config/puppet/db_config.ini`. Create the folders if they don't exist.
    ```bash
    $ mkdir -p ~/config/puppet
    $ vi ~/config/puppet/db_config.ini
    ```

* Populate it with following text and replace with appropriate values:
    ```dosini
    [PUPPET]
    Host = mysqlhost.example.com
    Port = 3306
    Database = puppet
    Username = myuser
    Password = 12345

    [SESSION-CACHE]
    Host = redishost.example.com
    Port = 6379
    Database = 0
    ```

* Now you have the config file, you should say the script where to find it. Open the file `config/__init__.py` and replace the following value with the right one:
    ```python
    DB_CONFIG_PATH = os.path.expanduser(os.path.join('~', 'config', 'puppet', 'db.ini'))
    ```

* Congrats! Now your API is ready to interact with the MySQL and Redis databases.
    
## Defining MySQL schema
PuppetFrame uses SQLAlchemy as an ORM and thus requires no manual creation of schemas directly in the database. Instead, define your schema in `models/puppet_model.py` and SQLAlchemy will create the required tables for you by running the script file `init/create_schema.py`.

## What's next?
Start with the `index.py` and follow the code. You will be able to build a robust API from here on.

## Contributions
If you are willing to contribute to the project, these are some of the immediate requirements you could consider:
    * Support for XML output
    * Ways to easily customize Voluptuous error messages
