This is an XML parser designed to turn rosters scraped from the alter
aeon website into HTML for injection into webpages.

Usage:
If you want to use my hacky injection method, Webpage you want to inject
should have <!-- BEGIN realm --> and <!-- END realm --> tags between
which your roster will be injected. FYI there are better ways to do this
such as PHP or JQuery. I'd suggest using those methods.

The script also assumes you are running on an apache webserver. /var/www/html might not be the location of your webapp.

Finally, the script is curling the clan wolf roster. You will need to change the clan ID to match your own. You can find this by checking the URL after clicking your clan name at http://alteraeon.com:3004/clanlist

You will need to edit the python script to generate html relevant to
you. This is built for clanwolf.rocks exclusively and is not meant to
generate HTML that will look good on your website.

After you get it edited, simply add autogen.sh to your crontab.

something like:
0 * * * * bash /var/www/html/autogen.sh
