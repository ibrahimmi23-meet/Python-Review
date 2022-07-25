
def creat_youtube_video(title , des):
	youtube_video={"title" : title , "des" : des , "likes" : 0  , "dislikes" : 0 , "comments" :  {}  }
	return youtube_video
print("hi")

def like(youtube_video):
	if "likes" in youtube_video:
		youtube_video["likes"] +=1

	return youtube_video
def dislike(youtube_video):
	if "dislikes" in youtube_video:
		youtube_video["dislikes"]+=1

	return youtube_video
def add_comment(youtube_video ,username , comment_lines):
	youtube_video["comments"] [username] =comment_lines

	return youtube_video


youtube_videokitten= creat_youtube_video('cat' , 'a small cat meowing')
for i in range (496):
	like(youtube_videokitten)

print(youtube_videokitten)


	
