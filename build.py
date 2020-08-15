from podgen import Podcast, Episode, Media
# Create the Podcast
p = Podcast(
   name="The Code Kitchen",
   description="Every Episode, Software Professional Divan Visagie"
               "Chats about the latest developments and issues in the software industry with co-host Simon Hornby",
   website="http://dvisagie.com/",
   explicit=False,
)
# Add some episodes
p.episodes += [
   Episode(
     title="Overcomplicated Design",
     media=Media("http://dvisagie.com/podcast/episodes/episode_1.mp3", 11932295),
     summary="In this episode we discuss the phenomenon of overcomplicated software design and how in most cases its unecessary",
   ),
#    Episode(
#       title="Alpaca",
#       media=Media("http://example.org/files/alpaca.mp3", 15363464),
#       summary="Thousands of years ago, alpacas were already "
#               "domesticated and bred to produce the best fibers. "
#               "Case in point: we have found clothing made from "
#               "alpaca fiber that is 2000 years old. How is this "
#               "possible, and what makes it different from llamas?",
#    ),
]
# Generate the RSS feed
rss = p.rss_str()

print(rss)