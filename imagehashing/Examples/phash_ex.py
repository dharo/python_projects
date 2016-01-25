from PIL import Image
import imagehash

hash = imagehash.phash(Image.open('test.png'))
print (hash)

otherhash = imagehash.phash(Image.open('other.png'))
print (otherhash)

print (hash == otherhash)
print (hash - otherhash)
