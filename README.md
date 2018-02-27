# Google Takeout and Transfer: Tools and Guide for Code and Asset Transfer

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1185158.svg)](https://doi.org/10.5281/zenodo.1185158)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/samapriya)

Command Line Interface Allows you to copy all codes and assets from one Google account to another

**Note: This is something that I have tested and have designed only for a windows machine with python 2.7.14 but can be easily ported into an different operating system. Use these tool and steps at your own risk and backup your scripts always just in case.**

If you still want to proceed which I assume you do in case you are still reading, I am including descriptions links to the tool I made and the steps I used to achieve the same. The tool is a single command line interface with three sections.

**Before you do this make sure of a few things**

* _Both your google accounts have an external password, since it requires that to download and perform a lot of the operations. Also enable [__Let Less Secure App use your account_][1]_ on both these accounts._
* _Your system has native python available in terminal or command prompt depending on what kind of system you are using. You can check this by typing_ `python --version`
* _Git is installed on your system. For windows you can find [__installation here_][2]
* _Earth Engine Command Line(earthengine cli) interface is installed, instructions are in the [__developer page_][3]
* _You have authenticated earthengine cli using _`earthengine authenticate`
* _Make sure you visit the [__git source for your account_][4]_ within earth engine and allow access._
* _Check git is accessible via your system path type_ `git help` _and check if the system can reach installed git command line tools._

Now we setup and install the tool by running the following set of steps. The Github repository containing this tool and codes [can be found here][5]

For windows [download the zip here][6] and after extraction go to the folder containing "setup.py" and open command prompt at that location and type
    
    
    python setup.py install  
    pip install -r requirements.txt

Now call the tool for the first time, by typing in `geetakeout -h`. This will only work if you have python in the system path which you can test for opening up terminal or command prompt and typing `**python**.` If you want, you don't have to install the tool to use it you can browse to the folder geetakeout inside the main zipped folder. You can then call the tool by simple

`python geetakeout.py -h`

The housekeeping and credential setup is optional since most of you have probably installed the earthengine cli and authenticated it using `**earthengine authenticate**.`

&gt; **Anatomy of the Process: How to transfer step by step**

Getting first things out of the way is to understand the three sections of this tool. To make life and this process simpler I designed the tool to have a flow so you can run these tools one after the other. The _EE Setup and Housekeeping_ sections are optional&nbsp;, since I will generally updated the selenium driver for mozilla and it assumes you have authenticated your earthengine CLI&nbsp;. The tool might show an error if you have not authenticated using earthengine authenticate
    
    
    If you have installed the tool run
    geetakeout -h
    
    If you have migrated into the folder
    python geetakeout.py -h

![][7]

The GEE Takeout Tool CLI&nbsp;printout

**Setting up the case study**

For this blog I decided to make the transfer simple I have a university account but since my university if shifting umail services to a google app service it means my domain would change from @umail.iu.edu to @iu.edu which are separate accounts. I created the iu.edu GEE account recently.

![][8]

Code Editor comparison Left(my @umail account and right my @iu&nbsp;account)

This also means that the root path for my home folder and repository are different. The idea is simple to be able to replicate the codes and assets from one account to the other. This includes every type if assets including collections but also making sure that the structure of the folders are same. That being said you will still have to change the home path in the codes but if the structure is same then only a single root-path changes.

![][9]

Comparing the root path and assets folder for both&nbsp;accounts

So now that we have a setup, I am going to approach it step by step and have a walk through to explain the process better.

**Step 1: Getting your Repository Lists(gee_repo)**

This assumes that you have visited the Git Source for your codes in Google Earth Engine and authorized it. If not [allow it here][4] and then you are set to download your repo contents and perform git operations. The tool is setup for accessing all repositories that are shared with you. This downloads the list into an html file which can then be parsed for your repositories.

![][10]

Create GEE Repo&nbsp;List

**Step 2: Setting up your Git with Earth Engine Credentials(git_auth)**

You can do this using two methods

* The first simple includes you visiting your [gitsource account page ][4]that we accessed earlier and click `**Generate Password **`and follow instructions.

I am going to talk more about the second method because this eliminates the need to get the password again and again since it is save as passkey. This will authenticate your git client with your git password using a browser less login and also store your gitkey

![][11]

GIT Auth (saves git&nbsp;key)

We will use this again to setup our second account post authorization. This will print our gitkey location and make sure you copy that so you can swap in out as needed. Note the name of the key is in the format `**git-"username"**`** **in this case it is `**git-roysam**`

**Step 3: Authorize your Git Client with Git Key(git_swap)**

The next step is to use the saved gitkey to authorize the git client. We are setting everything up so that we can clone the repositories to which we have access.

![][12]

Authorize using the git key stored&nbsp;earlier

**Step 4: Clone your repositories(git_clone)**

This tool makes use of your earlier created GIT list, now that your git client has been authorized in step 2, you should be able to download your repos. This tool uses the account already linked to your terminal account. If you are not sure try `**earthengine ls**` to see your username. The export path is noted for the collection of repositories.

![][13]

Cloning your Git Repositories

**Step 5: Working with Assets: Generating Asset Report(ee_report)**

This includes all your assets&nbsp;, including tables, images, image collections and folders. We need to make sure we have this list to work on copying over your assets to the secondary account. Running this is simple and just requires a location for the csv file (the full path).

![][14]

Running Earth Engine&nbsp;Reports

The output is a csv file consiting of the type of asset and the asset path to be replicated in the new account. And now that we have the list time to get permissions to copy these assets.

**Step 6: Setting Permissions to Assets(ee_permissions)**

We now use the report file generated to grant read access to all assets in your account. Once this is completed you will be able to copy your assets apart from being able to copy your codes.

![][15]

Getting permissions to&nbsp;assets

**Let us Begin to Copy&nbsp;: We change gears and switch over to the destination account**

**Step 7: Setting up the Destination Account(ee_user and git_swap)**

Now we have to do two steps one after the other, do a quick earthengine authenticate and authenticate to your new account and perform Step 2 and Step 3 this time using your new account. The tool `**ee_user**` will also allow you to change your accounts. I already created Step 2 for my secondary account and now I will use that to authorize my git client with the new account.

![][16]

Change your earthengine authentication and also validate your git&nbsp;key

![][17]

Now we authorized the git client with the second&nbsp;key

**Step 8: Replicate Repositories (git_create)**

To setup our new account we need to build the outline of the earlier account, the repolists and folders inside these repos and then similary the folders and empty collections in the secondary account.

Note: Git cannot push an empty repository so if you have an empty repository delete it before downloading and pushing to new&nbsp;account

![][18]

Git Create your folder based on your earlier&nbsp;account

The repo lists now look similar

![][19]

Repo created on secondary account

**Step 9: Push to New Account(git_replicate)**

Now we push all codes from our earlier account to our new account, this way our repositories will now be populated with the most recent codes.

"Do not push to any repository that already has code because this will overwrite it"

![][20]

git_replicate to new&nbsp;account

**Step 10: Replicate Asset Structure(asset_create) and Assets (asset_replicate)**

This is similar to git_create here we replicate the collection and folder structure so we can push our assets to them. You pass it the original report you created from your primary account and it sets up as needed.

![][21]

Creates asset structure (folders and collections)

This has replicated the collection and Image folder structures.

![][22]

Asset Collections and Folders have been created(Left: asset home before asset_create Right: asset home after asset_create)

However this is still empty and the last step makes sure that your assets are actually copied over to your new asset home. I have included a counter to measure transfers left incase it is a large collection.

![][23]

Asset Replication: Copying assets to your home&nbsp;folder

The final results is your assets and codes all copied, you will still have to edit codes to change your path as needed but for now we have replicated an Earth Engine account into a new location.

![][24]

Replicated Assets on Both Accounts Copied from Left to&nbsp;Right

There you go, over the last 10 steps we have managed to replicate and move an earth engine account from one place to another. Though I found this useful to move accounts within a university setting, I see some value in moving accounts and replicating when a project member leaves a project or for simply migrating at large. For now if an owner of an account deletes his/her account or looses access to his/her account and even if you are a writer to the repository and the collection, you will loose access to these codes and assets. So this can aid in maintaining continuity by moving codes to more persistent account.

Though I have not tested this tools in a linux setting, these setup tools can be adapted and used easily in that framework, since I have tested the individual components in such setups.

[1]: https://support.google.com/accounts/answer/6010255?hl=en
[2]: https://git-scm.com/downloads
[3]: https://developers.google.com/earth-engine/python_install_manual
[4]: https://earthengine.googlesource.com/
[5]: https://github.com/samapriya/gee-takeout
[6]: https://github.com/samapriya/gee-takeout/archive/master.zip
[7]: https://cdn-images-1.medium.com/max/2000/1*CVgzI0ro26lAHD3R37JKDg.jpeg
[8]: https://cdn-images-1.medium.com/max/1600/1*ZvsokVlQBbqiUv4UA-ow9Q.jpeg
[9]: https://cdn-images-1.medium.com/max/1600/1*uH3e6ORkgm5ikJjez844bw.png
[10]: https://cdn-images-1.medium.com/max/2000/1*tP5FzkRiWOTguTPwzXij8Q.gif
[11]: https://cdn-images-1.medium.com/max/2000/1*PRAn1xGQ4EDMRGJQWlEN1A.gif
[12]: https://cdn-images-1.medium.com/max/2000/1*yZJD-PNWUR9jk4Tv4yDTdA.gif
[13]: https://cdn-images-1.medium.com/max/2000/1*EFslzisYtbDEGFCzApaNyw.gif
[14]: https://cdn-images-1.medium.com/max/2000/1*4LIeCpEUMozxYmiTL2-STg.gif
[15]: https://cdn-images-1.medium.com/max/2000/1*M9lweMgxLlENWyy8SMqXZg.gif
[16]: https://cdn-images-1.medium.com/max/2000/1*PH6kz_kieM1nBvxbJ9Zd6Q.gif
[17]: https://cdn-images-1.medium.com/max/2000/1*3GvklH9xmcnlOLM17y526A.gif
[18]: https://cdn-images-1.medium.com/max/2000/1*aL2aHP1b9HlPY6-dbGgCnQ.jpeg
[19]: https://cdn-images-1.medium.com/max/1600/1*X6xtrR-rBfpqGkpmH1TsWQ.jpeg
[20]: https://cdn-images-1.medium.com/max/2000/1*4Im_nOru-j8fI0GYQe_duQ.gif
[21]: https://cdn-images-1.medium.com/max/2000/1*5OCk2sHYDZ2Pop6dxCWJrA.gif
[22]: https://cdn-images-1.medium.com/max/1600/1*bxqnJff5hpFYmGhXb7JU8Q.png
[23]: https://cdn-images-1.medium.com/max/2000/1*ulmG1mEu_D3eRsadvBFwiA.gif
[24]: https://cdn-images-1.medium.com/max/1600/1*jzQ9cLPIushKqFoZFfn9Sg.png
