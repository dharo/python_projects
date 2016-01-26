from PIL import Image
import imagehash

print ("Use dHash to determine if images are similar/same")

# Generate hashes for all
print ("screenshot #1")
hash = imagehash.dhash(Image.open('test.png'))
print (hash)

print ("\nscreenshot #2")
otherhash = imagehash.dhash(Image.open('other.png'))
print (otherhash)

print ("\nRandom screenshot")
unrelated_image = imagehash.dhash(Image.open('wrong.png'))
print (unrelated_image)

print ("\nBlank white FFFFFF.png")
white = imagehash.dhash(Image.open('FFFFFF.png'))
print (white)

print ("\nBlank black 000000.png")
black = imagehash.dhash(Image.open('000000.png'))
print (black)

print ("\nCompare first two screenshots")
print (hash == otherhash)
print (hash - otherhash)

print ("\nRandom image with the screenshots")
print (hash == unrelated_image)
print (hash - unrelated_image)

print (otherhash == unrelated_image)
print (otherhash - unrelated_image)

print ("\nCompare the Black and white images to each other")
print (white == black)
print (white - black)
