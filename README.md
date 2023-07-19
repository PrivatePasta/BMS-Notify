# BookMyShow Discord Notifier

Steps:
1. Fill out the discord webhook url in line 32 of the script

This is a very simple, bare-bones python script which uses Selenium to notify you when a movie becomes available for booking. The script works by using BMS' redirections to understand when a date is available for booking. BMS url's use the format - https://in.bookmyshow.com/buytickets/ + `[movie]-[format]-[location]/[movie_code]/[date]` for example:

https://in.bookmyshow.com/buytickets/oppenheimer-imax-trivandrum/movie-triv-ET00363396-MT/20230721

That date code at the end (YYYYMMDD) is what we use for the script. The above URL is for 21 July 2023, but if you want to know when booking will be available for 24 July 2023 you'd just need to change the date code to that as:

https://in.bookmyshow.com/buytickets/oppenheimer-imax-trivandrum/movie-triv-ET00363396-MT/20230724

So run the script with `python BMS-Notify.py [url]` and the script will reload the URL every 60 minutes to see if it's being redirected. If it is redirected, that means the date is not available yet and just prints "Not Yet" to the console, but when it is not redirected anymore, it prints "Book Now" to the console, sends a discord message through webhook and exits.

Note: The script only works with Windows afaik because BMS blocks automation tools without a GUI with cloudflare. When you run it on a linux server, it exits with a Forbidden error but it works just fine on Windows