# Web-Scraping-project
Extracting novel chapters from lightnovels.me

## How to use:
- Check to see if your Python installation has pip : `pip -h`
- Install the virtualenv package : `pip install virtualenv`
- Create virtual enviroment using:
 `virtualenv myenv`
 - You can activate the python environment by running :`myenv\Scripts\activate` on windows or `source myenv/bin/activate` on linux and mac.
 - Install requirements `pip install -r requirements.txt`
 - To decativate the virtual environment and use your original Python environment :`deactivate`
 - Run main.py and type the link, for example: `https://lightnovels.me/novel/the-beginning-after-the-end.html`
 - You have to enter the link for each page seperately for example: `https://lightnovels.me/novel/the-beginning-after-the-end.html?page=2`
 - Each chapter will be written into `.txt` file named with the chapter number