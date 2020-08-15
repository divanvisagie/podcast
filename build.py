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
        media=Media(
            "http://dvisagie.com/podcast/episodes/episode_1.mp3", 11932295),
        summary="In this episode we discuss the phenomenon of overcomplicated software "
        "design and how in most cases its unecessary",
    )
]
# Generate the RSS feed
rss = p.rss_str()

print(rss)
