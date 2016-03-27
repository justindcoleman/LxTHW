class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
happy_bday = Song(["Happy Birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])

cactus_where_yr_heart = Song(["I stick because",
								"I'm stuck because",
								"I just can't tear myself away"])

candy_pop = Song(["No",
					"Betsuni",
					"I'm not playing hard to get"])
						
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

cactus_where_yr_heart.sing_me_a_song()

candy_pop.sing_me_a_song()