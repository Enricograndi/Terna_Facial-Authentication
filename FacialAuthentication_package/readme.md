# Terna_Facial Authentication
 Project for the exam of Lab of software project devolpement

 Team Members: 
 Enrico Grandi 989993
 Tommaso Spessato 873197
 ...

In this repository you can find a file named ```main.py``` that try to simulate a database with a double authetication. The first with an easy password and the latter with a face match thanks to some API, either given by the user. (:warning: ... Pay attention the password).
  
In order to run the program some [parameters](#Command-line-parameters) are required.

If you run the program, executing the main file with: 

```$ python main.py -u totti -p totti -i data\test\totti.png``` the software will try a autentication test:
```
$ python main.py -u totti -p totti -i data\test\totti.png 
....
```
> **Note:** the project requires the following modules to run: *argparse, sqlite3, random, hashlib, os, CSV, cloudmersive_image_api_client, Image,
paramiko... unittest* and *sys*.


[Cloudmersive](https://cloudmersive.com//) is an on-line service that provides some API that allow to use some visual resource via cloaudm. The APIs are documented in a [API documentation page](https://api.cloudmersive.com/), they also provide an [Online console](https://api.cloudmersive.com/swagger/index.html?urls.primaryName=Image%20Recognition%20and%20Processing%20API)

## How does it work?
First of all, it is required to fill the database with almost one user, we did it with "totti". When Totti try to authenticate, he will pass to the terminal his name, password and the path where its image is. So, because the the free plan of the API, it is required to upload an image  that is smaller than 3.4MB and to avoid problems, we wrote a function that comprime if it is bigger. Than, the image will be saved to a temporary folder, in order to allow, the software to decript the binary and convert to jpg the image given when Totti was added. After all, the two images will be used to perform a match with the cloudmersive API. For more details, check on documentation.  

 
## Documentation :notebook_with_decorative_cover:
Documentation can be found in: ```docs/_build/html/index.html``` and provides infos about the functions you can find in the various modules.
 
To read them with your **default browser**, from the main folder use ```$ open docs/_build/html/index.html``` or, for other browsers you may have installed, follow these examples:
- **Chrome:** ```$ open -a "Google Chrome" docs/_build/html/index.html```
- **Safari:** ```$ open -a "Safari" docs/_build/html/index.html```


**DOCUMENTATION MADE WITH: [Sphinx](http://www.sphinx-doc.org/en/master/).**

We followed this [Tutorial](https://medium.com/better-programming/auto-documenting-a-python-project-using-sphinx-8878f9ddc6e9)

## Data Files :open_file_folder:

## Command line parameters :computer:
As we have mentioned in the first section, some command line parameters are required in order to run the main script.
#### Positional arguments
- **symbol**: The ticker (or stock) symbol associated with stocks of a company. **Only one** symbol can be passed.
> **Note:** You can access tickers (and add more! :heavy_plus_sign:) here: ```stock_package/data/allowed_companies.csv```.