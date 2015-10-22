Python interface library for Jfrog Artifactory
==============================================

.. image:: https://travis-ci.org/Parallels/artifactory.svg?branch=develop
    :target: https://travis-ci.org/Parallels/artifactory

This module is intended to serve as a logical descendant of `pathlib <https://docs.python.org/3/library/pathlib.html>`_, a Python 3 module for object-oriented path manipulations. As such, it implements everything as closely as possible to the origin with few exceptions, such as stat().

Usage Examples
--------------

Walking Directory Tree
~~~~~~~~~~~~~~~~~~~~~~

Getting directory listing:

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://repo.jfrog.org/artifactory/gradle-ivy-local")
    for p in path:
        print p


Find all .gz files in current dir, recursively:

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://repo.jfrog.org/artifactory/distributions/org/")
    
    for p in path.glob("**/*.gz"):
        print p


Downloading Artifacts
~~~~~~~~~~~~~~~~~~~~~

Download artifact to a local filesystem:

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://repo.jfrog.org/artifactory/distributions/org/apache/tomcat/apache-tomcat-7.0.11.tar.gz")
        
    with path.open() as fd:
        with open("tomcat.tar.gz", "wb") as out:
            out.write(fd.read())


Uploading Artifacts
~~~~~~~~~~~~~~~~~~~

Deploy a regular file ``myapp-1.0.tar.gz``

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/libs-snapshot-local/myapp/1.0")
    path.mkdir()
    
    path.deploy_file('./myapp-1.0.tar.gz')


Deploy a debian package ``myapp-1.0.deb``

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/ubuntu-local/pool")
    path.deploy_deb('./myapp-1.0.deb', 
                    distribution='trusty',
                    component='main',
                    architecture='amd64')


Authentication
~~~~~~~~~~~~~~

To provide username and password to access restricted resources, you can pass ``auth`` parameter to ArtifactoryPath:

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/myrepo/restricted-path",
        auth=('admin', 'ilikerandompasswords'))
    path.touch()


SSL Cert Verification Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See `Requests - SSL verification <http://docs.python-requests.org/en/latest/user/advanced/#ssl-cert-verification>`_ for more details.

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/libs-snapshot-local/myapp/1.0")

... is the same as

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/libs-snapshot-local/myapp/1.0", 
        verify=True)

Specify a local cert to use as client side certificate

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/libs-snapshot-local/myapp/1.0",
        cert="/path_to_file/server.pem")

Disable host cert verification 

.. code-block:: python

    from artifactory import ArtifactoryPath
    path = ArtifactoryPath(
        "http://my-artifactory/artifactory/libs-snapshot-local/myapp/1.0",
        verify=False)

**Note:** If host cert verification is disabled urllib3 will throw a `InsecureRequestWarning <https://urllib3.readthedocs.org/en/latest/security.html#insecurerequestwarning>`_.  
To disable these warning, one needs to call urllib3.disable_warnings().

.. code-block:: python

    import requests.packages.urllib3 as urllib3
    urllib3.disable_warnings()


Global Configuration File
~~~~~~~~~~~~~~~~~~~~~~~~~

Artifactory Python module also has a way to specify all connection-related settings in a central file, ``~/.artifactory_python.cfg`` that is read upon the creation of first ``ArtifactoryPath`` object and is stored globally. For instance, you can specify per-instance settings of authentication tokens, so that you won't need to explicitly pass ``auth`` parameter to ``ArtifactoryPath``.

Example:

.. code-block:: ini

    [http://artifactory-instance.com/artifactory]
    username = deployer
    password = ilikerandompasswords
    verify = false

    [another-artifactory-instance.com/artifactory]
    username = foo
    password = @dmin
    cert = ~/mycert


Whether or not you specify ``http://`` or ``https://`` prefix is not essential. The module will first try to locate the best match and then try to match URLs without prefixes. So if in the config you specify ``https://my-instance.local`` and call ``ArtifactoryPath`` with ``http://my-instance.local``, it will still do the right thing.
