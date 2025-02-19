## Setup

<details>
  <summary>Step 1 of 5</summary>
  
  Open your Discord app and enter the user settings.
  ![https://imgur.com/HnNnmRT](https://i.imgur.com/HnNnmRT.png "Step 1")
  
</details>

<details>
  <summary>Step 2 of 5</summary>
  
  Traverse to advanced and enable developer mode if it is not enabled.
  ![https://imgur.com/LTrGjVX](https://i.imgur.com/LTrGjVX.png "Step 2")
  ![https://imgur.com/7ItCXBV](https://i.imgur.com/v9JD4db.png "Step 3")
  
  It appears that the developers of the Discord desktop application have implemented another method by which to keep people from normally being able to access the developer tools.
  ![https://i.imgur.com/BuZf2qn.png](https://i.imgur.com/BuZf2qn.png "Developer Update")

  This doesn't necessarily prevent us from being able to make use of this script but I'm definitely going to have to figure something out that doesn't require you to have to put in your passwords or any two-factor authentication tokens; this is the most convenient method for me to implement for the time-being but it's becoming increasingly difficult to continue on like this given that people have accidentally pushed their own authorization tokens to their own public forks of this repository in the past which only serves to reinforce decisions like this from the Discord staff.
  
</details>

<<<<<<< HEAD
**Steps 2 and 3:**
Under the App settings, go to Advanced and enable developer mode (applicable for the web app and desktop version).
![https://imgur.com/LTrGjVX](https://i.imgur.com/LTrGjVX.png "Step 2")
![https://imgur.com/7ItCXBV](https://i.imgur.com/7ItCXBV.png "Step 3")
=======
<details>
  <summary>Step 3 of 5</summary>
  
  Open the developer tools by pressing <kbd>CTRL</kbd> <kbd>⇧ SHIFT</kbd> <kbd>I</kbd> or <kbd>Command ⌘</kbd> <kbd>⇧ Shift</kbd> <kbd>I</kbd> on macOS and navigate to the network tab to gather your authorization token by moving about the interface *(in this example I jumped to the Nitro tab and back to generate the "science" request)*.
  ![https://imgur.com/o9Sf0CH](https://i.imgur.com/o9Sf0CH.png "Step 4")
>>>>>>> 6e2232a96b7afd2a9e13f866cdf7cd03f08238f8


</details>

<details>
  <summary>Step 4 of 5</summary>
  
  Gather the guild ID that you want to scrape from by right-clicking on the icon for the guild on the left-side of the Discord window and selecting *"Copy ID"*.
  ![https://imgur.com/14ysTcN](https://i.imgur.com/14ysTcN.png "Step 5")

  If you're wanting to grab from a direct message instead, then this method won't return the correct ID that is needed by the script.

  The only real way to get this with ease through the Discord app is to open the direct message you want to scrape from and then open the developer tools to see the correct ID in the title bar of the developer tools window and paste it into the JSON file.

</details>

<details>
  <summary>Step 5 of 5</summary>

  Gather the channel ID that you want to scrape from by right-clicking on the channel name to the right of the guild icons and selecting *"Copy ID"*.
  ![https://imgur.com/cdpTLCG](https://i.imgur.com/cdpTLCG.png "Step 6")
  
  From there you should be ready to run the script to start the downloading process.

</details>

<details>
  <summary>Protecting your Authorization Token</summary>

  You'll want to create a new document, you can name it anything you want as long as the name ends with `.token`.
  Here's a list of examples that can be used:
  ```
  my.token.txt
  another.token.rtf
  yes another token.token
  ```

  The [gitignore](.gitignore) file will tell git *(or the Github desktop application)* to avoid pushing any file whose name and extension matches the ones in the file.

</details>

**Step 8:**
Run the JsonFormat.py script under the modules folder to output your scrape in a readable format. 
NOTE: This script is still a work in progress but it already makes the results legible so I figured I would push it.

## Notes

* You can copy in multiple channels on multiple guilds if you want to.
* You must make modifications to the JSON file before running the script *(otherwise you'll end up with errors)*.

## TODO

- DM grabbing
- Config options handling
- Non-image and non-video embedded content grabbing
- Text grabbing

## Changelog

**The dates below are in YYYY-MM-DD formatting (ISO 8601).**

<details>
  <summary>Changelog</summary>

2021-02-10 - Starting the path to finalizing the experimental branch:
* Fixed a major oversight when it comes to scraping more than 25 posts for each day (more than 25 requires an offset query to be added to the undocumented API call).
* Allowing for direct media grabbing alongside JSON caching to save on time (it was faster to grab both JSON and media simultaneously day-by-day as opposed to grabbing JSON data in bulk and then checking each JSON file afterwards).
  * Finally figured out a method of getting the script to stop whenever <kbd>Ctrl</kbd> <kbd>C</kbd> is pressed on the keyboard (apparently sys.exit cares about flushing stdout buffers as opposed to os._exit)

2020-12-30 - Alleviating some Issues:
* Opting for JSON caching as opposed to direct media grabbing *(smaller and comes with more info)*.
* Adding the use of a documented API function to retrieve the last known post in the channel.

2020-11-09 - Major Repository Overhaul:
* Removed the experimental branches and renamed the master branch.
* Overhauled the SimpleRequests module and ensured Python 2 and 3 compatibility.
* Updated the API target since the current API version is 8 despite what Discord says on their official API reference.
* Updated the wiki pages to add a reference guide for those wanting to make use of SimpleRequests or for those wanting to make their own scrapers for Discord.
* Forewent the PEP8 compliance because it just adds bulk on top of the code that's not really needed.

2019-11-20 - Experimental Overhaul:
* Resurrected the experimental branch again for some testing.
* Created a separate module for this script *(SimpleRequests)*.
* Added buffer size option in the JSON file *(defaults to 1 MiB)*.
* Merged and removed experimental branch yet again.

2019-06-18 - Maintenance Update:
* Updated the README to update the token gathering method.
* Updated the README to remove unnecessary image use.
* Added personal/direct message channel option in JSON file.
* Removed page count option from the JSON file.
* Updated the wiki for this repository.
  
2019-01-29 - Overhaul:
* Merged Python 2 and Python 3 functionality into a single file.
* Removed the experimental branch since it is no longer needed.
* Added functionality to download text data and links.
* Added ability to set number of pages to grab *(each page nets approximately 25 images)*.

2018-11-13 - Released:
* Implemented a new concept from the experimental branch.
* Updated the experimental branch to match the master branch.
* I will find a method of alleviating the duplicate image/videos issue.
* I will fix up the commenting and make the code easier on the eyes.

2018-08-28 - Added Experimental Branch:
* Python 3 version of script now uses a separate config.
* MFA token now goes in the separate config to help avoid accidental leakage of one's MFA token.
* Multiple channel and server support added.
* Replaced the requests module with `http.client` module which is built-in to Python 3.7.

2018-04-07 - Beta Fix #3:
* Fixed threading issue *(too many concurrent threads)*.
* Fixed filename issues when grabbing files with similar filenames *(still a potential issue with large amounts of files but significantly less issues)*.

2018-04-07 - Beta Fix #2:
* Fixed problems when downloading from channels with less than 25 images/videos as the older scripts assumed more than 25 images/videos in the channel.
* I will incorporate a better method of grabbing images where there's less corruptions and less missing photos.

2018-02-21 - Beta Update #1:
* Updated this README to include warning information.
* Created a version for those running Python 3.
* Updated the Python 2 version to match the Python 3 version with threading support.

2017-10-03 - Beta Fix #1:
* Fixed issue with URL appending offset query information on top of itself indefinitely.
* Fixed issue with uninitialized opener data when grabbing multiple pages of JSON data.
* Added new function to allow for the resetting of opener data when grabbing JSON data.

2017-10-03 - Beta Release:
* The first release of the script.
* Not meant for production use.
* Still has bugs to fix and features to implement.

</details>

## Resources

[Most of the resources that can be used to further development on this script have been provided in the wiki for this project](https://github.com/Dracovian/Discord-Scraper/wiki)
