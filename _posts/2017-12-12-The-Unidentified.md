For this assignment, I wanted to use the google quick draw dataset. I had a small idea, one that I was not passionate about, but I figured it met the requirements and would be at least a fun result if it worked.
In case you’re not familiar with Google Quick Draw, here's a [link](https://quickdraw.withgoogle.com/).

I desired to create a sort of "game" with the data. I thought it would be interesting to have the user try to guess the drawings which the neural network was unable to guess correctly.

My code is [here](https://github.com/MattCollyer/MattCollyer.github.io/tree/master/Final).

The dataset is free to the public [here](https://github.com/googlecreativelab/quickdraw-dataset).


Each document contains this data:
<p align="center">
 <img src="https://raw.githubusercontent.com/MattCollyer/MattCollyer.github.io/master/_posts/Images/data.png" alt="data">
</p>

Thankfully, Google was quite nice and created a simplified version of the data. In the README they describe the differences, “We've simplified the vectors, removed the timing information, and positioned and scaled the data into a 256x256 region.” 
The dataset is HUGE, around 22 gigabytes containing over 50 million doodles, which created a problem, since my trusty old mac had about 2 gigabytes of room left. So I ended up downloading it to my external hard drive (My trusty terabyte!). The download was surprisingly fast, and took around 30 minutes. 
But here I was left with a dilemma.

Oh man oh my oh me!! What type of database management system should I use! So many options! Should I stay true to a SQL system? Or, be edgy and go with something like… MongoDB? 
Okay here’s the thing. I think SQL’s are much more efficient and better overall, and possibly could have made my life easier. However, because I just finished working with mongo and it was still super fresh in my mind, and because I’m extremely familiar with the Java(script) syntax, I decided to go with Mongo. With my DBMS figured out, I then had to face the facts. I would have to move it onto my computer to use mongo. So with a tear in my eye I moved my entire itunes library onto the external drive. This made plenty of room, all that was left was to import the files into mongo. The terminal command is simply: 

`mongoimport -d <database name>  -c <collection> --file <file.json>`

But here came another issue. Here’s what the download actually looked like: 
<p align="center">
 <img src="https://raw.githubusercontent.com/MattCollyer/MattCollyer.github.io/master/_posts/Images/downloaded.png" alt="downloaded_data">
</p>

Oh man oh my oh me! I can’t possibly import all 345 files one by one! 
Well after searching around, I used bash to my advantage and ran this:

```FILES=/Volumes/MyPassport/QuickDraw/simplified/*
for f in $FILES; 
do
 mongoimport -d quickdraw -c qd --file $f;
done
```

And yes! It worked. How nice! I had a small fear that it would not be friendly to the .ndjson format. I then had everything in one, very very large, mongo collection. Because the schema is one dimensional, this was no issue. From here I realized that in order to display country information as well, I would need something better than the country’s ISO 3166-1 alpha 2 code! So I downloaded a json file containing the ISO 3166-1 alpha 2 code with its respective country name. Then created a python script (using pymongo) to add each country name to each document. Boy, I’ll tell ya, that took a long time to run! Side note: nothing is better than running scripts that take hours; you can kick back and binge netflix all the while feeling productive! Ha! Anyway, once that was finished I got to work creating indices for optimization purposes–and cha-ching! My data was all set (or so I thought). So I got to work on the rest of the project. I decided to again use python (using pymongo and web.py) to create the game’s foundation. 


Then I remembered– I needed to be able to make random queries. Now, after some searching it turns out there is a way to do this using mongo, however it was painfully slow even with the query indexed. So I had to change the data once again! So, because I would not be adding more data to this set, I figured it would work to change the key id of every document. So I created another script that set the key id of every doodle that was unrecognized to a number from 1-the number of unrecognized doodles. Thus querying one document by a randomly generated key id. And with that problem solved there was just one more roadblock to surpass. And that was the issue of actually drawing the image.  After many hours of trying to figure out d3 svg, I somehow got it all figured out.


I’m very happy with the way this project turned out. In the beginning I was not passionate about this project. However, after actually seeing the results, I must say I’m impressed with how it turned out. I think seeing miscommunication between an artificial neural network and a natural neural network (i.e a person) is something truly fascinating. When you get something right that was really difficult to guess, it gives you pride that you could figure it out. If you got it right and it was super easy, it makes you wonder:

 _“Why could the neural network not guess this?”_ 
 
And even if you get it wrong, it still makes you painfully curious:

*“Why on earth would someone draw this when prompted to draw ___?"*

And often you can find some truly amazing answers. 

And some humorous ones too :)

<p align="center">
 <img src="https://raw.githubusercontent.com/MattCollyer/MattCollyer.github.io/master/_posts/Images/octagon.png" alt="octagon?">
</p>
<p align="center">
 <img src="https://raw.githubusercontent.com/MattCollyer/MattCollyer.github.io/master/_posts/Images/envelope.png" alt="envelope?">
</p>
