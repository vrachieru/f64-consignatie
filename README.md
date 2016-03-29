# [@F64Consignatie](https://twitter.com/F64Consignatie)

```This is NOT in any way an official F64 or Twitter product.```

A twitter bot (**[@F64Consignatie](https://twitter.com/F64Consignatie)**) that keeps a watchful eye on the [used photo gear](http://www.f64.ro/echipament-foto-folosit-consignatie.html) (watching all their suff is just too much) sold by [F64](http://www.f64.ro).


## Motivation

Being a shutterbug myself I like the chance to take advantage of great photography gear deals but have little lime to check websites like this on a daily basis. I also like to develop shiny new things.  
Since I use Twitter as a source of information and have little time to check photo gear sellers on a daily basis why not combine both to save time?!

## Installation

1. Download the [latest release](https://github.com/vrachieru/f64-consignatie/releases/latest)
2. Extract the archive (zip / tar.gz)
3. Install the requirements: `pip install -r requirements.txt`
4. Fill out the configuration file with your twitter info
5. Create a cron job to run the bot at a certain interval  
`crontab -l | { cat; echo "0 * * * * cd /home/pi/f64; python main.py"; } | crontab -`


## License

This project is released under the terms of the [MIT license](http://en.wikipedia.org/wiki/MIT_License).